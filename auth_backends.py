
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import email_re


"""
http://djangosnippets.org/snippets/74/
http://pastebin.com/bVfqZY8P
"""
 
class EmailLoginBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        user = None

        #If username is an email address, then try to pull it up
        if email_re.search(username):
            # check email as username
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                pass

            # usernames ARE emails
            try:
                user = User.objects.get(username=username)
            except:
                pass
        else:
            #We have a non-email address username we should try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                pass

        if not user:
            return None

        if user.check_password(password):
            return user

 
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
