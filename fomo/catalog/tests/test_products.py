from django.test import TestCase
from catalog import models as cmod
from datetime import datetime, date
from decimal import Decimal


class UserTestCase(TestCase):
    def test_uniqueProduct(self):
        up1 = cmod.UniqueProduct()
        up1.name = 'Elephant Drums'
        cat1 = cmod.Category()
        cat1.codename = 'percussion'
        cat1.name = 'Percussion'
        cat1.save()
        up1.category = cat1
        up1.price = Decimal('100.01') #Decimal() is a constructor call
        up1.graphic = 'drumsticks.svg'
        up1.serial_number = '91274560890'
        up1.condition = 'new'
        up1.save()


        up2 = cmod.UniqueProduct.objects.get(id=up1.id)

        for setup in cmod.UniqueProduct.objects.filter(id=1).values():
            for field in setup:
                self.assertEquals(getattr(up1, field), getattr(up2, field))


    def test_product_category(self):
        '''Tests changing a product's category'''
        '''Create Categories'''
        cat1 = cmod.Category()
        cat1.codename = 'percussion'
        cat1.name = 'Percussion'
        cat1.save()

        cat2 = cmod.Category()
        cat2.codename = 'woodwind'
        cat2.name = 'Woodwind'
        cat2.save()

        '''Create product'''
        up1 = cmod.UniqueProduct()
        up1.name = 'Elephant Drums'
        up1.category = cat1
        up1.price = Decimal('100.01') #Decimal() is a constructor call
        up1.graphic = 'drumsticks.svg'
        up1.serial_number = '91274560890'
        up1.condition = 'new'
        up1.save()

        up2 = cmod.UniqueProduct.objects.get(id=up1.id)
        up2.category = cat2
        up2.save()

        up3 = cmod.UniqueProduct.objects.get(id=up2.id)

        self.assertEquals(up3.category, up2.category)
