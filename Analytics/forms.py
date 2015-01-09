from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User

class GenerateReportForm(forms.Form):
    APPAREL_PRICE_CHOICES = (
        ('1', '1000-2000'), ('2', '2000-3000'),
        ('3', '3000-4000'), ('4', '4000-5000'),
        ('5', '5000-6000'), ('6', '6000-7000'),
        ('7', '7000-8000'), ('8', '8000-9000'),
        ('9', '9000-10000'),
    )
    ACTION_CHOICES = (('1', 'Tried Apparels'),
        ('2', 'Shared on Facebook'),
        ('3', 'Shared on Google+'),
        ('4', 'Followed Apparels')
        )
    price = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=APPAREL_PRICE_CHOICES)
    action = forms.MultipleChoiceField(required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=ACTION_CHOICES)

class RegisterForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput(),
    #                            required=True)
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                 'email',]

class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput,
                               required=True)
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password']

