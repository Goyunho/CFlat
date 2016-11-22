import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from CFlatLexer import CFlatLexer
from CFlatParser import CFlatParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = CFlatLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CFlatParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = MyVisitor()
    visitor.visit(tree)
