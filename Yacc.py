from sly import Parser
from Lex import AverageLexer


class AverageParser(Parser):
    debugfile = 'parser.out'
    tokens = AverageLexer.tokens
    def error(self, p):
        print("Error in analyse")
        return
        # if p:
        #     print("Syntax error at token", p.type)
        #     # Just discard the token and tell the parser it's okay.
        #     self.errok()
        # else:
        #     print("Syntax error at EOF")

    precedence = (
        ('nonassoc', LEQ, NEQ, GEQ, EQUAL, GREATER, LESS),
        ('left', PLUS, MINUS),
        ('left', MULTIPLY, DIVIDE),
        ('left', AND, OR),
        ('right', NOT)

    )

    @_('MYSTATEMENT MYSTATEMENTLIST')
    def MYSTATEMENTLIST(self,p):
        return("Analyse done!")

    @_('MYSTATEMENT')
    def MYSTATEMENTLIST(self,p):
        return(p[0])

    @_('MYAVERAGE SEMICOLON','MYASSIGN SEMICOLON')
    def MYSTATEMENT(self, p):
        self.at
        return (p[0])

    @_('AVERAGE EXPRLIST MYSCOPE MYFOR MYWHILE MYTO MYNOOPTIMIZE')
    def MYAVERAGE(self, p):
        return (p[0], p[1],p[2],p[3],p[4],p[5],p[6])

    @_('ALL', 'NEXT NUMBER', 'RECORD NUMBERLIST', "REST",'')
    def MYSCOPE(self, p):
        if len(p) == 1:
            return ('MYSCOPE',p[0])
        if len(p) == 2:
            return ('MYSCOPE',p[0],p[1])
        else:
            return ('NOSCOPE')

    @_('FOR EXPR', '')
    def MYFOR(self, p):
        if len(p) == 2:
            return ('MYFOR',p[0],p[1])
        if len(p) == 0:
            return ('NOFOR')

    @_('WHILE EXPR', '')
    def MYWHILE(self, p):
        if len(p) == 2:
            return ('MYWHILE',p[0],p[1])
        if len(p) == 0:
            return ('NOWHILE')

    @_('TO IDENTIFIER', 'TOARRAY IDENTIFIER', '')
    def MYTO(self, p):
        if len(p) == 2:
            return ('MYTO',p[0],p[1])
        if len(p) == 0:
            return ('NOTO')

    @_('NOOPTIMIZE', '')
    def MYNOOPTIMIZE(self, p):
        if len(p) == 0:
            return('OPTIMIZE')
        if len(p) == 1:
            return (p[0])

    @_('EXPR COMMA EXPRLIST')
    def EXPRLIST(self, p):
        return('EXPRLIST', p[0],p[2])

    @_('EXPR')
    def EXPRLIST(self, p):
        return ("EXPRLIST",p[0])

    @_('IDENTIFIER ASSIGN EXPR')
    def MYASSIGN(self, p):
        return (p[0],p[1],p[2])

    @_('NUMBER', 'IDENTIFIER','TRUE','FALSE')
    def EXPR(self, p):
        return ("EXPR",p[0])

    @_(
       'EXPR PLUS EXPR',
       'EXPR MINUS EXPR',
       'EXPR MULTIPLY EXPR',
       'EXPR DIVIDE EXPR',
       'EXPR LESS EXPR',
       'EXPR GREATER EXPR',
       'EXPR GEQ EXPR',
       'EXPR LEQ EXPR',
       'EXPR NEQ EXPR',
       'EXPR EQUAL EXPR',
       'OP EXPR CP',
       'NOT EXPR',
       'EXPR AND EXPR',
       'EXPR OR EXPR',
        )
    def EXPR(self, p):
        return ('binary-expression', p[1], p.EXPR0, p.EXPR1)

    @_('NUMBER COMMA NUMBERLIST', 'NUMBER')
    def NUMBERLIST(self, p):
        return (p[0])






