from django import forms
from apps.user.models import User #, Student2, Mentor

class loginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['nick_name', 'password']

		widgets = {
           # telling Django your password field in the mode is a password input on the template		    
			'nick_name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
        	'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),			
        }
