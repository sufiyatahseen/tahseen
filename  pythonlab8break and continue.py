numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1 
    if count == 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)
a=(2,4,6,8,10)
num_sum=0
count=0
for i in numbers:
    num_sum=num_sum+i
    count=count+1
    if count==2:
        break
print("sum of first ",count,"integers is:",num_sum)
a=[1,2,3,4,5]
for x in a:
    if x%2==0:
        break
print(x)
a=[12345678]
for i in a:
    if i%1==0:
        break
print(i)
a=[12,34,56]
for i in a:
    if i%5==0:
        break
print(i)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1 
    if count == 5:
        continue
print("Sum of first ",count,"integers is: ", num_sum)
a=(1,2,3,4,5,6,7,8,9)
for i in a:
    if i%2==0:
        continue
print(i)
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if(i==2):
        break
print(i)
for x in range(7):
    if (x ==3):
        break
    print(x)
a = (2, 4, 6)
for x in a:
    if x%5==0:
        break
print(x)
for letter in 'Python':     
   if letter == 'h':
      break
   print (letter),letter
 
n=1
while True:
  print (n)
  n+=1
  if n==5:
    break
print("After Break")
 
for str in "Python":
    if str == "t":
        break
    print(str)
print("Exit from loop")


   
    

