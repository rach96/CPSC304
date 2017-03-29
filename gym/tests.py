from django.test import TestCase
from .sql_tables import Customer1

# Create your tests here.


# class Customer1(models.Model ):
#     cusID = models.IntegerField()
#     cusName = models.CharField( max_length= 30)
#     curPhoneNumber = models.IntegerField(max_length=10)


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer1.create(12345, "Rachel", 6047256348)
        Customer1.create(12346, "Tiff", 6047253957)

    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     cus1 = Customer1.objects.get(name="Rachel")
    #     cus2 = Customer1.objects.get(name="Tiff")
    #     self.assertEqual(, 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')