# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

def get_position_link(obj):
    model_type_id = ContentType.objects.get_for_model(obj.__class__).id
    url = reverse("url-admin-model-order", kwargs=dict(model_type_id=model_type_id, model_pk=obj.pk))
    return '<a target="blank" href="%s" class="order_link">%s</a>' % (url, _(u'move'))
