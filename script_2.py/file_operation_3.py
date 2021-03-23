# def write_to_file(file_name, file_contents):
#      print("")
#      # Add code to save data in variable file_contents to file named file_name

# if __name__ == '__main__':
#     file_name = input("Enter the name of file: ")
#     file_contents = input("Enter the contents to be stored in a file: ")
#     write_to_file(file_name, file_contents)

file_name = input("Enter the name of file: ")

content = input("Enter the contents to be stored in a file: ")

file = open(file_name, "w+")
file.write(content)
print(f"A file named {file.name} is created with {content} as its contents")
file.close()
