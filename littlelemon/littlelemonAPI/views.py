from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from .models import MenuItem, Category, Cart, Order, OrderItem, User
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, UserSerializer
from datetime import date
from django.contrib.auth.models import Group
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'price', 'category__title']
    ordering_fields = ['title', 'price', 'category__title']
    search_fields = ['title']
    def get(self, request):
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title = category_name)
        if to_price:
            items = items.filter(price = to_price)
        if search:
            self.queryset = self.queryset.filter(title__startswith = search)
        return super().get(request)

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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().put(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request, *args, **kwargs ):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().patch(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)

class CategoryViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().put(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().patch(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_403_FORBIDDEN)
    
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

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
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user == order.user or request.user.groups.filter(name='Menager').exists():
            return super().get(request, *args, **kwargs)
        
        return Response({'message':'This is not your order'}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = self.get_object()
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
        order = self.get_object()
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
                serializer = self.serializer_class(order, data= request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            return Response({'message':'You can update only status field'})
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        self.serializer_class = OrderSerializer
        order = self.get_object()
        if request.user.groups.filter(name='Menager').exists():
            self.perform_destroy(order)
            return Response({"message": "Order deleted"}, status = status.HTTP_403_FORBIDDEN)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GroupMenagersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            users = self.queryset.filter(groups=1)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            menagers = Group.objects.get(name='Menager')
            user = get_object_or_404(User, username=request.data['username'])
            menagers.user_set.add(user)
            user.is_staff=True
            user.save()
            return Response({'message':f'User {request.data["username"]} added to the group Menagers'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)

class GroupMenagerDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            menagers = Group.objects.get(name='Menager')
            user = get_object_or_404(User, username=request.data['username'])
            menagers.user_set.remove(user)
            user.is_staff=False
            user.save()
            return Response({'message':f'User {request.data["username"]} removed from the Menagers group'}, status=status.HTTP_200_OK)
        return super().delete(request, *args, **kwargs)
    
class GroupDeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            users = self.queryset.filter(groups=2)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            delivery_crew = Group.objects.get(name='Delivery Crew')
            user = get_object_or_404(User, username=request.data['username'])
            delivery_crew.user_set.add(user)
            return Response({'message':f'User {request.data["username"]} added to the group Delivery Crew'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)

class GroupDeliveryCrewDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        return Response({'message':'Denies access'}, status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Menager').exists() or request.user.is_superuser:
            delivery_crew = Group.objects.get(name='Delivery Crew')
            user = get_object_or_404(User, username=request.data['username'])
            delivery_crew.user_set.remove(user)
            return Response({'message':f'User {request.data["username"]} removed from the Delivery Crew group'}, status=status.HTTP_200_OK)
        return super().delete(request, *args, **kwargs)
    
    