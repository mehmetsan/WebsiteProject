from django import forms
from .models import PostItem, Tag
from django.core.exceptions import ValidationError


class CreatePostForm(forms.ModelForm):
    make_slider = forms.BooleanField(required = False,)
    add_tags = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Health, Insurance, Military",}        
        ),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta():
        model = PostItem
        fields = ['post_type','title', 'author', 'body', 'picture', 'color']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('make_slider') == True:
            if not cleaned_data.get('picture'):
                raise ValidationError("You forgot to add picture for the slider!")

        if cleaned_data.get('tags')  and cleaned_data.get('add_tags'):
            raise ValidationError("You can't add and select tags at the same time, add them first, then select.")

        if cleaned_data.get('tags') is None and cleaned_data.get('add_tags') != '':
            input_tags = cleaned_data.get('add_tags').split(',')
            input_tags = [each.strip() for each in input_tags]

            all_tags = [each.tag for each in Tag.objects.all()]
            for each in input_tags:
                if each not in all_tags:
                    Tag.objects.create(tag=each)

        return cleaned_data

class EmailForm(forms.Form):
    name = forms.CharField(max_length=120)
    email= forms.CharField()
    subject = forms.CharField(max_length=120)
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Enter your message here",}
        ),
    )

    name.widget.attrs.update({'placeholder': 'Name Surname'})
    email.widget.attrs.update({'placeholder': 'E-mail'})
    subject.widget.attrs.update({'placeholder': 'Subject'})


