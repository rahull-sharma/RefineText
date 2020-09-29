from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = (request.POST.get('text', 'default'))

    # check checkbox values
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charactercount = (request.POST.get('charactercount', 'off'))
    removenum = (request.POST.get('removenum', 'off'))

    purpose = ""

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = purpose + 'Removed Punctuations'

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = purpose + ' | Changed To Uppercase'

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = purpose + ' | New Line Removed'

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed = analyzed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = purpose + ' | Extra Space Removed'

    if removenum == 'on':
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed
        purpose = purpose + ' | Removed Numbers'

    if charactercount == 'on':
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'Number Of Characters In Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    params = {'purpose': purpose, 'analyzed_text': djtext}

    if removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on' or removenum == 'on' or charactercount == 'on':
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Please Write Something And Select A Operation In Order To Proceed")


refinetextinfo = {"aboutus": "This is my first Django website I made while learning.",
                  "contactus": "For any bugs/quires E-mail me at kickcrahul@gmail.com",
                  "title1": "About Us", "title2": "Contact Us"}


def aboutus(request):
    return render(request, 'aboutus.html', refinetextinfo)


def contactus(request):
    return render(request, 'contactus.html', refinetextinfo)
