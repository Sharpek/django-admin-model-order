from django.db import models
from admin_model_order.admin import get_position_link


class Example(models.Model):

    title = models.CharField('title', max_length=255)
    position = models.PositiveIntegerField('Position')


    def __unicode__(self):
        return self.title


    def position_link(self):
        return get_position_link(self)
    position_link.allow_tags = True



    class Meta:
        ordering = ['position']
