from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Lesson(models.Model):
	name = models.CharField(max_length=255, verbose_name='Предметь')
	

	def __str__(self):
		return self.name

class OrganizeStudy(models.Model):
	description = models.CharField(max_length=255, verbose_name='При организации изучения учебного материала учитель обеспечивает* и реализует')

	def __str__(self):
		return self.description

class CustomUser(AbstractUser):
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, verbose_name='Выберите предмет', blank=True, null=True)
    


class CategoryClass(models.Model):
	name = models.CharField(max_length=20, verbose_name='Класс')

	def __str__(self):
		return self.name


class Resources(models.Model):
	description = models.CharField(max_length=255, verbose_name='ресурсы')

	def __str__(self):
		return self.description

	# class Meta:
	# 	 ordering = ['-last_name']


class ComprehensiveControl(models.Model):
	TYPE_ASSESSMENT = [
		('Комплексное наблюдение урока', 'Комплексное наблюдение урока'),
		('Планирование урока', 'Планирование урока'),
		('Преподавание', 'Преподавание'),
		('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')
	]
	TYPE_PLAN = [
		('самостоятельно разработанного урока', 'самостоятельно разработанного урока'),
		('совместно разработанного с коллегами урока в рамках исследования урока', 'совместно разработанного с коллегами урока в рамках исследования урока'),
		('урока в рамках исследования практики', 'урока в рамках исследования практики'),
		('урока по авторской программе', 'урока по авторской программе'),
		('урока по авторской методике', 'урока по авторской методике' )
	]
	BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
	assessment_type = models.CharField(verbose_name="Тип оценивание", choices=TYPE_ASSESSMENT, max_length=255, default="Комлексное наблюдение урока")
	lesson_title  = models.CharField(max_length=255, verbose_name='Тема урока')
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
	categoryclass = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, verbose_name='Класс')
	date_of_observ = models.DateTimeField(verbose_name='Дата наблюдения урока', auto_now_add=True)
	teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Выберите учителя')
	goal_prof_develop = models.CharField(max_length=255, verbose_name='Цель профессионального развития на учебный год')
	observer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  verbose_name='Наблюдатель', related_name='+')
	plan = models.CharField(max_length=255, verbose_name='Предаставлен план', choices=TYPE_PLAN, default='самостоятельно разработанного урока')
	lern_obj = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Цели обучения соответствуют месту и роли урока в структуре раздела, темы')
	teacher_discus = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель обсуждает с учащимися цели обучения и ожидаемые результаты урока')
	teacher_follows = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель соблюдает структуру урока в соответствии с планом (при необходимости корректирует план урока, не нарушая логической последовательности этапов урока)')
	organizestudy = models.ManyToManyField(OrganizeStudy, verbose_name='При организации изучения учебного материала учитель обеспечивает* и реализует')
	teaching_techniques = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель использует приемы обучения, способствующие достижению целей обучения')
	resources = models.ManyToManyField(Resources, verbose_name='Учитель использует ресурсы, направленные на:')
	teacher_monitors = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель отслеживает вовлеченность каждого учащегося')
	teacher_offers = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель предлагает учащимся критерии и дескрипторы оценивания в соответствии с целями обучения')
	teacher_support = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель поддерживает обучение учащихся соответствующими приемами формативного оценивания')
	teacher_provide = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель предоставляет конструктивную обратную связь учащимся')
	teacher_uses = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель использует результаты формативного оценивания для планирования уроков')
	brief_feedback_observe = models.TextField(verbose_name = 'Краткий отзыв о наблюдении урока')
	brief_feedback = models.TextField(verbose_name = 'Краткий отзыв о продвижении учителя к достижению цели профессионального развития на учебный год')


class Teaching(models.Model):

	TYPE_ASSESSMENT = [
		('Комплексное наблюдение урока', 'Комплексное наблюдение урока'),
		('Планирование урока', 'Планирование урока'),
		('Преподавание', 'Преподавание'),
		('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')
	]

	TYPE_PLAN = [
		('самостоятельно разработанного урока', 'самостоятельно разработанного урока'),
		('совместно разработанного с коллегами урока в рамках исследования урока', 'совместно разработанного с коллегами урока в рамках исследования урока'),
		('урока в рамках исследования практики', 'урока в рамках исследования практики'),
		('урока по авторской программе', 'урока по авторской программе'),
		('урока по авторской методике', 'урока по авторской методике' )
	]
	BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
	assessment_type = models.CharField(verbose_name="Тип оценивание", choices=TYPE_ASSESSMENT, max_length=255, default="Комлексное наблюдение урока")
	date_of_observ = models.DateTimeField(verbose_name='Дата наблюдения урока', auto_now_add=True)
	categoryclass = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, verbose_name='Класс')
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
	lesson_title  = models.CharField(max_length=255, verbose_name='Тема урока')
	goal_prof_develop = models.CharField(max_length=255, verbose_name='Цель профессионального развития на учебный год')
	observer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,  verbose_name='Наблюдатель', related_name='+')
	teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Выберите учителя', related_name='+')
	plan = models.CharField(max_length=255, verbose_name='Учителем предоставлен', choices=TYPE_PLAN, default='самостоятельно разработанного урока')
	teacher_discus = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель обсуждает с учащимися цели обучения и ожидаемые результаты урока')
	teacher_follows = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель соблюдает структуру урока в соответствии с планом (при необходимости корректирует план урока, не нарушая логической последовательности этапов урока)')
	organizestudy = models.ManyToManyField(OrganizeStudy, verbose_name='При организации изучения учебного материала учитель обеспечивает* и реализует')
	teaching_techn_coll = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель использует приемы обучения, направленные на поддержку учебного сотрудничества')
	resources = models.ManyToManyField(Resources, verbose_name='Учитель использует ресурсы, направленные на:')
	brief_feedback_observe = models.TextField(verbose_name = 'Краткий отзыв о наблюдении урока')
	brief_feedback = models.TextField(verbose_name = 'Краткий отзыв о продвижении учителя к достижению цели профессионального развития на учебный год')


class PlanningLesson(models.Model):

	TYPE_ASSESSMENT = [
		('Комплексное наблюдение урока', 'Комплексное наблюдение урока'),
		('Планирование урока', 'Планирование урока'),
		('Преподавание', 'Преподавание'),
		('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')
	]

	TYPE_PLAN = [
		('самостоятельно разработанного урока', 'самостоятельно разработанного урока'),
		('совместно разработанного с коллегами урока в рамках исследования урока', 'совместно разработанного с коллегами урока в рамках исследования урока'),
		('урока в рамках исследования практики', 'урока в рамках исследования практики'),
		('урока по авторской программе', 'урока по авторской программе'),
		('урока по авторской методике', 'урока по авторской методике' )
	]
	BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
	assessment_type = models.CharField(verbose_name="Тип оценивание", choices=TYPE_ASSESSMENT, max_length=255, default="Комлексное наблюдение урока")
	date_of_observ = models.DateTimeField(verbose_name='Дата наблюдения урока', auto_now_add=True)
	categoryclass = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, verbose_name='Класс')
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
	lesson_title  = models.CharField(max_length=255, verbose_name='Тема урока')
	teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Выберите учителя')
	goal_prof_develop = models.CharField(max_length=255, verbose_name='Цель профессионального развития на учебный год')
	observer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,  verbose_name='Наблюдатель', related_name='+')
	plan = models.CharField(max_length=255, verbose_name='Учителем предоставлен', choices=TYPE_PLAN, default='самостоятельно разработанного урока')
	plan_contains = models.BooleanField(verbose_name="План содержит понятные для учащихся ожидаемые результаты урока и критерии успеха", choices=BOOL_CHOICES)
	organizestudy = models.ManyToManyField(OrganizeStudy, verbose_name='Учебный материал отражает')
	plan_lern_methods = models.BooleanField(verbose_name="Планируемые приемы обучения соотносятся с целями обучения и ожидаемыми результатами*", choices=BOOL_CHOICES)
	plan_resourсes = models.BooleanField(verbose_name="Планируемые ресурсы направлены на достижение целей обучения", choices=BOOL_CHOICES)
	plan_strategy = models.BooleanField(verbose_name="Планируемые стратегии оценивания учебных достижений учащихся направлены на достижение целей обучения", choices=BOOL_CHOICES)
	brief_feedback_observe = models.TextField(verbose_name = 'Краткий отзыв о наблюдении урока')
	brief_feedback = models.TextField(verbose_name = 'Краткий отзыв о продвижении учителя к достижению цели профессионального развития на учебный год')


class AssessmentStudentLearning(models.Model):

	TYPE_ASSESSMENT = [
		('Комплексное наблюдение урока', 'Комплексное наблюдение урока'),
		('Планирование урока', 'Планирование урока'),
		('Преподавание', 'Преподавание'),
		('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')
	]

	BOOL_CHOICES = [(True, 'Да'), (False, 'Нет')]
	assessment_type = models.CharField(verbose_name="Тип оценивание", choices=TYPE_ASSESSMENT, max_length=255, default="Комлексное наблюдение урока")
	date_of_observ = models.DateTimeField(verbose_name='Дата наблюдения урока', auto_now_add=True)
	categoryclass = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, verbose_name='Класс')
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
	lesson_title  = models.CharField(max_length=255, verbose_name='Тема урока')
	teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Выберите учителя')
	goal_prof_develop = models.CharField(max_length=255, verbose_name='Цель профессионального развития на учебный год')
	observer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,  verbose_name='Наблюдатель', related_name='+')
	teacher_observe = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель отслеживает вовлеченность каждого учащегося')
	teacher_offers = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель предлагает учащимся критерии и дескрипторы оценивания в соответствии с целями обучения')
	teacher_support = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель поддерживает обучение учащихся соответствующими приемами формативного оценивания')
	teacher_provides = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель предоставляет конструктивную обратную связь учащимся')
	teacher_uses = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Учитель использует результаты формативного оценивания для планирования уроков')
	brief_feedback_observe = models.TextField(verbose_name = 'Краткий отзыв о наблюдении урока')
	brief_feedback = models.TextField(verbose_name = 'Краткий отзыв о продвижении учителя к достижению цели профессионального развития на учебный год')