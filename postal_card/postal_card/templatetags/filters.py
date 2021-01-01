from django import template

register = template.Library()

@register.filter(name='change')
def change(value):
	dict1 = {'1': '۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹', '0':'۰'}
	for i in dict1.keys():
		value = value.replace(i, dict1[i])
	return value
