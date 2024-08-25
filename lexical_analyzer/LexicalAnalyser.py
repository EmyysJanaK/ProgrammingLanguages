import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class TokenType:
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    INTEGER = "INTEGER"
    OPERATOR = "OPERATOR"
    STRING = "STRING"
    PUNCTUATION = "PUNCTUATION"

class LexicalAnalyser:
    def __init__(self, inputFileName):
        self.inputFileName = inputFileName
        self.tokens = []

    def scan(self):
        try:
            with open(self.inputFileName, 'r') as file:
                lines = file.readlines()
                lineCount = 0
                for line in lines:
                    lineCount += 1
                    try:
                        self.tokenizeLine(line)
                    except Exception as e:
                        raise CustomException(str(e) + " in LINE: " + str(lineCount) + "\nERROR in lexical_analysis.")
        except IOError as e:
            print("Error reading file:", e)

        return self.tokens

    def tokenizeLine(self, line):
        digit = r"\d"
        letter = r"[a-zA-Z]"
        operatorSymbol = r"[+\-*/<>&.@/:=~|$!#%^_\[\]{}\"`\?]"
        escape = r"(\\\\'|\\\\t|\\\\n|\\\\\\\\)"
        
        identifierPattern = re.compile(letter + r"(" + letter + r"|" + digit + r"|" + r"_)*")
        integerPattern = re.compile(digit + r"+")
        operatorPattern = re.compile(operatorSymbol + r"+")
        
        punctuationPattern = re.compile(r"[(),;]")
        spacesPattern = re.compile(r"(\s|\t)+")
        
        stringPattern = re.compile(r"'(" + letter + r"|" + digit + r"|" + operatorSymbol + r"|" + escape + r"|" + punctuationPattern.pattern + r"|" + spacesPattern.pattern + r")*'")
        commentPattern = re.compile(r"//.*")
        
        currentIndex = 0
        while currentIndex < len(line):
            currentChar = line[currentIndex]

            spaceMatcher = spacesPattern.match(line[currentIndex:])
            commentMatcher = commentPattern.match(line[currentIndex:])
            if commentMatcher:
                currentIndex += len(commentMatcher.group())
                continue
            if spaceMatcher:
                currentIndex += len(spaceMatcher.group())
                continue

            matcher = identifierPattern.match(line[currentIndex:])
            if matcher:
                identifier = matcher.group()
                keywords = [
                    "let", "in", "fn", "where", "aug", "or", "not", "gr", "ge", "ls",
                    "le", "eq", "ne", "true", "false", "nil", "dummy", "within", "and", "rec"
                ]
                if identifier in keywords:
                    self.tokens.append(Token(TokenType.KEYWORD, identifier))
                else:
                    self.tokens.append(Token(TokenType.IDENTIFIER, identifier))
                currentIndex += len(identifier)
                continue

            # Match integers
            matcher = integerPattern.match(line[currentIndex:])
            if matcher:
                integer = matcher.group()
                self.tokens.append(Token(TokenType.INTEGER, integer))
                currentIndex += len(integer)
                continue
            
            # Match operators
            matcher = operatorPattern.match(line[currentIndex:])
            if matcher:
                operator = matcher.group()
                self.tokens.append(Token(TokenType.OPERATOR, operator))
                currentIndex += len(operator)
                continue

            matcher = stringPattern.match(line[currentIndex:])
            if matcher:
                string = matcher.group()
                self.tokens.append(Token(TokenType.STRING, string))
                currentIndex += len(string)
                continue

            matcher = punctuationPattern.match(currentChar)
            if matcher:
                self.tokens.append(Token(TokenType.PUNCTUATION, currentChar))
                currentIndex += 1
                continue
            
            raise Exception("Unable to tokenize the CHARACTER: " + currentChar + " at INDEX: " + str(currentIndex))

class CustomException(Exception):
    pass

# Example
if __name__ == "__main__":
    lexer = LexicalAnalyser('C:\\Users\\janak\\Desktop\\GitHub\\New folder\\ProgrammingLanguages\\lexical_analyzer\\t1.txt')
    tokens = lexer.scan()
    for token in tokens:
        print(token.token_type, token.value)
