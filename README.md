# Требования

    Python 3
    Flask
    Pandas
# установка
## клонирование репозитория
  ```git clone https://github.com/Flashwidow/test.git```
## активирование виртуальной среды
  ```python -m venv venv source venv/bin/activate ```
## установка зависимостей
  ```pip install -r requirements.txt```
## запуск
  ```flask run```
# API
## POST upload
  загрузка файлов csv формата
  для загрузки файлов используйте команду

  

## GET files
показыывет список загруженных файлов

## GET data/filename
 доступ к файлу с определенной сортировкой
 пример запроса
 ```GET /api/data?filter_column=age&filter_value=30&sort_by=name```


## DELETE /delete/filename
  удаление файлов из списка

  


