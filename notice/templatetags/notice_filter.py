from django import template


register = template.Library()

@register.filter
def enum(value):
    dic = {}
    for num, item in enumerate(value):
        dic[num] = item
    return dic.items()

@register.simple_tag
def page_range(count=1):
    num_list = []
    
    index = int(count) - 2
    while len(num_list) != 5:
        if index > 0:
            num_list.append(index) 
        index += 1
    return num_list

@register.filter
def date_blank(value):
    parts = value.split('-')
    return ' - '.join(parts)
