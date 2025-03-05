from django.db import models

class ContactUs(models.Model):
    user_email = models.EmailField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.title
