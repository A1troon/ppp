
from sly import Lexer


class AverageLexer(Lexer):
    tokens = {AVERAGE, ALL, NEXT, RECORD, REST, FOR, WHILE,
              TO, TO_ARRAY, NOOPTIMIZE, COMMA, PLUS, MINUS, MULTIPLY,
              DIVIDE, OP, CP, LEQ, GEQ, NEQ, EQUAL, LESS, TRUE, FALSE,
              GREATER, ASSIGN, AND, OR, NOT, IDENTIFIER, NUMBER, SEMICOLON}

    ignore = ' \t'

    AVERAGE = r'[aA][vV][eE][rR][aA][gG][eE]'
    TRUE = r'[tT][rR][uU][eE]'
    FALSE = r'[fF][aA][lL][sS][eE]'
    ALL = r'[aA][lL][lL]'
    NEXT = r'[nN][eE][xX][tT]'
    RECORD = r'[rR][eE][cC][oO][rR][dD]'
    REST = r'[rR][eE][sS][tT]'
    FOR = r'[fF][oO][rR]'
    WHILE = r'[wW][hH][iI][lL][eE]'
    TO = r'[tT][oO]'
    TO_ARRAY = r'[tT][oO] [aA][rR][rR][aA][yY]'
    NOOPTIMIZE = r'[nN][oO][oO][pP][tT][iI][mM][iI][zZ][eE]'
    COMMA = r','
    PLUS = r'\+'
    MINUS = r'-'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    OP = r'\('
    CP = r'\)'
    LEQ = r'<='
    GEQ = r'>='
    NEQ = r'<>|!='
    EQUAL = r'=='
    LESS = r'<'
    GREATER = r'>'
    ASSIGN = r'='
    AND = r'[aA][nN][dD]'
    OR = r'[oO][rR]'
    NOT = r'[nN][oO][tT]'
    IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9_]*'
    NUMBER = r'0|([1-9][0-9]*)'
    SEMICOLON = r';'

    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        val = 'Line %d: Bad character %r' % (self.lineno, t.value[0])
        self.index += 1
        return val