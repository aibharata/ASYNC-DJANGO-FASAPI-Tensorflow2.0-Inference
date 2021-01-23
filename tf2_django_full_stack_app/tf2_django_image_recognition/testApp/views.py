from django.shortcuts import render
import tensorflow as tf
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import image
import tensorflow.keras.applications.resnet50 as tfApps

def load_my_model():
	model = tfApps.ResNet50(weights='imagenet')
	model.summary()	
	return model


# This model will (and should) be only loaded once when server starts
model = load_my_model()

def run_predict(myfile):
	try:
		img = Image.open(myfile.file)
		img = img.convert('RGB')
		img = img.resize((224, 224), Image.NEAREST)
		
		img = image.img_to_array(img)
		img = np.expand_dims(img, axis=0)
		preds = model.predict(img)
		result = tfApps.decode_predictions(preds, top=3)[0]
		return result
	except Exception as err:
		return err
	

def predict(request):
	if request.method == 'POST' and request.FILES['img']:
		try:
			print(request.FILES['img'])
			post = request.method == 'POST'
			result = run_predict(request.FILES['img'])
			#result = "Vin"
			return render(request, "testApp/predict.html", {
				'result': result})
		except:
			return render(request, "testApp/predict.html", {
				'result': "Something Went Wrong.. Check Server Log"})			
	else:
		return render(request, "testApp/predict.html")