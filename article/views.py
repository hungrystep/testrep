from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def article(request, call='2004'):
	html="hello world %s"%call
	return HttpResponse(html)

def test_article(request):
	return HttpResponse("Hello world")

def article1(request,article_id="15"):
	b="Hello yout name is  a "%article_id
	return HttpResponse(b)

def test(request):
	return render_to_response('test.html')

def search(request):
	try:
		str="%s"%request.POST['book']
	except:
		return HttpResponse("VERY BAD")
	return HttpResponse(str)