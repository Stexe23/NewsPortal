from django import template

register = template.Library()


@register.filter()
def censor(value):
    wrong_words = ['редиска', 'сука', 'хуй', 'нах', 'блядь']
    value = value.lower()
    for i in wrong_words:
        if i in value:
            value = value.replace(i[1::], "*" * (len(i) - 1))
        value = value.capitalize()
    return f'{value}'
