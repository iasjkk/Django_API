from django.shortcuts import render
from django.http import HttpResponse
from .models import info
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class Process(APIView):


	def post(self, request):
		print(f'Printing:: {request.data}')
		print(request.FILES)
		file = request.data['file']
		df= pd.read_csv(file)
		print(df)
		name_list = [df.loc[i, 'Name'] for i in df.index]
		# print(name_list)
		dic = {'data': name_list}
		# dic = {'data': df.loc[0]}
		return render(request, 'home/process.html', context=dic)


def add(req):
    uid = req.GET.get('id')
    last_name = req.GET.get('last')
    first_name = req.GET.get('first')
    email_id = req.GET.get('email')
    city_name = req.GET.get('city')
    # obj = info(uid, 'Pradeep', 'Akash', 'Akash.P@gmail.com', 'Bhopal')
    obj = info(uid, last_name, first_name, email_id, city_name)
    obj.save()
    message = 'insertion done!!'
    return HttpResponse(f'{message}')

def work(request):
	dic = {'data': 'Jitendra'}
	return render(request, 'home/first.html', context=dic)

@csrf_exempt
def progress(request):
	# file = request.data('file')
	# df= pd.read_csv(file)
	dic = {'data': 'second'}
	return render(request, 'home/second.html', context=dic)

@csrf_exempt
def process(request):
	print(request.json())
	file = request.data['file']
	df= pd.read_csv(file)
	dic = {'data': df.loc[0, 'name']}
	return render(request, 'home/process.html', context=dic)
# Create your views here.
