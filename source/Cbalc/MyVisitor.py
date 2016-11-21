__author__ = 'jszheng'

from CbalcVisitor import CbalcVisitor
from CbalcParser import CbalcParser

def number(num): # 정수면 정수반환 실수면 실수반환
    try:
        return int(num)
    except:
        return float(num)

class MyVisitor(CbalcVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitShowme(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitNumber(self, ctx):
        return ctx.NUMBER().getText()
    
    def visitString(self, ctx):
        return ctx.STRING().getText()[1:-1]

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitSingleOper(self, ctx):
        expr = number(self.visit(ctx.expr()))
        if ctx.op.type == CbalcParser.NOT:
            return not expr
        elif ctx.op.type == CbalcParser.SUB:
            return -expr

    def visitMulDiv(self, ctx):
        try :
            left = number(self.visit(ctx.expr(0)))
        except :
            left = self.visit(ctx.expr(0))
        try :
            right = number(self.visit(ctx.expr(1)))
        except : 
            right = self.visit(ctx.expr(1))
        if ctx.op.type == CbalcParser.MUL:
            return left * right
        elif ctx.op.type == CbalcParser.AMP:
            return left % right
        return left / right

    def visitAddSub(self, ctx):
        try :
            left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        except :
            left, right = self.visit(ctx.expr(0)), self.visit(ctx.expr(1)) 
        if ctx.op.type == CbalcParser.ADD:
            return left + right
        return left - right

    def visitShiftOper(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        if ctx.op.type == CbalcParser.SHL:
            return left<<right
        elif ctx.op.type == CbalcParser.SHR:
            return left>>right

    def visitCompOper(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        if ctx.op.type == CbalcParser.GRT:
            return left>right
        elif ctx.op.type == CbalcParser.GRE:
            return left>=right
        elif ctx.op.type == CbalcParser.LES:
            return left<right
        elif ctx.op.type == CbalcParser.LEE:
            return left<=right
    
    def visitCompOper2(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        if ctx.op.type == CbalcParser.EQL:
            return left == right
        elif ctx.op.type == CbalcParser.NEQ:
            return left != right

    def visitBitOper(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        if ctx.op.type == CbalcParser.AND:
            return left&right
        elif ctx.op.type == CbalcParser.OR:
            return left|right
        elif ctx.op.type == CbalcParser.XOR:
            return left^right

    def visitLogicOperAnd(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        return left and right

    def visitLogicOperOr(self, ctx):
        left, right = number(self.visit(ctx.expr(0))), number(self.visit(ctx.expr(1)))
        return left or right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
