import datetime


def get_time():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("drake_ex.txt", "a") as op:
                op.write(str([str(get_time())]) + ":" + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("drake_food.txt", "a") as op:
                op.write(str([str(get_time())]) + ":" + value + "\n")
            print("Successfully written")

    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("rohan_ex.txt", "a") as op:
                op.write(str([get_time()]) + ":" + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("rohan_food", "a") as op:
                op.write(str([str(get_time())]) + ":" + value + "\n")
                print("Successfully written")

    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("hammad_ex.txt", "a") as op:
                op.write(str([str(get_time())]) + ":" + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("hammad_food.txt", "a") as op:
                op.write(str([str(get_time())]) + ":" + value + "\n")
            print("Successfully written")
    else:
        print("plz enter valid input 1(harry),2(rohan),3(hammad)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("drake_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("drake_food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("rohan_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("rohan_food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("hammad_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("hammad_food.txt") as op:
                for i in op:
                    print(i, end=" ")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve"))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad"))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad"))
    retrieve(b)
