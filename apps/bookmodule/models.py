from django.db import models




# class Author(models.Model):
#     fullname = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     address = models.TextField(null=True)
    
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50) 
    price = models.FloatField(default = 0.0) 
    edition = models.SmallIntegerField(default = 1)

    # author = models.ForeignKey(Author, on_delete=models.PROTECT)
    