from django.test import TestCase
from .models import Image, location, category
import datetime as dt


class  ImageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new location and saving it
        self.location = location(name = 'Testlocation')
        self.location.save()

        # Creating a new editor and saving it
        self.image= Image(image = "/images", name = "TestImage", description = "A image for testing", location =self.location )
        self.image.save_image()
        # Testing  instance
    
        # Creating a new category and saving it
        self.category = category(name = 'Testcategory')
        self.category.save()

        self.image.categories.add(self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()

