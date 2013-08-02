from django.core.cache import cache
from django.shortcuts import render
from django.conf import settings
import foursquare


def index(request):
    """
    https://developer.foursquare.com/docs/venues/categories
    https://developer.foursquare.com/docs/responses/category
    """

    foursquare_categories = cache.get('foursquare_categories')

    if foursquare_categories is None:
        client = foursquare.Foursquare(
            client_id=settings.FOURSQUARE_KEY,
            client_secret=settings.FOURSQUARE_SECRET
        )

        foursquare_categories = client.venues.categories()['categories']
        cache.set('foursquare_categories', foursquare_categories)

    context = {
        'categories': foursquare_categories
    }

    return render(request, 'index.html', context)
