# Repo for disease classification including Covid-19

1. A classification model for covid-19 chest X-ray images using ResNet50 was built.
2. Dataset used consists of four classes.
3. Covid-19 Positive, Normal, Viral Pneumonia, Bacterial Pneumonia are the four classes used for building the model.
4. Performed image preprocessing for all the training images.
5. Trained and saved the model with prediction result of 70% accuracy.
6. Deployed the model as web aplication using flask framework.

## Code and Resources Used

Python Version: 3.7

Packages: pandas, numpy, sklearn, matplotlib, seaborn, tensorflow, cv2, flask

Tutorial for Transfer learning: Dr. Ryan Ahmed (Udemy)

Tutorial for flask deployment: Dan We (Udemy)


### Dataset Structure

* Two folders

1. Train: 532 images
2. Test: 40 images

### Training process
* ResNet50 was used for transfer learning.
* Using ImageDataGenerator imported dataset and performed data augmentation to significantly increase the diversity of data available for training models.
* Dropout techniques were used to prevent the model from overfitting.
* Too many epochs can lead to overfitting of the training dataset, whereas too few may result in an underfit model. So, Early stopping is utilised which is a method that allows you to specify an arbitrary large number of training epochs and stop training once the model performance stops improving on a hold out validation dataset.
* After evaluating the model using Test dataset, the prediction results were 70% accurate.

### Visualization of predicted results
![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/prediction_image.png "Logo Title Text 1")

## Model deployment using Flask
* Using the flask framework, the model was deployed in web application.
* Model can be deployed using 'Flask Covid xray deploy.py'

![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/screenshot.png)

### Prediction
![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/prediction_screenshot.png)
 


