from django.db import models
import jsonfield
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_("name"), max_length=50)
    href = models.URLField(_("homepage url"), max_length=200)
    saramin_url = models.URLField(_("saramin info url"), max_length=200)
    avg_salary = models.IntegerField(_("average salary"))
    start_salary = models.IntegerField(_("freshman salary"))
    address = models.CharField(_("detail address"), max_length=250)
    scale = models.CharField(_("classification by scale"), max_length=50)
    lat = models.FloatField(_("latitude"))
    lng = models.FloatField(_("longitude"))
    viewport = jsonfield.JSONField(_("viewport geometry"))
    place_id = models.IntegerField(_("google map place_id"))
    ind_code = models.IntegerField(_("industry code"))
    ind_name = models.CharField(_("industry name"), max_length=50)
    ind_key_code = models.CharField(_("industry keyword code"), max_length=50)


class Job(models.Model):
    company = models.ForeignKey(Company, verbose_name=_(
        "company foreign key"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    saramin_url = models.URLField(_("saramin info url"), max_length=200)
    job = models.CharField(_("job category"), max_length=50)
    exp_min = models.IntegerField(_("minimum experience"))
    exp_max = models.IntegerField(_("maximum experience"))
    edu_code = models.IntegerField(_("education code"))
    edu_name = models.CharField(_("education name"), max_length=50)
    open = models.DateTimeField(
        _("open timestamp"), auto_now=False, auto_now_add=False)
    close = models.DateTimeField(
        _("close timestamp"), auto_now=False, auto_now_add=False)
    close_type = models.IntegerField(_("close type code"))


class Station(models.Model):
    name = models.CharField(_("name"), max_length=50)
    line = models.IntegerField(_("line number"))
    address = models.CharField(_("detail address"), max_length=250)
    lat = models.FloatField(_("latitude"))
    lng = models.FloatField(_("longitude"))
    place_id = models.IntegerField(_("google map place_id"))
