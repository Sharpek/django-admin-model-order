from django.db import models
from admin_model_order.admin import get_position_link
from django.db.models.signals import post_save
from admin_model_order.signals import object_post_save


class Example(models.Model):

    title = models.CharField('title', max_length=255)
    position = models.PositiveIntegerField('Position', blank=True, null=True)


#    @classmethod
#    def get_order_filter(cls, obj):
#        return cls.objects.filter(position=obj.position)


    def __unicode__(self):
        return self.title


    def position_link(self):
        return get_position_link(self)
    position_link.allow_tags = True


    class Meta:
        ordering = ['position']


post_save.connect(object_post_save, Example)
