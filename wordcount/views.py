import time
from django.http import HttpResponse
from django.shortcuts import render
import operator

datem1 = time.strftime("%Y-%m-%d %H:%M:%S")
datem2 = time.strftime("%d %B %Y - %I:%M:%S %p")

# def home(request):
# 	return HttpResponse('hello world')


def homepage(request):
	return render(request, 'home.html')


def about(request):
	# return HttpResponse("<h1>Welcome Robert,</h1>" + "  " + datem2)
	# return HttpResponse(datem2)
	today = time.strftime("%d %B %Y - %I:%M:%S %p")
	return render(request, 'about.html', {'today': today})


# function to count and sort noumber of words
def count(request):
	fulltext = request.GET['fulltext']
	# print(fulltext)
	wordlist = fulltext.split()

	worddict = {}

	for word in wordlist:
		if word in worddict:
			# Increase count
			worddict[word] += 1
		else:
			# Add to dictionary
			worddict[word] = 1

	sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})