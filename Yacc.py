from sly import Parser
from Lex import AverageLexer


class AverageParser(Parser):
    debugfile = 'parser.out'
    tokens = AverageLexer.tokens
    def __init__(self):
        self.statementCounter = 1

    def error(self, p):
        # print("Error in analyse")
        # return
        if p:
            print("Syntax error at statement", self.statementCounter, "at token", p.type)
            # Just discard the token and tell the parser it's okay.
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
        self.statementCounter += 1;
        return (str(self.statementCounter-1) + " statement is right")

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
        pass

    @_('NUMBER', 'IDENTIFIER')
    def EXPR(self, p):
        pass

    @_(
       'EXPR PLUS EXPR',
       'EXPR MINUS EXPR',
       'EXPR MULTIPLY EXPR',
       'EXPR DIVIDE EXPR',
       'OP EXPR CP',
        )
    def EXPR(self, p):
        pass

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






