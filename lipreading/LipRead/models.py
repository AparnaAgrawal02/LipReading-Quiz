from django.db import models

# Create your models here.
class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")


    def __str__(self):
        return self.name + ": " + str(self.videofile)


class quiz(models.Model):
    question_num = models.IntegerField()
    selected_answer = models.CharField(max_length=500)

    def __str__(self):
        return str(self.question_num) + ": " + self.selected_answer