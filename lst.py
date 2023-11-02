# l1=[1,2,3,4,5,6,7,8,9,10]
# l1=[11,13,15,17,18]

# List Comprehension
# ev=[x for x in l1 if x%2==0]
# od=[x for x in l1 if x%2==1]
# print(ev)
# print(od)


# Concatenation
# ev=[]
# od=[]
# for i in l1:
#     if i%2==0:
#         ev+=[i]
#     else:
#         od+=[i]
# print(ev)
# print(od)



# l1=[1,2,3,4,5,6,7,8,9,10]
# ev=[]
# od=[]
# c=0
# for i in l1:
#     c+=1
# for i in range(c):
#     if i%2==0:
#         od+=[l1[i]]
#     else:
#         ev+=[l1[i]]
# print(ev)
# print(od)


# length=int(input("Enter the length : "))
# l1=[]
# for i in range(length):
#     # n=input("Input : ")
#     # l1+=[n]
#     l1+=[input("Input : ")]
# print(l1,type(l1))



# class My_list:
#     def create_list(self,n):
#         l1=[int(input()) for i in range(n)]
#         return l1

# obj1=My_list()
# l1=obj1.create_list(5)
# print(l1)


import random as rdm


# l1=[rdm.randint(1,100) for i in range(int(input()))]
# print(l1)
# ev,od=0,0
# for i in l1:
#     if i%2==0: ev+=1
#     else: od+=1
# print(f"""
# Even          :        {ev}
# Odd           :        {od}""")

'''
10
[70, 97, 9, 98, 29, 26, 12, 94, 70, 98]

Even          :        7
Odd           :        3
'''




# l1=[rdm.randint(1,100) for i in range(int(input()))]
# print(l1)
# ev,od=[],[]
# for i in l1:
#     if i%2==0: ev+=[i]
#     else: od+=[i]
# d1={"Even" : ev, "Odd" : od}
# print(d1)
'''
5
[2, 92, 45, 28, 67]
{'Even': [2, 92, 28], 'Odd': [45, 67]}
'''

# l1=[]
# n=int(input())
# while len(l1)<n:
#     c=rdm.randint(1,100)
#     if c not in l1: l1+=[c]
# print(l1)

'''
5
[28, 52, 83, 24, 77]
'''


# n=int(input())
# l1=[rdm.randint(1,100) for i in range(int(input()))]
# def is_prime(x):
#     if n==1: return False
#     for i in range(2,x):
#         if x%i==0: return False
#     return True 


# l2=[]
# for i in l1:
#     if is_prime(i):
#         l2.append(i)
# print(l2)



# l1=[10,20,30,40,50,50]
# def list_sum(l):
#     a=0
#     for i in l:
#         a+=i
#     return a
# print(list_sum(l1))
'''
200
'''

# l1=[10,20,30,40,50,60,70,80]
# l2=[30,40,50,60]
# l3=[]
# mx = l1 if len(l1)>len(l2) else l2
# i=0
# while i<min(len(l1),len(l2)):
#     l3+=[l1[i]+l2[i]]
#     i+=1
# l3+=mx[i:]
# print(l3)
'''
[40, 60, 80, 100, 50, 60, 70, 80]
'''


# l1=[10,20,30,40,50,60,70,80,90]
# l2=[]
# a=True
# for i in l1:
#     if a:
#         l2+=[i]
#     else:
#         l2=[i]+l2
#     a=not(a)


## l2=l1[1::2][::-1] + l1[0::2]
# print(l2)

'''
[80, 60, 40, 20, 10, 30, 50, 70, 90]'''


# l1=[10,20,30,40,50,60,70,80,90]
# l2=[]
# k=int(input())
# # for i in range(0,len(l1),k):
#     # l2.append(l1[i:i+k])
#     # l2+=[l1[i:i+k]]


# l2=[l1[i:i+k] for i in range(0,len(l1),k)] 
# print(l2)

'''
3
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
'''

# l1=[10,20,30,40,50,60,70,80,90]
# l2=[]
# l2=l1.reverse()
# print(l2,l1)
'''
[90, 80, 70, 60, 50, 40, 30, 20, 10]
'''


# l1=[10,20,30,40,50,60,70]
# l2=[]
# for i in l1:
#     l2=[i]+l2
# print(l2)

'''
[70, 60, 50, 40, 30, 20, 10]
'''


# l1=[89,1,19,11,18,14,4,2,3,5,98,56,74]
# for i in range(len(l1)-1):
#     for j in range(i+1,len(l1)):
#         if l1[i] > l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)
'''
[1, 2, 3, 4, 5, 11, 14, 18, 19, 56, 74, 89, 98]
'''


# only integers sorting
# l1=['spi',10,'Iron',56,"Thor","Ant",74,83,'hulk',5,14,19]
# for i in range(len(l1)-1):
#     if type(l1[i])==int:
#         for j in range(i+1,len(l1)):
#             if type(l1[j])==int:
#                 if l1[i] > l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
# print(l1)
'''
['spi', 5, 'Iron', 10, 'Thor', 'Ant', 14, 19, 'hulk', 56, 74, 83]
'''

# only string sorting
# l1=['Spi',10,'Iron',56,"Thor","Ant",74,83,'Hulk',5,14,19]
# for i in range(len(l1)-1):
#     if type(l1[i])==str:
#         for j in range(i+1,len(l1)):
#             if type(l1[j])==str:
#                 if l1[i] > l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
# print(l1)
'''
['Ant', 10, 'Hulk', 56, 'Iron', 'Spi', 74, 83, 'Thor', 5, 14, 19]
'''
    
# Both integer and string sorting
# l1=['Spi',10,'Iron',56,"Thor","Ant",74,83,'Hulk',5,14,19]
# for i in range(len(l1)-1):
#         for j in range(i+1,len(l1)):
#             if type(l1[i])==type(l1[j]):
#                 if l1[i] > l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
# print(l1)
'''
['Ant', 5, 'Hulk', 10, 'Iron', 'Spi', 14, 19, 'Thor', 56, 74, 83]
'''


# converting multidimensional list to single dimensional list
l1=[['Spi',10],['Iron',[56,"Thor"],"Ant"],[74,83],'Hulk',[5,[14],19]]
# print(l1)

# l2=[]
# def fun(l):
#     global l2
#     for i in l:
#         if type(i)==list:
#             fun(i)
#         else:
#             l2+=[i]
# fun(l1)
# print(l2)

'''
[['Spi', 10], ['Iron', [56, 'Thor'], 'Ant'], [74, 83], 'Hulk', [5, [14], 19]]
['Spi', 10, 'Iron', 56, 'Thor', 'Ant', 74, 83, 'Hulk', 5, 14, 19]
'''


# n=input()
# if ord("A")<=ord(n) and ord(n)<=ord("Z"):
# # if "A"<=n<="Z":
#     print(f"{n} is an Upper case")
# # elif ord("a")<=ord(n) <= ord("z"):
# elif "a"<=n<="z":
#     print(f"{n} is a Lower case")
# elif "0"<=n<="9":
#     print(f"{n} is a number")
# else:
#     print(f"{n} is a Special Character")




# a=input()
# u,l,n,s=0,0,0,0
# for i in a:
#     if "A"<=i<="Z":
#         u+=1

#     elif "a"<=i<="z":
#         l+=1
#     elif "0"<=i<="9":
#         n+=1
#     else: 
#         s+=1

# print(f'''
# Upper      :       {u}
# Lower      :       {l}
# Number     :       {n}
# Special    :       {s}''')


# l1=["$p!der","!ron",1947,18.10,"B@tm@n","Hulk","Thor3"]
# l2=[]
# for i in l1:
#     if type(i)==str:
#         c=0
#         for j in i:
#             if not("A"<=j<="Z" or  "a"<=j<='z' or '0'<=j<='9'):
#                 c+=1
#         if c!=0 and c%2==0:
#             l2.append(i)  
# print(l2)


# l1=["a","b","c"]
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# print(fact(len(l1)))
# c=[]
# while len(c)!=fact(len(l1)):
#     d=[]
#     while len(d)!=len(l1):
#         e=rdm.randint(0,len(l1)-1)
#         if e not in d:
#             d.append(e)
#     if d not in c:
#         c.append(d)
#     d=[]
# # print(c)
# res=[]
# for i in c:
#     l2=[]
#     for j in i:
#         l2.append(l1[j])
#     res.append(l2)
# print(res)

'''
6
[['c', 'a', 'b'], ['c', 'b', 'a'], ['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'c', 'a'], ['b', 'a', 'c']]
'''



# l1=["a","b","c"]
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# print(fact(len(l1)))
# c=[]
# while len(c)!=fact(len(l1)):
#     d=[]
#     while len(d)!=len(l1):
#         # e=rdm.randint(0,len(l1)-1)
#         e=rdm.choice(l1)
#         if e not in d:
#             d.append(e)
#     if d not in c:
#         c.append(d)
#     d=[]
# print(c)
'''
6
[['a', 'c', 'b'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['a', 'b', 'c'], ['b', 'a', 'c'], ['c', 'b', 'a']]
'''


# l1=[10,20,30,40,50]
# k=int(input())
# for i in range(k):
#     l1=l1[-1:]+l1[:-1]
# print(l1)

'''
k=1
[50, 10, 20, 30, 40]
k=2
[40, 50, 10, 20, 30]'''

# l1=[10,20,30,40,50]
# k=int(input())
# for i in range(k):
#     l1=l1[1:]+l1[:1]
# print(l1)
'''
k=2
[30, 40, 50, 10, 20]
k=1
[20, 30, 40, 50, 10]
'''



# l1 = [52, 10, 19, 18, 5, 4, 10, 11, 23, 9, 85, 62]

# maximum = l1[0]
# minimum = l1[0]

# for i in l1:
#     if i > maximum:
#         maximum = i
#     elif i < minimum:
#         minimum = i

# print("Maximum value in the list is:", maximum)
# print("Minimum value in the list is:", minimum)
'''
Maximum value in the list is: 85
Minimum value in the list is: 4
'''


# l1=[10,20,10,30,40,20,10,30,45,20,10,50,60,30]
# print(l1)
# l1=list(set(l1))
# print(l1)

'''
[40, 10, 45, 50, 20, 60, 30]
'''

# l1=[10,20,10,30,40,20,10,30,45,20,10,50,60,30]
# print(l1)
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)
'''
[10, 20, 10, 30, 40, 20, 10, 30, 45, 20, 10, 50, 60, 30]
[10, 20, 30, 40, 45, 50, 60]
'''


# l1=[10, 20, 30, 40, 45, 50, 60]
# def rem(n):
#     if n not in l1:
#         print("number is not in list")
#     else:
#         l1.remove(n)
#         print(l1)
# rem(int(input("n:"))) 
'''
n:10
[20, 30, 40, 45, 50, 60]'''


# l1=[10,20,30,40,50,60,70,80,90]
# print(l1)
# n=int(input())
# for i in range(len(l1)):
#     if l1[i]==n:
#         l1=l1[:i]+l1[i+1:]
#         break
# else:
#     print(f"{n} not in list")
#     exit()
# print(l1)
'''
50
[10, 20, 30, 40, 60, 70, 80, 90]
'''


# l1=[10,20,30,40,50,60,70,80,90]
# print(l1)
# n=int(input())
# for i in range(len(l1)):
#     if i==n:
#         l1=l1[:i]+l1[i+1:]
#         break
# else:
#     print(f"IndexError: list index out of range")
#     exit()
# print(l1)
'''
2
[10, 20, 40, 50, 60, 70, 80, 90]

[10, 20, 30, 40, 50, 60, 70, 80, 90]
10
IndexError: list index out of range
'''

# l1=[10,20,30,10,20,40,50,30,10,50,60,70,20,10]
# print(l1)
# k=int(input())
# c=0
# for i in l1:
# for i in l1:
#     if i==k:
#         c+=1
# print(c) 
'''
[10, 20, 30, 10, 20, 40, 50, 30, 10, 50, 60, 70, 20, 10]
10
4
'''



# l1=[10,20,30,10,20,40,50,30,10,50,60,70,20,10]
# print(l1)
# d1={}
# for i in set(l1):
# # for i in l1:
#     c=0
#     for j in l1:
#         if i==j:
#             c+=1
#     d1[i]=c
# print(d1)
'''
[10, 20, 30, 10, 20, 40, 50, 30, 10, 50, 60, 70, 20, 10]
{70: 1, 40: 1, 10: 4, 50: 2, 20: 3, 60: 1, 30: 2}
'''

# Difference between diagonals




# l1=[[1,2,3],[2,3,1],[4,5,1]]
# l2=[[9,8,7],[1,3,5],[1,4,4]]
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(l1)):
#     for j in range(len(l1[i])):
#         result[i][j] = l1[i][j] + l2[i][j]

# print(result)
'''
[[10, 10, 10], [3, 6, 6], [5, 9, 5]]
'''