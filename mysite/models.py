from django.db import models
from django.contrib.auth.models import User

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = value = models.TextField()
    date_inclusion = models.DateTimeField(auto_now_add=True)
    user_inclusion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'modelo'
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name