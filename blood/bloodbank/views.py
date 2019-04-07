from django.shortcuts import render
from .models import Admin, Donor, Organisation, StateCity, Inbox

# Admin Login //////////////////////////////////////////////////////////////
def onLogin(request):
    ad = request.POST.get("admin")
    apass = request.POST.get("password")
    qs = Admin.objects.filter(username=ad, password=apass)
    if not qs:
        return render(request,"adminLogin.html",{"message":"Invalid User Or Password"})
    else:
        return render(request,"admin.html",{"message":"Welcome"})

# Donor steps /////////////////////////////////////////////////////////////
def donorreg(request):
    return render(request,"donorReg.html")

def onRegister(request):
    return render(request,"registrationDonor.html")

def saveDonor(request):
    na = request.POST.get("name")
    iid = request.POST.get("uid")
    upass = request.POST.get("pwd")
    gender = request.POST.get("m")
    email = request.POST.get("email")
    contact = request.POST.get("contact")
    bgroup = request.POST.get("bgroup")
    state = request.POST.get("state")
    city = request.POST.get("city")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    lddate = request.POST.get("lddate")
    Donor(name=na,userId=iid,password=upass,gender=gender,email=email,contact=contact,bloodgroup=bgroup,state=state,city=city,age=age,weight=weight,ldd=lddate).save()
    return render(request,"saveDonor.html")

def onDonorlogin(request):
    uid = request.POST.get("admin")
    upass = request.POST.get("password")
    qs = Donor.objects.filter(userId=uid,password=upass)
    if not qs:
        return render(request,"donorReg.html",{"message":"Invalid User Or Password"})
    else:
        return render(request,"donor.html")

# organization Steps ////////////////////////////////////////////////////////////
def organisation(request):
    return render(request,"organizationlogin.html")

# FAQS Problems /////////////////////////////////////////////////////////////////
def faqs(request):
    return render(request,"faqs.html")
#
#////////////////////////////////////////////////////////////////////////////////
# Donor Info
def leftDonor(request):
    return render(request,"aboutDonors.html")


def leftDonorNext(request):
    city = StateCity.objects.all()
    return render(request, "aboutDonorsNext.html",{"data":city})

def leftDonorSecondNext(request):
    qs = Donor.objects.all()
    return render(request, "aboutDonorsSecondNext.html",{"data":qs})
#
# Blood Bank Info //////////////////////////////////////////////////
def leftBloodBank(request):
    return render(request, "aboutBloodBank.html")

def leftBloodBankNext(request):
    city = StateCity.objects.all()
    return render(request,"aboutonBankNext.html",{"data":city})

def leftBloodBanksecondNext(request):
    qs = Organisation.objects.filter(orgtype="Blood Bank")
    return render(request,"aboutonSecondBankNext.html",{"data":qs})
#
# Hospital Info ///////////////////////////////////////////////////////
def lefthospital(request):
    return render(request,"aboutHospital.html")

def leftHospitalNext(request):
    city = StateCity.objects.all()
    return render(request,"aboutonHospitalNext.html",{"data":city})

def leftHospitalSecondNext(request):
    qs = Organisation.objects.filter(orgtype="Hospital")
    return render(request,"aboutonSecondHospitalNext.html",{"data":qs})
#
# Clinic Info /////////////////////////////////////////////////////////
def leftclinic(request):
    return render(request,"aboutClinic.html")

def leftonClinicNext(request):
    city = StateCity.objects.all()
    return render(request,"aboutonClinicNext.html",{"data":city})

def leftonClinicSecondNext(request):
    qs = Organisation.objects.filter(orgtype="Clinic")
    return render(request,"aboutonSecondClinicNext.html",{"data":qs})
#
# Additon By Admin (state and city)
def stateCity(request):
    return render(request,"stateCity.html")

def saveStateDetails(request):
    state = request.POST.get("state")
    city = request.POST.get("city")
    StateCity(state=state,city=city).save()
    return render(request,"stateCity.html",{"message":"Details Saved"})

#Additon By Admin (organization)
def organisationReg(request):
    return render(request,"organisationReg.html")

def organisationSave(request):
    orgname = request.POST.get("orgname")
    password = request.POST.get("password")
    type = request.POST.get("type")
    state = request.POST.get("state")
    city = request.POST.get("city")
    cno = request.POST.get("contact")

    Organisation(orgname=orgname,password=password,orgtype=type,state=state, city=city,contact=cno).save()
    return render(request, "organisationReg.html",{"message":"Organization Details Saved"})

#By Admin (profile view)
def profilesView(request):
    return render(request,"profiles.html")

def profilesViewOfDonor(request):
    qs = Donor.objects.all()
    return render(request,"donorprofile.html",{"data":qs})

def profilesViewOfOrg(request):
    qs = Organisation.objects.all()
    return render(request,"orgProfile.html",{"data":qs})


def organisationLogin(request):
    return render(request,"orgOnLogin.html")

def logout(request):
    return render(request,"home.html")

#left Admin suggetion
def suggetion(request):
    return render(request,"suggetion.html")

# FAQS message
def inboxTo(request):
    us =request.POST.get("user")
    msg = request.POST.get("message")
    Inbox(userId=us,message=msg).save()
    return render(request,"faqs.html",{"message":"Message sent"})

#inbox
def inbox(request):
    qs = Inbox.objects.all()
    return render(request,"inbox.html",{"data":qs})
