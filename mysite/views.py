# Created by Bigyan Luitel
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text and checkbox values
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    smallcaps = request.POST.get('smallcaps', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')

    # Define the punctuation characters
    punctuation = '''?!,;:()[]{}<>'-—.../\|*&@~^_%$+÷×'''
    
    # Initialize analyzed text
    analyzed = djtext

    # Check which options are on and apply transformations
    if (removepunc=="on"):
        
        analyzed=" "
        for char in djtext:
            if(char not in punctuation):
                analyzed=analyzed + char
    if fullcaps == "on":
        analyzed = analyzed.upper()

    if smallcaps == "on":
        analyzed = analyzed.lower()

    if capfirst == "on":
        analyzed = analyzed.capitalize()

    if newlineremove == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", " ")

    if spaceremover == "on":
        analyzed = " ".join(analyzed.split())

    if countchar == "on":
        char_count = len(analyzed)
        info = {'purpose': 'Count Characters', 'analyzed_text': char_count}
        return render(request, 'analyze.html', info)

    # If no options are selected, return an error message
    if (removepunc != "on" and fullcaps != "on" and smallcaps != "on" and
        capfirst != "on" and newlineremove != "on" and spaceremover != "on" and
        countchar != "on"):
        return HttpResponse("Error: Please select at least one operation.")

    # Return the final analyzed text
    info = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', info)
