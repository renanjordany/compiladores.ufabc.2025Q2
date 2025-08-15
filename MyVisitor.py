from generated.ZetaVisitor import ZetaVisitor
from generated.ZetaParser import ZetaParser

class MyZetaVisitor(ZetaVisitor):
    def __init__(self):
        self.vars = {}  # dicionário de variáveis

    # programa
    def visitProg(self, ctx: ZetaParser.ProgContext):
        print("Bem-vindo ao programa de teste!")
        return self.visitChildren(ctx)

    # declarações
    def visitDecl(self, ctx: ZetaParser.DeclContext):
        for var in ctx.ID():
            name = var.getText()
            if name in self.vars:
                print(f"Variável {name} já declarada!")
            else:
                self.vars[name] = 0.0  # inicializa com 0
        return None

    # bloco de comandos
    def visitBloco(self, ctx: ZetaParser.BlocoContext):
        for c in ctx.cmd():
            self.visit(c)
        return None

    # leitura
    def visitCmdLeitura(self, ctx: ZetaParser.CmdLeituraContext):
        var_name = ctx.ID().getText()
        if var_name not in self.vars:
            raise Exception(f"Variável {var_name} não declarada!")
        try:
            val = float(input(f"Digite {var_name}: "))
        except ValueError:
            val = 0.0
        self.vars[var_name] = val
        return val

    # escrita
    def visitCmdEscrita(self, ctx: ZetaParser.CmdEscritaContext):
        if ctx.TEXTO():
            print(ctx.TEXTO().getText().strip('"'))
        elif ctx.expr():
            value = self.visit(ctx.expr())
            print(value)
        return None

    # atribuição
    def visitCmdExpr(self, ctx: ZetaParser.CmdExprContext):
        var_name = ctx.ID().getText()
        if var_name not in self.vars:
            raise Exception(f"Variável {var_name} não declarada!")
        value = self.visit(ctx.exprRel())
        self.vars[var_name] = value
        return value

    # if/else
    def visitCmdIf(self, ctx: ZetaParser.CmdIfContext):
        cond = self.visit(ctx.exprRel())
        if cond:
            self.visit(ctx.bloco(0))
        elif ctx.SENAO():
            self.visit(ctx.bloco(1))
        return None

    # enquanto
    def visitCmdEnquanto(self, ctx: ZetaParser.CmdEnquantoContext):
        while self.visit(ctx.exprRel()):
            self.visit(ctx.bloco())
        return None

    # faça-enquanto
    def visitCmdFacaEnquanto(self, ctx: ZetaParser.CmdFacaEnquantoContext):
        while True:
            self.visit(ctx.bloco())
            if not self.visit(ctx.exprRel()):
                break
        return None

    # expressões relacionais
    def visitExprRel(self, ctx: ZetaParser.ExprRelContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '<': return left < right
            elif op == '>': return left > right
            elif op == '<=': return left <= right
            elif op == '>=': return left >= right
            elif op == '==': return left == right
            elif op == '!=': return left != right
        else:
            return self.visit(ctx.expr(0))

    # expressões aritméticas
    def visitExpr(self, ctx: ZetaParser.ExprContext):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.term(i))
            if op == '+': result += val
            elif op == '-': result -= val
        return result

    def visitTerm(self, ctx: ZetaParser.TermContext):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i-1).getText()
            val = self.visit(ctx.factor(i))
            if op == '*': result *= val
            elif op == '/': result /= val
        return result

    def visitFactor(self, ctx: ZetaParser.FactorContext):
        if ctx.NUM():
            return float(ctx.NUM().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            if name not in self.vars:
                raise Exception(f"Variável {name} não declarada!")
            return self.vars[name]
        elif ctx.expr():
            return self.visit(ctx.expr())

