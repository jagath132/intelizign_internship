# 1.Get the name from given input data. (Note: Don't use direct slicing..)
def name_extraced():
    data1 = "From nandhini@gmail.com Sat Jan 21 11:24:32.008173"
    data2 = "From selvakumar@gmail.com Sat Jan 21 11:24:32.008173"
    data3="From jagath@gmail.com Sat Jan 26 11:24:32.008173"

    def extract_name(data):
        email=data.split()[1]
        name=data.split('@')[0]
        return name
        
    name1=extract_name(data1)
    name2=extract_name(data2)
    name3=extract_name(data3)
    
    print (f'filename1 = "{name1}", name2 = "{name2}","name3={name3}"')

# Reverse the 5-digit number entered by the user
def reverse():
    num=list(input("Enter the numbers to reverse:"))
    # num = [1,2,3,4,5]
    output=[]
    le=len(num)
    for c in range(le):
        last_dig =le - c -1
        output.append(num[last_dig])
    print(output)

# 3.Remove the duplicate elements from given Input list:
def removing_duplicate():
    duplicate_list= ["Apple" ,"Mango" , "Pineapple", "Orange", "Apple", "Mango", "Grapes","Grapes"]
    new_list=[]
    for d in duplicate_list:
        if d in new_list:
            pass
        else:
            new_list.append(d)
    print(new_list)

# 4.find the occurrence and count of vowels in an input string:
def vowels():
    input_string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    vowel_count = {}

    for char in input_string:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
    print(f"Vowel occurrences and count: {vowel_count}")

# 5.write a program to find the sum of first 10 nos which is divisible by 3 and 5
def sum():
    count = 0
    total_sum = 0
    num = 1
    while count<10:
        if num%3==0 and num%5==0:
            total_sum+=num
            count+=1
        num+=1
    print(f'the sum of first 10 nos which is divisible by 3 and 5:{total_sum}')

# 6.Find the second Largest & smallest nos from an Input list:
def second_value():
    num=[45,98,32,19,67,55,90]
    print(f'the user input list before sorting:',num)
    for a in range(0,len(num)):
        for b in range(a+1,len(num)):
            if num[a]>= num[b]:
        
                num[a], num[b] = num[b], num[a]
    print(f'the user input list after sorting:',num)
    print(f'the second largest no from the input list:',num[1])
    print(f'the second smallest no from the input list:',num[-2])

# 7.Sort this list:['greeting', 'goodbye', 'thanks', 'about', 'name', 'help', 'create account', 'complaint']
# sorted_list = ['greeting', 'goodbye', 'thanks', 'about', 'name', 'help', 'create account', 'complaint']
# sorted_list.sort()
# print(sorted_list) need to change



# 8.Find the square of first 10 numbers:
def square():
    n=10
    number={}
    for i in range (1,n+1):
        number[i] =i*i
    print("the square of first 10 numbers:",number)


# 13.convert Input sentence into list of words.
def sen_split():
    sen="The coding question of Java Programming will help you to crack the coding interview rounds"
    sentence = sen.split()
    print(sentence) 

# 14.Convert List of values into string:
def sen_join():
    sen1=["The", "coding", "question", "of", "Java", "Programming", "will" , "help", "you", "to", "crack" , "the", "coding", "interview", "rounds"]
    sentence_join=" ".join(sen1)
    print(sentence_join)

# 15.write a program to print following patterns:
# *
# **
# ***
# ****
# *****
def pattern_1():
    n=int(input("enter the number to print the '*':"))
    for i in range(0,n+1):
        for j in range(i):
            print("*",end=" ")
        print()

# *****
# ****
# ***
# **
# *
def pattern_2():
    n=int(input("enter the number to print the '*':"))
    for i in range(0,n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
def pattern_3():
    print("pattern_3")
    n=int(input("the no .of rows to print:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()

# 4.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def pattern_4():
    print("pattern_4")
    n=int(input("the no .of rows to print:"))
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1
        print()

# 5.
# A
# A B
# A B C
# A B C D
# A B C D E

def pattern_5():
    print("pattern_5")
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


# 6.
# A
# B C
# D E F
# G H I J
def pattern_6():
     print("pattern_6")
     n = int(input("enter the number of rows:"))
     for i in range(1, n + 1):
          for j in range(i):
               print(chr(65 + j), end=" ")
          print()        


# 9.Write a program to bring the output
# Input: [{"id": 47,"name":"sravya", "game":"cricket"},
# {"id": 49,"name":"krishna", "game":"tennis"},
# {"id": 33,"name":"vinothini", "game":"volleyball"},
# {"id": 21,"name":"samuel", "game":"cricket"},
# {"id": 17,"name":"bhuvana", "game":"tennis"}]
# output: {"cricket":[sravya,samuel],"tennis":[krishna,bhuvana],"volleyball":[vinothini]}
def get_players():
    input = [{"id": 47,"name":"sravya", "game":"cricket"},
                {"id": 49,"name":"krishna", "game":"tennis"},
                {"id": 33,"name":"vinothini", "game":"volleyball"},
                {"id": 21,"name":"samuel", "game":"cricket"},
                {"id": 17,"name":"bhuvana", "game":"tennis"}]
    output = {}
    for a in input:
        if a["game"] in output:
            output[a["game"]].append(a["name"])
        else:
            output[a["game"]] = [a["name"]]
    print(output)

# function calling stmt
if __name__ == "__main__":
    # name_extraced()
    # reverse()   
    # vowels()
    # removing_duplicate()
    # sum()
    # square()
    # second_value()
    # get_players()
    # sen_split()
    # sen_join()
    # pattern_1()
    # pattern_2()
    # pattern_3()
    # pattern_4()
    # pattern_5()
    # pattern_6()
    pass