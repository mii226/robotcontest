from django import forms
from robot.models import Person

class PersonForm(forms.Form):

    # school 
    SCHOOL=((0,'PHITSANULOK'),
        (1,'CHIANGRAI'),
        (2,'CHONBURI'),
        (3,'TRANG'),
        (4,'NAKORNSITHAMMARAT'),
        (5,'LOPBURI'),
        (6,'LOEI'),
        (7,'MUKDHAHAN'),
        (8,'PATHUMTHANI'),
        (9,'SATUN'),
        (10,'PHETCHABURI'),
        (11,'BURIRAM'))

    # school
    school = forms.ChoiceField(required=True,choices=SCHOOL)

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('school','contesttype','lname','fname','tel','email','size','gender','food','tlname','tfname')