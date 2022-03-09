# Скрипт по выгрузке иерархии классификаций Maximo

## Установка зависимостей

```
pip install -r requirements.txt
```

## Использование

Необходимо создать файл `.env` со следующим содержимым

```
DATABASE=db_name
HOSTNAME=hostname_or_ip
PORT=port
PASSWORD=password
LOGIN=username
```
либо определить аналогичные переменные среды

После выполнения скрипта `classification_dbi.py` - в папке появится файл `classification.xls` с иерархией классификаций