# Covid-19-Xray-classification-RESNET50-flask-deployment-
## A classification model for covid-19 chest X-ray images using ResNet50.

Number of classes: 4
Classes = Covid-19 Positive, Normal, Viral Pneumonia, Bacterial Pneumonia.

### Dataset Structure

* Two folders

1. Train: 532 images
2. Test: 40 images

## Training process
* ResNet50 used for transfer learning.
* Using ImageDataGenerator imported dataset and performed data augmentation to to significantly increase the diversity of data available for training models.
* Dropout techniques were used to prevent the model from overfitting.
* Too many epochs can lead to overfitting of the training dataset, whereas too few may result in an underfit model. So, Early stopping is utilised wwhich is a method that allows you to specify an arbitrary large number of training epochs and stop training once the model performance stops improving on a hold out validation dataset.
* After evaluating the model using Test dataset, the prediction results were 70% accurate.

### Visualization of predicted result
![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/prediction_image.png "Logo Title Text 1")

## Model deployment using Flask
* Using the flask framework, the model was deployed in web application.
![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/screenshot.png)
### Prediction screeshot
![alt text](https://github.com/Jishan-works/Covid-19-Xray-classification-RESNET50-flask-deployment-/blob/master/prediction_screenshot.png)
 


