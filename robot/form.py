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
        (11,'BURIRAM'),)
    # contesttype
    CONTESTTYPE = ((0,"TYPE1"),(1,"TYPE2"),(2,"TYPE3"),(3,"TYPE4"),)
    # gender
    GENDER =((0,"MAN"),(1,"WOMAN"),)
    # size
    SIZE = ((0,"S"),(1,"M"),(2,"L"),(3,"XL"),)
    # food
    FOOD = ((0,"ALL"),(1,"MUSLIM"),)

    # make form
    lname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Lastname "}))
    fname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your FamilyName "}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Phone number"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your E-mail Address"}))
    tlname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your teacher's Lastname "}))
    tfname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your teacher's FamilyName "}))
    
    # school
    school = forms.ChoiceField(widget=forms.Select, required=True,choices=SCHOOL)
    # contesttype
    contesttype = forms.ChoiceField(widget=forms.RadioSelect,choices=CONTESTTYPE,required=True)
    # gender
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER,required=True)
    # size
    size = forms.ChoiceField(widget=forms.RadioSelect,choices=SIZE,required=True)
    # food
    food = forms.ChoiceField(widget=forms.RadioSelect, required=True,choices=FOOD)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('school','contesttype','lname','fname','phone','email','size','gender','food','tlname','tfname')