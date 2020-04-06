from django.http import HttpResponse
from django.shortcuts import render
import operator 
def homepage(request):
    return render(request,'home.html ')

def about(request):
    return render(request,'about.html') 

def count(request):
    ft=request.GET['fulltext']
    wordlist=ft.split()
    worddictionary ={}
    for word in wordlist:
        if word in worddictionary:
            #increment 
            worddictionary[word]+=1

        else:
            #add word to dictionary
            worddictionary[word]=1
   
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request , 'count.html',{'fulltext':ft,'count':len(wordlist),'worddictionary':sortedwords})
