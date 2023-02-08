from django.db import models

class Topic(models.Model):
    """Theme, that read user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return string value of model
        return self.text

class Entry(models.Model):
    # Information
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Get topic by key
    text = models.TextField() # Add text
    date_added = models.DateTimeField(auto_now_add=True) #Add date

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if self.text.length < 50: #Check length
            return f"{self.text}"
        return f"{self.text[:50]}..."