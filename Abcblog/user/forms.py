from django import forms # type: ignore 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm # type: ignore

from user.models import Profile # type: ignore

from django.contrib.auth import get_user_model # type: ignore

User = get_user_model() # type: ignore

class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))

    full_name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))

    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Correo'}))

    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User

        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):

    username = forms.CharField(label=False, help_text=None, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))

    password = forms.CharField(label=False, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    
    class Meta: 
        model = User
        
        fields = [
            'username',
            'password',
            ]


class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None,
                               label='Nombre de usuario')
    
    full_name = forms.CharField(help_text=None,
                                label='Nombre completo')
    
    email = forms.EmailField(label='Correo')

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label='Foto',
                             help_text=None,
                             required=False,
                             widget=forms.FileInput())
    about = forms.CharField(label='about',
                            help_text=None,
                            required=False,
                            widget=forms.TextInput())
    profesion =forms.CharField(label='profesion',
                               help_text=None,
                               required=None,
                               widget=forms.TextInput())
    birthday = forms.DateField(label='birthday',
                               help_text=None,
                               required=True,
                               widget=forms.DateInput())
    twitter =forms.MultipleChoiceField(label='twitter',
                                       help_text=None,
                                       required=None,
                                       widget=forms.Textarea())
    linkedin = forms.MultipleChoiceField(label='linkedin',
                                         help_text=None,
                                         required=None,
                                         widget=forms.Textarea())
    facebook = forms.MultipleChoiceField(label='facebook',
                                         help_text=None,
                                         required=True,
                                         widget=forms.Textarea())

    
    class Meta:
        model = Profile
        fields = [
            'photo',
            'about',
            'profesion',
            'birthday',
            'twitter',
            'linkedin',
            'facebook',
        ]

class PaswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(label=False, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña actual'}))

    new_password1 = forms.CharField(label=False, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}))

    new_password2 = forms.CharField(label=False, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]