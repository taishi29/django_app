from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
def __str__(self):
    return '<Friend:id=' + str(self.id) + ', ' + \
        self.name + '(' + str(self.age) + ')>'
        
'''
SQL文でいう、CLEATE TABLE文。(設計図)

~SQL文で表すと~
CREATE TABLE Friend (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Djangoが自動的に生成するプライマリキー
    name VARCHAR(100) NOT NULL,
    mail VARCHAR(200) NOT NULL,
    gender BOOLEAN NOT NULL,
    age INTEGER NOT NULL DEFAULT 0,
    birthday DATE NOT NULL
);
'''
# Create your models here.
