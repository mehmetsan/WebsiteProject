from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.text import slugify
from colorfield.fields import ColorField

import sys
import io
import re
import datetime
from io import BytesIO
from PIL import Image
from ckeditor.fields import RichTextField

class Slider( models.Model ):

    title1  = models.CharField( max_length = 120)
    picture = models.ImageField(upload_to="slider_pics/", blank=True, null=True)
    publishable = models.BooleanField(default=False)
    description = models.CharField( max_length = 300, blank=True, null=True)
    color = models.CharField( max_length = 300, blank=True, null=True)
    deploy = models.BooleanField(default=False)
    site_url = models.CharField( max_length = 300, blank=True, null=True )

    def __str__(self):
        return self.title1

    def save(self, *args, **kwargs):
        # SLIDER PICTURE MANAGEMENT
        if  self.picture and (not self.publishable):
            im = Image.open(self.picture)
            output = BytesIO()
            #Resize/modify the image
            im = im.resize( (1920,930) )
            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            #change the imagefield value to be the newley modifed image value
            self.picture = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            self.publishable = True
        super(Slider,self).save()

class Tag( models.Model):
    tag = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.tag

class PostItem( models.Model ):  
    POST_TYPE_CHOICES = [
        ('Article', 'Article'),
        ('News', 'News'),
    ]
      
    post_type = models.CharField( max_length= 20,
                                    choices = POST_TYPE_CHOICES, 
                                    default = 'ARTICLE')
    tags = models.ManyToManyField(Tag)
    slider = models.OneToOneField(Slider, null=True, blank=True, on_delete=models.CASCADE)
    title  = models.CharField( max_length = 120, null=True, unique = True)
    author = models.CharField( max_length = 120, null=True)
    body   = RichTextField(null=True)
    date   = models.DateTimeField(auto_now_add=True, null=True)
    date_as_day = models.DateField(auto_now_add=True, null=True)
    picture  = models.ImageField(upload_to="posts/pictures/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="posts/thumbnails/", blank=True, null=True)
    publishable = models.BooleanField(default=False, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130, blank=True, null=True)
    description = models.CharField( max_length = 300, blank=True, null=True)
    color = ColorField(default='#FF0000', blank=True, null=True)

    def __str__(self):
        return self.title      

    def custom_date(self):
        return datetime.datetime, datetime.date

    def get_unique_slug(self):
        slug = slugify( self.title )
        unique_slug = slug
        counter = 1

        while PostItem.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug
   
    def get_description(self):
        text = self.body

        # Print string after removing tags 
        removed = re.compile(r'<[^>]+>').sub('', text)
        return removed

    def save(self, *args, **kwargs):
        date, date_as_day = self.custom_date()
        if not self.date:
            self.date = date
        if not self.date_as_day:
            self.date = date_as_day

        # GENERATE SLUG
        if not self.slug:
            self.slug = self.get_unique_slug()
        
        # DESCRIPTION
        temp_desc = self.get_description().split('.')
        if len(temp_desc) > 1:
            self.description = temp_desc[0] + '.' + temp_desc[1] + '.'
        else:
            self.description = temp_desc[0] + '.'
        

        # SLIDER CHECKS
        try:
            slider_object = self.slider

            # UPDATE DESCRIPTION
            slider_object.title1 = self.title
            slider_object.publishable = self.publishable
            slider_object.description = self.description     
            slider_object.color = self.color   
            slider_object.picture = self.picture
            slider_object.save()  
            self.slider = slider_object
        except:
            pass  

        # POST PICTURE MANAGEMENT
        if  self.picture and (not self.publishable):
            # PICTURE PART
            im = Image.open(self.picture)
            output = BytesIO()
            #Resize/modify the image
            im = im.resize( (1920,930) )
            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            #change the imagefield value to be the newley modifed image value
            self.picture = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            self.publishable = True

            # THUMBNAIL PART
            im = Image.open(self.picture)
            output = BytesIO()
            #Resize/modify the image
            im = im.resize( (400,230) )
            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            #change the imagefield value to be the newley modifed image value
            self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(PostItem,self).save()

