from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.validators import validate_email, RegexValidator


from .models import Post, Comment

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=False) # validators should be a list

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'phone_number')

    def clean(self):
        super(SignUpForm, self).clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        try:
            validate_email(email)
        except VallidationError as e:
            self._errors['email'] = self.error_class([" bad email, details:", e])
        return self.cleaned_data                    

class loginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password', )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image_post',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)