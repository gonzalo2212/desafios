import unittest

def zero(x=None): return eval(f"0{x}") if x else 0
def one(x=None): return eval(f"1{x}") if x else 1
def two(x=None): return eval(f"2{x}") if x else 2
def three(x=None): return eval(f"3{x}") if x else 3
def four(x=None): return eval(f"4{x}") if x else 4
def five(x=None): return eval(f"5{x}") if x else 5
def six(x=None): return eval(f"6{x}") if x else 6
def seven(x=None): return eval(f"7{x}") if x else 7
def eight(x=None): return eval(f"8{x}") if x else 8
def nine(x=None): return eval(f"9{x}") if x else 9

def plus(x=0): return f"+{x}"
def minus(x=0): return f"-{x}"
def times(x=0): return f"*{x}"
def divided_by(x=0): return f"//{x}"

assert (seven(times(five())) == 35)
assert (five(times(seven())) == 35)
assert (four(plus(nine())) == 13)
assert (eight(minus(three())) == 5)
assert (six(divided_by(two())) == 3)
print("Test Correctos!")