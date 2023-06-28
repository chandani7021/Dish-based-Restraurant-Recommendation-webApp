from django.shortcuts import render
from .models import Dish
import json
from django.core.paginator import Paginator

# Create your views here.
def search(request):
    query = request.GET.get('query')
    page_number = request.GET.get('page')


    if query:
        dishes = Dish.objects.filter(items__icontains = query)
        paginator = Paginator(dishes, 5)  # Pagination
        page_obj = paginator.get_page(page_number)

        results = []
   
        for dish in page_obj:
            items_dict = json.loads(dish.items)

            matching_items = {k: v for k, v in items_dict.items() if query.lower() in k.lower()}
            
            for item, value in matching_items.items():
                if query.lower() in item.lower():
                    result = {
                        'name':dish.name,
                        'location':dish.location,
                        'dish': item,
                        'price': value
                                }
                    results.append(result)
        
    else:
        page_obj = None
        results = []

    return render(request, 'dish/search.html', {
        'results': results, 
        'query': query,
        'page_obj':page_obj
        })
