from lark import Lark

parser = Lark("""
expr: expr op expr       -> dyad
    | op expr            -> monad
    | /[0-9]+/
    | NAME
    | STRING

op: /[^0-9\.]/
  | /[^0-9\.](:|\.)/

%import common.ESCAPED_STRING -> STRING
%import common.SIGNED_NUMBER  -> NUMBER
%import common.CNAME          -> NAME
%import common.WS
%ignore WS
""", start='expr')

print(parser.parse(input('> ')).pretty())
