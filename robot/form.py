from django import forms
from robot.models import Person

class PersonForm(forms.Form):
    # school 
    SCHOOL=((0,'เชียงราย'),
        (1,'พิษณุโลก'),
        (2,'ลพบุรี'),
        (3,'เลย'),
        (4,'มุกดาหาร'),
        (5,'บุรีรัมย์'),
        (6,'ปทุมธานี '),
        (7,'ชลบุรี'),
        (8,'เพรชบุรี'),
        (9,'นครศรีธรรมราช'),
        (10,'ตรัง'),
        (11,'สตูล'),)
    # contesttype
    CONTESTTYPE = ((0,"WRO2019 ระดับมัธยมศึกษาตอนต้น"),
                    (1,"WRO2019 ระดับมัธยมศึกษาตอนปลาย"),
                    (2,"หุ่นยนต์ระดับกลาง ระดับมัธยมศึกษาตอนต้น"),(3,"หุ่นยนต์ระดับกลาง ระดับมัธยมศึกษาตอนปลาย"),)
    # gender
    GENDER =((0,"ชาย"),(1,"หญิง"),(2,"อื่น ๆ"))
    # size
    SIZE = ((0,"S"),(1,"M"),(2,"L"),(3,"XL"),)
    # food
    FOOD = ((0,"อาหารทั่วไป / Normal Food"),(1,"อาหารฮาลาล / HALAL Food"),)

    # make form
    name1 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your name "}))
    name2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your name "}))
    name3 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your name "}))
    tname = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your name "}))

    phone1 = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Phone number"}))
    phone2 = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Phone number"}))
    phone3 = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Phone number"}))
    tphone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your Phone number"}))
    email1 = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your E-mail Address"}))
    email2 = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your E-mail Address"}))
    email3 = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your E-mail Address"}))
    temail = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder":"Please write your E-mail Address"}))


    
    # school
    school = forms.ChoiceField(widget=forms.Select, required=True,choices=SCHOOL)
    # contesttype
    contesttype = forms.ChoiceField(widget=forms.Select,choices=CONTESTTYPE,required=True)

    # gender
    gender1 = forms.ChoiceField(widget=forms.Select,choices=GENDER,required=True)
    gender2 = forms.ChoiceField(widget=forms.Select,choices=GENDER,required=True)
    gender3 = forms.ChoiceField(widget=forms.Select,choices=GENDER,required=True)
    tgender = forms.ChoiceField(widget=forms.Select,choices=GENDER,required=True)

    # size
    size1 = forms.ChoiceField(widget=forms.Select,choices=SIZE,required=True)
    size2 = forms.ChoiceField(widget=forms.Select,choices=SIZE,required=True)
    size3 = forms.ChoiceField(widget=forms.Select,choices=SIZE,required=True)
    tsize = forms.ChoiceField(widget=forms.Select,choices=SIZE,required=True)

    # food
    food1 = forms.ChoiceField(widget=forms.Select, required=True,choices=FOOD)
    food2 = forms.ChoiceField(widget=forms.Select, required=True,choices=FOOD)
    food3 = forms.ChoiceField(widget=forms.Select, required=True,choices=FOOD)
    tfood = forms.ChoiceField(widget=forms.Select, required=True,choices=FOOD)

    # allergy
    allergy1 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"If you have food allergy, write your food allergy."}))
    allergy2 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"If you have food allergy, write your food allergy."}))
    allergy3 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"If you have food allergy, write your food allergy."}))
    tallergy = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder":"If you have food allergy, write your food allergy."}))


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('school','contesttype','name','phone','email','size','gender','food','allergy')

        def __init__(self, *args, **kwargs):
            super(PersonModelForm, self).__init__(*args, **kwargs)
            self.fields["allergy"].required = False