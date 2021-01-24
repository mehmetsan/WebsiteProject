from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(
        blank = True,
        null = True,
        max_length=50
    )
    email = models.EmailField(
        _('Email Address'), unique=True, blank=True, null=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    phone = models.CharField(
        _('Phone Number'), max_length=30, unique=False, blank=True, null=True,
        help_text=_('Enter phone number with our without +()'),
        validators=[
            RegexValidator(
                r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
                _('Enter a valid phone number.'),
                'invalid'
            ),
        ],
    )   
    picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    position = models.CharField(
        max_length=50,
        null = True,
        blank = True
        
    ) 
    linked_In_URL = models.CharField( max_length=120, blank=True, null=True )

    def __str__(self):
        return self.full_name
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        self.full_name = self.get_full_name()
        super(Employee, self).save(*args, **kwargs)
