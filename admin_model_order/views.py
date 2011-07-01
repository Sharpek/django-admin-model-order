# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse

def change_order(request, model_pk, model_type_id=None):
    klass = ContentType.objects.get(id=model_type_id).model_class()
    order_field = getattr(klass, 'order_field', 'position')
    if hasattr(klass, 'get_order_filter'):
        klass = klass.get_order_filter(klass.objects.get(pk=model_pk))

    elements = klass.order_by(order_field).all()

    if request.method == 'POST':
        for element in elements:
            element.position = request.POST['position_%d' % element.pk]
            element.save()


    return TemplateResponse(request, 'admin_model_order/change_order/index.html', {
        'elements': elements
    })
