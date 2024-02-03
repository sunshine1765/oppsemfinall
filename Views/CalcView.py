class CalcView:
    def __init__(self):
        self.number_one = input("Введите первое комлексное число: ").strip()
        self.number_two = input("Введите второе комплексное число: ").strip()
        self.__list_actions()
        self.action = input("Выберите действие: ").strip()

    @staticmethod
    def print_result(result):
        print(result)

    @staticmethod
    def __list_actions():
        print("1. Cложение\n2.Умножение\n3.Деление")
