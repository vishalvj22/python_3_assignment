file_to_read = "main.txt"
write_to_file = "duplicate.txt"
file = open(file_to_read, "r")
data = file.read()
file.close()

with open(write_to_file, "a") as file:
    file.write(data)

print('completed')
