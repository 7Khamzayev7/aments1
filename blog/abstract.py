from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_("updated at"))

    class Meta:
        abstract = True



class OrderModel(models.Model):
    order = models.IntegerField(verbose_name=_("order"))

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True, verbose_name=_("active"))


    class Meta:
        abstract = True