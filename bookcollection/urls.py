from django.urls import path
from bookcollection  import views

'''
make sure to check space blanks in paths path("",views...)
'''
urlpatterns =[
    path("",views.index,name='catalog'),
    path("books/",views.booklist,name='books'),
    path("book/<int:pk>/",views.bookdetails,name="book-detail"),
    path("author/",views.author,name='author'),
    path("author/<int:pk>/",views.authordetail,name='author-detail'),
    path("borrowed",views.loanbook.as_view(),name='borrowed'),
    path("allbooks",views.my_staff,name='allbooks'),
    path('book/<uuid:pk>/userrenew/',views.userrenewsystem,name='userrenewsystem'),
    path('book/<uuid:pk>/renew/',views.renewsystem,name='renew-system'),
    path('available',views.availale,name='available'),
    path('issued/<uuid:pk>/issue',views.issuesystem,name='issue'),
    

    
]   