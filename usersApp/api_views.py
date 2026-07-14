import stripe
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Cache the list endpoint for 15 minutes
    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only see their own orders
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_payment_intent(request):
    """
    Create a Stripe PaymentIntent for the given order amount.
    """
    try:
        # In a real app, calculate the amount from the database, not request data
        # to prevent users from tampering with the price.
        # This is a basic example assuming amount is passed in cents.
        data = request.data
        amount = int(data.get('amount', 0))

        if amount <= 0:
            return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return Response({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
