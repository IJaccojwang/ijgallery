from django.test import TestCase
from .models import images, location, category
import datetime as dt


class  ImageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.image= Image(image = "/images", name = "TestImage", description = "A image for testing",)
        self.image.save_image()
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

        # Creating a new category and saving it
        self.category = tags(name = 'Testcategory')
        self.category.save()

        # Creating a new location and saving it
        self.location = tags(name = 'Testlocation')
        self.location.save()

        self.image.location.add(self.location)
        self.image.category.add(self.category)

    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()

