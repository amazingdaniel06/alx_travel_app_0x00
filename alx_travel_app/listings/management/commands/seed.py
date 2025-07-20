from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                'title': 'Beachfront Villa',
                'description': 'Luxury villa with ocean view.',
                'location': 'Accra',
                'price_per_night': 250.00
            },
            {
                'title': 'Cozy Apartment',
                'description': 'Comfortable city apartment near main attractions.',
                'location': 'Kumasi',
                'price_per_night': 100.00
            },
            {
                'title': 'Mountain Cabin',
                'description': 'Peaceful retreat in the mountains.',
                'location': 'Aburi',
                'price_per_night': 150.00
            }
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded sample listings.'))
