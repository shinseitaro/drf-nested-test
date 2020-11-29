from django.db import models

class District(models.Model):
    district_name = models.CharField(max_length=10)

    def __str__(self):
        return self.district_name 

class Information(models.Model):
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.text[:20] 


class Library(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    info = models.OneToOneField(Information, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name 

class Author(models.Model):
    author_name = models.CharField(max_length=20)

    def __str__(self):
        return self.author_name 


class Category(models.Model):
    division = models.CharField(max_length=10)

    def __str__(self):
        return self.division 

class Book(models.Model):
    ## 共著は無いものとする
    title = models.CharField(max_length=20)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ManyToManyField(Library)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="Non-genre")

    def __str__(self):
        return self.title 