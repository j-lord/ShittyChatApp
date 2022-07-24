# simple NLP
import words as wd  # correct word templates
import re
import getMessage as gm

# Here we define some indexes to keep track of the format of the expressions data-structure
SECURITY = 0
SECURITY_ATTRIBUTE = 1
FEELINGS = 2
messages = []
message = (gm.update()) # updates database and returns client message
for i in message: messages.append(str(i)) # need to use str here to convert from unicode 
# print("message: {}".format(messages))


inputString = messages
# inputString = "I am just not sure about my portfolio, its up, its down. \nWho the hell knows anything anymore. Aple seems to be looking fairly ugly at the moment! Wouldn't you agree?\n"  # The question that we want to answer
# inputString = gm[0]  # The question that we want to answer
# print("This should be the first client message: ".format(inputString))


systemInput = {"question": inputString, "history": []}  # datastructure for controlling that data


def cleanText(inputString):
    # convert the input to lower case
    for i in range (len(inputString)): inputString[i] = inputString[i].lower()
    # print(inputString)
    # good here but need to check for numbers inside the list, not character by character 
    # not unless this will always be only querying one line at a time, therefor there 
    # would be no need for a list

    # remove all the characters that are not alphanumeric, or spaces
    print("len: {}".format(len(inputString)))
    cleanedInput = ""
    for word in inputString:
        for character in word:
            if(character.isalnum() or character == " "):  # Check alpha numeric or space
                cleanedInput += character
            # Then we add it to the cleaned input string, building it up character by character
        else:  # If not skip
            pass
    print("input {}".format(inputString))
    print("clean: {}",format(cleanedInput))
    return cleanedInput


def removeStopWords(inputString):
    cachedStopWords = wd.stop_words  # caching the list from the module yields a significant speedup
#   text = 'hello bye the the hi'
    text = ' '.join([word for word in inputString.split() if word not in cachedStopWords])
    return text


# Spell check in a very lazy way simply looking for an intersection for name and commonly misspelled versions
def spellCheckSecurity(word):
    cachedMisspellings = wd.apple_list 
    word = word.split()
    intersection = list(set(word) & set(cachedMisspellings)) 
    if intersection:
        for i in range(len(word)):
            # this fails if more than 1 company name mentioned in single messge - address this 
            if word[i] == str(intersection[0]):
                word[i] = "apple"
        return word
    else:
        return 

# !!!!!!! Here we could use the Levenshtein distance algorithm for check spelling
# https://en.wikipedia.org/wiki/Levenshtein_distance
# But there may be no sence in re-creating the wheel when the nltk library exists


def extractLogicalForm(inputString):
    # Next we are going to look through all the patterns that we have until we find one that matches a template
    # extractedLogicalForm = None
    # For every regex pattern that we have
    for regex, logicalForm in wd.EXPRESSIONS:
        # convert pattern from a string to something python understands
        compiledRegex = re.compile(regex) 
        # Check to see if the regular expression matches the chat question
        result = compiledRegex.match(inputString)
        if(result != None):  # If there is a match
            print("\tRegex:", regex)
            print("\tLogical Form:", logicalForm)
            return logicalForm
            # Return the logical form so we are able to use it later
    # If no match return None
    return None 


def getAttributeValue(security, attribute, feeling):
    if (security != None and attribute != None):
        if(security == "apple" and attribute == "feeling" and feeling == "good"):
            return "Send_suggestion({})".format(security)
        if(security == "apple" and attribute == "feeling" and feeling == "bad"):
            return "Sleep(30 days) then inquire_about({})".format(security)
        if(security == "apple" and attribute == "feeling" and feeling == "ugly"):
            return "Remove_from_Suggestion({})".format(security)
        else:
            return None
    else: 
        raise Exception("There was an error parsing the sentence, got: " + str(security) + ", " + str(attribute))

         
rawInputString = systemInput["question"]
print("Original Input:", rawInputString)
# rawInputString = rawInputString.encode('ascii',"ignore")
# rawInputString = rawInputString.replace("u'", "'")
# print("Original Input2:", str(rawInputString.encode('utf8')))
# print("Original Input2:", (rawInputString))



cleanedInput = cleanText(rawInputString)
print("Cleaned: {}".format(cleanedInput))

removedStop = removeStopWords(cleanedInput)
print("Type: {}".format(type(removedStop)))
print("Cleaned and stop words removed: {}".format(removedStop))
removedStop = str(removedStop)
spelled = cleanedInput

spelled = spellCheckSecurity(removedStop)
if spelled != None:
    spelled = ' '.join(spellCheckSecurity(removedStop))
else: 
    spelled = cleanedInput
    

extractedLogicalForm = extractLogicalForm(spelled)
if extractedLogicalForm == None:
        print("We didn't find a match")  # If we didn't find a match, say so
else:
    targetSecurity = extractedLogicalForm[SECURITY]
    descriptor = extractedLogicalForm[SECURITY_ATTRIBUTE]
    feeling = extractedLogicalForm[FEELINGS]
    print("\nThe outlook", "on", targetSecurity, "is {} - ".format(feeling), getAttributeValue(targetSecurity, descriptor, feeling))   

