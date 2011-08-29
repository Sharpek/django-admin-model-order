# -*- coding: utf-8 -*-

def object_post_save(sender, **kwargs):
    instance = kwargs['instance']
    if instance.position is None:
        order_field = getattr(sender, 'order_field', 'position')
        if hasattr(sender, 'get_order_filter'):
            sender = sender.get_order_filter(sender.objects.get(pk=instance.pk))
        else:
            sender = sender.objects.all()

        sender = sender.order_by(order_field)
        try:
            last = (sender.reverse()[0].position or 0) + 1
        except IndexError:
            last = 0

        instance.position = last
        instance.save()
