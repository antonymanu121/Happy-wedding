from django.urls import path
from wed import views

urlpatterns=[
   
    path('home/',views.index.as_view(),name="home"),
    path('vendor-register/',views.vendorRegview.as_view(),name="vendor-register"),
    path('category/<int:pk>/detail',views.categorylist.as_view(),name="cat-det"),
    path('vendor/<int:pk>/detail',views.vendordetail.as_view(),name="vendor-det"),
    path('Login/',views.signinviews.as_view(),name="login"),
    path('Logout/',views.signoutview.as_view(),name="logout"),
    path('enquiry/',views.enquiryview.as_view(),name="enquiry"),
    path('dashboard/',views.DashboardView.as_view(),name='dash'),
    path('vendorlisting/',views.vendorlist.as_view(),name='vendor-list')

]

    
    