from antlr4 import *
from generated.ZetaLexer import ZetaLexer
from generated.ZetaParser import ZetaParser
from MyVisitor import MyZetaVisitor

def main():
    input_stream = FileStream("programa.zeta", encoding='utf-8')
    lexer = ZetaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ZetaParser(stream)
    tree = parser.prog()
    visitor = MyZetaVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

