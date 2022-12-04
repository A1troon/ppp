from sly import Parser
from Lex import AverageLexer


class AverageParser(Parser):
    debugfile = 'parser.out'
    tokens = AverageLexer.tokens

    def __init__(self):
        self.statementCounter = 1
        self.assignDict = dict()
        self.Arithmetics = list()

    def error(self, p):
        if p:
            #print("Syntax error at statement", self.statementCounter, "at token", p.type)
            self.errok()


    precedence = (
        ('right', NOT),
        ('left', AND, OR),
        ('nonassoc', LEQ, NEQ, GEQ, EQUAL, GREATER, LESS),
        ('left', PLUS, MINUS),
        ('left', MULTIPLY, DIVIDE),


    )

    @_('MYSTATEMENT MYSTATEMENTLIST')
    def MYSTATEMENTLIST(self,p):
        return str(p[0])+"\n"+str(p[1])

    @_('MYSTATEMENT')
    def MYSTATEMENTLIST(self,p):
        return p[0]

    @_('MYAVERAGE SEMICOLON','MYASSIGN SEMICOLON')
    def MYSTATEMENT(self, p):
        self.statementCounter += 1
        return (str(self.statementCounter-1) + " statement is right")


    @_('error SEMICOLON')
    def MYSTATEMENT(self, p):
        self.statementCounter += 1
        return (str(self.statementCounter - 1) + " statement has grammar error")

    @_('AVERAGE EXPRLIST MYSCOPE MYFOR MYWHILE MYTO MYNOOPTIMIZE')
    def MYAVERAGE(self, p):
        pass

    @_('ALL', 'NEXT NUMBER', 'RECORD NUMBERLIST', "REST",'')
    def MYSCOPE(self, p):
        pass

    @_('FOR CONDITIONEXPR', '')
    def MYFOR(self, p):
        pass

    @_('WHILE CONDITIONEXPR', '')
    def MYWHILE(self, p):
        pass

    @_('TOARRAY IDENTIFIER', 'TO IDENTIFIER', '')
    def MYTO(self, p):
        pass

    @_('NOOPTIMIZE', '')
    def MYNOOPTIMIZE(self, p):
        pass

    @_('EXPR COMMA EXPRLIST')
    def EXPRLIST(self, p):
        pass

    @_('EXPR')
    def EXPRLIST(self, p):
        pass

    @_('IDENTIFIER ASSIGN EXPR')
    def MYASSIGN(self, p):
        self.Arithmetics.append(f"[{self.statementCounter} statement] {p[0]} = {p[2]}")
        self.assignDict[p[0]] = p[2]

    @_('NUMBER')
    def EXPR(self, p):
        return p[0]

    @_('IDENTIFIER')
    def EXPR(self, p):
        if p[0] in self.assignDict.keys():
            return self.assignDict[p[0]]

    @_(
       'EXPR PLUS EXPR',
       'EXPR MINUS EXPR',
       'EXPR MULTIPLY EXPR',
       'EXPR DIVIDE EXPR',
       'OP EXPR CP',
        )
    def EXPR(self, p):
        try:
            if p[1] == '+':
                value = p[0] + p[2]
            elif p[1] == '-':
                value = p[0] - p[2]
            elif p[1] == '*':
                value = p[0] * p[2]
            elif p[1] == '/':
                if p[2] != 0:
                    value = p[0] / p[2]
                else:
                    self.Arithmetics.append(f"[{self.statementCounter} statement] Zero division error: {p[0]} {p[1]} {p[2]}")
                    return None
            else:
                return p[1]
            self.Arithmetics.append(f"[{self.statementCounter} statement] {p[0]} {p[1]} {p[2]} = {value}")
            return value
        except:
            self.Arithmetics.append(f"[{self.statementCounter} statement] operation with NONE value: {p[0]} {p[1]} {p[2]}")

    @_('TRUE','FALSE')
    def CONDITIONEXPR(self,p):
        pass

    @_('NOT CONDITIONEXPR')
    def CONDITIONEXPR(self,p):
        pass

    @_(
        'EXPR LESS EXPR',
        'EXPR GREATER EXPR',
        'EXPR GEQ EXPR',
        'EXPR LEQ EXPR',
        'EXPR NEQ EXPR',
        'EXPR EQUAL EXPR',
    )
    def CONDITIONEXPR(self, p):
        pass

    @_(
        'CONDITIONEXPR AND CONDITIONEXPR',
        'CONDITIONEXPR OR CONDITIONEXPR',
        'OP CONDITIONEXPR CP'
    )
    def CONDITIONEXPR(self, p):
        pass

    @_('NUMBER COMMA NUMBERLIST', 'NUMBER')
    def NUMBERLIST(self, p):
        pass






