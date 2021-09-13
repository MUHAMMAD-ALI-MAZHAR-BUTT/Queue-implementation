def Queue_Implementation(object):
    input_ = 1
    while (input_ != 0):
        print("Press 1: for insert")
        print("Press 2: for pop")
        print("Press 3: for top")
        print("Press 4: for size of Queue")
        print("Press 5: for printing elements")
        print("Press 6: for sort elements")
        print("Press 7: for reverse elements")
        print("Press 8: for print min element")
        print("Press 9: for print max element")
        print("Press 0: for exit")
        input_ = int(input("Enter operation want to perform : "))
        if (input_ == 1):
            var = int(input("Enter value to insert in Queue : "))
            object.append(var)
        elif (input_ == 2):
            if not object:
                print("Queue is empty")
            else:
                print("Value ", object.pop(0), " poped from Queue")
        elif (input_ == 3):
            if not object:
                print("Queue is empty")
            else:
                print("Top element of Queue is : " + object[0])
        elif (input_ == 4):
            print("Size of Queue is : ", len(object))
        elif (input_ == 5):
            if not object:
                print("Queue is empty")
            else:
                print(object)
        elif (input_ == 6):
            if not object:
                print("Queue is empty")
            else:
                object.sort()
        elif (input_ == 7):
            if not object:
                print("Queue is empty")
            else:
                object.reverse()
        elif (input_ == 8):
            if not object:
                print("Queue is empty")
            else:
                print(min(object))
        elif (input_ == 9):
            if not object:
                print("Queueis empty")
            else:
                print(max(object));
        else:
            print("Invalid input")


# Main body
object = []
Queue_Implementation(object)
