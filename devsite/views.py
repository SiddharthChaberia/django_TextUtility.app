# made by Sidd

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('textreceiver', 'default')
    remove = request.GET.get('removepunc', 'off')
    caps=request.GET.get('fullcaps','off')
    small=request.GET.get('fullsmall','off')
    reneli=request.GET.get('newlineremover','off')
    extraspacerem=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    # print(remove)
    # print(djtext)
    if remove=="on":
        # analyzed=djtext
        punctuations = '''"':!@#$%^&*();[{]},<.>/?\|'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif caps=='on':
        analyzed=""
        for i in djtext:
            analyzed+=i.upper()
        params={'purpose':'Fully Upper Case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif small=='on':
        analyzed=""
        for i in djtext:
            analyzed+=i.lower()
        params={'purpose':'Fully Lower Case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif reneli=='on':
        analyzed = ""
        for i in djtext:
            if i!='\n':
                analyzed += i
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspacerem=='on':
        analyzed = ""
        for i in djtext:
            if i==' ':
                if analyzed and analyzed[-1]!=' ':
                    analyzed += i
                else:
                    analyzed+=i
            else:
                analyzed+=i
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount=='on':
        count=0
        for i in djtext:
            count+=1
        analyzed="Number of characters is: "+str(count)
        params={'purpose':'Counted Number of Characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error")

def ex1(request):
    return render(request,'navigation.html')

def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("Remove Punc")


def capfirst(request):
    return HttpResponse("Capitalize First")


def newlineremove(request):
    return HttpResponse("New Line Remove")


def spaceremover(request):
    return HttpResponse("Space Remover")


def charcount(request):
    return HttpResponse("Character Counter")
