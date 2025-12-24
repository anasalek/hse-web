from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    '''Мероприятие'''

    name = models.CharField(verbose_name="Название мероприятия", unique=True, max_length=200)
    description = models.TextField(
        verbose_name="Описание мероприятия"
    )
    # поля со связями
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='organized_events',
        help_text="Организатор этого мероприятия"
    )
    participants = models.ManyToManyField(
        User,
        through = "Participation", # через какую таблицу связывает
        through_fields= ("event", "participant"), # через какие поля в этой таблице
        blank=True, # поле может быть пустым, если никто не пришел
        related_name='participanting_events',
        help_text="Мероприятие, в котором участвует пользователь"
    )

    def is_user_participating(self, user=None):
        """Проверяет, записан ли пользователь на событие"""
        if user and not user.is_authenticated:
            return False
        if user:
            return self.participants.filter(id=user.id).exists()
        return False
    
    def __str__(self):
        return self.name
    
class Participation(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patricipants",
        help_text="Зарегестрированные участники"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, # при удалении все связанные таблицы удалятся тоже
        related_name="events",
        help_text= "Мероприятия, созданные этим организатором"
    )
    def __str__(self):
        return f'{self.participant.username} посетил мероприятие {self.event.name}'


