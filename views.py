# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:07:35 2019

@author: Dariusz
"""

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddictionary = {}
    worldlist = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] += 1
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(worldlist)})
    
def about(request):
    return render(request, 'about.html')