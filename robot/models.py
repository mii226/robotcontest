from django.db import models

# Create your models here.

class Person(models.Model):
    # gender
    GENDER = {"MAN":0,"WOMAN":1}

    # size of shirts
    SIZE = {
        "S":0,
        "M":1,
        "L":2,
        "XL":3
        }
    # school 
    SCHOOL = {
        "PHITSANULOK":0,
        "CHIANGRAI":1,
        "CHONBURI":2,
        "TRANG":3,
        "NAKORNSITHAMMARAT":4,
        "LOPBURI":5,
        "LOEI":6,
        "MUKDHAHAN":7,
        "PATHUMTHANI":8,
        "SATUN":9,
        "PHETCHABURI":10,
        "BURIRAM":11
        }

    # type of contest
    CONTESTTYPE={
    "WROLOW":0,
    "WROHIGH":1,
    "ROBOTLOW":2,
    "ROBOTHIGH":3
    }
    # food
    FOOD={"ALL":0,"MUSLIM":1}

    # school
    school = models.CharField(max_length=128)
    # contesttype
    contesttype = models.CharField(max_length=128)
    # last name
    lname = models.CharField(max_length=128)
    # first name
    fname = models.CharField(max_length=128)
    # phone
    phone = models.IntegerField()
    # email
    email = models.CharField(max_length=128)
    # tshirts size
    size = models.CharField(max_length=128)
    # sex
    gender = models.CharField(max_length=128)
    # food
    food = models.CharField(max_length=128)
    # teacher last name
    tlname = models.CharField(max_length=128)
    # teacher first name
    tfname = models.CharField(max_length=128)
    # register time
    # register_at = models.DateTimeField()