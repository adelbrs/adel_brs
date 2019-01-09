def main():
    age=input("enter your age")
    if (int(age)>=8 and int(age)<=10):
        print ("kids")
    elif(int(age)>=11 and int(age)<=18) :
        print("teenage")
    else:
        print("young")
    print("out of range")


if __name__ == '__main__':main()
