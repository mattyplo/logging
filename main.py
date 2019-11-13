def countImperdietInSentence(sentence):
  count = 0
  wordsInSentence = sentence.split()
  for word in wordsInSentence:
    if word == "imperdiet":
      count += 1
  return count

def imperdietIsInSentence(count):
  return count > 0

def getImperdietCounts(file):
  sentences = file.split(".")
  numLinesWithImperdiet = 0
  numImperdietInFile = 0
  for sentence in sentences:
    numImperdietInSentence = countImperdietInSentence(sentence)
    numImperdietInFile += numImperdietInSentence
    if numImperdietInSentence > 0:
      numLinesWithImperdiet += 1
  imperdietCounts = {"numLinesWithImperdiet": numLinesWithImperdiet, "numImperdietInFile": numImperdietInFile}
  return imperdietCounts
  
def readFile():
  
  fileSource = input("What is the destination of the file you'd like to read?")
  file = open(fileSource, "r")
  fileText = file.read()
  imperdietCounts = getImperdietCounts(fileText)

  print("number of lines with imperdiet: ", imperdietCounts["numLinesWithImperdiet"])
  print("number of times imperdiet appears: ", imperdietCounts["numImperdietInFile"])
  
def getNumSentencesInFile(text):
  sentences = text.split(".")
  # must subtract one from length of sentences, since the split occurs before and after the period.  The last split will be empty text, which isn't a sentence.
  numSentences = len(sentences) - 1
  return numSentences

def writeFile():
  
  fileSource = input("What is the destination of the file you'd like to write to?")
  file = open(fileSource, "w")
  userSentences = input("Type senetences.  When your heart is content hit return to submit your sentences.")
  file.write(userSentences)
  numSentences = getNumSentencesInFile(userSentences)
  print(getImperdietCounts(userSentences))
  print(numSentences)
  
  
def readOrWritePrompt():
  
  readWriteChoice = input("Would you like to read a file or write to a file?\nType r to read, or type w to write. ")
  if readWriteChoice is 'r':
    readFile()
  elif readWriteChoice is 'w':
    writeFile()
  else: 
    print("I'm sorry, but you must select w or r to move forward with this program.  Try starting the program over.")


readOrWritePrompt()      
