from django.urls import path
from .views import ProductCreateView, ImageFormView, ProductListView, ProductDetailView, ProductSearchResultView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name = "product-create"),
    path('create/image/', ImageFormView.as_view(), name = "images"),
    path('', ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail" ),
    path("search/", ProductSearchResultView.as_view(), name="product_search_result"),

]