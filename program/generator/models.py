from django.db import models


class Record(models.Model):
    class Meta:
        unique_together = (('channelid', 'efirweek', 'variant'),)

    name = models.URLField('program_url')
    efirweek = models.DateField('Эфирная неделя')
    channel = models.CharField('Название канала', max_length=10)
    channelid = models.CharField('ID канала', max_length=10)
    updated = models.DateTimeField('Время обновления канала')
    variant = models.CharField('ID канала', max_length=1)
