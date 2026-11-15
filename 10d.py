#get a list of 5 numbers and ask the user to enter the index value
#and return the element and also handle the exception.

list=[0,1,2,3,4,5,6]

while True:
    try:
        index=int(input("enter the index value: "))
        print(list[index])

    except ValueError:
        print("try entering a correct integer value")
    except IndexError:
        print("index error occured")
    except Exception:   #if in case any other exception comes along
            print("somethng went wrong")
    finally:
        print("thank you")
