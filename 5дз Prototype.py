import copy

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def clone(self):
        return copy.deepcopy(self)


class Order:
    def __init__(self, delivery_cost, payment_method):
        self.products = []
        self.delivery_cost = delivery_cost
        self.payment_method = payment_method

    def add_product(self, product):
        self.products.append(product)

    def clone(self):
        return copy.deepcopy(self)

    def show_info(self):
        print("Заказ:")
        for p in self.products:
            print(f"- {p.name} ({p.quantity} шт.) по {p.price} тг")
        print("Доставка:", self.delivery_cost, "тг")
        print("Метод оплаты:", self.payment_method)
        total = sum(p.price * p.quantity for p in self.products) + self.delivery_cost
        print("Итого:", total, "тг\n")


if __name__ == "__main__":
    order1 = Order(1000, "Карта")
    order1.add_product(Product("Кондиционер", 150000, 1))
    order1.add_product(Product("Пульт", 8000, 1))

    print("Оригинальный заказ:")
    order1.show_info()

    order2 = order1.clone()
    order2.add_product(Product("Кронштейн", 5000, 2))
    order2.payment_method = "Наличные"

    print("Клонированный заказ:")
    order2.show_info()
