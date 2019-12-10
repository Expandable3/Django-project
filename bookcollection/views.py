import datetime
from django.shortcuts import render ,get_object_or_404
from bookcollection.models import Book,Author,Bookinstances,Genre,layout
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User ,Permission
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from bookcollection.forms import renewalbookform,issuessystemform
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    book_request=Book.objects.all().count()
    author_request=Author.objects.all().count()
    book_copies=Bookinstances.objects.all().count()
    book_available=Bookinstances.objects.filter(status='a').count()
    image=layout.objects.all()
    print(image)
    context={
        'numbook':book_request,
        'numauthor':author_request,
        'numcopies':book_copies,
        'numavailable':book_available,
        'image':image,
    }

    return render(request,'bookcollection/home.html',context=context)


# using the class based generic list view  ListView


def booklist(request):
    book=Book.objects.all()
    context={'bookinfo':book}
    return render (request,'bookcollection/book.html',context=context)



def bookdetails(request,pk):
    
    try:
        book=Book.objects.get(pk=pk)
    
    except Book.DoesNotExist:
            raise Http404("Book-detail does not exist")

    
    return render(request,'bookcollection/book-detail.html',context={'book':book})


def author(request):
    authorinfo=Author.objects.all()
    context={'authorinfo':authorinfo}
    return render(request,'bookcollection/author.html',context=context)


def authordetail(request,pk):
    try:
        author=Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        raise Http404('author-details does not exit')

    return render(request,'bookcollection/author-details.html',context={'authordetail':author})

'''
def loanbook(request):

    loan=Bookinstances.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back')
    return render(request,'bookcollection/loaned-book.html',context={'loanedbook':loan})
'''

class loanbook(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Bookinstances
    template_name ='bookcollection/loaned-book.html'
    user=User.objects.all()
    print(user) 

    
    def get_context_data(self,**kwargs):
          context = super(loanbook, self).get_context_data(**kwargs)
          context['bookborrow']= Bookinstances.objects.filter(borrower=self.request.user).order_by('due_back')
          return context




''' 
    def get_queryset(self):
        print(self.request.user)
        print(Bookinstances.objects.filter(borrower=self.request.user).order_by('due_back'))
        return Bookinstances.objects.filter(borrower=self.request.user).order_by('due_back')

'''
# @permission_required('staff')
@permission_required('bookcollection.can_mark_returned')
def my_staff(request):
    
    users=User.objects.all()
    print(users)
    booklist=Bookinstances.objects.all()
    return render(request,'bookcollection/allbooks.html',context={'users':users,'booklist':booklist})    

# @permission_required('bookcollection.can_mark_returned')
# @permission_required('bookcollection.can_renew')
def renewsystem(request,pk):
    book_instance=get_object_or_404(Bookinstances,pk=pk)   
    print(book_instance)
    if request.method=='POST':  
        renewform=renewalbookform(request.POST)
        if renewform.is_valid():
            # safe the new date into the database
            book_instance.due_back=renewform.cleaned_data['renew']

            book_instance.save()
            return HttpResponseRedirect(reverse('allbooks'))


    else:
        
        suggested=datetime.date.today() + datetime.timedelta(weeks=3)
        # making new form
        renewform=renewalbookform(initial={'renew':suggested})
        
    context={
        'renewform':renewform,
        'book_instance':book_instance,
        }

    return render(request,'bookcollection/renewsystem.html',context)




def userrenewsystem(request,pk):
    book_instance=get_object_or_404(Bookinstances,pk=pk)   
    print(book_instance)
    if request.method=='POST':  
        renewform=renewalbookform(request.POST)
        if renewform.is_valid():
            # safe the new date into the database
            book_instance.due_back=renewform.cleaned_data['renew']
            print("useruser is gooing it")

            book_instance.save()
            return HttpResponseRedirect(reverse('borrowed'))

    else:
        
        suggested=datetime.date.today() + datetime.timedelta(weeks=3)
        # making new form
        renewform=renewalbookform(initial={'renew':suggested})
        
    context={
        'renewform':renewform,
        'book_instance':book_instance,
        }

    return render(request,'bookcollection/renewsystem.html',context)






def availale(request):
    book=Book.objects.all()
    context={'book':book}
    return render(request,'bookcollection/available.html',context=context)


def issuesystem(request,pk):
    bookinst=Bookinstances.objects.get(pk=pk)
    if request.method=='POST':
        renewform=issuessystemform(request.POST)
        if renewform.is_valid():
            bookinst.due_back=renewform.cleaned_data['due_date']
            bookinst.borrower=renewform.cleaned_data['borrower']
            bookinst.status='o'
            bookinst.save()
            return HttpResponseRedirect(reverse('allbooks'))

    
    else: 
        suggested=datetime.date.today() + datetime.timedelta(weeks=3)
        # making new form
        
        renewform=issuessystemform(initial={'due_date':suggested})

    context={
        'renewform':renewform,
        'bookinst':bookinst,
    }
    return render(request,'bookcollection/issuesystem.html',context=context)


