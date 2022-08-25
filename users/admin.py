from django.contrib import admin
from django.apps import apps

from users.models import User

admin.site.register(User)

# if there are any models in graphql_auth, register them
apps = apps.get_app_config("graphql_auth")

for model_name, model in apps.models.items():
    admin.site.register(model)