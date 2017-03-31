## Try this:
<ex>
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
</ex>
This will yeild the following table.
<table>

	               bark           blooded        scales
	dogs           1              1              None
	cats           0              1              None
	fish           None           0              1

	               bark           blooded        scales
	dogs           1              1              1
	cats           0              1              1
	fish           0.5            0              1

</table>
While the results of this underlying algorithm can are bad on small data sets, in places where the sample size is larger this fitting provides smooth toplogies in n dimensional space to fit any data. 
