from django.db import models


# Create your models here.
class HotList(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.TextField(null=True)
    title = models.TextField(null=True)
    count = models.TextField(null=True)
    link = models.TextField(null=True)
    image = models.TextField(null=True)
    source = models.TextField(null=True)

    def __str__(self):
        return "id: "+str(self.id)+ ", 제목: "+self.title
