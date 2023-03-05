# def find_max(num1, num2):
#     max_num=-1
#     a=[]
#     # Write your logic here
#     if(num1<num2):
#         for i in range(num1,num2+1):
#             st=str(i)
#             if(st==2 and i%5==0):
#
#               s=0
#               r=i%10
#               s=s+r
#               i=i/10
#               if(s%3==0):
#                 a.append(i)
#     max_num=max(a)
#     return max_num
#
# max_num=find_max(10,15)
# #print(max_num)

def find_max(num1, num2):
    list2=[]
    max_num=-1
    list1=list(range(num1,num2+1))
    if num1>=num2:
        max_num=-1
    else:
        for i in list1:
            temp = i
            rem=0
            s=0
            while temp!=0:
                rem=temp%10
                s=s+rem
                temp=temp//10
            if s%3==0 and i%5 ==0 and len(str(i)) == 2:
                    list2.append(i)
        if(len(list2)!=0):
            list2.sort()
            max_num = list2[-1]
        else:
            max_num=-1
    return max_num
max_num=find_max(10,15)
print(max_num)

