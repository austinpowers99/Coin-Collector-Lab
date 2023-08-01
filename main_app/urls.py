from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
    path('coins/<int:coin_id>/add_minting/', views.add_minting, name='add_minting'),
    path('coins/<int:coin_id>/add_photo/', views.add_photo, name='add_photo'),
    path('coins/<int:coin_id>/assoc_material/<int:material_id>/', views.assoc_material, name='assoc_material'),
    path('coins/<int:coin_id>/unassoc_material/<int:material_id>/', views.unassoc_material, name='unassoc_material'),
    path('materials/', views.MaterialList.as_view(), name='materials_index'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='materials_detail'),
    path('materials/create/', views.MaterialCreate.as_view(), name='materials_create'),
    path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='materials_update'),
    path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='materials_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]