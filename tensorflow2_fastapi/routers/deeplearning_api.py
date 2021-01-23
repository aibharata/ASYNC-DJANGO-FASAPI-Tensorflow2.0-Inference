from fastapi import Body, APIRouter, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import image
import tensorflow.keras.applications.mobilenet_v2 as tfApps




router = APIRouter()
poiAPP = 0

def load_my_model():
	model = tfApps.MobileNetV2(weights='imagenet')
	model.summary()	
	return model

model = load_my_model()

async def run_predict(myfile):
    try:
        img = Image.open(myfile)
        img = img.convert('RGB')
        img = img.resize((224, 224), Image.NEAREST)
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        preds = model.predict(img)
        result = tfApps.decode_predictions(preds, top=3)[0]
        return result
    except Exception as err:
        return err

@router.post('/predict')
async def ai1_router(files: UploadFile = File(...)):
    outputs = dict()
    result = await run_predict(files.file)
    outputs['prediction'] = str(result)
    # outputs['model_name'] = 'resnet50'
    return outputs