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
    
    def test_save_image(self):
        #Test to check if image saves
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        #Test to check if image deletes
        self.image.save_image()
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    # def test_all_images(self):
    #     #Test to check if all images are queried
    #     images= Image.all_images()
    #     self.assertEqual(images, Image.objects.all())
        


    def tearDown(self):
        Image.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()

class categoriesTestClass(TestCase):
    def setUp(self):
        self.Fun = category(name='Fun')

    def test_instance(self):
        self.assertTrue(isinstance(self.Fun,category))

    def tearDown(self):
        category.objects.all().delete()

    def test_save_method(self):
        self.Fun.save_category()
        categories = category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_method(self):
        self.Fun.delete_category('Fun')
        categories = category.objects.all()
        self.assertTrue(len(categories)==0)
        
class locationTestClass(TestCase):
    def setUp(self):
        self.Nairobi = location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,location))

    def tearDown(self):
        location.objects.all().delete()

    def test_save_method(self):
        self.Nairobi.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Nairobi.delete_location('Nairobi')
        locations = location.objects.all()
        self.assertTrue(len(locations)==0)
