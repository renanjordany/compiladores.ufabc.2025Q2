from generated.ZetaParser import ZetaParser
from generated.ZetaVisitor import ZetaVisitor

class MyZetaVisitor(ZetaVisitor):
    def __init__(self):
        self.vars = {}

    def visitProg(self, ctx: ZetaParser.ProgContext):
        print("Bem-vindo ao programa de teste!")
        return self.visitChildren(ctx)

    def visitDeclara(self, ctx: ZetaParser.DeclaraContext):
        for id_ctx in ctx.ID():
            self.vars[id_ctx.getText()] = 0.0
        return None

    def visitCmdLeitura(self, ctx: ZetaParser.CmdLeituraContext):
        var_name = ctx.ID().getText()
        valor = float(input(f"Digite {var_name}: "))
        self.vars[var_name] = valor
        return None

    def visitCmdEscrita(self, ctx: ZetaParser.CmdEscritaContext):
        if ctx.ID():
            var_name = ctx.ID().getText()
            print(f"{var_name} =", self.vars[var_name])
        else:
            texto = ctx.TEXTO().getText()
            print(texto.strip('"'))
        return None

    def visitCmdExpr(self, ctx: ZetaParser.CmdExprContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[var_name] = value
        return value

    def visitCmdIf(self, ctx: ZetaParser.CmdIfContext):
        cond = self.visit(ctx.cond())
        if cond:
            for cmd in ctx.bloco(0).cmd():
                self.visit(cmd)
        elif ctx.bloco(1):
            for cmd in ctx.bloco(1).cmd():
                self.visit(cmd)
        return None

    def visitCmdEnquanto(self, ctx: ZetaParser.CmdEnquantoContext):
        while self.visit(ctx.cond()):
            for cmd in ctx.bloco().cmd():
                self.visit(cmd)
        return None

    def visitCond(self, ctx: ZetaParser.CondContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op_rel().getText()
        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right
        if op == '==': return left == right
        if op == '!=': return left != right
        return False

    def visitExpr(self, ctx: ZetaParser.ExprContext):
        result = self.visit(ctx.termo(0))
        for i, op in enumerate(ctx.getChildren()):
            if i % 2 == 1:  # operador
                operator = op.getText()
                right = self.visit(ctx.termo((i+1)//2))
                if operator == '+': result += right
                elif operator == '-': result -= right
        return result

    def visitTermo(self, ctx: ZetaParser.TermoContext):
        result = self.visit(ctx.fator(0))
        for i, op in enumerate(ctx.getChildren()):
            if i % 2 == 1:
                operator = op.getText()
                right = self.visit(ctx.fator((i+1)//2))
                if operator == '*': result *= right
                elif operator == '/': result /= right
        return result

    def visitFator(self, ctx: ZetaParser.FatorContext):
        if ctx.NUM(): return float(ctx.NUM().getText())
        if ctx.ID(): return self.vars.get(ctx.ID().getText(), 0.0)
        if ctx.expr(): return self.visit(ctx.expr())
        return 0.0

