#i have created this file-----jasleen
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
            return render(request,'index.html')
def analyze(request):
    #input text
    submit_text = request.POST.get('input_text','')
    #print(submit_text)
    if(submit_text):
        #checkboxes input
        removepunctuation_text = request.POST.get('removepunctuation','off')
        capitalized_text = request.POST.get('capitalize','off')
        newlineremove_text = request.POST.get('newlineremove','off')
        spaceremove_text = request.POST.get('spaceremove','off')
        extraspaceremove_text = request.POST.get('extraspaceremove','off')
        charcount_text = request.POST.get('charcount','off')
        #analyze =""

        analyzed_text = submit_text
        count_char = ""

        #check if checkbox on

        # removing puctuations
        if(removepunctuation_text=='on'):
                analyze = ""
                punctuations='''!()-{}[];:'"\,<>./?@#$%^&*_~'''
                for char in analyzed_text:
                    if char not in punctuations:
                        analyze = analyze+char
                analyzed_text=analyze
                #params = {'purpose':'Remove Punctuation','analyzed_text':analyze}
                #return render(request,'analyze.html',params)

        # capitalize text
        if(capitalized_text=='on'):
                analyze = ""
                for char in analyzed_text:
                    analyze = analyze+char.upper()
                analyzed_text=analyze
                #params = {'purpose':'Capitalize','analyzed_text':analyze}
                #return render(request,'analyze.html',params)

        #remove newline
        if(newlineremove_text=='on'):
                analyze = ""
                for char in analyzed_text:
                    if (char !="\n" and char!="\r"):
                        analyze = analyze+char
                analyzed_text=analyze
                #params = {'purpose':'Newline Remove','analyzed_text':analyze}
                #return render(request,'analyze.html',params)

        #removing space
        if(spaceremove_text=='on'):
                analyze = ""
                for char in analyzed_text:
                    if (char!=' '):
                        analyze = analyze + char
                analyzed_text=analyze
                #params = {'purpose':'Space Remove','analyzed_text':analyze}
                #return render(request,'analyze.html',params)

        #removing extra space
        if(extraspaceremove_text=='on'):
                analyze = ""
                for index,char in enumerate(analyzed_text):
                        if not (analyzed_text[index]==' ' and analyzed_text[index+1]==' ' ):
                            analyze = analyze + char
                analyzed_text=analyze
                #params = {'purpose':'Extra Space Remove','analyzed_text':analyze}
                #return render(request,'analyze.html',params)

        #character count
        if(charcount_text=='on'):
                count = 0
                for char in analyzed_text:
                    if ((char>='A' and char<='Z') or (char>='a' and char<='z') or (char>=0 and char<=9) ):
                        count = count+1
                count_char = f"no of characters : {count}"

                #params = {'purpose':'Character Count','analyzed_text':count}
                #return render(request,'analyze.html',params)

        #print(analyzed_text)
        params = {'purpose':'Analyze Text','analyzedtext':analyzed_text,'countcharacters':count_char}
        return render(request,'analyze.html',params)
        #else:
                    #return HttpResponse("ERROR")
    else:
        params = {'purpose':'Analyze Text','analyzedtext':"no input",'countcharacters':''}
        return render(request,'analyze.html',params)
