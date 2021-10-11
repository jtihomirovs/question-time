from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # In future, if we will need to add new custom fields to user model,
    # we would remove pass instruction and add these new fields
    pass
