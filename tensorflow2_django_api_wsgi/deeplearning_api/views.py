from django.shortcuts import render

# Create your views here.
import tensorflow as tf
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import image
import tensorflow.keras.applications.mobilenet_v2 as tfApps

from rest_framework.response import Response
from rest_framework.status import ( HTTP_400_BAD_REQUEST, HTTP_200_OK)

from rest_framework import exceptions
from rest_framework import generics

def load_my_model():
	model = tfApps.MobileNetV2(weights='imagenet')
	model.summary()	
	return model

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


from rest_framework import serializers
class PredictSerializer(serializers.Serializer):
	files = serializers.FileField()

class HealthCheck(generics.GenericAPIView):
	def get(self, request, *args, **kwargs):
		return Response({"status": "I.m alive"})


class PredictAPI(generics.GenericAPIView):
	serializer_class = PredictSerializer
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			result = run_predict(serializer.validated_data['files'])
			print(result)
			return Response({"prediction": result})
		else: 
			return Response({"error": serializer.errors})


    