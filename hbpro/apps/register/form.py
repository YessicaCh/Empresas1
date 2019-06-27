from django import forms
from apps.user.models import User, Student2

class studentForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name', 'last_name', 'nick_name',
                    'password', 'age', 'e_mail', 'number_phone', 'github']
		#q = forms.CharField(label='search',
         #             widget=forms.TextInput(attrs={'placeholder': 'Search'}))		
		widgets = {
           # telling Django your password field in the mode is a password input on the template
		    'name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
			'nick_name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
        	'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
			'age': forms.NumberInput(attrs={'placeholder': 'Age', 'min': 18}),
			'e_mail': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
			'number_phone': forms.NumberInput(attrs={'placeholder': 'Phone'}),
           	'github': forms.URLInput(attrs={'placeholder': 'Github'})
        }
		subject = forms.CharField(max_length=100, help_text='100 characters max.')
