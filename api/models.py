from django.db import models

# Create your models here.
class YtVideos(models.Model):
  video_id = models.CharField(
    null = False,
    blank = False,
    max_length = 300
  )
  titles = models.CharField(
    null = False,
    blank = False,
    max_length = 500
  )
  desc = models.TextField(
    null = False,
    blank = False,
    max_length = 10000
  )
  publishersDate = models.DateTimeField()
  thumbnails = models.URLField()
  chnl_id = models.CharField(
    null = False,
    blank = False,
    max_length = 300
  )
  chnl_title = models.CharField(
    null = False,
    blank = False,
    max_length = 500
  )
created_at = models.DateTimeField(auto_now_add=True,null=True)