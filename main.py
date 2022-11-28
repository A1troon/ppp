#!/usr/bin/env python
from Lex import AverageLexer
import optparse

from Yacc import AverageParser


def first():
    inputPath = "inp"
    outputPath = "out"
    lexer = AverageLexer()
    parser = AverageParser()
    with open(inputPath, "r") as readFile:
        with open(outputPath, "w") as writeFile:
                for tok in lexer.tokenize(''.join(readFile.readlines())):
                    if type(tok) is str:
                        writeFile.write(tok)#catch errors for output
                    else:
                        writeFile.write('type=%r, value=%r\n' % (tok.type, tok.value))


def second():
    inputPath = "inp"
    outputPath = "outYacc"
    lexer = AverageLexer()
    parser = AverageParser()
    with open(inputPath, "r") as readFile:
        with open(outputPath, "w") as writeFile:
            lexResult = lexer.tokenize(''.join(readFile.readlines()))
            result = parser.parse(lexResult)
            writeFile.write(result)
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

if __name__ == '__main__':
    #first()
    second()
    # lexer = AverageLexer()
    # parser = AverageParser()
    # # text = 'AVERAGE 5 - 4,6 - 1 for x+2'
    # text = 'average qwerty,b,a Record 2, 4 for item <=4 toarray my_array;'
    # lexResult = lexer.tokenize(text)
    # for tok in lexResult:
    #     print('type=%r, value=%r' % (tok.type, tok.value))
    #result = parser.parse(lexResult)
    #print(result)