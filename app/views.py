from flask import render_template , request
import os
import cv2
from app.face_recognition import faceRecognitionPipeline
import matplotlib.image as matimg

UPLOAD_FOLDER = 'static/upload/'
UPLOAD_FOLDER_PREDICTION = 'static/predict/'

def index():
    return render_template('index.html')

def app():
    return render_template('app.html')

def genderapp():
    if request.method == 'POST':
        f = request.files['image_name']
        filename = f.filename
        #save our image on upload folder
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        #get prediction
        pred_image,predictions = faceRecognitionPipeline(path)
        pred_filename = 'prediction_image.jpg'
        cv2.imwrite(os.path.join(UPLOAD_FOLDER,pred_filename),pred_image)
        print(predictions)
        #generate repport
        reprot = []
        for i , obj in enumerate(predictions):
            gray_image = obj['roi']
            eigen_image = obj['eig_img'].reshape(100,100)
            gender_name = obj['prediction_name']
            score = round( obj['score']*100,2)

            ## save grayscale and eigne in predict folder
            gray_image_name = f'roi_{i}.jpg'
            eig_image_name = f'eigen_{i}.jpg'
            matimg.imsave(f'./static/predict/{gray_image_name}',gray_image,cmap='gray')
            matimg.imsave(f'./static/predict/{eig_image_name}',eigen_image,cmap='gray')
            #save report
            # save report 
            reprot.append([gray_image_name,
                           eig_image_name,
                           gender_name,
                           score])
        return render_template('gender.html', fileupload=True,reprot=reprot)

        print('ML model prediction sussesfully')
    else:
        return render_template('gender.html', fileupload=False)
    