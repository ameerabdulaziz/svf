import csv

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms
from location_field.forms.plain import PlainLocationField

from posts.models import Post, Comment


def return_choices(file_name, column_number):
    choices = []
    with open(file_name) as f:
        file_reader = csv.reader(f, skipinitialspace=True)
        next(file_reader)
        choices.append(('', 'Choose...'))
        for row in file_reader:
            choices.append((row[column_number][1:-1], row[column_number][1:-1]))
    return tuple(choices)


class PostForm(forms.ModelForm):
    # vehicle_type = forms.ChoiceField(choices=return_choices('posts/data/car_type.csv', 1))
    # make = forms.ChoiceField(choices=return_choices('posts/data/car_make.csv', 1))
    # model = forms.ChoiceField(choices=return_choices('posts/data/car_model.csv', 2))
    location = PlainLocationField(based_fields=['city'], initial='-22.2876834,-49.1607606')

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'vehicle_type', 'make', 'model', 'vehicle_numbers',
                  'vehicle_characters', 'city', 'region', 'location']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('comment', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register New Account', css_class='form-group'),
            # HTML('''<span class="small"> Already have an account? <a href="{% url 'accounts:login' %}?next={{ request.path }}">Login To Your Account</a></span>'''),
        )
