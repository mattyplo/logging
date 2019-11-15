import logging

# Initialize logger
logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
DEBUG_LEVELV_NUM = 5
logging.addLevelName(DEBUG_LEVELV_NUM, "TRACE")
def trace(self, message, *args, **kws):
    if self.isEnabledFor(DEBUG_LEVELV_NUM):
        # Yes, logger takes its '*args' as 'args'.
        self._log(DEBUG_LEVELV_NUM, message, args, **kws) 
logging.Logger.trace = trace
logging.basicConfig(format=logFormatter, level=5, filename="consoleapp.log")
logger = logging.getLogger(__name__)


# Handler
#handler = logging.FileHandler('logs/myLogs.log')
#handler.setLevel(logging.DEBUG)
#logger.addHandler(handler)

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
  
def outputImperdietCounts(imperdietCounts):
  print("number of lines with imperdiet: ", imperdietCounts["numLinesWithImperdiet"])
  print("number of times imperdiet appears: ", imperdietCounts["numImperdietInFile"])  
  
def readFile():
  # Logger
  logger.debug('readFile Function', extra={'input': ''})
  
  # Function code
  fileSource = input("What is the destination of the file you'd like to read?")
  
  try:
    file = open(fileSource, "r")
    fileText = file.read()
    imperdietCounts = getImperdietCounts(fileText)
    outputImperdietCounts(imperdietCounts)
  
  except IOError as e:
    logging.critical('file does not exist.  System output: ' + str(e))
  
  #Logger
  logger.debug('readFile Function', extra={'output': ''})
  
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
  imperdietCounts = getImperdietCounts(userSentences)
  outputImperdietCounts(imperdietCounts)
  print("The number of sentences your wrote is: ", numSentences)
  
  
def readOrWritePrompt():
  
  readWriteChoice = input("Would you like to read a file or write to a file?\nType r to read, or type w to write. ")
  logger.debug('readWriteChoice user Input = ' + readWriteChoice, extra={'userInput': readWriteChoice})
  if readWriteChoice is 'r':
    readFile()
  elif readWriteChoice is 'w':
    writeFile()
  else: 
    logger.error('readWriteChoice is not an r or w')
    print("I'm sorry, but you must select w or r to move forward with this program.  Try starting the program over.")

logger.trace('trace')
logger.info('program started')
readOrWritePrompt()      
logger.info('program finished')
