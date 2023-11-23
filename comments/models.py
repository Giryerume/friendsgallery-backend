from django.db import models
from photos.models import Photo

# Create your models here.
class Comment(models.Model):
    user=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    photo=models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
