from django.db import models

# Create your models here.

class Song(models.Model):
  title = models.CharField(max_length = 50)
  singer = models.TextField()
  track_time = models.IntegerField()

  def __str__(self):
    return self.title + '  ' + self.singer

class Album(models.Model):
  title = models.CharField(max_length = 100)
  total_songs = models.TextField()
  created_at = models.DateTimeField()
  album_id = models.ForeignKey(Song, on_delete = models.CASCADE)
  is_favourite = models.BooleanField(default = False)

  def __str__(self):
    return self.title