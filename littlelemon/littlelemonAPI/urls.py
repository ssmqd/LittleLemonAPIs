from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns =[
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('category/', views.CategoryViews.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category/<int:pk>', views.SingelCategoryView.as_view()),
    path('cart/menu-items/', views.CartView.as_view()),
    path('order/', views.OrderView.as_view()),
    path('order/<int:pk>', views.OrderItemView.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('groups/manager/users/', views.GroupMenagersView.as_view()),
    path('groups/manager/users/<int:pk>', views.GroupMenagerDetailView.as_view()),
    path('groups/delivery-crew/users/', views.GroupDeliveryCrewView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.GroupDeliveryCrewDetailView.as_view()),
]