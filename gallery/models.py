from django.db import models
import datetime as dt 


class location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,category):
        cls.objects.filter(category=category).delete()


class category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()


class Image(models.Model):
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
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image(cls, name):
        images = cls.objects.filter(name__icontains=name)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images
    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.filter(id = id)
        return images