# def process_string(sentence):
#      print("")


# if __name__ == '__main__':
#     sentence = input("Enter a long sentence:")
#     process_string(sentence)

user_input = input("Enter your word ")
print("Uppercase", user_input.upper())
print("lowercase",user_input.lower())
print("capatalize",user_input.capitalize())
print("D replaced by H", user_input.replace('d','h'))
print("O replaced by ZM",user_input.replace('o','zm'))
print("A occurs",user_input.count('a'),"times")
print("No. of letter",len(user_input))
