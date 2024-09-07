from django import forms
from courses.models.newsletter import Subscribers, MailMessage


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'