from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='invent-home'),
    path('inventory/',views.inventory,name='invent-inventory'),
    path('log/',views.log,name='invent-log'), 
    path('help/',views.help,name='invent-help'),
    path('menu/',views.menu,name='invent-menu'),
    path('inventory/add_item_form_submission',views.add_item_form_submission,name='add_item_form_submission'),
    path('add/<int:id>',views.add,name='invent-add'),
    path('subtract/<int:id>',views.subtract,name='invent-subtract'),
    path('delete/<int:id>',views.delete,name='invent-delete')
]
