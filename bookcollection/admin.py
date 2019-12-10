from django.contrib import admin
from bookcollection.models import  Book,Genre,Author,Bookinstances,layout
# Register your models here.
#admin.site.register(Book)
admin.site.register(Genre)
#admin.site.register(Author)
#admin.site.register(Bookinstances)
admin.site.register(layout)
class bookinline(admin.TabularInline):
    model=Book



## editing the admin interface
#Define the admin class
#helps in showing the name ,dateofbirth and dateofdeath togther
class Authoradmin(admin.ModelAdmin):
    list_display=('name','dateofbith','dateofdeath')
    inlines=[bookinline]
    print("sahil")

admin.site.register(Author,Authoradmin)



# admin.TabularInline  helps in showing records inline with other records horizontally

class bookinstances(admin.TabularInline):
    #entering the model name to be inline some other model
    model= Bookinstances
    print("SAHIL")


    


class Bookadmin(admin.ModelAdmin):
    list_display=['title','author','display_genre','isbn']
    inlines=[bookinstances]
    print('LLLLLLLLLLLLL')


admin.site.register(Book,Bookadmin)

class BookinstancesAdmin(admin.ModelAdmin):
    #list_filter = ('status', 'due_back')

    # fieldsets can be used to divide the no of columb into 2 different section
    fieldsets=(
        (None,{
            'fields':('id','book1')  
            }),
        ('Availability',
        {'fields':('due_back','status','borrower')}),
    )
    print("okkkkkkkkkkkk")



admin.site.register(Bookinstances,BookinstancesAdmin)





