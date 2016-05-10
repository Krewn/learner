try this:

#!/bin/python

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

While the results of this underlying algorithm can be funny on small data sets, in places where the sample size is larger this fitting provides smooth toplogies in n dimensional space to fit any data. 
