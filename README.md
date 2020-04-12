# ocr_image_to_text
python script that performs ocr with tesseract software on pdf jpg and png files



Build instructions:
This project requires two downloads, Tesseract for the OCR and Poppler for pdf conversion
Tesseract executable files can be downloaded at https://digi.bib.uni-mannheim.de/tesseract/
Once tesseract is installed, if you are on Windows, you will have to add tesseract to your windows path

This project was run in a virtual python environment called anaconda. Anaconda can be downloaded and installed at https://www.anaconda.com/distribution/

poppler can be installed through anaconda by running 




    conda install -c conda-forge poppler




Once these are installed, you can install all the requirements in requirments.txt by running





    pip install -r requirements.txt
    
    
    
Run instructions:
to run the application, navigate to the folder with the python application and type



    python ocr_text.py --filepath 'name of file you want to process'
    --outputpath 'txt filename you want to output to'
    --verbose 'True or False whether you want to see detailed logs'
    
    
    
