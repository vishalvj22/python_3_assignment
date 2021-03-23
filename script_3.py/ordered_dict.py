# def orderdict(elements):
#      print(elements)


# if __name__ == '__main__':
#     count_of_elements = int(input("Enter no of Elements:"))
#     elements = []
#     for i in range(1,count_of_elements+1):
#         temp_variable = int(input("Input "+str(i)+":"))
#         elements.append(i)
#     orderdict(elements)
li=[]
dict={}
n=int(input("Enter number of inputs:"))
for i in range(n):
    n=input("enter number:")
    li.append(n)
    dict[i+1]=n
    print("List:",li)
    print("OrderedDict:",dict)
