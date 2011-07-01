# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse

def change_order(request, model_type_id=None):
    klass = ContentType.objects.get(id=model_type_id).model_class()
    order_field = getattr(klass, 'order_field', 'order')

    return TemplateResponse(request, 'admin_model_order/change_order/index.html', {
        'elements': klass.objects.all()
    })
