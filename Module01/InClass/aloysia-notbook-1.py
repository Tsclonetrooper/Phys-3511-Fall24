


def concatinate():
    list1 = ['wh','Y','gon','ca']
    list2 = ['o','a','na','ll']
    list3 = [list1[0] + list2[0],list1[1] + list2[1],list1[2] + list2[2],list1[3] + list2[3]]
    print(list3)

def numbers():
    previous_number = 0
    sum = 0
    for i in range(10):
        #print(i)
        
        sum = previous_number + i
        print('Current Number: {}, Previous Number: {}, Total Sum: {}'.format(i,previous_number,sum))
        previous_number = i

def is_odd():
    #print(n)

    n = int(input('Give me number: '))


    if n == 0:
        print('{} is Zero'.format(n))
    elif n % 2 == 0:
        print('{} is even'.format(n))
    elif n % 2 != 0:
        print('{} is odd'.format(n))
    else:
        print('error')
        


def tup():
    tuple1 = (0, 5, 10, 15)
    a = tuple1[0]
    print(a)
    b = tuple1[1]
    print(b)
    c = tuple1[2]
    print(c)
    d = tuple1[3]
    print(d)




def main():
    print()
    concatinate()
    print()
    numbers()
    print()
    is_odd()
    print()
    tup()
    


if __name__ == '__main__':
    main()
