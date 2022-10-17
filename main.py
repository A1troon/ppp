#!/usr/bin/env python
from Lex import AverageLexer
import optparse

if __name__ == '__main__':
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