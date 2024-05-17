from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from wed.models import vendorcategory,vendors,enquiry,vendorlisting
from wed.forms import vendorRegForm,loginForm,enquiryForm,vendorlistForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import TemplateView



class index(ListView):
    model=vendorcategory
    template_name="wed/home.html"
    context_object_name="categories"



class vendorRegview(CreateView):
    form_class=vendorRegForm
    template_name="wed/vendorRegister.html"
    model=vendors
    success_url=reverse_lazy("login")

class categorylist(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=vendorlisting.objects.filter(category_id=id)
        name=vendorcategory.objects.get(id=id)
        return render(request,"wed/vendorcatdetail.html",{"data":data,"name":name})


class vendordetail(View):
     def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=vendorlisting.objects.filter(id=id)
        return render(request,"wed/vendordetail.html",{"data":data})
     

class signinviews(View):
    def get(self, request):
        return render(request, 'wed/signin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve the Realtor object from the database based on the provided username
        try:
            vendor = vendors.objects.get(username=username)
        except vendors.DoesNotExist:
            vendor = None

        if vendor is not None:
            # Check if the provided password matches the password in the database
            if password == vendor.password:
                # Password matches, so log in the realtor
                request.session['logged_in'] = True
                request.session['vendor_id'] = vendor.id
                return redirect('home')  # Redirect to dashboard or any other page
            else:
                # Password does not match
                messages.error(request, 'Invalid password.')
        else:
            # Realtor does not exist
            messages.error(request, 'Realtor does not exist.')
            return redirect('login')

class signoutview(View):
    def get(self,request):
        logout(request)
        return redirect('home')
    

class enquiryview(CreateView):
    model=enquiry
    form_class=enquiryForm
    template_name="wed/enquiry.html"
    success_url=reverse_lazy("home")

class DashboardView(TemplateView):
    template_name = 'wed/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logged_in'):
            # Redirect to login page if user is not logged in
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor_id = self.request.session.get('vendor_id')
        
        # Query UserInquiry objects for the logged-in realtor
        enquiries = enquiry.objects.filter(vendor_id=vendor_id)
        
        # Get the realtor object
        try:
            vendor = vendors.objects.get(id=vendor_id)
        except vendors.DoesNotExist:
            vendor = None
        
        context['enquiries'] = enquiries
        context['vendor'] = vendor
        return context
    

class vendorlist(CreateView):
    template_name="wed/listing.html"
    model=vendorlisting
    form_class=vendorlistForm
    success_url=reverse_lazy("home")

    
    

    
    













    











        
    

  


