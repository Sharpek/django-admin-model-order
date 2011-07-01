# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


def get_position_link(obj):
    model_type_id = ContentType.objects.get_for_model(obj.__class__).id
    kwargs = {"model_type_id": model_type_id}
    url = reverse("url-admin-model-order", kwargs=kwargs)
    return '<a href="%s" class="order_link">%s</a>' % (url, str(obj.pk) or '')
