import re
from datetime import datetime
from django import template

register = template.Library()

ban_words = [
	'Редиска',
    'редиска',
    'Редис',
    'редис',
    'РЕДИС',
    'РЕДИСКА',
]

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    # фильтр заменяет слова из стоп-листа на '*'
#    ban_words_pattern = '|'.join(ban_words)
#    value = re.sub(rf"{ban_words_pattern}", (len(ban_words) - 1)*'*', value)
#    return value

    for word in ban_words:
        value = value.replace(word[1:], len(word[1:])*'*')
    return value

@register.simple_tag()
def current_time(format_string='%b %d %Y', name='date'):
   return datetime.utcnow().strftime(format_string)
