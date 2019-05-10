from django.db import models
import datetime as dt 
from django.db.models import Q



class location(models.Model):
    '''
    This is a Class for the location of images
    '''
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        '''
        Method to save new locations
        '''
        self.save()

    @classmethod
    def delete_location(cls,location):
        '''
        Method to delete locations
        '''
        cls.objects.filter(name=location).delete()
    
    @classmethod
    def update_location(cls,location, new_location):
        '''
        Method to update locations
        '''
        cls.objects.filter(name=location).update(name=new_location)


class category(models.Model):
    '''
    This is a Class for the category of images
    '''
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        Method to save new categories
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        '''
        Method to save new categories
        '''
        cls.objects.filter(name=category).delete()
    


class Image(models.Model):
    '''
    image Class for all images added to the app
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(category)
    location = models.ForeignKey(location)
   

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-post_date']
    
    def save_image(self):
        '''
        Method to save new images
        '''
        self.save()
    
    def delete_image(self):
        '''
        Method to delete images
        '''
        self.delete()
    
    @classmethod
    def all_images(cls):
        '''
        Method to view all images
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search(cls,search_term):
        '''
        Method to search for images according to category, name or location
        '''
        images = cls.objects.filter(Q(categories__name=search_term) | Q(name__icontains=search_term) | Q(location__name=search_term))

        return images

    @classmethod
    def filter_by_location(cls, location):
        '''
        Method to filter images according to location
        '''
        images = cls.objects.filter(location__name=location)
        return images

    @classmethod
    def filter_by_category(cls, cat):
        '''
        Method to filter images according to category
        '''
        images = cls.objects.filter(categories__name=cat)
        return images

    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method to filter images according to id
        '''
        images = cls.objects.filter(id = id)
        return images