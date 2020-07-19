from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from book_selling.models import Author, Book, PurchaseRequest
from book_selling.serializers import BookSerializer, AuthorSerializer
from book_selling.utils import send_superuser_emails


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return JsonResponse(data=serializer.data, status=200)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return JsonResponse(data=serializer.data, status=200, json_dumps_params={'ensure_ascii': False}, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_purchase_request(request):
    book_id = request.data.get('book_id') # Create all validators:
    comment = request.data.get('comment')
    tel_number = request.data.get('tel')
    user = request.user
    book = Book.objects.get(pk=book_id)
    purchase_request = PurchaseRequest(book=book, user=user, tel_number=tel_number, comment=comment)
    purchase_request.save()
    send_superuser_emails.delay('Title example', 'email body')
    return JsonResponse(data='ok', status=200, safe=False)