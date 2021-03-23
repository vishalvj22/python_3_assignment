# def append_ing(sentence):
#      print("")


# if __name__ == '__main__':
#     sentence = input("Enter a string:")
#     append_ing(sentence)
def add_string(str1):
    
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1

print("output string:",add_string(input()))
