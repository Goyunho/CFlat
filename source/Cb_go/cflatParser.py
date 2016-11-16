# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3K")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\3")
        buf.write("\6\3\35\n\3\r\3\16\3\36\3\4\3\4\5\4#\n\4\3\5\3\5\7\5\'")
        buf.write("\n\5\f\5\16\5*\13\5\3\5\3\5\3\6\6\6/\n\6\r\6\16\6\60\3")
        buf.write("\6\5\6\64\n\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b<\n\b\f\b\16")
        buf.write("\b?\13\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\2\3\4\2\6\b\n\nC\2\30\3\2\2")
        buf.write("\2\4\34\3\2\2\2\6\"\3\2\2\2\b$\3\2\2\2\n.\3\2\2\2\f\65")
        buf.write("\3\2\2\2\168\3\2\2\2\20@\3\2\2\2\22B\3\2\2\2\24D\3\2\2")
        buf.write("\2\26F\3\2\2\2\30\31\5\4\3\2\31\32\7\2\2\3\32\3\3\2\2")
        buf.write("\2\33\35\5\6\4\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2")
        buf.write("\2\2\36\37\3\2\2\2\37\5\3\2\2\2 #\5\b\5\2!#\5\n\6\2\"")
        buf.write(" \3\2\2\2\"!\3\2\2\2#\7\3\2\2\2$(\7F\2\2%\'\5\6\4\2&%")
        buf.write("\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3")
        buf.write("\2\2\2+,\7G\2\2,\t\3\2\2\2-/\5\f\7\2.-\3\2\2\2/\60\3\2")
        buf.write("\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\64\7I")
        buf.write("\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\13\3\2\2\2\65\66\5")
        buf.write("\16\b\2\66\67\7@\2\2\67\r\3\2\2\28=\5\20\t\29:\7A\2\2")
        buf.write(":<\5\20\t\2;9\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\17")
        buf.write("\3\2\2\2?=\3\2\2\2@A\t\2\2\2A\21\3\2\2\2BC\7\3\2\2C\23")
        buf.write("\3\2\2\2DE\7\4\2\2E\25\3\2\2\2FG\7\5\2\2G\27\3\2\2\2\b")
        buf.write("\36\"(\60\63=")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'++'", "'--'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'case'", "'break'", "'continue'", 
                     "'default'", "'for'", "'while'", "'if'", "'else'", 
                     "'return'", "'switch'", "<INVALID>", "'int'", "'float'", 
                     "'string'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "<INVALID>", "'&'", "'|'", "'^'", "'<<'", "'>>'", "<INVALID>", 
                     "'&&'", "'||'", "'!'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'='", "'.'", "':'", "';'", "','", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Initialisation", "Assignment", "Declaration", "Value", 
                      "Calculator", "Calculator_pmad", "Calculator_bit", 
                      "Calculator_logic", "Valiable", "Val_int", "Val_float", 
                      "Val_string", "Val_boolean", "Val_void", "Digit", 
                      "Nondigit", "Case", "Break", "Continue", "Default", 
                      "For", "While", "If", "Else", "RETURN", "Switch", 
                      "Type", "Int", "Float", "String", "Boolean", "Void", 
                      "TRUE", "FALSE", "NULL", "Plus", "Minus", "Asterisk", 
                      "Div", "Bit", "And", "Or", "Caret", "Leftshift", "Rightshift", 
                      "Logic", "Andand", "Oror", "Not", "Equal", "Notequal", 
                      "Less", "Lessequal", "Greater", "Greaterequal", "Assign", 
                      "Dot", "Colon", "Semi", "Coma", "Leftparen", "Rightparen", 
                      "Leftbracket", "Rightbracket", "Leftbrace", "Rightbrace", 
                      "Whitespace", "Newline", "Block_comment", "Line_comment" ]

    RULE_run = 0
    RULE_frame = 1
    RULE_group = 2
    RULE_brace_group = 3
    RULE_line = 4
    RULE_action_end = 5
    RULE_actions = 6
    RULE_action = 7
    RULE_increase = 8
    RULE_decrease = 9
    RULE_percent = 10

    ruleNames =  [ "run", "frame", "group", "brace_group", "line", "action_end", 
                   "actions", "action", "increase", "decrease", "percent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Initialisation=4
    Assignment=5
    Declaration=6
    Value=7
    Calculator=8
    Calculator_pmad=9
    Calculator_bit=10
    Calculator_logic=11
    Valiable=12
    Val_int=13
    Val_float=14
    Val_string=15
    Val_boolean=16
    Val_void=17
    Digit=18
    Nondigit=19
    Case=20
    Break=21
    Continue=22
    Default=23
    For=24
    While=25
    If=26
    Else=27
    RETURN=28
    Switch=29
    Type=30
    Int=31
    Float=32
    String=33
    Boolean=34
    Void=35
    TRUE=36
    FALSE=37
    NULL=38
    Plus=39
    Minus=40
    Asterisk=41
    Div=42
    Bit=43
    And=44
    Or=45
    Caret=46
    Leftshift=47
    Rightshift=48
    Logic=49
    Andand=50
    Oror=51
    Not=52
    Equal=53
    Notequal=54
    Less=55
    Lessequal=56
    Greater=57
    Greaterequal=58
    Assign=59
    Dot=60
    Colon=61
    Semi=62
    Coma=63
    Leftparen=64
    Rightparen=65
    Leftbracket=66
    Rightbracket=67
    Leftbrace=68
    Rightbrace=69
    Whitespace=70
    Newline=71
    Block_comment=72
    Line_comment=73

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def frame(self):
            return self.getTypedRuleContext(cflatParser.FrameContext,0)


        def EOF(self):
            return self.getToken(cflatParser.EOF, 0)

        def getRuleIndex(self):
            return cflatParser.RULE_run

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRun" ):
                return visitor.visitRun(self)
            else:
                return visitor.visitChildren(self)




    def run(self):

        localctx = cflatParser.RunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_run)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.frame()
            self.state = 23
            self.match(cflatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FrameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.GroupContext)
            else:
                return self.getTypedRuleContext(cflatParser.GroupContext,i)


        def getRuleIndex(self):
            return cflatParser.RULE_frame

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrame" ):
                return visitor.visitFrame(self)
            else:
                return visitor.visitChildren(self)




    def frame(self):

        localctx = cflatParser.FrameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_frame)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.group()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Calculator))) != 0) or _la==cflatParser.Leftbrace):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brace_group(self):
            return self.getTypedRuleContext(cflatParser.Brace_groupContext,0)


        def line(self):
            return self.getTypedRuleContext(cflatParser.LineContext,0)


        def getRuleIndex(self):
            return cflatParser.RULE_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)




    def group(self):

        localctx = cflatParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_group)
        try:
            self.state = 32
            token = self._input.LA(1)
            if token in [cflatParser.Leftbrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.brace_group()

            elif token in [cflatParser.Initialisation, cflatParser.Assignment, cflatParser.Declaration, cflatParser.Calculator]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.line()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Brace_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Leftbrace(self):
            return self.getToken(cflatParser.Leftbrace, 0)

        def Rightbrace(self):
            return self.getToken(cflatParser.Rightbrace, 0)

        def group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.GroupContext)
            else:
                return self.getTypedRuleContext(cflatParser.GroupContext,i)


        def getRuleIndex(self):
            return cflatParser.RULE_brace_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrace_group" ):
                return visitor.visitBrace_group(self)
            else:
                return visitor.visitChildren(self)




    def brace_group(self):

        localctx = cflatParser.Brace_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_brace_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(cflatParser.Leftbrace)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Calculator))) != 0) or _la==cflatParser.Leftbrace:
                self.state = 35
                self.group()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(cflatParser.Rightbrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.Action_endContext)
            else:
                return self.getTypedRuleContext(cflatParser.Action_endContext,i)


        def Newline(self):
            return self.getToken(cflatParser.Newline, 0)

        def getRuleIndex(self):
            return cflatParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = cflatParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 43
                    self.action_end()

                else:
                    raise NoViableAltException(self)
                self.state = 46 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 49
            _la = self._input.LA(1)
            if _la==cflatParser.Newline:
                self.state = 48
                self.match(cflatParser.Newline)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Action_endContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actions(self):
            return self.getTypedRuleContext(cflatParser.ActionsContext,0)


        def Semi(self):
            return self.getToken(cflatParser.Semi, 0)

        def getRuleIndex(self):
            return cflatParser.RULE_action_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction_end" ):
                return visitor.visitAction_end(self)
            else:
                return visitor.visitChildren(self)




    def action_end(self):

        localctx = cflatParser.Action_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.actions()
            self.state = 52
            self.match(cflatParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.ActionContext)
            else:
                return self.getTypedRuleContext(cflatParser.ActionContext,i)


        def Coma(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Coma)
            else:
                return self.getToken(cflatParser.Coma, i)

        def getRuleIndex(self):
            return cflatParser.RULE_actions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActions" ):
                return visitor.visitActions(self)
            else:
                return visitor.visitChildren(self)




    def actions(self):

        localctx = cflatParser.ActionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.action()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cflatParser.Coma:
                self.state = 55
                self.match(cflatParser.Coma)
                self.state = 56
                self.action()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Initialisation(self):
            return self.getToken(cflatParser.Initialisation, 0)

        def Assignment(self):
            return self.getToken(cflatParser.Assignment, 0)

        def Declaration(self):
            return self.getToken(cflatParser.Declaration, 0)

        def Calculator(self):
            return self.getToken(cflatParser.Calculator, 0)

        def getRuleIndex(self):
            return cflatParser.RULE_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = cflatParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Calculator))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncreaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_increase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncrease" ):
                return visitor.visitIncrease(self)
            else:
                return visitor.visitChildren(self)




    def increase(self):

        localctx = cflatParser.IncreaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(cflatParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DecreaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_decrease

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecrease" ):
                return visitor.visitDecrease(self)
            else:
                return visitor.visitChildren(self)




    def decrease(self):

        localctx = cflatParser.DecreaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(cflatParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PercentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_percent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPercent" ):
                return visitor.visitPercent(self)
            else:
                return visitor.visitChildren(self)




    def percent(self):

        localctx = cflatParser.PercentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(cflatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





