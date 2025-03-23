from django import template

register = template.Library()

@register.filter
def niveau_display(value):
    mapping = {
        "A1": "A1 - Débutant",
        "A2": "A2 - Élémentaire",
        "B1": "B1 - Intermédiaire",
        "B2": "B2 - Avancé",
        "C1": "C1 - Expérimenté",
        "C2": "C2 - Maîtrise",
    }
    return mapping.get(value, value)  
