from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from countries.models import Country
from django.core.paginator import Paginator
from django.db.models import Count


def countries_list(request):
    query = request.GET.get('q', '')          
    region_filter = request.GET.get('region', '')  

    countries = Country.objects.all()
    if query:
        countries = countries.filter(name__icontains=query)
    if region_filter:
        countries = countries.filter(region=region_filter)

    paginator = Paginator(countries, 20)  # 20 pays par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    regions = Country.objects.values_list('region', flat=True).distinct().order_by('region')


    return render(request, 'countries/countries_list.html', {
        'page_obj': page_obj,
        'query': query,
        'region_filter': region_filter,
        'regions': regions
    })

def country_detail(request, cca3):
    country = get_object_or_404(Country, cca3=cca3)
    return render(request, 'countries/country_detail.html', {'country': country})



def stats(request):
    total_countries = Country.objects.count()

    top_population = Country.objects.order_by('-population')[:10]

    top_area = Country.objects.order_by('-area')[:10]

    region_distribution = Country.objects.values('region').annotate(count=Count('id'))

    return render(request, 'countries/stats.html', {
        'total_countries': total_countries,
        'top_population': top_population,
        'top_area': top_area,
        'region_distribution': region_distribution
    })