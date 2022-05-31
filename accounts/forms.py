from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        # self.fields['full_name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['username'].widget.attrs['placeholder'] = 'Your username'

        # self.fields['message'].widget.attrs['placeholder'] = 'Enter your message'
