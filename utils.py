from functools import reduce

SUB = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

def nth_x(i):
  return "x%s" % SUB[i]

def nth_slack_x(i):
  return "xF%s" % SUB[i]

def equation(coefficients):
  with_var = [
    "%i%s" % (coefficient, nth_x(i + 1))
      for i, coefficient in enumerate(coefficients)
  ]

  return reduce(lambda a, b:
    a + " - " + b[1:] if b[0] == "-"
    else a + " + " + b
  , with_var)

