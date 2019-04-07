
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from bloodbank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Loading First Page
    path('index/',TemplateView.as_view(template_name="home.html")),
    #top menu items
    #admin
    path('adminlog/',TemplateView.as_view(template_name="adminLogin.html")),
    path('onlogin/',views.onLogin),
    path('inbox/',views.inbox),
    #donor
    path('donor/',views.donorreg),
    path('onregister/',views.onRegister),
    path('onregister/iframe.html/',TemplateView.as_view(template_name="iframe.html")),
    path('savedonor/',views.saveDonor),
    path('onDonorlogin/',views.onDonorlogin),
    #organizations
    path('org/',views.organisation),
    path('orgLogin/',views.organisationLogin),
    #faqs
    path('faqs/',views.faqs),
    path("faqsSend/",views.inboxTo),
    #left side menu
    #donor
    path('donorA/',views.leftDonor),
    path('onNext/',views.leftDonorNext),
    path('onSecondNext/',views.leftDonorSecondNext),
    #bloodbanks
    path('bloodA/',views.leftBloodBank),
    path('onBankNext/',views.leftBloodBankNext),
    path('onSecondBankNext/',views.leftBloodBanksecondNext),
    #hospital
    path('hospitalA/',views.lefthospital),
    path('onHospitalNext/',views.leftHospitalNext),
    path('onSecondHospitalNext/',views.leftHospitalSecondNext),
    #Clinic
    path('clinicA/',views.leftclinic),
    path('onClinicNext/',views.leftonClinicNext),
    path('onSecondClinicNext/',views.leftonClinicSecondNext),
    # State Added by Admin
    path('state/',views.stateCity),
    path('saveStateDetails/',views.saveStateDetails),
    #Organization Added by Admin
    path('organisation/',views.organisationReg),
    path('saveOrganizationDetails/',views.organisationSave),
    #
    path('profiles/',views.profilesView),
    path('donorProfiles/',views.profilesViewOfDonor),
    #
    path('organizationProfiles/',views.profilesViewOfOrg),
    # Logout
    path('logout/',views.logout),
    # Suggetion
    path('sugges/',views.suggetion),


]
