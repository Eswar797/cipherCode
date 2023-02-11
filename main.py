alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text1=list(text)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#def encrypt(text,shift):
def encrypt(text,shift):
  text1=list(text)
  str=[]
  for i in range(len(text1)):
    for j in range(len(alphabet)):
      if(text1[i]==alphabet[j]):
        #text1[i]=alphabet[j+shift]
        new_shift=j+shift
        
    str.append(alphabet[new_shift])
  str1=""
  for i in str:
    str1=str1+i
  print("Your encoded word is "+str1)


def decrypt(text,shift):
  text1=list(text)
  str=[]
  for i in range(len(text1)):
    for j in range(len(alphabet)):
      if(text1[i]==alphabet[j]):
        #text1[i]=alphabet[j+shift]
        new_shift=j-shift
        
    str.append(alphabet[new_shift])
  str1=""
  for i in str:
    str1=str1+i
  print("Your decoded word is "+str1)


        
if(direction=="encode"):
  encrypt(text,shift)
else:
  decrypt(text,shift)
