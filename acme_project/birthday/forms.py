from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=20, required=True)
    last_name = forms.CharField(
        label="Фамилия", required=False, help_text="Необязательное поле")
    birthday = forms.DateField(
        required=True, label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
        )
