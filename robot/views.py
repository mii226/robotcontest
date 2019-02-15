from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,FormView

from django.template.context_processors import csrf
from robot.form import PersonForm,PersonModelForm
from robot.models import *


class RobotTopView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        context = super(RobotTopView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)


class RobotInputView(TemplateView):
    template_name = "input.html"

    # GETリクエスト
    def get(self, request, *args, **kwargs):
        # context = super(RobotInputView, self).get_context_data(**kwargs)
        context = {'form': PersonForm()} 
        return render(self.request, self.template_name, context)
        
    
    # POSTリクエスト
    def post(self, request):
        person_form=PersonForm(request.POST)
        form_list = person_form.cleaned_data
        if person_form.is_valid() ==False: 
           # 指定されたフォームでフォームオブジェクトを作成 
            form_list = PersonForm() 
            # 作成されたフォームオブジェクトをコンテキストへ格納             # 最初にブラウザから呼び出されたときに指定テンプレートとコンテキストで描画する 

        context = {'form': form_list} 
        print(context)
        return render(self.request, self.template_name, context)

class RobotConfirmView(TemplateView):
    template_name = "confirm.html"

    SCHOOL = ('PHITSANULOK','CHIANGRAI','CHONBURI','TRANG','NAKORNSITHAMMARAT','LOPBURI','LOEI','MUKDHAHAN','PATHUMTHANI','SATUN','PHETCHABURI','BURIRAM')
    # gender
    SEX=('MAN','WOMAN')

    # size of shirts
    SIZE=('S','M','L','XL')
    
    # type of contest
    CONTEST=("","","","")
    WROLOW = 0
    WROHIGH = 1
    ROBOTLOW = 2
    ROBOTHIGH = 3

    # food
    FOOD=("ALL","MUSLIM")
    def get(self, request, *args, **kwargs):
        context = super(RobotConfirmView, self).get_context_data(**kwargs)

        person = Person.objects.all()  # データベースからオブジェクトを取得して
        context['person'] = person  # 入れ物に入れる
        return render(self.request, self.template_name, context)

    def post(self, request):
        post_data = request.POST
        person_form=PersonForm()
        context ={
            "fname":post_data.get("fname"),
            "lname":post_data.get("lname"),
            "school":self.SCHOOL[int(post_data.get("school"))],
            "gender":self.SEX[int(post_data.get("gender"))],
            "contesttype":self.CONTEST[int(post_data.get("contesttype"))],
            "phone":post_data.get("phone"),
            "email":post_data.get("email"),
            "size":self.SIZE[int(post_data.get("size"))],
            "food":self.FOOD[int(post_data.get("food"))],
            "tfname":post_data.get("tfname"),
            "tlname":post_data.get("tlname"),
            }
        return render(self.request, self.template_name, context)

class RobotCompleteView(TemplateView):
    template_name = "complete.html"

    def post(self, request):
        person=Person()
        form=PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
        else:
            print("Regist Error invalid data.")
        return render(self.request, self.template_name)