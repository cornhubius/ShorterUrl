from django.db import models


class Links(models.Model):
    link = models.CharField(max_length=255)
    short_link = models.CharField(max_length=255, unique=True)
    id_admin = models.ForeignKey(
        'auth.User', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.link}'
