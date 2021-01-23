from django.http.response import HttpResponse, JsonResponse

# Create your views here.
import tensorflow as tf
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import image
import tensorflow.keras.applications.mobilenet_v2 as tfApps



def load_my_model():
	model = tfApps.MobileNetV2(weights='imagenet')
	model.summary()	
	return model

model = load_my_model()


async def run_predict(myfile):
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



async def healthcheck(request, *args, **kwargs):
	return JsonResponse({'status':'I.m up and Alive'})

async def predict(request, *args, **kwargs):
	if request.method == 'POST' and request.FILES['files']:
		try:
			result = await run_predict(request.FILES['files'])
			return JsonResponse({'result':str(result)})
		except Exception as Err:
			return JsonResponse({'error':Err})
	else:
		if request.method != 'POST':
			return JsonResponse({'error':'Method Not Allowed'})
		else:
			return JsonResponse({'error':'No File Submitted'})


    