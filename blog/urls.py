from django.urls import path
import blog.views as view
urlpatterns=[
    path('all',view.all,name='all_blog'),
    path('<int:id>',view.one,name='get_one'),
    path('edit/<id>',view.edit,name='edit'),
    path('create',view.create,name='create'),
    path('delete/<id>',view.delete,name='delete')
]