import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_menu.models import AuthorModel, BookModel
from app_menu.serializers import AuthorSerializer, BookSerializer


@csrf_exempt
def author_list_create(request):
    if request.method == 'GET':
        # Serialize all authors
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # Deserialize JSON data and create a new author
        data = json.loads(request.body)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()  # Automatically creates a new AuthorModel instance
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        # Deserialize JSON data for updating an existing author
        data = json.loads(request.body)
        author_id = data.get('id')

        try:
            author = AuthorModel.objects.get(id=author_id)  # Find the author by ID
        except AuthorModel.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)

        # Pass the existing author instance and updated data to the serializer
        serializer = AuthorSerializer(author, data=data)

        if serializer.is_valid():
            serializer.save()  # Saves changes to the existing author
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        # Deserialize JSON data for partially updating an existing author
        data = json.loads(request.body)
        author_id = data.get('id')

        try:
            author = AuthorModel.objects.get(id=author_id)  # Find the author by ID
        except AuthorModel.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)

        # Pass the existing author instance and updated data to the serializer
        serializer = AuthorSerializer(author, data=data, partial=True)  # partial=True allows partial updates

        if serializer.is_valid():
            serializer.save()  # Saves changes to the existing author
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Handle DELETE request to remove an existing author
        data = json.loads(request.body)
        author_id = data.get('id')

        try:
            author = AuthorModel.objects.get(id=author_id)  # Find the author by ID
            author.delete()  # Delete the author
            return JsonResponse({'status': 'success', 'message': 'Author deleted'}, status=204)
        except AuthorModel.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)
@csrf_exempt
def book_list_create(request):
    if request.method == 'GET':
        # Serialize all books
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # Deserialize JSON data and create a new author
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()  # Automatically creates a new AuthorModel instance
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        # Deserialize JSON data for updating an existing book
        data = json.loads(request.body)
        book_id = data.get('id')

        try:
            book = BookModel.objects.get(id=book_id)  # Find the author by ID
        except BookModel.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        # Pass the existing author instance and updated data to the serializer
        serializer = BookSerializer(book, data=data)

        if serializer.is_valid():
            serializer.save()  # Saves changes to the existing author
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        # Deserialize JSON data for partially updating an existing author
        data = json.loads(request.body)
        book_id = data.get('id')

        try:
            author = BookModel.objects.get(id=book_id)  # Find the author by ID
        except BookModel.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        # Pass the existing author instance and updated data to the serializer
        serializer = BookSerializer(author, data=data, partial=True)  # partial=True allows partial updates

        if serializer.is_valid():
            serializer.save()  # Saves changes to the existing author
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Handle DELETE request to remove an existing author
        data = json.loads(request.body)
        book_id = data.get('id')

        try:
            book = BookModel.objects.get(id=book_id)  # Find the author by ID
            book.delete()  # Delete the author
            return JsonResponse({'status': 'success', 'message': 'Book deleted'}, status=204)
        except BookModel.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

