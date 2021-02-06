from django.shortcuts import render, redirect
from posts.models import PostItem, Slider
from posts.forms import EmailForm
from users.models import Employee

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

from wsgiref.util import FileWrapper
import os
import mimetypes
import requests
import json
from dotenv import load_dotenv

def home_view(request):
    sliders = Slider.objects.filter(deploy=True).order_by('-id')[:3]

    # Latest News

    latest_news = PostItem.objects.all().filter(post_type="News", publishable=True).order_by('-id')[:3]

    return render(request, 'index.html', {'sliders': sliders, 'latest_news':latest_news})


def team_view(request):

    team_members = Employee.objects.all().order_by("-id")

    return render(request, 'team.html', {'team_members': team_members})


def contact_view(request):

    load_dotenv('.env')

    CAPTCHA_SECRET = os.getenv('CAPTCHA_SECRET')

    email_form = EmailForm(request.POST or None)

    if request.method == 'POST':

        cap_token = request.POST.get('g-recaptcha-response')
        cap_url = 'https://www.google.com/recaptcha/api/siteverify'
        cap_secret = CAPTCHA_SECRET
        cap_data = {'secret':cap_secret, 'response':cap_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)

        # IF CAPTHCA FAILS
        if cap_json['success'] == False:
            messages.error( request, "Invalid attempt, please refresh the page.")
            return redirect('/contact')

        address = 'info@mosaichealth.com.tr'
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']

        # FORMATTING
        message_content = "From Email:    " + message_email + "\n\n"
        message_content += "From Name:    " + message_name + "\n\n"
        message_content += request.POST['message']

        send_mail(
            message_subject,  # subject
            message_content,  # content
            address,  # from email
            [address],  # to email
        )
        return redirect('/')

    return render(request, 'contact.html', {'form': email_form})


def about_view(request):
    return render(request, 'company_about.html', {})


def overview_view(request):
    return render(request, 'company_overview.html', {})

def search_panel_view(request):
    search = request.GET.get('search')

    all_posts = PostItem.objects.all().order_by('-id')
    searched_posts = []

    
    for each in all_posts:
        added = False
        # Search tags
        for tag in list(each.tags.all()):
            if search.lower() in tag.tag.lower():
                if each not in searched_posts:   # If not already in the bag
                    searched_posts.append(each)  
                    added = True
        # Search titles
        if added is not True:
            for word in each.title.strip().split():
                if search.lower() in word.lower(): # If not already in the bag
                    if each not in searched_posts:
                        searched_posts.append(each)

    rows = []
    row = []
    ind = 1

    # Add posts in rows or 3
    for each in searched_posts:
        if ind % 3 == 0:
            row.append( each )
            rows.append( row )
            row = []
        else:
            row.append( each )
        ind += 1   

    # add leftover row if any     
    if len(row):
        rows.append(row)

    return render(request, 'search_panel.html', {'rows':rows})


def pdf_download(request, filename):
    path = os.getcwd()
    path += '/static/'

    file_path = path + filename

    wrapper = FileWrapper(open(file_path, 'rb'))
    response = HttpResponse(
        wrapper, content_type=mimetypes.guess_type(file_path)[0])

    response['Content-Disposition'] = "attachment; filename=" + filename

    return response

def quality_view( request ):
    return render(request, 'quality_assurance.html', {})

def services_view( request, servicename ):

    return render(request, servicename+'.html', {})

def privacy_view( request):
    return render(request, 'privacy.html', {})