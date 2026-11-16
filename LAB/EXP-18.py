import re

# FOPC grammar handled by this recursive-descent parser
#   formula := ('all'|'exists') var '.' formula | implication
#   implication := disjunction ['->' implication]
#   disjunction := conjunction ('|' conjunction)*
#   conjunction := unary ('&' unary)*
#   unary := '-' unary | '(' formula ')' | Pred '(' term {',' term} ')'

TOKEN = re.compile(r"\s*(->|(?:all|exists)\b|[A-Za-z_]\w*|[().,&|\-])")

def tokenize(s):
    pos, out = 0, []
    while pos < len(s):
        m = TOKEN.match(s, pos)
        if not m:
            raise SyntaxError(f"bad character at {pos}: {s[pos:]!r}")
        out.append(m.group(1)); pos = m.end()
    return out

class Parser:
    def __init__(self, text):
        self.t, self.i = tokenize(text), 0
    def peek(self):  return self.t[self.i] if self.i < len(self.t) else None
    def eat(self, x=None):
        tok = self.peek()
        if tok is None:
            raise SyntaxError("unexpected end of formula")
        if x and tok != x:
            raise SyntaxError(f"expected {x!r} but found {tok!r}")
        self.i += 1; return tok
    def parse(self):
        f = self.formula()
        if self.peek() is not None: raise SyntaxError("extra input: " + self.peek())
        return f
    def formula(self):
        if self.peek() in ("all", "exists"):
            q = self.eat(); v = self.eat(); self.eat("."); return (q, v, self.formula())
        return self.implication()
    def implication(self):
        l = self.disjunction()
        if self.peek() == "->":
            self.eat(); return ("->", l, self.formula())
        return l
    def disjunction(self):
        l = self.conjunction()
        while self.peek() == "|":
            self.eat(); l = ("|", l, self.conjunction())
        return l
    def conjunction(self):
        l = self.unary()
        while self.peek() == "&":
            self.eat(); l = ("&", l, self.unary())
        return l
    def unary(self):
        if self.peek() == "-":
            self.eat(); return ("-", self.unary())
        if self.peek() == "(":
            self.eat(); f = self.formula(); self.eat(")"); return f
        name = self.eat(); self.eat("(")
        args = [self.eat()]
        while self.peek() == ",":
            self.eat(); args.append(self.eat())
        self.eat(")")
        return ("pred", name, args)

def pretty(t, ind=0):
    p = "  " * ind
    if t[0] in ("all", "exists"):
        print(f"{p}{t[0].upper()} {t[1]}"); pretty(t[2], ind + 1)
    elif t[0] == "pred":
        print(f"{p}{t[1]}({', '.join(t[2])})")
    elif t[0] == "-":
        print(f"{p}NOT"); pretty(t[1], ind + 1)
    else:
        print(f"{p}{t[0]}"); pretty(t[1], ind + 1); pretty(t[2], ind + 1)

for f in ["all x.(Dog(x) -> Animal(x))",
          "exists y.(Cat(y) & Likes(y, John))",
          "all x.(Student(x) -> exists y.(Book(y) & Reads(x, y)))",
          "-Happy(Mary) | Sad(Mary)",
          "all x.(Dog(x) ->"]:
    print("Formula:", f)
    try:
        pretty(Parser(f).parse(), 1)
    except SyntaxError as e:
        print("   Syntax error:", e)
    print()
