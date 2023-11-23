from django.db import models
from photos.models import Photo

# Create your models here.
class Like(models.Model):
    photo=models.ForeignKey(Photo, related_name='likes', on_delete=models.CASCADE)
    user=models.ForeignKey('auth.user', related_name='liked_by', on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.photo.title
