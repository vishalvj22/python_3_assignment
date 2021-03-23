# def file_process(file_name):
#      print("Here are the contents of",file_name+".txt" )
#      # Add code to read numbers/<file_name>.txt and print its content


# if __name__ == '__main__':
#     file_name = int(input("Enter a number between 1 and 10: "))
#     file_process(file_name)

number = input("Enter a number between 1 and 10 : ")
if int(number) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    filename = number + ".txt"
    file = open(filename, 'r')
    print(file.read())
else:
    print("Please select number between 1 and 10.")
