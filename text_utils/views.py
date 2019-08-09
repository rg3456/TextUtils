# i have created this file-ritik

from django.http import HttpResponse
from django.shortcuts import render
#code for video 6 code with harry
"""def index(request):
	return HttpResponse("hello")

def about(request):
	return HttpResponse("<h1>about</h1>")"""
# code for video 7 code with harry
def index(request):
	#param={'name':'harry','place':'mars'} to pass as third argument in below function

	return render(request,'index.html')
	#return HttpResponse("hello")

#def ex1(request):
#	return HttpResponse("hello")

#initially defined remove punc function is analyze function
def analyze(request):
	#get the text
	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','default')
	f=request.POST.get('fullcaps','default')
	n=request.POST.get('new','default')
	print(removepunc)
	print(djtext)
	#analyzed=djtext
	if(removepunc=='on'):
		punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char
		params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
		djtext=analyzed
		#analyze text
		#return HttpResponse("remove punc")
		#return render(request,'analyze.html',params)
	if(n=='on'):
		analyzed=""
		for char in djtext:
			if char!="\n" and char!="\r":
				analyzed=analyzed+char
		params={'purpose':'New Line Remover','analyzed_text':analyzed}
		djtext=analyzed
		#analyze text
		#return HttpResponse("remove punc")
		#return render(request,'analyze.html',params)
	if(f=='on'):
		analyzed=djtext.upper()
		params={'purpose':'Capitalize','analyzed_text':analyzed}
		djtext=analyzed


		#analyze text
		#return HttpResponse("remove punc")
		#return render(request,'analyze.html',params)
	#else:
	#	return HttpResponse("Error")

	if(removepunc!="on" and n!="on" and f!="on" or djtext==""):
		return HttpResponse("error")
	return render(request,'analyze.html',params)
"""def capfirst(request):
	return HttpResponse("capitalize first")

def newlineremove(request):
	return HttpResponse("new line remove")


def spaceremove(request):
	return HttpResponse("space remove")


def charcount(request):
	return HttpResponse("char count")"""
