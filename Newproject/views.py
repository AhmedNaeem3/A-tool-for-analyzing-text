from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    info_dict = {
        'name': 'Ahmed',
        'age': 18
    }
    return render(request, 'homepage.html', info_dict)


def about_us(request):
    # save_text = request.Get.get('text', 'default')
    return HttpResponse("our information!")


def analyze_text(request):
    save_text = request.POST.get('text', 'default')
    print(save_text)
    removepunc = request.POST.get('removepunc', 'off')
    # print(removepunc)
    capital_letter = request.POST.get('capital', 'off')
    # print(capital_letter)

    analyzed_text = ""

    punctuations = '''()<>?/:;!@#$%^*&<,\|'''
    error_check = save_text
    if error_check == "":
        return HttpResponse("ERROR!")

    elif removepunc == 'on' and capital_letter == 'on':
        for char in save_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
        analyzed_text = analyzed_text.upper()
    elif capital_letter == 'on':
        analyzed_text = save_text.upper()
    elif removepunc == 'on':
        for char in save_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
    else:
        analyzed_text = save_text
    new_dict = {
        'purpose': 'Removed Punctuations',
        'analyzed_text': analyzed_text
    }
    if removepunc == 'on' and capital_letter == 'on':
        new_dict['purpose'] = 'REMOVED PUNCTUATIONS AND CHANGE YOUR STRING TO UPPER CASE!'
    elif capital_letter == 'on':
        new_dict['purpose'] = 'Change Your String To UpperCase!'
    elif removepunc == 'off' and capital_letter == 'off':
        new_dict['purpose'] = 'Punctuations Not Removed And Also String Doesnt Changes To UpperCase!'
    return render(request, 'remove_punc.html', new_dict)



