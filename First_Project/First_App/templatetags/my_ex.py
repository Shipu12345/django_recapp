from django import template
registor=template.Library()

@registor.filter(name='fal')
def cut(value,arg):
    return value.replace(arg,'')

# reg.filter('fal',cut)
