from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile, Recipe

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email Already in use.")
        return data
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
    def clean_data(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return data

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Recipe Title', 'class': 'form-control'}),
    )
    cuisine = forms.CharField(
        max_length=50, required=True,
        widget=forms.TextInput(attrs={'placeholder': "Korean, Chinese......etc", 'class': 'form-control'}),
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Description about the Recipe', 'class': 'form-control', 'rows': 5}),
    )
    ingredients = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Description about the Recipe', 'class': 'form-control', 'rows': 5}),
    )
    instructions = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Description about the Recipe', 'class': 'form-control', 'rows': 5}),
    )
    cooking_time = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    servings = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Recipe
        fields = ['title', 'cuisine', 'description', 'ingredients', 'instructions', 'cooking_time', 'servings', 'image']
