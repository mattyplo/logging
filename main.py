def countImperdietInSentence(sentence):
  count = 0
  wordsInSentence = sentence.split()
  for word in wordsInSentence:
    if word == "imperdiet":
      count += 1
  return count

fileSource = input("What is the destination of the file you'd like to read?")
file = open(fileSource, "r")
fileText = file.read()
sentences = fileText.split(".")
for sentence in sentences:
  print(countImperdietInSentence(sentence))
  
      
