import random
import math

def openFile():
    try:
        file = open("C:\\Users\\Mark Verschuuren\\Documents\\School\\Jaar 3\\Blok 10\\Programmeren\\Linear model\\Linear_Model\\Linear_input.csv").readlines()

        return file
    except(IOError):
        print("IOError in 'Linear_input'")



def get_predict(Input):
    error_Dict ={}
    for repeat in range(1000000):
        a = random.randrange(-10, 10)
        b = random.randrange(-10, 10)
        c = random.randrange(-10, 10)

        Errors = []
        for index in range(1, len(Input)):
            Column = Input[index].split(";")

            predict = a + b * int(Column[0]) + c * int(Column[1])    # predict = a * int(Column[0]) + c * int(Column[1]) + b

            Errors = get_error(predict, Column, Errors)

        error_Dict[sum(Errors)] = str(a), "|", str(b), "|" , str(c)
    print(min(error_Dict, key=error_Dict.get))
    print(error_Dict[min(error_Dict, key=error_Dict.get)])
def get_error(predict, Column, Errors):

    Errors.append((int(Column[2]) - predict)**2)

    return Errors


def main():
    file = openFile()
    get_predict(file)

main()