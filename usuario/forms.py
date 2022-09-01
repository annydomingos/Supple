from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioCreateForm(UserCreationForm):
  class Meta:
    fields = ['first_name', 'last_name']
    label = {'username' : 'Email' }

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    user.email = self.cleaned_data['username']
    if commit:
      user.save()
    return user

class UsuarioChangeForm(UserChangeForm):
  class Meta:
    model = Usuario
    fields = ['first_name', 'last_name']

