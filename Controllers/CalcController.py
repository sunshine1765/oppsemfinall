from Enums.ActionEnum import ActionEnum
from Logs.CalcLogs import CalcLog
from Views.CalcView import CalcView


class CalcController:
    def __init__(self):
        self.view = CalcView()

    #Вычисление примера
    def get_result(self):
        # i = "i"
        # self.result = eval(self.view.equation)  # eval - преобразует строку в python код

        if self.view.action == ActionEnum.plus.value:
            action = '+'
            result = self.__multiply_comprehensive(self.view.number_one, self.view.number_two)

        elif self.view.action == ActionEnum.multiply.value:
            action = '*'
            number_one, imaginary_one = self.__split_comprehensive(self.view.number_one)
            number_two, imaginary_two = self.__split_comprehensive(self.view.number_two)

            result = str((number_one * number_two) - (imaginary_one * imaginary_two))

            imaginary_part = str((number_one * imaginary_two) + (number_two * imaginary_one)) + 'i'
            if imaginary_part[0] != '-':
                result += '+' + imaginary_part
            else:
                result += imaginary_part

        elif self.view.action == ActionEnum.division.value:
            action = '/'
            number_one, imaginary_one = self.__split_comprehensive(self.view.number_one)
            number_two, imaginary_two = self.__split_comprehensive(self.view.number_two)

            numerator_number = (number_one * number_two) + ((imaginary_one * (imaginary_two * -1)) * -1)
            numerator_imaginary = (number_one * (imaginary_two * -1)) + (imaginary_one * number_two)

            denomerator_number = (number_two * number_two) + ((imaginary_two * (imaginary_two * -1)) * -1)
            denomerator_imaginary = (number_two * (imaginary_two * -1)) + (imaginary_two * number_two)

            result = str(numerator_number / (denomerator_number + denomerator_imaginary))
            imaginary_part = str(numerator_imaginary / (denomerator_number + denomerator_imaginary)) + 'i'

            if imaginary_part[0] != '-':
                result += '+' + imaginary_part
            else:
                result += imaginary_part

        CalcLog("(" + self.view.number_one + ")" + action + "(" + self.view.number_two + ")", result)
        self.view.print_result(result)

    def __split_comprehensive(self, comprehensive: str) -> tuple:
        for i in range(len(comprehensive)):
            if comprehensive[i] in '+-':
                number = int(comprehensive[0:i])
                imaginary = int(comprehensive[i: -1].replace(' ', ''))

        return (number, imaginary)

    def __multiply_comprehensive(self, number_first: str, number_second: str) -> str:
        number_one, imaginary_one = self.__split_comprehensive(number_first)
        number_two, imaginary_two = self.__split_comprehensive(number_second)

        result = str(number_one + number_two)
        imaginary_part = str(imaginary_one + imaginary_two) + 'i'
        if imaginary_part[0] != '-':
            result += '+' + imaginary_part
        else:
            result += imaginary_part
        return result