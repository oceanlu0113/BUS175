# define alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

# encrypt method
def encrypt(original, N):
  # define the final message, will append to this 
  finalMessage = ""
  # define the counter
  counter = 0
  # in the string original, char is each character
  for char in original:
    # validate if char is alphanumeric
    if (char.isdigit() or char.isalpha()):
      # find the index in the alphabet
      location = int(alphabet.find(char))
      # find the new position, in respects to alphabet, N, and counter
      position = location + N + counter
      # find the remainder of position 36 so does not go out of bounds
      position %= 36
      # find the new character 
      finalChar = alphabet[position]
      # append the character to the final string message
      finalMessage = finalMessage + finalChar
      # increase counter
      counter = counter + 1
    # perserve characters that are not alphanumeric
    else:
      # preserve the characters and add them to final message
      finalMessage = finalMessage + char
      # increase counter
      counter = counter + 1
  # print the secret message
  print("Your secret message is: " + finalMessage)

# decrypt method
def decrypt(secret, N):
  finalMessage = ""
  # define the counter
  counter = 0
  # in the string original, char is each character
  for char in secret:
    # validate if char is alphanumeric
    if (char.isdigit() or char.isalpha()):
      # find the index in the alphabet
      location = int(alphabet.find(char))
      # find the new position, in respects to alphabet, N, and counter
      position = location - N - counter
      # find the remainder of position 36 so does not go out of bounds
      position %= 36
      # find the new character 
      finalChar = alphabet[position]
      # append the character to the final string message
      finalMessage = finalMessage + finalChar
      counter = counter + 1
    # perserve characters that are not alphanumeric
    else:
      finalMessage = finalMessage + char
      counter = counter + 1
  # print the original message
  print("Your original message is: " + finalMessage)

# run the main program forever until otherwise
while True:  
  # this message will repeat until entered "q" to quit
  message = input("Please enter a message, or q to quit: ");
  
  # validation for user to quit by breaking while loop
  if(message=="q"):  
    break 

  # see if string has "<>"
  elif (message.find("<>") != -1):
    # define function type (enc/dec)
    indexForFunc = message.index("<>")
    function = message[0:indexForFunc]
  
    # define N
    indexForN = message.rindex("<>") + 2
    N = int(message[indexForN:])

    # define message typed
    typedMessage = message[indexForFunc+2:indexForN-2]
  
    # calling encrypt function
    if(function == "enc"):
      # print message
      print("Your original message is: " + typedMessage)
      encrypt(typedMessage, N)
  
    # calling decrypt function
    elif(function == "dec"):
      # print secret message
      print("Your secret message is: " + typedMessage)
      decrypt(typedMessage, N)
    
    # validation for correct way to enter message with "<>"
    else:
      print("this is not the right way to enter a message")
  
  # validation for correct way to enter message
  else:
    print("this is not the right way to enter a message")
