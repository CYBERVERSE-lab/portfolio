from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
# Create your views here.

cards_data = [
    {
        "title": "Welcome to My Portfolio",
        "description": "Explore my work, skills, and contact information.",
        "link": None,
        "order": 1,
        "image": "./static/home_page.jpg",
        "background_color": "#f9f9f9",
    },
    {
        "title": "About Me",
        "description": "Learn more about my background, skills, and interests.",
        "link": "/card/2",
        "order": 2,
        "image": "./static/sub_page.jpg",
        "background_color": "#e3f2fd",
    },
    {
        "title": "My Projects",
        "description": "View the projects I’ve worked on, from web apps to data analysis.",
        "link": "/card/3",
        "order": 3,
        "image": "./static/sub_page.jpg",
        "background_color": "#e8f5e9",
    },
    {
        "title": "Contact Me",
        "description": "Get in touch for collaboration or opportunities.",
        "link": "/card/4",
        "order": 4,
        "image": "./static/sub_page.jpg",
        "background_color": "#f3e5f5",
    }
]

def home(request):
    return HttpResponse("Hello, World!")

def main_page(request):
    # cards = Card.objects.all().order_by('order')
    cards = cards_data
    return render(request, 'main_page.html', {'cards': cards})

def sub_page(request, card_id):
    # card = Card.objects.get(id=card_id)
    for card in cards_data:
        if card['link'] == f"/card/{card_id}":
            return render(request, 'sub_page.html', {'card': card})
        else:
            return render(request, 'sub_page.html', {'card': None})
