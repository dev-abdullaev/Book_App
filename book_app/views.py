from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    books = Book.objects.all()
    context = {'file': Book.objects.all(), 'books': books}
    return render(request, 'index.html', context)


def add(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = BookForm(request.POST or None, request.FILES)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('index')
            else:
                form = BookForm()

            context = {'form': form}
            return render(request, 'add.html', context)

        else:
            return redirect('index')

    return redirect('login')


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})


def edit(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('detail', id)
    else:
        form = BookForm(instance=book)

    return render(request, 'update.html', {'book': book, 'form': form})


def delete(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('index')

    return render(request, 'delete.html', {'book': book})


def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(content_type='application/upload_file'))
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404

    return render(request, 'book_detail.html', context)
