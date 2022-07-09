from django import forms
from django.contrib.auth.models import User
from django.core import validators

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه عبور'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمی باشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
        label='تکرار کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است')
        return email
