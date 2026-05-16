from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "Title": "Products",
        'is_active': False,
    }
    return render(request, 'products/index.html', context)


def products(request,):
    context = {
        "Title": "Products",
        "products": [
            {
                "image" : "/static/vendor/img/products/Adidas-hoodie.png",
                "name": "Худи черного цвета с монограммами adidas Originals",
                "description": " Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                "price": '6 090,00 грн.',
            },
            {
                    "image" : "/static/vendor/img/products/Adidas-hoodie.png",
                    "name": "Худи черного цвета с монограммами adidas Originals",
                    "description": " Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                    "price": '6 090,00 грн.',
            },
            {
                    "image" : "/static/vendor/img/products/Adidas-hoodie.png",
                    "name": "Худи черного цвета с монограммами adidas Originals",
                    "description": " Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                    "price": '6 090,00 грн.',
            }
        ]
    }
    return render(request, 'products/products.html',context)