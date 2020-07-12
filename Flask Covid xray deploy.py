from flask import Flask, request, jsonify, url_for, render_template
import uuid
import os
from tensorflow.keras.models import load_model
import numpy as np
from werkzeug import secure_filename
from PIL import Image, ImageFile
from io import BytesIO
from tensorflow.keras.preprocessing import image
import cv2



ALLOWED_EXTENSION  =set(['txt', 'pdf', 'png','jpg','jpeg','gif'])
IMAGE_HEIGHT =256
IMAGE_WIDTH = 256
IMAGE_CHANNELS = 3

label_names = {0 : 'Covid-19 Positive', 1 : 'Healthy' , 2: 'Viral Pneumonia', 3 : 'Bacterial Pneumonia'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSION


app = Flask(__name__)
model = load_model("model.h5")
@app.route('/')
def index():
    return render_template('ImageML.html')

@app.route('/api/image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return render_template('ImageML.html', prediction='No posted image. Should be attribute named image')
    file = request.files['image']
    
    if file.filename =='':
        return render_template('ImageML.html', prediction = 'You did not select an image')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print("***"+filename)
        x = []
        ImageFile.LOAD_TRUNCATED_IMAGES = False
        img = Image.open(BytesIO(file.read()))
        img.load()
        
        img = image.img_to_array(img)
        if img.shape[2] == 3:
            img = cv2.resize(img,(256,256))
            img = img / 255
            img = img.reshape(-1,256,256,3)
            predict = model.predict(img)
            predict = np.argmax(predict)
        
        else:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            img = cv2.resize(img,(256,256))
            img = img / 255
            img = img.reshape(-1,256,256,3)
            predict = model.predict(img)
            predict = np.argmax(predict)
        
        
        response = (label_names[predict])
        return render_template('ImageML.html', prediction = '{}'.format(response))
    else:
        return render_template('ImageML.html', prediction = 'Invalid File extension')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
