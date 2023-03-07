from django import forms


class postjobform(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    jobtitle = forms.CharField(max_length=20)
    worktype = forms.CharField(max_length=20)
    experiencerequired = forms.CharField(max_length=20)
    jobtype = forms.CharField(max_length=20)


class regform(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    dob = forms.DateField()
    qualification = forms.CharField(max_length=25)
    phoneno = forms.IntegerField()
    password = forms.CharField(max_length=20)
    cspassword = forms.CharField(max_length=20)


class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class applyjobform1(forms.Form):
    qualification=forms.CharField(max_length=20)
    phone=forms.IntegerField()
    exp=forms.IntegerField()
    resume=forms.FileField()

