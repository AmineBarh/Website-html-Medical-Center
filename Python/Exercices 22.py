
# Ex1::

ch= input("Enter the char : \n")
print("La longeur est : "+ "is", len(ch))
print("OR")
print("La longeur est :     "+ "is", len(input()))

# Ex2::

# ch=input("Enter the phrase: \n")
# j=0
# for i in range(len(ch)):
#     if (ch[i]==" "):
#         j= j+1
# print("Length of the ch is: ", len(ch)-j)
# {OR
# {L = ch.split()
# {print(len(L)-1)


# Ex3::  
# ch = input("Entrez une chaîne de caractères : ")

#  Afficher la liste de caractères
# listec = list(ch)
# print("Liste de caractères :", listec)

# Ex4::

# ch=input("Enter char: \n")
# for i in range(len(ch)):
#     if (i==7):
#         nch=ch[:7]+ch[8:]
#         print(nch)

# Ex5::

# j,k= 0,0
# ch=input("Enter the phrase:\n")
# for i in range(len(ch)): #       for c in ch:
#     if ch[i].isupper():   #        if c.islower():
#         j=j+1
#     elif ch[i].islower(): #        elif c.isupper():
#             k=k+1
# print("Maajus number is:", j ," and minus number is: ", k)

# Ex6::

# ch="Monsieur Monsieur monsieur Plombier est là"
# nch=ch.replace("Monsieur", "M.")
# print(nch)

# Ex7::

# 
# ch="RACECAR "
# ch=ch.lower()
# ch=ch.split()
# j=0
# for i in range(len(ch)):
#     if(ch[i]!=ch[len(ch)-i-1]):
#         j=1
#         print("The word is not palindrom")
#         break
# if j==0:
#     print("Word is palindrom")
# 
# print("OR:\n")
# 
# if ch == ch[::-1]:
#     print("Word is a palindrom")
# else:
#     print("Word is not palindrom")

# Ex8::

# ch=[]
# while True:
#     nu = int(input("Entrez un entier, 0 pour arrêter : "))
#     if nu == 0:
#         break
#     ch.append(nu)
# s=0
# print("La liste est: \n", ch)
# print("Longeur du list est:   ",len(ch))
# for i in range(len(ch)):
#     s=s+int(ch[i])
# 
# print("La somme du liste est:   ",s)        #               (( Or ))          n=sum(ch)   then/  print(n)
# pos=int(input("Enter position:  "))
# newel=int(input("Enter the element:   "))
# ch.insert(pos,newel)
# print(ch)
# ch.sort()   
# print("Sorted list is:  ", ch)
# pos1=int(input("Enter position '2':  "))
# ch.pop(pos1) #  del ch[pos1]
# print(ch)

# Ex9::

# idk={}     #  or idk={"num1": 1, "num2": 7, "num3": 9} ...
# idk["num1"]=1
# idk["num2"]=7
# idk["num3"]=9
# idk["num4"]=2
# print("Nombre d'élement:    ",len(idk))
# idk.update({"num5": 5})
# print("La nouvelle dic est:    ", idk)

# # Ex10::


# idk={}
# keys = ["Dix","Vingt","Trente"]
# values = [10 , 20 , 30]
# idk.update(zip(keys, values))
# print(idk)

# Ex11::

# s=0
# ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
# print(ventes.values())
# for i in ventes.values():
#     s=s+i
# print("somme est:"  ,s)   #         OR      sum(ventes.values())

# Ex12::

# ventes.pop("Dupont")
# print(ventes)

# Ex13::

# dic={}
# s=0
# ch=input("Enter ur phrase:  ")
# for i in range(len(ch)):                #  for c in ch:
#     s=ch.count(ch[i])
#     dic[ch[i]]=s
# print(dic)

# Ex14::

# num1=input("Enter number 1: ")
# num2=input("Enter number 2: ")
# num3=input("Enter number 3: ")
# max=num1
# if num2>max:
#     max=num2
# if num3>max:
#     max=num3
# print("Max of the three numbers is: ", max)

# Ex15::

# ch=input("Enter your caracter")
# if 'a'<= ch <= 'z' or 'A'<= ch <= 'Z' :
#     print("ch is alphabet")
# elif '0' <= ch <= '9':
#     print("ch is number")
# else:
#     print("nor number nor alphabet")

# Ex16::

# sum=0
# l=[]
# while True:
#     num=int(input("Enter number or 0 to stop:   "))
#     if num==0:
#         l.append(num)
#         break
#     sum= sum+ num
# print("La somme est:    ", sum, "   de la liste", l)

# Ex17::

# fact=1
# num=int(input("Enter number:    "))
# def fact(num):
    # while True:
    #     for i in range(1, num+1):  #  you need that +1 to reach the final
    #         fact=fact*i
    #     break
    #    ---------   # 
    # if num==0:
    #     return 1
    # else:
    #     return num*fact(num-1)
# print("Factoriel de", num, " est:\n",fact(num))


# Ex18::

# num=int(input("Enter amplitude of the triangle:     "))
# while True:                                              
#     for i in range(1,num+1):                            
#         print(" "*(num-i),"*"*(2*i-1))
#     break

# Ex19::

#  202 if we are talking about the first 100 paire numbers
# 
# i=2
# sum=0
# while i<102:
#     sum=sum+i
#     i=i+2
# print("la somme des 100 premiers entiers paires:    ", sum)
# sum2=0
# for i in range(2,102,2):
#     sum2=sum2+i
# print("la somme 2 des 100 premiers entiers paires:    ", sum2)


# Ex20::

# dic={}
# ch=input("Exter the sentence:   ")
# for i in range(len(ch)):
#     if ch[i] in {'o', 'u', 'y', 'e','i'}:
#         dic[ch[i]]=ch.count(ch[i])
# print(dic)

# Ex21::


# for i in range(6,0,-1):
#        for j in range(i,0,-1):  
#             print(j)            #  there is some kind of problem here


#Ex22::

# niveau=0
# dic={}
# ch=input("Enter your password:  ")
# for c in ch:
#     if any( len(ch)<8, c.islower(), c.isupper()):
#         return False