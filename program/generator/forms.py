from django import forms
from datetime import datetime, timedelta

# get current datetime
def week_choices():
    dt = datetime.now()
    now_weekday = dt.weekday()
    last_monday = datetime.now() - timedelta(days=now_weekday)
    return [
        ((last_monday + timedelta(days=i)).date().strftime("%Y-%m-%d"),(last_monday + timedelta(days=i)).date().strftime("%y-%m-%d"))  for i in (0,7,14)]

PROGRAMMES = (
    '1TV',
    'RTR',
    'TVC_RT',
    'NTVmsk',
    'Piter5_RUS',
    'KUL',
    'STS',
    'TNT',
    'TV3',
    'RenTV',
    'ZVEZDA',
    'OTR',
    'DOMASHNIY',
    'Friday',
    '360d',
    'Karusel',
    'MIR',
    'MatchTV',
)

PROGRAMMES_CHOICES = (('1TV','Первый'),
    ('RTR','РОССИЯ 1'),
    ('TVC_RT','ТВ Центр Москва'),
    ('NTVmsk','НТВ-Москва'),
    ('Piter5_RUS','Пятый канал Россия'),
    ('KUL','КУЛЬТУРА'),
    ('STS','СТС'),
    ('TNT','ТНТ'),
    ('TV3','ТВ-3'),
    ('RenTV','РЕН ТВ'),
    ('ZVEZDA','ЗВЕЗДА'),
    ('OTR','ОТР'),
    ('DOMASHNIY','ДОМАШНИЙ'),
    ('Friday','Пятница'),
    ('360d','360°'),
    ('Karusel','Карусель'),
    ('MIR','МИР'),
    ('MatchTV','МАТЧ!'),
)
VARIANT_CHOICES = (
    ('R', 'Основное расписание'),
    ('А', 'Анонсы'),
    ('P', 'Правки'),
)
class GeneratorForm(forms.Form):
    week        = forms.ChoiceField(label="Выберите неделю", choices = week_choices)
    programme   = forms.ChoiceField(label="Выберите программу", choices = PROGRAMMES_CHOICES)
    variant     = forms.ChoiceField(label="Выберите тип программы", choices = VARIANT_CHOICES)