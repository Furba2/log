from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField()
    
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField()

    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        return f"{self.text[:10]}..."

      
class Chapter(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.text[:10]}..."
