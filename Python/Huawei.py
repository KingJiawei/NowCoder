#字符串最后一个单词的长度 
str_input = input()
str_split = str_input.strip().split()
last_str = str_split[-1]
print(len(last_str))

#计算字符个数 
input_str = input()
input_char = input()

input_char_lower = input_char.lower()
input_str_lower = input_str.lower()

print(input_str_lower.count(input_char_lower))

#明明的随机数 
num = int(input())
num_set = set()
for i in range(num):
    random_num = int(input())
    if random_num not in num_set:
        num_set.add(random_num)
        
num_list = list(num_set)
num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])
    print('\n')
	
#字符串分隔 
str1 = input()
str2 = input()
def split_str(input_str):
    str_length = len(input_str.strip())
    zero_num = 0
    if str_length % 8 != 0:
        zero_num = 8 - (str_length % 8)
    for i in range(zero_num):
        input_str += '0'
    j = 0
    while j < (len(input_str)):
        print(input_str[j:j+8])
        j += 8

split_str(str1)
split_str(str2)

#进制转换 
while True:
    input_str = input()
    str_split = input_str.split()
    for i in range(len(str_split)):
        print(int(str_split[i],16))
		
#质数因子 
input_num = int(input())
result_list = []
start_data = 2
def getResult(start_data,data):
    if data == 0:
        return 0
    for i in range(start_data,data):
        if data%i == 0:
            result_list.append(i)
            getResult(i,int(data/i))
            return 1
    result_list.append(data)
    return 0
getResult(start_data,input_num)
for i in range(len(result_list)):
    print(result_list[i],end=" ")

#取近似值 
import math
input_float = float(input())
left = math.floor(input_float)
right = input_float - left
if (right>=0.5):
    print(left+1)
else:
    print(left)
	
#合并表记录 

dict_num = int(input())
dict_input = {}
for i in range(dict_num):
    key,value = map(int,input().strip().split())
    if key not in dict_input.keys():
        dict_input[key] = value
    else:
        dict_input[key] += value
dict_order = sorted(dict_input.items(),key=lambda x:x[0])
for item in dict_order:
    print(item[0],end=" ")
    print(item[1])

#提取不重复的整数 
input_str = input()
i = -1
resever_str = ""
try:
    while input_str[i]:
        if resever_str.find(input_str[i]) == -1:
            resever_str += input_str[i]
        i -= 1
except:
    pass
resever_int = int(resever_str)
print(resever_int)

#字符个数统计 
input_str = input()
ascii_set = set()
count = 0
for i in range(len(input_str)):
    ascii = ord(input_str[i])
    if 0<=ascii<=127 and ascii not in ascii_set:
        ascii_set.add(ascii)
        count += 1        
print(count)

#数字颠倒 
print(input()[::-1])

#字符串反转 
input_str = input()
print("".join(input_str[i] for i in range(len(input_str)-1,-1,-1)))

#句子逆序 
input_str = input()
input_list = input_str.strip().split()
reverse_list = " ".join(input_list[i] for i in range(len(input_list)-1,-1,-1))
print(reverse_list)

#字串的连接最长路径查找 
input_num = int(input())
input_str_list = []
for i in range(input_num):
    input_str_list.append(input())
input_str_list.sort()
for i in range(len(input_str_list)):
    print(input_str_list[i])
	
#求int型正整数在内存中存储时1的个数 
input_num = bin(int(input()))
input_str = str(input_num)
print(input_str.count('1'))




