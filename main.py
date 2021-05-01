import os
import fileinput
import datetime

def DisplayMenu():
    print('==========OPTIONS=================')
    print('(1) Add Item')
    print('(2) Remove Item')
    print('(3) Ready Item')
    print('(4) Search Item ')
    print('(99) Quit')
    try:
        CHOICE = int(input("Enter choice: "))
        menuSelection(CHOICE)
    except ValueError:
        print("The input was not valid integer")

def menuSelection(CHOICE):
    if CHOICE == 1:
        addItem()
    elif CHOICE == 2:
        removeItem()
    elif CHOICE == 3:
        readyItem()
    elif CHOICE == 4:
        searchItem()
    elif CHOICE == 99:
        exit()
    else :
        print("choose a valid option")
        DisplayMenu()

def addItem():
    print('=========add item==========')
    item_file = open('list.txt','a')
    item_name= input("Enter the name of the item: ")
    item_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    txt = '{},{}'.format(item_name,item_date)
    print(item_name)
    item_file.write(txt + '\n')
    item_file.close()


    DisplayMenu()


def removeItem():
    print('======remove item==========')

    item_name = input("Enter the item name to remove from inventory: ")

    with open('list.txt', "r") as f:
        lines = f.readlines()
    with open('list.txt', "w") as f:
        for line in lines:
            if line.find(item_name):
                f.write(line)

    DisplayMenu()

def searchItem():
    print('======search item==========')

    item_name = input("Enter the item name to find from inventory: ")
    with open('list.txt', "r") as f:
        lines = f.readlines()
    
    for i,line in enumerate(lines):
        if not line.find(item_name):
            print(line)

    DisplayMenu()

def readyItem():
    print('=======ready item==========')
    with open('list.txt', "r") as f:
        lines = f.readlines()
    time_now =datetime.datetime.now()
    print('time : {}'.format(time_now))

    for i,line in enumerate(lines):
        # print(line.split(",",1)[1])
        date = line.strip('\n').split(",",1)[1]
        tstamp1 = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
        
        diff = time_now-tstamp1

        if  divmod(diff.total_seconds() , 3600)[0] >15 :
            print(i,line)
            

    DisplayMenu()


if __name__=="__main__":
    DisplayMenu()