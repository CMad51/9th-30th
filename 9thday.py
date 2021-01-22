'''for number in range(11):
   print(number)

_number=10
while _number>=0:
  print(_number)
 _number-=1

for  item in range(11) :
 str_of_item=str(item)
 print(str_of_item,'x',str_of_item,'=',str(item**2))


#9
_sum=0
for number in range(0,101):
 _sum+=number
print(_sum)'''

#12

fruit_list=['banana', 'orange', 'mango', 'lemon']
length=len(fruit_list)
print(length)
reverse_fruit_list=[ ]

for number in range (length-1,-1 ,-1):
 reverse_fruit_list.append(fruit_list[number])
print(reverse_fruit_list)

