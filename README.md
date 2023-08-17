# Калькулятор Количества Сессий Пользования Кредитной Карты

Данная функция была реализована в качестве тестового задания, его формулировка следующая:

Написать ф-ю расчета количества сессий пользования кредитной карты. На вход подается временной ряд с задолженностью, дата начала периода и дата окончания периода. Возвращает количество сессий пользования кредитной карты за указанный период.
Сессия пользования кредитной картой это непрерывная (не нулевая) задолженность по кредитной карте. 
Пример:
Временной ряд, где индекс это номер месяца, а значение это задолженность по 
кредитной карте
[200, 0, 1000, 1100, 900, 0, 0, 100, 0, 2] – 4 сессии

На вход подается:
arrears: list[dict] – временной ряд, ключи словаря см в таблице.
start_date: datetime – дата начала периода, 
end_date: datetime – дата окончания периода. 

| Название  | Тип | Обязательность |
| ------------- | ------------- | ------------- |
| calcucationDate  | str  | 0  |
| outstanding  | float  | 0  |

На выходе 1 число
Примеры входных данных, которые будут подаваться на вход находятся в json файлах в папке data_example

#Пример использования функции
file_json = open(f"C:/Users/Septem/Downloads/data_example/777.json")
arrears = json.load(file_json)
start_date = datetime(2001, 1, 1)
end_date = datetime(2024, 1, 1)
session_count = calculate_sessions(arrears, start_date, end_date)
print(session_count)
