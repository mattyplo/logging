import logging
import time
import datetime

############### READ WRITE PROGRAM ########################

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
  logger.debug("enter getImperdietCounts() - file contents")
  sentences = file.split(".")
  logger.trace("sentences variable assigned by splitting file contents by .")
  numLinesWithImperdiet = 0
  logger.trace("numLinesWithImperdiet variable assigned: " + str(numLinesWithImperdiet))
  numImperdietInFile = 0
  logger.trace("numImperdietInFile variable assigned: " + str(numImperdietInFile))
  logger.trace("enter for loop: each sentence in sentences")
  for sentence in sentences:
    logger.trace("call numImperdietInSentence()")
    numImperdietInSentence = countImperdietInSentence(sentence)
    logger.trace("numImperdietInSentence variable assigned: " + str(numImperdietInSentence))
    numImperdietInFile += numImperdietInSentence
    logger.trace("numImperdietInFile varaible assigned: " + str(numImperdietInFile))
    if numImperdietInSentence > 0:
      logger.trace("Entered if numperdietInSentence > 0 statement")
      numLinesWithImperdiet += 1
      logger.trace("numLinesWithImperdiet variable assigned: " + str(numLinesWithImperdiet))
  logger.trace("exit for loop")
  imperdietCounts = {"numLinesWithImperdiet": numLinesWithImperdiet, "numImperdietInFile": numImperdietInFile}
  logger.trace("imperdietCounts variable assigned: " + str(imperdietCounts))
  logger.debug("exit getImperdietCounts() - return: " + str(imperdietCounts))
  return imperdietCounts
  
def outputImperdietCounts(imperdietCounts):
  print("number of lines with imperdiet: ", imperdietCounts["numLinesWithImperdiet"])
  print("number of times imperdiet appears: ", imperdietCounts["numImperdietInFile"])  
  
def readFile():
  logger.debug("enter readFile() - No Args")
  
  # Function code
  fileSource = input("What is the destination of the file you'd like to read?")
  logger.trace("fileSource variable assigned: " + fileSource)
  
  try:
    logger.trace("enter try block")
    file = open(fileSource, "r")
    logger.trace("file variable assigned to open: " + file.name)
    fileText = file.read()
    logger.trace("fileText variable assigned contents of: " + file.name)
    logger.trace("call imperdietCounts()")
    imperdietCounts = getImperdietCounts(fileText)
    logger.trace("imperdietCounts Variable assigned: " + str(imperdietCounts))
    logger.trace("call outputImperdietCounts()")
    outputImperdietCounts(imperdietCounts)
    logger.trace("exit try block")
  
  except IOError as e:
    logger.critical('file does not exist.  System output: ' + str(e))
  
  logger.debug('exit readFile() - No Return')
  
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
  logger.debug("Enter readOrWritePrompt() - No Args")
  readWriteChoice = input("Would you like to read a file or write to a file?\nType r to read, or type w to write. ")
  logger.trace("readWriteChoice variable assigned: " + readWriteChoice)
  if readWriteChoice is 'r':
    logger.info("program mode = read")
    logger.trace("call readFile()")
    readFile()
  elif readWriteChoice is 'w':
    logger.info("program mode = write")
    logger.trace("call writeFile()")
    writeFile()
  else: 
    logger.error('readWriteChoice is not an r or w')
    print("I'm sorry, but you must select w or r to move forward with this program.  Try starting the program over.")


logger.info('program started')
#startTime = time.time()
logger.trace('call readOrWritePrompt()')
readOrWritePrompt()      
logger.info('program finished')
#endTime = time.time()
#executionTime = endTime - startTime
#print("--- %s seconds ---" % executionTime)

############## PERFORMANCE METRICS #############################

def getMostRecentLogRun():
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logsList = logText.split('program finished')
  mostRecentLog = logsList[-2]
  mostRecentLogList = mostRecentLog.split('\n')
  del mostRecentLogList[0]
  return mostRecentLogList

def timestamp_to_milliseconds(timestamp):
    hours, minutes, seconds, milliseconds = [int(x) for x in timestamp.replace(',', ':').split(':')]
    return milliseconds + 1000 * (seconds + 60 * (minutes + 60 * hours))

def convertLogTime(logTime):
  logDateTime = logTime.split("- INFO -")[0]
  logDateTime = logDateTime[:-1]
  logTimeDateList = logDateTime.split(" ")
  time = logTimeDateList[1]
  logTimeMilliseconds = timestamp_to_milliseconds(time)
  return logTimeMilliseconds
  
def calculateExecutionTime(currentLogList):
  startEntry = currentLogList[0]
  finishEntry = currentLogList[-1]
  startMilli = convertLogTime(startEntry)
  finishMilli = convertLogTime(finishEntry)
  runTime = finishMilli - startMilli
  return runTime

def generateMetrics():
  # determine runtime
  currentLogList = getMostRecentLogRun()
  runTime = calculateExecutionTime(currentLogList)

  print(runTime)
  
generateMetrics()
