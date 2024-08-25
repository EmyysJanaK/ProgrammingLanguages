from enum import Enum

class TokenType(Enum):
    KEYWORD = 1
    IDENTIFIER = 2
    INTEGER = 3
    OPERATOR = 4
    STRING = 5
    PUNCTUATION = 6
    DELETE = 7
    EndOfTokens = 8