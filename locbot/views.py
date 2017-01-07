from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import words
import requests
import json
#credentials
app_id = 'd91b9bb0'
app_key = '3de79c03abb64b024def260427502bcd'

language = 'en'
#word_id = 'Ace'
# Create your views here.
def home(request):
	context = {'latest_question_list': "latest_question_list"}
	return render(request, 'index.html', context)

def use_api(request):
	response = request.GET.get('key')
	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + response.lower()
	b = words(words_searched=response)
	b.save()
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	print("code {}\n".format(r.status_code))
	print r.content
	#print("json \n" + json.dumps(r.json()))
	return HttpResponse(r.content)