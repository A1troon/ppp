from Lex import AverageLexer

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)/n While'
    lexer = AverageLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))