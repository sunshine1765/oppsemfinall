class CalcLog:

    def __init__(self, example: str, result: str):
        with open("logs.txt", 'a') as file:
            file.write(example + " = " + result + '\n')



