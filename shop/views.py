from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView, DetailView
from .models import Product, Image, Category
from .forms import FileFieldForm
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    success_url = 'image'
    fields = ["title", "category", "price", "description",]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)




class ImageFormView(FormView):
    form_class = FileFieldForm
    template_name = "image_create.html"
    success_url = 'success'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        prod = Product.objects.latest("pub_date")

        for f in files:
            prod.image_set.create( image=f)
              # Do something with each file.
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

    def get_queryset(self):
        return Product.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('title')
        context['image_list'] = Image.objects.order_by('product')
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('title')
        context['image_list'] = Image.objects.filter(product=self.get_object())
        return context

class ProductSearchResultView(ListView):
    model = Product
    template_name = "product_search_result.html"
    #queryset = Product.objects.filter(title__icontains="b")

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(title__icontains=query)
        return object_list