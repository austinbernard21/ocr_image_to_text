#!/usr/bin/env python
# coding: utf-8

import os

import numpy as np
import cv2
import logging

import click
import pytesseract
import pdf2image
from textblob import TextBlob

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.command()
@click.option('filepath', '--filepath', help='path of input file',type=click.Path())
@click.option('outputpath', '--outputpath', help='path of output file', type=click.Path())
@click.option('verbose', '--verbose', help='display logs', default=False)
def img_to_text(filepath, outputpath, verbose):
    if verbose:
        logger.info('converting file to image')
    images = file_to_img(filepath)
    if verbose:
        logger.info('processing image..')
    try:
        output = get_output(images)
    except TypeError:
        logger.error('your file was not read correctly, please check that it has the correct extension')
        return
    if verbose:
        logger.info('writing to file')
    write_to_file(output, outputpath)


def file_to_img(path):
    file_split = os.path.splitext(path)
    extension = file_split[-1]

    images = []

    try:
        if extension == '.jpg' or extension == '.png':
            images.append(cv2.imread(path))
        else:
            pages = pdf2image.convert_from_path(path)
            i = 1
            for page in pages:
                page.save('output' + str(i) + '.jpg', 'JPEG')
                images.append(cv2.imread('output' + str(i) + '.jpg'))
                i = i + 1
        return images
    except:
        return


def get_output(images):
    text = ''
    # common preprocessing methods. some left out because they did not work well with samples
    for img in images:
        # upscale the image
        # img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply dilation and erosion to remove some noise
        # kernel = np.ones((1, 1), np.uint8)
        # img = cv2.dilate(img, kernel, iterations=1)
        # img = cv2.erode(img, kernel, iterations=1)
        # Apply blur to smooth out the edges
        # img = cv2.GaussianBlur(img, (5, 5), 0)
        # Apply threshold to get image with only b&w (binarization)
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        result = pytesseract.image_to_string(img, lang="eng")
        text += result

    # post processing for small spell check
    output = TextBlob(text)

    output = output.correct()

    return output


def write_to_file(text_output, filename):
    file = open(filename,'w+')
    for text in text_output:
        file.write(text)
    file.close()


if __name__ == '__main__':
    img_to_text()


