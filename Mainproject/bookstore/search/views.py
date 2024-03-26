from django.shortcuts import render
from shop.models import Book
from django.db.models import Q
# Create your views here.
def search(request):
    q=""
    book=None
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
            book=Book.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))

    return render(request,'search.html',{'p':book,'query':q})