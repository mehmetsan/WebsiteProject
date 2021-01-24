from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.text import slugify
import datetime

from posts.models import Slider, PostItem, Tag
from .forms import CreatePostForm

# Create your views here.

def create_post_view(request):
    post_form = CreatePostForm(request.POST or None, request.FILES)

    if request.method == 'POST':

        if post_form.is_valid():
            
            # GET THE NEWS OBJECT WITHOUT COMMITTING
            post_object = post_form.save(commit=True)

        
            # EDIT SLUG
            post_object.slug = slugify(post_object.title)

            # GET THE TAGS FOR POSTS
            selected_tags = post_form.cleaned_data.get('tags')
            post_object.tags.set(selected_tags)

            # CREATE SLIDER IF REQUESTED
            if post_form.cleaned_data.get('make_slider') == True:

                title1 = post_form.cleaned_data.get('title')
                body = post_form.cleaned_data.get('body').split('.')[0]

                if '</p>' not in body:
                    body += '</p>'

                Slider.objects.create(
                    title1=title1,
                    picture=post_form.cleaned_data.get('picture'),
                    publishable=False,
                    description=post_form.cleaned_data.get('description'),
                    color = post_form.cleaned_data.get('color')
                )

                post_object.slider = Slider.objects.get(
                    title1=post_object.title)


            # COMMIT CHANGES
            post_object.save(commit=True)

            return redirect('/')

    return render(request, 'create_post.html', {'form': post_form})

def display_all_posts(request, post_type):
    page_title = ['ARTICLES' if post_type == 'Article' else 'NEWS'][0]

    posts_list = PostItem.objects.all().filter(
        publishable=True, post_type=post_type).order_by('-date')

    recents_list = posts_list[:4]

    # DATES PART
    posts_dates = [each.date.date() for each in posts_list]        # STORE DATE ATTRIBUTES

    # REMOVE DUPLICATES BY USING SETS
    posts_dates = list(set(posts_dates))[:5]
    posts_dates.sort()
    posts_dates.reverse()

    # PAGINATION
    listed_posts = list(posts_list)

    paginator = Paginator(posts_list, 2)

    page_count = paginator.num_pages
    temp = []
    for i in range(page_count):
        temp.append(i+1)
    page_count = temp

    page = request.GET.get('page')
    posts_on_page = paginator.get_page(page)

    max_elements = []

    try:
        # TAGS PART
        all_posts = PostItem.objects.all().filter(post_type=post_type)
        tags_dictionary = {}
        for news in all_posts:
            for tag in news.tags.all():
                try:
                    tags_dictionary[str(tag)] += 1
                except:
                    tags_dictionary[str(tag)] = 1

        MAX_ELEMENT_COUNT = 3
        count = 0
        

        while count < MAX_ELEMENT_COUNT:
            # GET THE MAX ELEMENT
            max_elements.append(max(tags_dictionary, key=tags_dictionary.get))
            # REMOVE THE MAX ELEMENT
            tags_dictionary.pop(max_elements[-1])
            count += 1
    except:
        max_elements = []

    return render(request, 'all_posts.html', {'recents_list': recents_list, 'posts_list': posts_list, 'posts_on_page': posts_on_page, 'page_count': page_count, 'max_tags': max_elements,
                                              'dates': posts_dates, 'title': page_title, 'post_type': post_type})

def single_post_view(request, post_type,  slug):

    selected_post = PostItem.objects.get(slug=slug, post_type=post_type)
    title = selected_post.title

    # TAGS PART
    recents_list = PostItem.objects.all().filter(post_type=post_type, publishable=True)[:4]

    max_elements = []
    post_tags = []

    try:
        tags_dictionary = {}
        for post in recents_list:
            for tag in post.tags.all():
                try:
                    tags_dictionary[str(tag)] += 1
                except:
                    tags_dictionary[str(tag)] = 1

        MAX_ELEMENT_COUNT = 3
        count = 0

        while count < MAX_ELEMENT_COUNT:
            # GET THE MAX ELEMENT
            max_elements.append(max(tags_dictionary, key=tags_dictionary.get))
            # REMOVE THE MAX ELEMENT
            tags_dictionary.pop(max_elements[-1])
            count += 1

        post_tags = selected_post.tags.all()
    except:
        post_tags = []

    # DATES PART

    posts_by_date = PostItem.objects.all().filter(
        post_type=post_type).order_by('-date')[:3]     # GET THE LATEST 3 DATES
    posts_dates = [each.date.date()
                   for each in posts_by_date]        # STORE DATE ATTRIBUTES
    # REMOVE DUPLICATES BY USING SETS
    posts_dates = list(set(posts_dates))


    return render(request, 'post-details.html', {'recents_list': recents_list, 'selected_post': selected_post, 'max_tags': max_elements, 'post_tags': post_tags,
                                                 'dates': posts_dates, 'title': title, 'post_type': post_type})

def posts_by_date_view(request, post_type, date):
    page_title = ['ARTICLES' if post_type == 'Article' else 'NEWS'][0]
    posts_list = PostItem.objects.all().filter(
        publishable=True, post_type=post_type).order_by('-id')
    recents_list = posts_list[:4]
    
    page_date = datetime.datetime.strptime(date, '%Y-%m-%d')

    posts_by_date = PostItem.objects.all().filter(
        publishable=True, date_as_day=date, post_type=post_type).order_by('-date')
    paginator = Paginator(posts_by_date, 2)

    page_count = paginator.num_pages
    temp = []
    for i in range(page_count):
        temp.append(i+1)
    page_count = temp

    page = request.GET.get('page')
    posts_on_page = paginator.get_page(page)

    # TAGS PART
    all_posts = PostItem.objects.all().filter(post_type=post_type)
    tags_dictionary = {}
    for post in all_posts:
        for tag in post.tags.all():
            try:
                tags_dictionary[str(tag)] += 1
            except:
                tags_dictionary[str(tag)] = 1

    MAX_ELEMENT_COUNT = 3
    count = 0
    max_elements = []

    while count < MAX_ELEMENT_COUNT:
        # GET THE MAX ELEMENT
        max_elements.append(max(tags_dictionary, key=tags_dictionary.get))
        # REMOVE THE MAX ELEMENT
        tags_dictionary.pop(max_elements[-1])
        count += 1

    # DATES PART

    post_items = PostItem.objects.all().filter(post_type=post_type,
                                               publishable=True).order_by('-date')[:3]     # GET THE LATEST 3 DATES

    posts_dates = [each.date.date()
                   for each in post_items]       # STORE DATE ATTRIBUTES
    # REMOVE DUPLICATES BY USING SETS
    posts_dates = list(set(posts_dates))

    return render(request, 'posts-date.html', {'recents_list': recents_list, 'posts_on_page': posts_on_page, 'page_count': page_count, 'post_type': post_type,
                                               'max_tags': max_elements, 'dates': posts_dates, 'title': page_title, 'page_date': page_date})

def posts_by_search_view(request, post_type):
    page_title = ['ARTICLES' if post_type == 'Article' else 'NEWS'][0]
    posts_list = PostItem.objects.all().filter(
        publishable=True, post_type='post_type').order_by('-id')

    par = request.GET.get('par')
    post_items = list(PostItem.objects.all().filter(
        publishable=True, post_type=post_type))

    cleaned_posts = []
    for each in post_items:
        added = False
        # Search tags
        for tag in list(each.tags.all()):
            if par.lower() in tag.tag.lower():
                if each not in cleaned_posts:   # If not already in the bag
                    cleaned_posts.append(each)  
                    added = True
        # Search titles
        if added is not True:
            for word in each.title.strip().split():
                if par.lower() in word.lower(): # If not already in the bag
                    if each not in cleaned_posts:
                        cleaned_posts.append(each)
    

    paginator = Paginator(cleaned_posts, 2)

    page_count = paginator.num_pages
    temp = []
    for i in range(page_count):
        temp.append(i+1)
    page_count = temp

    page = request.GET.get('page')
    posts_on_page = paginator.get_page(page)

    # TAGS PART
    all_posts = PostItem.objects.all().filter(post_type=post_type)
    tags_dictionary = {}
    for news in all_posts:
        for tag in news.tags.all():
            try:
                tags_dictionary[str(tag)] += 1
            except:
                tags_dictionary[str(tag)] = 1

    MAX_ELEMENT_COUNT = 3
    count = 0
    max_elements = []

    while count < MAX_ELEMENT_COUNT:
        # GET THE MAX ELEMENT
        max_elements.append(max(tags_dictionary, key=tags_dictionary.get))
        # REMOVE THE MAX ELEMENT
        tags_dictionary.pop(max_elements[-1])
        count += 1

    # DATES PART

    posts_by_date = PostItem.objects.all().filter(
        post_type=post_type).order_by('-date')[:3]     # GET THE LATEST 3 DATES
    posts_dates = [each.date.date()
                   for each in posts_by_date]        # STORE DATE ATTRIBUTES
    # REMOVE DUPLICATES BY USING SETS
    posts_dates = list(set(posts_dates))

    return render(request, 'all_posts.html', {'posts_list': posts_list, 'posts_on_page': posts_on_page, 'page_count': page_count, 'max_tags': max_elements,
                                              'dates': posts_dates, 'title': page_title, 'post_type': post_type, 'page': page, 'par': par})
