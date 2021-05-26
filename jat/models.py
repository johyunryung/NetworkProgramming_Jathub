from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #ropo1.introduction_set

    class Meta:
        verbose_name_plural = 'Repositories'

    def __str__(self):
        return self.name

class Introduction(models.Model):
    repositiory = models.ForeignKey(Repository, on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    contents = models.TextField()


    def __str__(self):
        return f'{self.version} {self.contents}'

class Comment(models.Model):
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
