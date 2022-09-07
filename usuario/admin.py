from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreateForm, UsuarioChangeForm

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
  list_per_page = 10
  add_form = UsuarioCreateForm
  form = UsuarioCreateForm
  model = Usuario
  list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
  readonly_fields = ['last_login', 'date_joined', 'password']
  fieldsets = (
   ('Login', {'fields' : ('email','password')}),
   ('Informações', {'fields' : ('first_name', 'last_name')}),
   ('Permissões', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
   ('Datas Importantes', {'fields' : ('last_login', 'date_joined')})

  )



  # add_fieldsets = (
  # (None, {'fields' : ('username', 'password1', 'password2')}),
  # )
