from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.utils import timezone
import threading
from django.core.mail import send_mail
from .dataschema import data_set

def convert_date_format(date_str):
    date_obj = datetime.strptime(str(date_str), '%d/%m/%Y %H:%M:%S')
    formatted_date = date_obj.strftime('%d-%B-%Y')
    return formatted_date

@api_view(['GET', 'POST'])
def data_view(request):
    if request.method == 'GET':
        return Response(data_set)
    elif request.method == 'POST':
        new_data = request.data
        new_data['Date'] = convert_date_format(new_data['DateTime'])
        data_set.append(new_data)
        return Response(new_data)
    # Implement PUT and DELETE similarly

@api_view(['GET'])
def data_session_expiry(request):
    response = Response(data_set)
    response['Cache-Control'] = 'max-age=3600'
    response.set_cookie('sessionid', 'your-session-id', max_age=3600)
    return response


def send_notification():
    send_mail(
        'Your Job Completed',
        'Your job has completed successfully.',
        'info@creative.com',
        ['admin@creative.com'],
        fail_silently=False,
    )

@api_view(['POST'])
def trigger_job(request):
    threading.Timer(15.0, send_notification).start()
    return Response({"message": "Your job notification will be triggered."})
