from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inqbook/', views.inqbook, name='inqbook'),
    path('addstyle/', views.addstyle, name='addstyle'),
    path('style/', views.style, name='style'),
    path('addbook/', views.addbook, name='addbook'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('edit/', views.edit, name='edit'),
    path('editbook/', views.editbook, name='editbook'),
    path('editbooks/', views.editbooks, name='editbooks'),
    path('isedit/', views.isedit, name='isedit'),
    path('delbook/', views.delbook, name='delbook'),
    path('delbooks/', views.delbooks, name='delbooks'),
    path('isdel/', views.isdel, name='isdel'),
    path('isdelbook/', views.isdelbook, name='isdelbook'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('addstudents/', views.addstudents, name='addstudents'),
    path('inqstudent/', views.inqstudent, name='inqstudent'),
    path('isStudent/', views.isStudent, name='isStudent'),
    path('student/', views.student, name='student'),
    path('editstudent/', views.editstudent, name='editstudent'),
    path('editstudents/', views.editstudents, name='editstudents'),
    path('editStudent/', views.editStudent, name='editStudent'),
    path('delstudent/', views.delstudent, name='delstudent'),
    path('delstudents/', views.delstudents, name='delstudents'),
    path('isdelstudent/', views.isdelstudent, name='isdelstudent'),
    path('addmanager/', views.addmanager, name='addmanager'),
    path('isaddmanager/', views.isaddmanager, name='isaddmanager'),
    path('delmanager/', views.delmanager, name='delmanager'),
    path('isdelmanager/', views.isdelmanager, name='isdelmanager'),
    path('logout/', views.logout, name='logout'),
    path('returnBook/', views.returnBook, name='returnBook'),
    path('borrowBook/', views.borrowBook, name='borrowBook'),
    path('isborrowBook/', views.isborrowBook, name='isborrowBook'),
    path('ReturnBook/', views.ReturnBook, name='ReturnBook'),
]
