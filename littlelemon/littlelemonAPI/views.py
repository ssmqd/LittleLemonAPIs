from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status
from .models import MenuItem, Category, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, OrderDetailSerializer, OrderItemSerializer
from datetime import date

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    def post(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)

class CategoryViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def post(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    
class SingelCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().post(request)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get(self, request):
        if request.user.is_authenticated:
            user_cart = self.queryset.filter(user=request.user)
            serializer = self.serializer_class(user_cart, many=True)
            return Response(serializer.data)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(data=request.data, context =  {'request': request})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request):
        if request.user.is_authenticated:
            user_cart = self.queryset.filter(user=request.user)
            user_cart.delete()
            return Response({'message':'Cart successfully deleted'}, status= status.HTTP_200_OK)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Menager').exists():
                user_order = self.queryset.all()
                serializer = self.serializer_class(user_order, many=True)
                return Response(serializer.data)
            if request.user.groups.filter(name='Delivery Crew').exists():
                user_order = self.queryset.filter(delivery_crew=request.user)
                serializer = self.serializer_class(user_order, many=True)
                return Response(serializer.data)
            else:
                user_order = self.queryset.filter(user=request.user)
                serializer = self.serializer_class(user_order, many=True)
                return Response(serializer.data)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request):
        if request.user.is_authenticated:
            if not request.user.groups.filter(name=['Menager', 'Delivery Crew']).exists():
                items = Cart.objects.all()
                if items.exists():
                    order = Order.objects.create(
                        user = request.user,
                        total = 0,
                        date = date.today()
                    )
                    for item in items:
                        OrderItem.objects.create(
                            order=order,
                            menuitem=item.menuitem,
                            quantity=item.quantity,
                            unit_price=item.unit_price,
                            price=item.price
                        )
                        order.total += item.price
                    order.save()
                    items.delete()
                    return Response({'message':'Order was successfully created and cart items deleted'}, status=status.HTTP_201_CREATED)
                return Response({'message':'Your cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    
class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user == order.user:
            return super().get(request, *args, **kwargs)
        
        return Response({'message':'This is not your order'}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = Order.objects.all()
        if request.user.groups.filter(name='Menager').exists():
            if not request.data:
                return Response({"message": "Request must contain data to update."}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(order, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = Order.objects.all()
        if request.user.groups.filter(name='Menager').exists():
            if not request.data:
                return Response({"message": "Request must contain data to update."}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(order, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.user.groups.filter(name='Delivery Crew').exists():
            if not request.data:
                return Response({"message": "Request must contain data to update."}, status=status.HTTP_400_BAD_REQUEST)
            if len(request.data) == 1 and 'status' in request.data:
                serializer = self.serializer_class(order, data= request.data, portial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            return Response({'message':'You can update only status field'})
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = Order.objects.all()
        if request.user.group.filter(name='Menager').exists():
            self.delete(order)
            return Response({"message": "Order deleted"}, status = status.HTTP_403_FORBIDDEN)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    