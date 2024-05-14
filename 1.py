import json


def load_data(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def get_loyal_customers(data_day1, data_day2):
    # Получаем уникальные идентификаторы клиентов для каждого дня
    customers_day1 = set(entry["CustomerId"] for entry in data_day1)
    customers_day2 = set(entry["CustomerId"] for entry in data_day2)

    # Находим пересечение клиентов, которые посетили сайт оба дня
    loyal_customers = customers_day1.intersection(customers_day2)

    # Фильтруем клиентов, которые посетили не менее двух уникальных страниц
    loyal_customers = {
        customer
        for customer in loyal_customers
        if len(
            {entry["PageId"] for entry in data_day1 if entry["CustomerId"] == customer}
        )
        >= 2
        and len(
            {entry["PageId"] for entry in data_day2 if entry["CustomerId"] == customer}
        )
        >= 2
    }

    return list(loyal_customers)


def display_loyal_customers(loyal_customers):
    print("Лояльные клиенты:")
    for customer in loyal_customers:
        print(customer)


if __name__ == "__main__":
    data_day1 = load_data("day1.json")
    data_day2 = load_data("day2.json")
    loyal_customers = get_loyal_customers(data_day1, data_day2)
    display_loyal_customers(loyal_customers)
