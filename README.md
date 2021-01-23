# ASYNC-DJANGO-FASAPI-Tensorflow2.0-Inference

ASYNC-DJANGO-FASAPI-Tensorflow2.0-Inference Performance Comparision

## Tensorflow2.0-ModelServing-Comparision

## About

This repo shows various ways of deploying Tensorflow2.0 models on webservers - The Django way, DRF way (Both Sync/UWSGI servers), Django Aysnc way, and fastapi Async way

### tf2_django_full_stack_app

This project is full stack django ML/DL inference app integrated with Tensorflow, with both frontend and backend served from django. This shows how to efficiently and properly integrate Tensorflow2.0 with Django to serve AI/ML Models in website. This code works for Tensorflow CPU version and Tensorflow-GPU version.

### tensorflow2_django_api_wsgi

This project is rest-api based django ML/DL inference app integrated with Tensorflow, based on djangorestframework (drf). This is a synchronous app that can be deployed with uwsgi server.

### tensorflow2_django_api_asgi

This demonstates the async capabilities of django. This project is rest-api based django ML/DL inference app integrated with Tensorflow, without drf. Currently there is no out of box aysnc support for drf. This is a asynchronous app that can be deployed with uvicorn and gunicorn server.

### tensorflow2_fastapi

This project is rest-api based FASTAPI ML/DL inference app integrated with Tensorflow. This is a asynchronous app that can be deployed with uvicorn and gunicorn server.

### Successful Build Environment

Tested with Following Environments: 

		Python - 3.7.7 and 3.8.5
		Tensorflow-GPU / Tensorflow-CPU
		Django
		locust
		uvicorn (for async)
		gunicorn (for async)
		uwsgi (for sync)


## Django Async Runsever Locally

		uvicorn tensorflow2_django_api_asgi.asgi:application --reload

## Django UWSGI Runsever Locally

		python manage.py runserver

## Fastapi Runserver Locally

		uvicorn main:app --reload

## Test With Locust

		locust -f locust_stress_test.py --host="http://localhost:8000"


# Curl To Server

		curl --location --request POST 'http://localhost:8000/api/predict' --form 'files=@"/C:/Downloads/SampleImages/cat.jpg"'