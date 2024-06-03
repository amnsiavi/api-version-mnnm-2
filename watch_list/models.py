from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        
        return self.name


class WatchList(models.Model):
    
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default = datetime.now())
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name='watch_list')
    
    
    def __str__(self):
        
        return self.title

class Review(models.Model):
    
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField()
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='review')
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        
        return f'{self.rating}  {self.watchlist}' 