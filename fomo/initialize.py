import os, os.path, sys
from django.core import management
from django.db import connection
from datetime import date, datetime


# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

#imports for our project
from account.models import FOMOUser
from catalog import models as cmod
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from decimal import Decimal
# List all current permissions
# for p in Permission.objects.all():
#     print(p.codename)

# Change color for print statements
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
#Example Print Statement: print(R + '\nQuery 3: Prints all female users\n' + W)


'''Function to Create Permission'''
def CreatePermission(content_type, codename, name):
    content_type = ContentType.objects.get_for_model(content_type)  #Content Type = FOMOUser
    permission = Permission.objects.create(
    codename=codename,
    name=name,
    content_type=content_type,
    )
    print(R + '>>>>> Created Permission: ', codename + W)

CreatePermission(cmod.RentalProduct, 'rent_product', 'Can Rent a Product')
CreatePermission(cmod.Product, 'buy_product', 'Can Buy a Product')
CreatePermission(FOMOUser, 'manager_menu', 'Can access manager menu')
CreatePermission(FOMOUser, 'change_self', 'Can edit own information')


'''Function to Create Group'''
def CreateGroup(name, permissions):
    group = Group()
    group.name = name
    group.save()
    for permission in permissions:
        group.permissions.add(Permission.objects.get(codename=permission))
    print(R + '>>>>> Created Group:', name + W)

# Initialize Groups
#CreateGroup('Administrator', permissions= Permission.objects.all())
CreateGroup('UserManagers', permissions = ['add_fomouser', 'change_fomouser', 'delete_fomouser', 'manager_menu', 'change_self'])
CreateGroup('ProductManagers', permissions = ['add_product', 'change_product', 'delete_product', 'manager_menu', 'change_self'])
CreateGroup('Employees', permissions = ['change_product', 'change_fomouser', 'manager_menu', 'change_self'])
CreateGroup('Customers', permissions = ['buy_product', 'rent_product', 'change_self'])


'''Function to Create Users'''
def CreateUser(Username, Password, First_name, Last_name, Email, Is_staff, Is_superuser, Is_active, jyear, jmonth, jday, Address, City, State, Zipcode, Phone, Pref_contact, byear, bmonth, bday, Gender):
    user = FOMOUser()
    user.username = Username
    user.set_password(Password)
    user.last_login = datetime.now()
    user.first_name = First_name
    user.last_name = Last_name
    user.email = Email
    user.is_staff = Is_staff
    user.is_superuser = Is_superuser
    user.is_active = Is_active
    user.date_joined = date(jyear, jmonth, jday)
    user.address = Address
    user.city = City
    user.state = State
    user.zipcode = Zipcode
    user.phone = Phone
    user.pref_contact = Pref_contact
    user.birthday = date(byear, bmonth, bday)
    user.gender = Gender
    user.save()
    print(R + ">>>>> Created User: ", Username + W)





'''Initialize User Data'''
#CreateUser(Username,   Password,       First_name,     Last_name,  Email,                      Is_staff,   Is_superuser,   Is_active,  jyear,  jmonth, jday,   Address,        City,       State,  Zipcode,    Phone,          Pref_contact,   byear,  bmonth, bday,   Gender)
CreateUser('kyardley',  '123!@#qweQWE', 'Klynt',        'Yardley',  'klynt.yardley@gmail.com',  True,       True,           True,       2001,   1,      1,      '830 N 100 W',  'Provo',    'UT',   '84604',    '4355313456',   'text',         1993,   9,      10,     'M') #kyardley
CreateUser('byardley',  '123!@#qweQWE', 'Bonnie',       'Yardley',  'bonnie.yardley@gmail.com', False,      False,          True,       2001,   1,      1,      '123 Ave',      'Las Vegas','NV',   '78204',    '7026897894',   'text',         1993,   12,     29,     'F') #byardley
CreateUser('lyardley',  '123!@#qweQWE', 'Lynn',         'Yardley',  'lynn.yardley@gmail.com',   False,      False,          True,       2001,   1,      1,      '270 W 200 S',  'Beaver',   'UT',   '84713',    '4354211759',   'email',        1954,   12,     12,     'M') #lyardley
CreateUser('myardley',  '123!@#qweQWE', 'Melissa',      'Yardley',  'melissa.yardley@gmail.com',False,      False,          True,       2001,   1,      1,      '270 W 200 S',  'Beaver',   'UT',   '84713',    '4354211758',   'voice',        1964,   3,      2,      'F') #myardley
CreateUser('zyardley',  '123!@#qweQWE', 'Zane',         'Yardley',  'zane@mailinator.com',      False,      False,          True,       2005,   12,     12,     '321 Street',   'Beaver',   'UT',   '84713',    '4355314569',   'text',         1999,   1,      1,      'M') #zyardley


#Change kyardley's permissions
# u1 = FOMOUser.objects.get(username= 'kyardley')
# p = Permission.objects.get(codename= 'add_fomouser')
# u1.user_permissions.add(p)

def AddToGroup(username, groupname):
    user = FOMOUser.objects.get(username=username)
    group = Group.objects.get(name=groupname)
    group.user_set.add(user)
    print(R + ">>>>> Added: ", user.username, 'to ', group.name + W)

AddToGroup('lyardley', 'ProductManagers')
AddToGroup('myardley', 'UserManagers')
AddToGroup('byardley', 'Employees')
AddToGroup('zyardley', 'Customers')



'''Function to Create Categories'''
def CreateCategory(codename, name):
    category = cmod.Category()
    category.codename = codename
    category.name = name
    category.save()
    print(R + '>>>>> Created Category:', category.name + W)

'''Initialize Categories'''
CreateCategory('string', 'String Instrument')
CreateCategory('brass', 'Brass Instrument')
CreateCategory('woodwind', 'Woodwind Instrument')
CreateCategory('accessory', 'Accessory')
CreateCategory('percussion', 'Percussion')





'''Function to Create BulkProduct'''
def CreateBulkProduct(name, cat_codename, description, price, graphic, barcode, quantity, reorder_trigger, reorder_quantity):
    bulkproduct = cmod.BulkProduct()
    bulkproduct.name = name
    cat1 = cmod.Category.objects.get(codename=cat_codename)
    bulkproduct.category = cat1
    bulkproduct.description = description
    bulkproduct.price = Decimal(price)
    bulkproduct.graphic = graphic
    bulkproduct.barcode = barcode
    bulkproduct.quantity = quantity
    bulkproduct.reorder_trigger = reorder_trigger
    bulkproduct.reorder_quantity = reorder_quantity
    bulkproduct.save()
    print(R + '>>>>> Created BulkProduct:', bulkproduct.name + W)

'''Initialize BulkProduct'''
# CreateBulkProduct(name,           cat_codename,  description,   price,      graphic,       barcode,        quantity,  reorder_trigger, reorder_quantity):
CreateBulkProduct(  'Drumsticks',   'accessory',  'If you are going to rock, rock hard with these bad boys',   '15.99',    'drumsticks.svg',   '01234567890',  40,         5,              50)
CreateBulkProduct(  'Microphone',   'accessory',  'The perfect gift for aspiring singers...no matter how bad they may be.',    '25.99',    'microphone.svg',    '01274569890',  5,          1,             10)
CreateBulkProduct(  'Amplifier',    'accessory',  'Buy this if you like LOUD MUSIC!!!',     '9.50',     'amplifier.svg',     '11374969890',  20,         5,        30)
CreateBulkProduct(  'Headphones',    'accessory',  'Dislike interacting with the outside world? Then buy these.',       '14.50',     'headphones.svg',     '234569890',  8,         5,        30)

'''Function to Create UniqueProduct'''
def CreateUniqueProduct(name, cat_codename, description, price, graphic, serial_number, condition):
    uniqueproduct = cmod.UniqueProduct()
    uniqueproduct.name = name
    cat1 = cmod.Category.objects.get(codename=cat_codename)
    uniqueproduct.category = cat1
    uniqueproduct.description = description
    uniqueproduct.price = Decimal(price) #Decimal() is a constructor call
    uniqueproduct.graphic = graphic
    uniqueproduct.serial_number = serial_number
    uniqueproduct.condition = condition
    uniqueproduct.save()
    print(R + '>>>>> Created UniqueProduct:', uniqueproduct.name + W)

'''Initialize UniqueProduct'''
#CreateUniqueProduct(name,      cat_codename,  description,   price,      graphic,  serial_number,  condition):
CreateUniqueProduct('Tuba',     'brass', 'This instrument sounds horrible no matter what. Perfect for beginners.',       '129.99',   'tuba.svg',     'YWByK2Fe',     'used')
CreateUniqueProduct('Trombone', 'brass',  'I once knew a guy who would have married his trombone if it was legal.',      '129.99',   'trombone.svg', 'zrQsPhub',     'used')
CreateUniqueProduct('Oboe',     'woodwind', 'The truth is no one has actually ever seen an Oboe, but I guess it is a thing.',    '99.50',    'oboe.svg',     'asdfasdf',     'new')
CreateUniqueProduct('Violin', 'string',    'My wife plays this and she is super hot!...So does Jaden...:)',     '89.99',    'violin.svg',   'Gboc9Suj',       'used')
CreateUniqueProduct('Xylophone', 'percussion',  "The cool man's piano." , '119.99',    'xylophone.svg', 'Acg39Suj',    'used')
CreateUniqueProduct('Saxophone', 'woodwind',  "Kenny G will have nothing on you after you buy this sweet item.",  '129.99',    'saxophone.svg', 'Wb1c9Suj',    'new')

'''Function to Create RentalProduct'''
def CreateRentalProduct(name, cat_codename, description, price, graphic, serial_number, is_rented, condition, due_year, due_month, due_day):
    rentalproduct = cmod.RentalProduct()
    rentalproduct.name = name
    cat1 = cmod.Category.objects.get(codename=cat_codename)
    rentalproduct.category = cat1
    rentalproduct.description = description
    rentalproduct.price = Decimal(price) #Decimal() is a constructor call
    rentalproduct.graphic = graphic
    rentalproduct.serial_number = serial_number
    rentalproduct.is_rented = is_rented
    rentalproduct.condition = condition

    if due_year != 0:
        rentalproduct.due_date = date(due_year, due_month, due_day)
    rentalproduct.save()
    print(R + '>>>>> Created RentalProduct:', rentalproduct.name + W)

'''Initialize RentalProduct'''
#CreateRentalProduct(name, cat_codename, price, graphic, serial_number, is_rented, condition, due_date):



'''Function to Add detail images to products'''
def AddProductImages(product_name, path1, path2, path3):
    product = cmod.Product.objects.get(name = product_name)
    i1 = cmod.ProductPicture()
    i1.product = product
    i1.path = path1
    i1.save()
    i2 = cmod.ProductPicture()
    i2.product = product
    i2.path = path2
    i2.save()
    i3 = cmod.ProductPicture()
    i3.product = product
    i3.path = path3
    i3.save()
    print(R + '>>>>> Added 3 pictures for :', product.name + W)

AddProductImages('Amplifier', 'catalog/media/detail_imgs/amplifier/amplifier-1.jpg', 'catalog/media/detail_imgs/amplifier/amplifier-2.jpg', 'catalog/media/detail_imgs/amplifier/amplifier-3.jpg')
AddProductImages('Drumsticks', 'catalog/media/detail_imgs/drumsticks/drumsticks-1.jpg', 'catalog/media/detail_imgs/drumsticks/drumsticks-2.jpg', 'catalog/media/detail_imgs/drumsticks/drumsticks-3.jpg')
AddProductImages('Headphones', 'catalog/media/detail_imgs/headphones/headphones-1.jpg', 'catalog/media/detail_imgs/headphones/headphones-2.jpg', 'catalog/media/detail_imgs/headphones/headphones-3.jpg')
AddProductImages('Microphone', 'catalog/media/detail_imgs/microphone/microphone-1.jpg', 'catalog/media/detail_imgs/microphone/microphone-2.jpg', 'catalog/media/detail_imgs/microphone/microphone-3.jpg')
AddProductImages('Oboe', 'catalog/media/detail_imgs/oboe/oboe-1.jpg', 'catalog/media/detail_imgs/oboe/oboe-2.jpg', 'catalog/media/detail_imgs/oboe/oboe-3.jpg')
AddProductImages('Saxophone', 'catalog/media/detail_imgs/saxophone/saxophone-1.jpg', 'catalog/media/detail_imgs/saxophone/saxophone-2.jpg', 'catalog/media/detail_imgs/saxophone/saxophone-3.jpg')
AddProductImages('Trombone', 'catalog/media/detail_imgs/trombone/trombone-1.jpg', 'catalog/media/detail_imgs/trombone/trombone-2.jpg', 'catalog/media/detail_imgs/trombone/trombone-3.jpg')
AddProductImages('Tuba', 'catalog/media/detail_imgs/tuba/tuba-1.jpg', 'catalog/media/detail_imgs/tuba/tuba-2.jpg', 'catalog/media/detail_imgs/tuba/tuba-3.jpg')
AddProductImages('Violin', 'catalog/media/detail_imgs/violin/violin-1.jpg', 'catalog/media/detail_imgs/violin/violin-2.jpg', 'catalog/media/detail_imgs/violin/violin-3.jpg')
AddProductImages('Xylophone', 'catalog/media/detail_imgs/xylophone/xylophone-1.jpg', 'catalog/media/detail_imgs/xylophone/xylophone-2.jpg', 'catalog/media/detail_imgs/xylophone/xylophone-3.jpg')
