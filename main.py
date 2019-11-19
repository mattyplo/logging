import logging
import time
import datetime


############### INITIALIZE LOGGER ########################
logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
DEBUG_LEVELV_NUM = 5
logging.addLevelName(DEBUG_LEVELV_NUM, "TRACE")
def trace(self, message, *args, **kws):
    if self.isEnabledFor(DEBUG_LEVELV_NUM):
        # Yes, logger takes its '*args' as 'args'.
        self._log(DEBUG_LEVELV_NUM, message, args, **kws) 
logging.Logger.trace = trace
logging.basicConfig(format=logFormatter, level=5, filename="consoleapp.log", filemode="w")
logger = logging.getLogger(__name__)


############### READ WRITE PROGRAM ########################

def countImperdietInSentence(sentence):
  logger.debug("enter countImperdietInSentence() - Args: " + sentence)
  count = 0
  logger.trace("count variable assigned: " + str(count))
  wordsInSentence = sentence.split()
  logger.trace("wordsInSentence variable assigned: " + str(wordsInSentence))
  logger.trace("enter for loop: each word in wordsInSentence")
  for word in wordsInSentence:
    if word == "imperdiet":
      logger.trace("Entered if word == 'imperdiet' statement")
      count += 1
      logger.trace("count variable assigned: " + str(count))
  logger.debug("exit countImperdietInSentence() - return: " + str(count))
  return count

def getImperdietCounts(file):
  logger.debug("enter getImperdietCounts() - Args: file contents")
  sentences = file.split(".")
  logger.trace("sentences variable assigned by splitting file contents by .")
  numLinesWithImperdiet = 0
  logger.trace("numLinesWithImperdiet variable assigned: " + str(numLinesWithImperdiet))
  numImperdietInFile = 0
  logger.trace("numImperdietInFile variable assigned: " + str(numImperdietInFile))
  logger.trace("enter for loop: each sentence in sentences")
  for sentence in sentences:
    logger.trace("call countImperdietInSentence()")
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
  logger.debug("enter outputImperdietCounts() - Args: " + str(imperdietCounts))
  logger.trace("print statement: 'number of lines with imperdiet: ', imperdietCounts['numLinesWithImperdiet']")
  print("number of lines with imperdiet: ", imperdietCounts["numLinesWithImperdiet"])
  logger.trace("print statement: 'number of times imperdiet appears: ', imperdietCounts['numImperdietInFile']")
  print("number of times imperdiet appears: ", imperdietCounts["numImperdietInFile"])  
  logger.debug("exit outputImperdietCounts() - No Return")
  
def readFile():
  logger.debug("enter readFile() - No Args")
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
    logger.info("Presenting results.")
    logger.trace("call outputImperdietCounts()")
    outputImperdietCounts(imperdietCounts)
    logger.trace("exit try block")
  
  except IOError as e:
    logger.critical('file does not exist.  System output: ' + str(e))
  
  logger.debug('exit readFile() - No Return')
  
def getNumSentencesInFile(text):
  logger.debug("enter getNumSentencesInFile() - Args: " + text)
  sentences = text.split(".")
  logger.trace("sentences variable assigned by splitting text variable contents by .")
  # must subtract one from length of sentences, since the split occurs before and after the period.  The last split will be empty text, which isn't a sentence.
  numSentences = len(sentences) - 1
  logger.trace("numSentences variable assigned: " + str(numSentences))
  logger.debug("exit getNumSentencesInFile - Return: " + str(numSentences))
  return numSentences

def writeFile():
  logger.debug("enter writeFile() - No Args")
  fileSource = input("What is the destination of the file you'd like to write to?")
  logger.trace("fileSource variable assigned: " + fileSource)
  
  try:
    logger.trace("enter try block")
    file = open(fileSource, "w")
    logger.trace("file variable assigned to open: " + file.name)
    userSentences = input("Type senetences.  When your heart is content hit return to submit your sentences.")
    logger.trace("userSentences variable assigned: " + userSentences)
    file.write(userSentences)
    logger.trace("write userSentences variable to file")
    logger.trace("call getNumSentencesInFile()")
    numSentences = getNumSentencesInFile(userSentences)
    logger.trace("numSentences variable assigned" + str(numSentences))
    logger.trace("call getImperdietCounts()")
    imperdietCounts = getImperdietCounts(userSentences)
    logger.trace("imperdietCounts Variable assigned: " + str(imperdietCounts))
    logger.info("Presenting results.")
    logger.trace("call outputImperdietCounts()")
    outputImperdietCounts(imperdietCounts)
    logger.trace("print statement: 'The number of sentences you wrote is: ', numSentences")
    print("The number of sentences you wrote is: ", numSentences)
  
  except IOError as e:
    logger.critical('cannot assign empty string as file destination: ' + str(e))
  
  logger.debug("exit writeFile() - No Args")
  
def readOrWritePrompt():
  logger.debug("enter readOrWritePrompt() - No Args")
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
    
  logger.debug("exit readOrWritePrompt() - No Return")
    
    
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

def convertLogTime(logTime, logLevel):
  logDateTime = logTime.split(logLevel)[0]
  logDateTime = logDateTime[:-1]
  logTimeDateList = logDateTime.split(" ")
  time = logTimeDateList[1]
  logTimeMilliseconds = timestamp_to_milliseconds(time)
  return logTimeMilliseconds
  
def calculateExecutionTime(currentLogList):
  startEntry = currentLogList[0]
  finishEntry = currentLogList[-1]
  startMilli = convertLogTime(startEntry, '- INFO -')
  finishMilli = convertLogTime(finishEntry, '- INFO -')
  runTime = finishMilli - startMilli
  return runTime

def calcTimeToReadAllLines():
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logTextList = logText.split('call countImperdietInSentence()')
  # remove first entry from list, it is the precursor to the inside of the first method call.
  logTextList.pop(0)
  
  # Calculate time of first line read
  startTime = convertLogTime(logTextList[0], '- DEBUG -')
  # Calculate time of last line read finished.
  exitTime = 0
  lastEntryByLine = logTextList[-1].split('\n')
  for line in lastEntryByLine:
    lineContainsExit = line.find("exit countImperdietInSentence()")
    if lineContainsExit > 0:
      exitTime = convertLogTime(line, '- DEBUG ')
  
  # Calculate time between first line read and last line read finished
  timeToReadAllLines = exitTime - startTime
  return timeToReadAllLines

def calculateAverageLineReadTime():
  #countImperdietEntries = currentLogList.split("enter countImperdietInSentence")
  #print(str(currentLogList))
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logTextList = logText.split('call countImperdietInSentence()')
  # remove first entry from list, it is the precursor to the inside of the first method call.
  logTextList.pop(0)
  
  # Calculate time between first line read and last line read finished
  timeToReadAllLines = calcTimeToReadAllLines()
  
  # Divided time between by number of lines for average time to read a line
  numberOfLines = len(logTextList)
  # in milliseconds
  avgTimeToReadLine = timeToReadAllLines / numberOfLines
  return avgTimeToReadLine
  
  
def calcNumImperdietInFile():
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logTextList = logText.split('call outputImperdietCounts()') 
  logTextList.pop(0)
  numImperdietInFile = logTextList[0].split("'numImperdietInFile':")
  numImperdietInFile.pop(0)
  numImperdiet = numImperdietInFile[0].split('}')
  numImperdiet = numImperdiet[0].strip()
  return int(numImperdiet)
  
def calcAvgTime2FindImperdiet():
  timeToReadAllLines = calcTimeToReadAllLines()
  numImperdietInFile = calcNumImperdietInFile()
  avgTimeToFindImperdiet = timeToReadAllLines / numImperdietInFile
  return avgTimeToFindImperdiet
  
def getReadWriteMode():
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logTextList = logText.split('readWriteChoice variable assigned:') 
  logTextList.pop(0)
  readWriteMode = logTextList[0].split('\n')[0]
  readWriteMode = readWriteMode.strip()
  return readWriteMode
  
def calcAvgLineWriteTime():
  logFile = open('consoleapp.log', "r")
  logText = logFile.read()
  logTextList = logText.split('TRACE - file variable assigned to open:')
  writeStartTime = logTextList[0].split('\n')[-1]
  logTextList = logText.split('TRACE - write userSentences variable to file')
  writeFinishTime = logTextList[0].split('\n')[-1]
  print(writeStartTime)
  print(writeFinishTime)
  
def generateMetrics():
  # determine runtime
  # time is in milliseconds
  currentLogList = getMostRecentLogRun()
  readWriteMode = getReadWriteMode()
  runTime = calculateExecutionTime(currentLogList)
  if readWriteMode is 'r':
    avgTimeToReadLine = calculateAverageLineReadTime()
    avgTimeToFindImperdiet = calcAvgTime2FindImperdiet()
    print("Time to execute program: " + str(runTime) + " milliseconds")
    print("Average time to read a line: " + str(avgTimeToReadLine) + " milliseconds") 
    print("Average time to find Imperdiet in a line: " + str(avgTimeToFindImperdiet) + " milliseconds")
    
  elif readWriteMode is 'w':
    calcAvgLineWriteTime()
    print(readWriteMode)
    
  runTime = calculateExecutionTime(currentLogList)
  
  
generateMetrics()
