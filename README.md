# Проект — Transactions

Transactions — это проект, который показывает до 5 последних успешных банковских операций клиента, отсортированных 
по убыванию. Формат предоставления результатов: </br>
- <*дата перевода*> <*описание перевода*> </br>
- <*откуда*> -> <*куда*> </br>
- <*сумма перевода*> <*валюта*> </br>


# Дополнительная информация

- Файл с информацией об банковских операциях находится в директории:
   - `transactions/scr/operation.json` </br>
- При необходимости вы можете изменить файл, добавив в него данные любым удобным способом, но в следующем формате:  </br>
   - `date` — информация о дате совершения операции.
   - `state` — статус перевода:
      - `EXECUTED`  — выполнена,
      - `CANCELED`  — отменена.
   - `operationAmount` — сумма операции и валюта.
   - `description` — описание типа перевода.
   - `from` — откуда.
   - `to` — куда. </br>
- Номер карты замаскирован и не отображается целиком: `XXXX XX** **** XXXX` </br>
- Номер счета замаскирован и не отображается целиком: `**XXXX`  </br>
- Для просмотра покрытия кода тестами введите в консоли:
   ```
    cd tests
    pytest --cov --cov-report term-missing
    ```


# Клонирование репозитория и локальный запуск

Выполните в консоли: </br>

Для Windows: </br>
```
git clone git@github.com:DmitriiParfenov/transactions.git
python -m venv venv
venv\Scripts\activate
pip install poetry
poetry install
poetry run python main.py
```

Для Linux: </br>
```
git clone git@github.com:DmitriiParfenov/transactions.git
cd transactions
python3 -m venv venv
source venv/bin/activate
curl -sSL https://install.python-poetry.org | python3
poetry install
poetry run python3 main.py
```
