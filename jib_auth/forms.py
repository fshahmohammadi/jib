from django import forms

class login_form(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class upgrade_form(forms.Form):
	receipt = forms.IntegerField()

class register_form(forms.Form):
	name = forms.CharField(required = True)
	lname = forms.CharField(required = True)
	username = forms.CharField(required = True)
	password = forms.CharField(widget=forms.PasswordInput, required = True)
	confirm = forms.CharField(widget=forms.PasswordInput, required = True)
	email = forms.EmailField(required = True)
