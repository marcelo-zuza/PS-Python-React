from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('nome', 'username', 'email')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['username']
        user.nome = self.cleaned_data['nome']
        if commit:
            user.save()
        return user




class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('nome',)

