from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date       
from django.contrib.auth.models import Permission
# Create your models here.
class Book(models.Model):
    title=models.CharField('Title',max_length=300)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(null=True,blank=True)
    genre=models.ManyToManyField('Genre',help_text='select the genre for this book')
    isbn  =models.CharField('ISBN',max_length=20,help_text='13 digit unique international code')

    def display_genre(self):
        "creating the string of genre" 
        return ','.join(genre.name for genre in self.genre.all())

    display_genre.short_description = 'Genreeee'     
    class Meta:
        ordering=['title']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
       
        return reverse('book-detail', args=[str(self.id)])


class Genre(models.Model):
    name=models.CharField('Genre',max_length=30,help_text='enter genre like fiction,action,romantic ')

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField("Name",max_length=200)
    dateofbith=models.DateField("Birth-date",null=True,blank=True)
    dateofdeath=models.DateField("Died",null=True,blank=True)

    def __str__(self):
        return self.name

    #  get_absolute-url is used for creating the url of this modelclass
    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])



class Bookinstances(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='unique id for this part of the book across library')
    book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    imprint=models.CharField(max_length=300)
    due_back=models.DateField(null=True,blank=True)
    loan_status=[('m','Maintenance'),('o','onloan'),('r','reserved'),('a','available')]


    status=models.CharField(max_length=40,choices=loan_status,default='m',help_text='Book Avalilability')

    borrower=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    
    class Meta:
        permissions= (("can_mark_returned","set book as returned "),)
        ordering=['id']
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


    
    def __str__(self):  
        return ('{0} {1}'.format(self.id,self.book.title))



    

