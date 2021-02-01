def handle_uploaded_file(f):
    with open('book_app/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
