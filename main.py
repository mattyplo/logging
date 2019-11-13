def countImperdietInSentence(sentence):
  count = 0
  wordsInSentence = sentence.split()
  for word in wordsInSentence:
    if word == "imperdiet":
      count += 1
  return count

def imperdietIsInSentence(count):
  return count > 0

def readFile():
  
  fileSource = input("What is the destination of the file you'd like to read?")
  file = open(fileSource, "r")
  fileText = file.read()
  sentences = fileText.split(".")
  numLinesWithImperdiet = 0
  numImperdietInFile = 0
  for sentence in sentences:
    numImperdietInSentence = countImperdietInSentence(sentence)
    numImperdietInFile += numImperdietInSentence
    if numImperdietInSentence > 0:
      numLinesWithImperdiet += 1

  print("number of lines with imperdiet: ", numLinesWithImperdiet)
  print("number of times imperdiet appears: ", numImperdietInFile)
  
def writeFile():
  
  fileSource = input("What is the destination of the file you'd like to write to?")
  file = open(fileSource, "w")

def readOrWritePrompt():
  
  readWriteChoice = input("Would you like to read a file or write to a file?\nType r to read, or type w to write. ")
  if readWriteChoice is 'r':
    readFile()
  elif readWriteChoice is 'w':
    writeFile()
  else: 
    print("I'm sorry, but you must select w or r to move forward with this program.  Try starting the program over.")


readOrWritePrompt()      
