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
        return render(self.request, self.template_name)


class RobotInputView(TemplateView):
    template_name = "input.html"

    # GETリクエスト from toppage
    def get(self, request, *args, **kwargs):
        context = {'form': PersonForm()} # for school
        return render(self.request, self.template_name, context)
    
    # POSTリクエスト from confirm
    # TODO
    def post(self, request):
        person_form=PersonForm(request.POST)
        form_list = person_form.cleaned_data
        if person_form.is_valid() ==False: 
           # 指定されたフォームでフォームオブジェクトを作成 
            form_list = PersonForm() 
            # 作成されたフォームオブジェクトをコンテキストへ格納         
            # 最初にブラウザから呼び出されたときに指定テンプレートとコンテキストで描画する 

        context = {'form': form_list} 
        return render(self.request, self.template_name, context)

class RobotConfirmView(TemplateView):
    template_name = "confirm.html"

    # TODO ここのデータ類は辞書型にしたほうがよさそう
    SCHOOL = ('PHITSANULOK','CHIANGRAI','CHONBURI','TRANG','NAKORNSITHAMMARAT','LOPBURI','LOEI','MUKDHAHAN','PATHUMTHANI','SATUN','PHETCHABURI','BURIRAM')
    # gender
    SEX=('MAN','WOMAN')

    # size of shirts
    SIZE=('S','M','L','XL')
    
    # type of contest 
    # TODO
    CONTEST=("WROLOW","WROHIGH","ROBOTLOW","ROBOTHIGH")

    # food
    FOOD=("ALL","MUSLIM")

    def post(self, request):
        post_data = request.POST
        #TODO 画面に表示させるデータの扱い　クエリをDB登録に使用するため
        #ここでvalidationする？
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

# TODO 不正データ入力時の動作　画面クエリの変換をここでする？
class RobotCompleteView(TemplateView):
    template_name = "complete.html"

    def post(self, request):
        person=Person()
        # # 画面のデータをvalueの形式に変換しないとDB登録できないので変換する
        # update_request=request.POST.copy().update({
        #     "school":person.SCHOOL[request.POST["school"]],
        #     "gender":person.GENDER[request.POST["gender"]],
        #     "contesttype":person.CONTESTTYPE[request.POST["contesttype"]],
        #     "size":person.SIZE[request.POST["size"]],
        #     "food":person.FOOD[request.POST["food"]],
        # })
        form=PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
        else:
            # TODO LOGGER
            print("Regist Error invalid data.",form.errors)
        return render(self.request, self.template_name)