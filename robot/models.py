from django.db import models

# Create your models here.

class Person(models.Model):
    # gender
    MAN = 0
    WOMAN = 1

    # size of shirts
    SIZES = 0
    SIZEM = 1
    SIZEL = 2
    SIZEXL = 3

    # school 
    PHITSANULOK = 0
    CHIANGRAI = 1
    CHONBURI = 2
    TRANG = 3
    NAKORNSITHAMMARAT = 4
    LOPBURI = 5
    LOEI = 6
    MUKDHAHAN = 7
    PATHUMTHANI = 8
    SATUN = 9
    PHETCHABURI = 10
    BURIRAM = 11

    # type of contest
    WROLOW = 0
    WROHIGH = 1
    ROBOTLOW = 2
    ROBOTHIGH = 3

    # food
    ALL = 0
    MUSLIM = 1

    # school
    school = models.IntegerField()
    # contesttype
    contesttype = models.IntegerField()
    # last name
    lname = models.CharField(max_length=128)
    # first name
    fname = models.CharField(max_length=128)
    # tel
    tel = models.IntegerField()
    # email
    email = models.EmailField()
    # tshirts size
    size = models.IntegerField()
    # sex
    gender = models.IntegerField()
    # food
    food = models.IntegerField()
    # teacher last name
    tlname = models.CharField(max_length=128)
    # teacher first name
    tfname = models.CharField(max_length=128)
    # register time
    # register_at = models.DateTimeField()