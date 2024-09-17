from django.db import models
from django.contrib.auth.models import User

# Message2クラス
class Message2(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
        related_name='message2_owner')
    owner_name = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    good_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content) + '(' + str(self.owner) + ')'
    
    class Meta:
        ordering = ('-pub_date',)
        

# Good2クラス
class Good2(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
        related_name='good2_owner')
    message2 = models.ForeignKey(Message2, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '"' + str(self.message2) + '" (by ' + \
            str(self.owner) + ')'
    
    class Meta:
        ordering = ('-pub_date',)

# Create your models here.
