from django.test import TestCase
from .models import Customer1

# Create your tests here.


# class Customer1(models.Model ):
#     cusID = models.IntegerField()
#     cusName = models.CharField( max_length= 30)
#     curPhoneNumber = models.IntegerField(max_length=10)


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer1.objects.create(cusID=12345, cusName="Rachel", cusPhoneNumber = 6047256348)
        Customer1.objects.create(cusID=12346, cusName="Tiff", cusPhoneNumber = 6047253957)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')