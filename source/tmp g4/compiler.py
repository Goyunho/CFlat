__author__ = 'Yoonho GO'

import sys
from antlr4 import *
from cflatLexer import cflatLexer
from cflatParser import cflatParser
from cflatVisitor import cflatVisitor

class MyVisitor(cflatVisitor):
    self.memory={}

def main(argv):
    input = FileStream(argv[1])
    lexer = cflatLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cflatParser(stream)
    tree = parser.run()

    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)

