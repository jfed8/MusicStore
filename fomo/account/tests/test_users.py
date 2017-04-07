from django.test import TestCase
from account import models as amod
from datetime import datetime, date
from django.contrib.auth.models import Permission, Group

class UserTestCase(TestCase):
    def test_create_user(self):
        '''Tests validity of createing user'''
        u1 = amod.FOMOUser()
        u1.username = 'harry'
        u1.set_password('harryizkool')
        u1.last_login = datetime.now()
        u1.first_name = 'Harry'
        u1.last_name = 'Reid'
        u1.email = 'harry@gmail.com'
        u1.is_staff = False
        u1.is_superuser = False
        u1.is_active = True
        u1.date_joined = datetime.now()
        u1.address = '12th Street'
        u1.city = 'Provo'
        u1.state = 'UT'
        u1.zipcode = '84135'
        u1.phone = '4567894353'
        u1.pref_contact = 'voice'
        u1.birthday = date(2000, 3, 15)
        u1.gender = 'M'
        u1.save()


        u2 = amod.FOMOUser.objects.get(id=u1.id)

        for setup in amod.FOMOUser.objects.filter(id=1).values():
            for field in setup:
                self.assertEquals(getattr(u1, field), getattr(u2, field))


    def test_user_group(self):
        '''Tests changing a user's group'''
        '''Create User'''
        u1 = amod.FOMOUser()
        u1.username = 'harry'
        u1.set_password('harryizkool')
        u1.last_login = datetime.now()
        u1.first_name = 'Harry'
        u1.last_name = 'Reid'
        u1.email = 'harry@gmail.com'
        u1.is_staff = False
        u1.is_superuser = False
        u1.is_active = True
        u1.date_joined = datetime.now()
        u1.address = '12th Street'
        u1.city = 'Provo'
        u1.state = 'UT'
        u1.zipcode = '84135'
        u1.phone = '4567894353'
        u1.pref_contact = 'voice'
        u1.birthday = date(2000, 3, 15)
        u1.gender = 'M'
        u1.save()

        '''Create Groups'''
        groups = {'Customers', 'Employees'}
        for g in groups:
            group = Group()
            group.name = g
            group.save()

        group = Group.objects.get(name='Customers')
        group.user_set.add(u1)

        ###Assign user new group
        u2 = amod.FOMOUser.objects.get(id=u1.id)
        u2.groups.clear()
        newgroup = Group.objects.get(name='Employees')
        u2.groups.add(newgroup)
        u2.save()

        u3 = amod.FOMOUser.objects.get(id=u2.id)

        u3groups = u3.groups.all()
        u2groups = u2.groups.all()


        self.assertEquals(u3groups[0], u2groups[0])
