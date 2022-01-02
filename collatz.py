print("put a number")
user_input = int(input())


def Coll(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


number = Coll(user_input)


while number != 1:
    number = Coll(number)
