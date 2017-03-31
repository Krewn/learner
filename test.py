import make as lrnr

t = lrnr.smarty()

t.learn("dogs bark")
t.learn("cats do not bark")
t.learn("dogs are warm blooded")
t.learn("cats are warm blooded")
t.learn("fish are not warm blooded")
t.learn("fish have scales")

t.think()
t.prt()
t.predPrt()