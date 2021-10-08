from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, int_list_validator

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	mobile = forms.CharField(max_length=10,
    validators=[int_list_validator(sep=''),MinLengthValidator(10),], 
    required=True)

	class Meta:
		model = User
		fields = ("username", "mobile", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.mobile = self.cleaned_data['mobile']
		if commit:
			user.save()
		return user