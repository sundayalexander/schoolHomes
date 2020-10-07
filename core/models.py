from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils import timezone
from core.states import states
from prototype.settings import settings


class User(AbstractUser):
    title_types = (('Mr.', 'Mr.'),
                   ('Miss.', 'Miss.'),
                   ('Mrs.', 'Mrs.'),
                   ('Dr.', 'Dr.'),
                   ('Prof.', 'Prof.'),
                   )
    title = models.CharField(max_length=100, choices=title_types, null=True, blank=True, default='Mr.')
    user_types = (('Admin', 'Admin'),
                  ('Tutor', 'Tutor'),
                  ('Student', 'Student'),
                  ('Parent', 'Parent'),
                  ('Vendor', 'Vendor'),
                  ('School', 'School'))
    avatar = models.ImageField(null=True, blank=True, upload_to='profile/')
    mobile = models.CharField(unique=True, max_length=13)
    type = models.CharField(max_length=7, choices=user_types, default='Student')
    country = models.CharField(max_length=150, default='Nigeria')
    state = models.CharField(max_length=100, null=True, choices=states)
    email_from_tutor = models.BooleanField(default=True)
    content_suggestion = models.BooleanField(default=True)
    newsletter = models.BooleanField(default=True)
    product_feature = models.BooleanField(default=True)
    updated_at = models.DateTimeField('last updated', auto_now=True)
    created_at = models.DateTimeField('created', auto_created=True, default=timezone.now)

    class Meta:
        db_table = 'user'
        ordering = ('-created_at',)

    def __str__(self):
        return '{} ({})'.format(self.username, self.type)

    # def save(self, *args, **kwargs):
    #
    #     super(User, self).save(*args, **kwargs)


class Domain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255, blank=True, null=True)
