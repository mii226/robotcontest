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
        request.session.delete()
        return render(self.request, self.template_name)


class RobotInputView(TemplateView):
    template_name = "input.html"

    # GETリクエスト from toppage
    def get(self, request, *args, **kwargs):
        # school_form.school
        context={"form":PersonForm()}     
        # from confirm page
        if request.session.get("fname") is not None:
            context.update({
                    "form":PersonForm(initial=request.session),
                    "fname":request.session.get("fname"),
                    "lname":request.session.get("lname"),
                    "phone":request.session.get("phone"),
                    "email":request.session.get("email"),
                    "tfname":request.session.get("tfname"),
                    "tlname":request.session.get("tlname"),
                    })

        return render(self.request, self.template_name, context)

class RobotConfirmView(TemplateView):
    template_name = "confirm.html"

    SCHOOL = ('PHITSANULOK','CHIANGRAI','CHONBURI','TRANG','NAKORNSITHAMMARAT','LOPBURI','LOEI','MUKDHAHAN','PATHUMTHANI','SATUN','PHETCHABURI','BURIRAM')
    # gender
    GENDER=('MAN','WOMAN')

    # size of shirts
    SIZE=('S','M','L','XL')
    
    # type of contest 
    CONTEST=("WROLOW","WROHIGH","ROBOTLOW","ROBOTHIGH")

    # food
    FOOD=("ALL","MUSLIM")

    # TODO def get ()

    def post(self, request):
        post_data = request.POST
        form_data = {
            "fname":post_data.get("fname"),
            "lname":post_data.get("lname"),
            "school":post_data.get("school"),
            "gender":post_data.get("gender"),
            "contesttype":post_data.get("contesttype"),
            "phone":post_data.get("phone"),
            "email":post_data.get("email"),
            "size":post_data.get("size"),
            "food":post_data.get("food"),
            "tfname":post_data.get("tfname"),
            "tlname":post_data.get("tlname"),}
        # save input data to session
        request.session.update(form_data)
        # make data for screen
        form_data.update({
            "school":self.SCHOOL[int(post_data.get("school"))],
            "gender":self.GENDER[int(post_data.get("gender"))],
            "contesttype":self.CONTEST[int(post_data.get("contesttype"))],
            "size":self.SIZE[int(post_data.get("size"))],
            "food":self.FOOD[int(post_data.get("food"))],
            })
        context = form_data
        # make screen
        return render(self.request, self.template_name, context)

class RobotCompleteView(TemplateView):
    template_name = "complete.html"

    def post(self, request):
        person=Person()
        form=PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            person=form.save(commit=False)
            person.save()
            # delete session because complete register
            request.session.delete()
        else:
            # TODO LOGGER
            print("Regist Error invalid data.",form.errors)
        return render(self.request, self.template_name)