# def defaultdict(elements):
#      print(elements)


# if __name__ == '__main__':
#     count_of_elements = int(input("Enter no of Elements:"))
#     elements = []
#     for i in range(1,count_of_elements+1):
#         temp_variable = int(input("Input "+str(i)+":"))
#         elements.append(i)
#     defaultdict(elements)
from collections import OrderedDict
n = int(input("enter length: "))
d={}
for i in range(1,n+1):
    inp = int(input(f"Input {i}: "))
    d[inp] = i
d2 = OrderedDict(d)
print("Distionary: ",d)
print(d2)
    
