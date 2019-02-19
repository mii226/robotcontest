from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,FormView

from django.http import HttpResponseServerError
from django.template.context_processors import csrf
from robot.form import PersonForm,PersonModelForm
from robot.models import *


class RobotTopView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        request.session.delete()
        return render(self.request, self.template_name)


class RobotInputView(TemplateView):
    template_name = "input.html"

    # GETリクエスト from toppage
    def get(self, request, *args, **kwargs):
        # school_form.school
        context={"form":PersonForm()}     
        # from confirm page
        if request.session.get("name1") is not None:
            context.update({"form":PersonForm(initial=request.session)})

        return render(self.request, self.template_name, context)

class RobotConfirmView(TemplateView):
    template_name = "confirm.html"

    SCHOOL = ('โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย เชียงราย',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย พิษณุโลก',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย ลพบุรี',
    ' โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย เลย',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย มุกดาหาร',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย บุรีรัมย์',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย ปทุมธานี',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย ชลบุร',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย เพรชบุรี',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย นครศรีธรรมราช',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย ตรัง',
    'โรงเรียนวิทยาศาสตร์จุฬาภรณราชวิทยาลัย สตูล')
    # gender
    GENDER=('ชาย','หญิง','อื่น ๆ')

    # size of shirts
    SIZE=('S','M','L','XL')
    
    # type of contest 
    CONTEST=("WRO2019 ระดับมัธยมศึกษาตอนต้น",
    "WRO2019 ระดับมัธยมศึกษาตอนปลาย",
    "หุ่นยนต์ระดับกลาง ระดับมัธยมศึกษาตอนต้น",
    "หุ่นยนต์ระดับกลาง ระดับมัธยมศึกษาตอนปลาย")

    # food
    FOOD=("อาหารทั่วไป","อาหารฮาลาล")


    def post(self, request):
        post_data = request.POST

        input_form_data = {
            "school":post_data.get("school"),
            "contesttype":post_data.get("contesttype"),
            "name1":post_data.get("name1"),
            "gender1":post_data.get("gender1"),
            "phone1":post_data.get("phone1"),
            "email1":post_data.get("email1"),
            "size1":post_data.get("size1"),
            "food1":post_data.get("food1"),
            "allergy1":post_data.get("allergy1"),
            "name2":post_data.get("name2"),
            "gender2":post_data.get("gender2"),
            "phone2":post_data.get("phone2"),
            "email2":post_data.get("email2"),
            "size2":post_data.get("size2"),
            "food2":post_data.get("food2"),
            "allergy2":post_data.get("allergy2"),
            "name3":post_data.get("name3"),
            "gender3":post_data.get("gender3"),
            "phone3":post_data.get("phone3"),
            "email3":post_data.get("email3"),
            "size3":post_data.get("size3"),
            "food3":post_data.get("food3"),
            "allergy3":post_data.get("allergy3"),
            "tname":post_data.get("tname"),
            "tgender":post_data.get("tgender"),
            "tphone":post_data.get("tphone"),
            "temail":post_data.get("temail"),
            "tsize":post_data.get("tsize"),
            "tfood":post_data.get("tfood"),
            "tallergy":post_data.get("tallergy"),
        }
        # save input data to session
        request.session.update(input_form_data)
        input_form_data.update({
            "school":self.SCHOOL[int(post_data.get("school"))],
            "contesttype":self.CONTEST[int(post_data.get("contesttype"))],
            "gender1":self.GENDER[int(post_data.get("gender1"))],
            "size1":self.SIZE[int(post_data.get("size1"))],
            "food1":self.FOOD[int(post_data.get("food1"))],
            "gender2":self.GENDER[int(post_data.get("gender2"))],
            "size2":self.SIZE[int(post_data.get("size2"))],
            "food2":self.FOOD[int(post_data.get("food2"))],
            "gender3":self.GENDER[int(post_data.get("gender3"))],
            "size3":self.SIZE[int(post_data.get("size3"))],
            "food3":self.FOOD[int(post_data.get("food3"))],
            "tgender":self.GENDER[int(post_data.get("tgender"))],
            "tsize":self.SIZE[int(post_data.get("tsize"))],
            "tfood":self.FOOD[int(post_data.get("tfood"))],
        })
        # make data for screen
        form_data={            
            "form":PersonForm(initial=input_form_data)            
        }
        context = form_data
        # make screen
        return render(self.request, self.template_name, context)

class RobotCompleteView(TemplateView):
    template_name = "complete.html"

    def post(self, request):
        
        post_data = request.POST
        print(post_data.get("size1"))
        student1 = {
            "school":post_data.get("school"),
            "contesttype":post_data.get("contesttype"),
            "name":post_data.get("name1"),
            "gender":post_data.get("gender1"),
            "phone":post_data.get("phone1"),
            "email":post_data.get("email1"),
            "size":post_data.get("size1"),
            "food":post_data.get("food1"),
            "allergy":post_data.get("allergy1")
            }
        student2 = {
            "school":post_data.get("school"),
            "contesttype":post_data.get("contesttype"),
            "name":post_data.get("name2"),
            "gender":post_data.get("gender2"),
            "phone":post_data.get("phone2"),
            "email":post_data.get("email2"),
            "size":post_data.get("size2"),
            "food":post_data.get("food2"),
            "allergy":post_data.get("allergy2")
            }
        student3 = {
            "school":post_data.get("school"),
            "contesttype":post_data.get("contesttype"),
            "name":post_data.get("name3"),
            "gender":post_data.get("gender3"),
            "phone":post_data.get("phone3"),
            "email":post_data.get("email3"),
            "size":post_data.get("size3"),
            "food":post_data.get("food3"),
            "allergy":post_data.get("allergy3")
            }
        teacher = {
            "school":post_data.get("school"),
            "contesttype":post_data.get("contesttype"),
            "name":post_data.get("tname"),
            "gender":post_data.get("tgender"),
            "phone":post_data.get("tphone"),
            "email":post_data.get("temail"),
            "size":post_data.get("tsize"),
            "food":post_data.get("tfood"),
            "allergy":post_data.get("tallergy")
            }
        person1=Person()
        person2=Person()
        person3=Person()
        person4=Person()        
        form1=PersonModelForm(student1, instance=person1)
        form2=PersonModelForm(student2, instance=person2)
        form3=PersonModelForm(student3, instance=person3)
        form4=PersonModelForm(teacher, instance=person4)

        if form1.is_valid() & form2.is_valid() & form3.is_valid() & form4.is_valid():
            person1=form1.save(commit=False)
            person1.save()
            person2=form2.save(commit=False)
            person2.save()
            person3=form3.save(commit=False)
            person3.save()
            person4=form4.save(commit=False)
            person4.save()
            # delete session because complete register
            request.session.delete()
        else:
            # TODO LOGGER
            print("Regist Error invalid data.",form1.errors,form2.errors,form3.errors,form4.errors)
            raise HttpResponseServerError()
        
        return render(self.request, self.template_name)