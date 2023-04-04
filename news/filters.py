from django_filters import FilterSet
from .models import News


class NewsFilter(FilterSet):

	class Meta:
		# В Meta классе мы должны указать Django модель,
		# в которой будем фильтровать записи.
		model = News
		# В fields мы описываем по каким полям модели
		# будет производиться фильтрация.
		fields = {
			# поиск по названию
			'name': ['icontains'],
			# количество товаров должно быть больше или равно
			'category': ['gt'],
			'date': [
				'lt',  # цена должна быть меньше или равна указанной
				'gt',  # цена должна быть больше или равна указанной
			],
		}
