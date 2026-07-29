SIZE=5
queue=[0]*SIZE
front=-1
rear=-1
def enqueue (value):
    global front,rear
    if rear==SIZE-1:
        print("Queue is FULL!!! Insertion is not possible!!!")
    else:
        rear+=1
        queue[rear]=value
        print(value,"inserted into the queue")
def dequeue():
    global front,rear
    if front==rear:
        print("queue is EHPTV!!!")
    else:
        front+=1
        print(queue[front],"deleted from the queue")
    if front==rear:
        front=-1
        rear=-1
def display():
    global front,rear
    if front==rear:
        print("Queue is EMPTY!!!")
    else:
        print("Queue Element:")
        for i in range(front +1,rear+1):
            print(queue [i],end="")
        print()
def size():
    print("Queue size=",rear-front)
while True:
    print("/n QUEUE OPERATIONS")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.size")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=input("Enter car number:")
        enqueue(value)
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        size()
    elif choice==5:
        print("program Ended")
        break
    else:
        print("Invalid choice")
