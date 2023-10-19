# Kurs3

Данный проект - реализация курсовой работы.

### Описание
---
Этот проект выводит на экран список из 5 последних выполненных клиентом операций в формате:

```
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта> 
```

Вот пример правильной работы кода:
```
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```
Тесты для функуций написаны на pytest

# Установка и запуск
1. Чтобы клонировать репозиторий необходимо ввести следующую команду:
    ```bash
    git clone https://github.com/Denis-Shevchenko-228/Kurs3.git 
    ``` 
2. Перейти в директорию проекта:
    ```bash
    cd Kurs3
    ```
3. Активировать окружение и установить зависимости:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
4. Запустить программу:
    ```bash
    python main.py
    ```
# Тестирование
После установки для тестирования введите команду:
```bash
pytest
```