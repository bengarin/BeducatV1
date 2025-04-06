from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identifiant'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Le nom d'utilisateur ne peut pas être vide.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Le mot de passe ne peut pas être vide.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            if username == password:
                raise forms.ValidationError("Le nom d'utilisateur et le mot de passe ne peuvent pas être identiques.")
        
        return cleaned_data


class ChangerAuthForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nouveau mot de passe'}))
    conf_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}))
    
    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if not new_password:
            raise forms.ValidationError("Le mot de passe ne peut pas être vide.")
        return new_password

    def clean_conf_password(self):
        conf_password = self.cleaned_data.get('conf_password')
        if not conf_password:
            raise forms.ValidationError("La confirmation du mot de passe ne peut pas être vide.")
        return conf_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        conf_password = cleaned_data.get('conf_password')

        if new_password and conf_password:
            if new_password != conf_password:
                raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        return cleaned_data
