from django.contrib.auth.models import AbstractUser # type: ignore
from decouple import config # type: ignore
from django.db import models # type: ignore
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from django.core.mail import send_mail # type: ignore


EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=str, default=True)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    photo  = models.ImageField(default='Profiles/default-user.png', upload_to='Profiles', blank=True, null=True)
    profesion = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(max_length=50, null=True)
    linkedin = models.URLField(max_length=50, null=True)
    facebook = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        try:
            subject = 'Bienvenido a ABC blog'
            message = str('Hola, ' + instance.full_name + ', usted se ha registrado satisfactoriamente al blog.'
                                                '¡Es un placer que seas parte de nuestra familia!'),
                
            
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [instance.email]
            )

        except Exception as e:
            print('Error al enviar email:', e)
