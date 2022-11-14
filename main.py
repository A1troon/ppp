#!/usr/bin/env python
from Lex import AverageLexer
import optparse

from Yacc import AverageParser

if __name__ == '__main__':
    lexer = AverageLexer()
    parser = AverageParser()
    #text = 'AVERAGE 5 - 4,6 - 1 for x+2'
    text = 'a = 2 AND 3 + 435;' \
           'AVERAGE 5 - 4,6 - 1 for x+2;' \
           'AVERAGE a, 8+1 for t > 2 while t > 2 to myarray nooptimize;' \

    lexResult = lexer.tokenize(text)
    # for tok in lexResult:
    #     print('type=%r, value=%r' % (tok.type, tok.value))
    result = parser.parse(lexResult)
    print(result)


def prod():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input", dest='inputPath', help='read data from file')
    parser.add_option("-o", "--output", dest='outputPath', help='file to write')
    (options, arguments) = parser.parse_args()
    inputPath = options.inputPath
    outputPath = options.outputPath
    lexer = AverageLexer()
    with open(inputPath, "r") as readFile:
        with open(outputPath, "w") as writeFile:
            for line in readFile.readlines():
                for tok in lexer.tokenize(line):
                    #writeFile.write((str)(tok.value) + '\n')
                    if type(tok) is str:
                        writeFile.write(tok)
                    else:
                        writeFile.write('type=%r, value=%r\n' % (tok.type, tok.value))