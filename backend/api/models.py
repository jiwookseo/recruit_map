from datetime import datetime
from django.db import models
import jsonfield
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import SuspiciousOperation


class Company(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    href = models.URLField(
        _("homepage url"), max_length=200, default="", blank=True)
    saramin_url = models.URLField(
        _("saramin info url"), max_length=200, default="", blank=True)
    avg_salary = models.IntegerField(
        _("average salary"), default=0, blank=True)
    start_salary = models.IntegerField(
        _("freshman salary"), default=0, blank=True)
    address = models.CharField(_("detail address"), max_length=250)
    scale = models.CharField(_("classification by scale"),
                             max_length=50, default="", blank=True)
    lat = models.FloatField(_("latitude"))
    lng = models.FloatField(_("longitude"))
    place_id = models.CharField(_("google map place_id"), max_length=150)
    ind_code = models.CharField(
        _("industry code"),  max_length=50, default=0, blank=True)
    ind_name = models.CharField(
        _("industry name"), max_length=100, default="", blank=True)
    ind_key_code = models.CharField(
        _("industry keyword code"), max_length=50, default="", blank=True)

    @property
    def ind_array(self):
        return self.ind_code.split(",")

    @property
    def ind_key_array(self):
        return self.ind_key_code.split(",")

    @property
    def jobs_count(self):
        return len(self.jobs.filter(close__gt=datetime.now()))


class Job(models.Model):
    company = models.ForeignKey(Company, verbose_name=_(
        "company foreign key"), on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(_("title"), max_length=100)
    saramin_url = models.URLField(
        _("saramin info url"), max_length=200, default="", blank=True)
    job = models.CharField(
        _("job category"), max_length=100, default="", blank=True)
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
    name = models.CharField(_("name"), max_length=50, unique=True)
    line = models.CharField(_("line list"), max_length=50)
    address = models.CharField(_("detail address"), max_length=250)
    lat = models.FloatField(_("latitude"))
    lng = models.FloatField(_("longitude"))
    place_id = models.CharField(_("google map place_id"), max_length=150)

    @property
    def line_array(self):
        return self.line.split(",")


class Route(models.Model):
    time = models.IntegerField(_("transit time"))
    company = models.ForeignKey(
        Company, verbose_name=_("destination company"), on_delete=models.CASCADE, related_name="routes")
    station = models.ForeignKey(
        Station, verbose_name=_("origin station"), on_delete=models.CASCADE, related_name="routes")

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.company.routes.filter(station=self.station):
                raise SuspiciousOperation("Already exists")
        super().save(*args, **kwargs)
