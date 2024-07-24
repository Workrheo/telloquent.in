from django.db import models
from enum import unique
from accounts.models import User, UserProfile
from accounts.utils import send_notification
from datetime import time, date, datetime




# Create your models here.
class Architect(models.Model):
    user = models.OneToOneField(User, related_name='architect_user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='architect_userprofile', on_delete=models.CASCADE)
    architect_name = models.CharField(max_length=1000)
    architect_slug = models.SlugField(max_length=1000, unique=True)
    architect_license = models.ImageField(upload_to='Architect/license')
    architect_description = models.TextField(null=True , blank=True)
    offical_number = models.PositiveIntegerField(null=True, blank=True)
    website = models.CharField(max_length=50 , null=True, blank=True)
    experience = models.PositiveIntegerField(null=True , blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.architect_name
    

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Update
            orig = Architect.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                mail_template = 'accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                    'to_email': self.user.email,
                }
                if self.is_approved == True:
                    #Send notification email
                    mail_subject = "Congratulations! Your firm Portfolio has been approved."
                    send_notification(mail_subject, mail_template, context)
                else:
                    # Send notification email
                    mail_subject = "We're sorry! You are not eligible for publishing your Portfolio on our marketplace."
                    send_notification(mail_subject, mail_template, context)
        return super(Architect, self).save(*args, **kwargs)
    


DAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]

HOUR_OF_DAY_24 = [(time(h, m).strftime('%I:%M %p'), time(h, m).strftime('%I:%M %p')) for h in range(0, 24) for m in (0, 30)]
class Architect_OpeningHour(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS)
    from_hour = models.CharField(choices=HOUR_OF_DAY_24, max_length=10, blank=True)
    to_hour = models.CharField(choices=HOUR_OF_DAY_24, max_length=10, blank=True)
    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ('day', '-from_hour')
        unique_together = ('architect', 'day', 'from_hour', 'to_hour')

    def __str__(self):
        return self.get_day_display()
    


class Architect_ProjectImages(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='projectimages/', blank=True, null=True)

    def __str__(self):
        return self.architect.architect_name

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

class Architect_OfficeImages(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='projectimages/', blank=True, null=True)

    def __str__(self):
        return self.architect.architect_name
    


    class Meta:
        verbose_name = 'Architect_OfficeImage'
        verbose_name_plural = 'Architect_OfficeImages'
