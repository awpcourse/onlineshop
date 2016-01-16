from django.forms import Form, CharField, Textarea, PasswordInput
from django.contrib.auth.forms import UserCreationForm

class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)

class UserRegisterForm(UserCreationForm):
	first_name = CharField(max_length=30)
	last_name = CharField(max_length=30)
	

