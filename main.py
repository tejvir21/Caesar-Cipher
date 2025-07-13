
while True:
  small_letters=[]
  capital_letters=[]
  numbers=['0','1','2','3','4','5','6','7','8','9']
  symbols=['!','@','#','$','%','^','&','*','(',')','_','-','=','+','/','`','~',';',':','<','>','.','?',',','"',"'",'€','£','¥','₩','°','•','○','÷','●','□','■','♤','♡','◇','♧','☆','▪︎','¤','《','》','¡','¿']
  for i in range(97,123):
    small_letters.append(chr(i))
  
  for i in range(65,91):
    capital_letters.append(chr(i))
  
  def encryption(message,shift_no):
    new_message=''
    i=0
    while i<len(message):
      character=message[i]
      if character in small_letters:
        for j in range(26):
          if character==small_letters[j]:
            encrypted_no=(j+shift_no)%26
            new_message+=small_letters[encrypted_no]
            break
      elif character in capital_letters:
        for k in range(26):
          if character==capital_letters[k]:
            encrypted_no=(k+shift_no)%26
            new_message+=capital_letters[encrypted_no]
            break
      elif character in numbers:
        for l in range(10):
          if character==numbers[l]:
            encrypted_no=(l+shift_no)%10
            new_message+=numbers[encrypted_no]
            break
      elif character in symbols:
        for m in range(48):
          if character==symbols[m]:
            encrypted_no=(m+shift_no)%48
            new_message+=symbols[encrypted_no]
            break
      else:
        new_message+=character
      i+=1
    return new_message
  
  def decryption(message,shift_no):
    new_message=''
    i=0
    while i<len(message):
      character=message[i]
      if character in small_letters:
        for j in range(26):
          if character==small_letters[j]:
            decrypted_no=(j+shift_no)
            if decrypted_no<0:
              decrypted_no=(decrypted_no+26)%26
              new_message+=small_letters[decrypted_no]
              break
            else:
              new_message+=small_letters[decrypted_no%26]
              break
              
      elif character in capital_letters:
        for k in range(26):
          if character==capital_letters[k]:
            decrypted_no=(k+shift_no)
            if decrypted_no<0:
              decrypted_no=(decrypted_no+26)%26
              new_message+=capital_letters[decrypted_no]
              break
            else:
              new_message+=capital_letters[decrypted_no%26]
              break
      elif character in numbers:
        for l in range(10):
          if character==numbers[l]:
            decrypted_no=(l+shift_no)
            if decrypted_no<0:
              decrypted_no=(decrypted_no+10)%10
              new_message+=numbers[decrypted_no]
              break
            else:
              new_message+=numbers[decrypted_no%10]
              break
      elif character in symbols:
        for m in range(48):
          if character==symbols[m]:
            decrypted_no=(m+shift_no)
            if decrypted_no<0:
              decrypted_no=(decrypted_no+48)%48
              new_message+=symbols[decrypted_no]
              break
            else:
              new_message+=symbols[decrypted_no%48]
              break
      else:
        new_message+=character
      i+=1
    return new_message
    
      
    
  
  choice=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
  
  message=input("Type your message:\n")
  
  shift_no=int(input("Type the shift number:\n"))
  
  if choice=='encrypt':
    result=encryption(message,shift_no)
    print("Your encrypred message is:")
    print(result)
  elif choice=='decrypt':
    shift_no=(-1)*shift_no
    result=decryption(message,shift_no)
    print("Your decrypted message is:")
    print(result)
  else:
    print("Error! Please \n")

  print()
  run_again=input("You want to run again['yes' or 'no']:\n")
  if run_again=='yes' or run_again=='Yes':
    continue
  else:
    break

print("Goodbye!!!!")