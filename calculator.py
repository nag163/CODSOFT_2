print('*'*80)
print("\t\t\t\t CALCULATOR")
print('*'*80)
print(" HELLO USER")
print("\n1) ADDITION\n2) SUBRACTION\n3) MULTIPLICATION\n4)DIVISION\n5)SQUARE OF NUMBER\n6)EXPONENTIAL\n7)EXIT")
while(True):
   a=int(input('enter the operation that you need to perform:.'))
   if a==1:
        m=int(input('please enter the first number:  '))
        n=int(input('please enter the second number:  '))
        print('*'*80)
        print(' result of addition is : ',m+n)
        print('*'*80)
   elif a==2:
        m=int(input('please enter the first number:  '))
        n=int(input('please enter the second number:  '))
        print('*'*80)
        print(' result of subraction is : ',m-n)
        print('*'*80)
   elif a==3:
        m=int(input('please enter the first number:  '))
        n=int(input('please enter the second number:  '))
        print('*'*80)
        print(' result of multiplication is : ',m*n)
        print('*'*80)
   elif a==4:
        m=int(input('please enter the first number:  '))
        n=int(input('please enter the second number:  '))
        print('*'*80)
        print(' result of division is : ',m/n)
        print('*'*80)
   elif a==5:
        m=int(input('please enter the base number:  '))
        print('*'*80)
        print(' result of square is : ',m**2)
        print('*'*80)
   elif a==6:
        m=int(input('please enter the base number:  '))
        n=int(input('please enter the power of the number:  '))
        print('*'*80)
        print(' result of square root  is : ',m**n)
        print('*'*80)
   else:
        break

