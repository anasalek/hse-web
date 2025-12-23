from django.contrib.auth.models import User
from Events.models import Event, Participation

# Создаем организаторов
ivan = User.objects.create_user(username='ivan', first_name='Иван', last_name='Петров')
olga = User.objects.create_user(username='olga', first_name='Ольга', last_name='Сидорова')

# Создаем участников
alex = User.objects.create_user(username='alex', first_name='Алексей', last_name='Кузнецов')
maria = User.objects.create_user(username='maria', first_name='Мария', last_name='Иванова')
dmitry = User.objects.create_user(username='dmitry', first_name='Дмитрий', last_name='Соколов')
anna = User.objects.create_user(username='anna', first_name='Анна', last_name='Васильева')
sergey = User.objects.create_user(username='sergey', first_name='Сергей', last_name='Попов')

# Создаем мероприятия
beer_fest = Event.objects.create(
    name='Фестиваль пива',
    description='Дегустация лучших сортов пива со всей страны',
    organizer=ivan  # организатор - Иван
)

dwarf_tossing = Event.objects.create(
    name='Метание карликов',
    description='Соревнования по метанию карликов на дальность',
    organizer=ivan  # организатор - Иван
)

sad_fridge_day = Event.objects.create(
    name='День грусти у холодильника',
    description='Грустное поедание еды из холодильника в одиночестве',
    organizer=olga  # организатор - Ольга
)

# Распределяем участников по мероприятиям
# Алексей ходит на все 3 мероприятия
beer_fest.participant.add(alex)
dwarf_tossing.participant.add(alex)
sad_fridge_day.participant.add(alex)

# Мария ходит на 2 мероприятия
beer_fest.participant.add(maria)
sad_fridge_day.participant.add(maria)

# Дмитрий ходит на 2 мероприятия
dwarf_tossing.participant.add(dmitry)
sad_fridge_day.participant.add(dmitry)

# Анна ходит только на фестиваль пива
beer_fest.participant.add(anna)

# Сергей ходит на метание карликов и день грусти
dwarf_tossing.participant.add(sergey)
sad_fridge_day.participant.add(sergey)

# Также добавим участников в качестве участников своих же мероприятий (кроме организаторов)
# Иван - организатор, но может быть участником других мероприятий
sad_fridge_day.participant.add(ivan)

# Ольга - организатор, но может быть участником других мероприятий
beer_fest.participant.add(olga)
dwarf_tossing.participant.add(olga)

print("Данные успешно созданы!")
print(f"Организаторы: {ivan.first_name} {ivan.last_name}, {olga.first_name} {olga.last_name}")
print(f"Участники: {alex.first_name}, {maria.first_name}, {dmitry.first_name}, {anna.first_name}, {sergey.first_name}")
print(f"Мероприятия: {beer_fest.name}, {dwarf_tossing.name}, {sad_fridge_day.name}")