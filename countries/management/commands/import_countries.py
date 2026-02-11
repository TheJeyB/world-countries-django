import requests
from django.core.management.base import BaseCommand
from countries.models import Country


class Command(BaseCommand):
    help = "Import countries from REST Countries API"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,capital,region,subregion,population,area,flags,currencies"
        response = requests.get(url)
        data = response.json()

        count = 0
        for item in data:
            country, created = Country.objects.update_or_create(
                cca3=item.get('cca3'),
                defaults={
                    'name': item.get('name', {}).get('common'),
                    'cca2': item.get('cca2'),
                    'capital': item.get('capital', [None])[0] if item.get('capital') else None,
                    'region': item.get('region'),
                    'subregion': item.get('subregion'),
                    'population': item.get('population'),
                    'area': item.get('area'),
                    'flag': item.get('flags', {}).get('png'),
                    'currencies': item.get('currencies')
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} countries imported or updated."))
