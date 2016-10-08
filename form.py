from django import forms
class SignupForm(forms.Form):
    username = forms.CahrField(
        label=_("username"),
        max_length=30,
    )

    email = forms.EmailField(label=_('email'),)
    password_1 = forms.CharField(
        label=_("password"),
        widget=forms.PasswordInput,
    )
    password_2 = forms.CharField(
        label=_("password_confirmed"),
        widget=forms.PasswordInput,
    )

    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError(_('password confirm failed'))
        return password_2