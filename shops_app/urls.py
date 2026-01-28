from django.urls import path
from shops_app.views import form_view, main


urlpatterns = [
    path('', main.main_page, name='main_page'),
    path('login/', form_view.login, name='login'),
    path('register/', form_view.register, name='register'),
    path('logout/', form_view.logout_page, name="logout_page"),
    path('product_add/', form_view.product_add, name='product_add'),
    path('shop_add/', form_view.shop_add, name='shop_add'),
]













#V1
# urlpatterns = [
#     path('', main.main_page, name='main_page'),
#     path('register/', register.user_register, name='register_page'),
#     path('login/', register.login_page, name='login_page'),
#     path('biznes_add/', businessmen_menu.add_biznes, name='add_biznes'),
#     path('product_add/', businessmen_menu.add_product, name='product_add_page'),
# ]