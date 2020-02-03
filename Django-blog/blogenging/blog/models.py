from django.db import models
# Описание модели(класса):
# Create your models here.
"""
slug — дружественная к восприятию человеком — 
буквенно-цифровая часть универсального адреса интернет-ссылки (URL) к рубрицируемому содержимому 
или ЧПУ(человекопонятный урл).
SlugField - валидатор, разрешает использовать буквы, цифры, нижнее подчеркивание и дефисы.
blunk=True - исключение, позволяет полю остоваться пустым.
db_index=True - флаг на индексацию, чтобы сделать более быстрый поиск по содержанию.
unique=True - индексация происходит автоматически.
auto_now_add=True - позволяет заполнять поле date_pub при сохранении объекта в базе данных
и заполнять это поле текущей датой.
"""
# Определение полей:
class Post(models.Model)
    title = models.CharField(max_lenght=150, db_index=True)
    slug = models.SlugField(max_lenght=150, unique=True) 
    body = models.TextField(blunk=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
"""
Метод(__str__) модели(класса), отвечает, за вывод информации об объекте, 
будет возвращать(return), строку, {} - место подстановки данных, 
при переформатировании текста,что удобно при выводе на печть(print), 
c визуальной точки зрения, метод(format), подставляет конкретный экземпляр класса Post
где self - значение:
"""
def __str__(self):
    return '{}'.format(self.title)