# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.template.response import TemplateResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


@staff_member_required
def change_order(request, model_pk, model_type_id=None):
    klass = ContentType.objects.get(id=model_type_id).model_class()
    order_field = getattr(klass, 'order_field', 'position')
    if hasattr(klass, 'get_order_filter'):
        klass = klass.get_order_filter(klass.objects.get(pk=model_pk))
        elements = klass.order_by(order_field).all()
    else:
        elements = klass.objects.order_by(order_field).all()

    if request.method == 'POST':
        for element in elements:
            element.position = request.POST['position_%d' % element.pk]
            element.save()

        return redirect(reverse('url-admin-model-order', kwargs=dict(model_pk=model_pk, \
                                                     model_type_id=model_type_id)) + '?refresh=1')

    return TemplateResponse(request, 'admin_model_order/change_order/index.html', {
        'elements': elements
    })
