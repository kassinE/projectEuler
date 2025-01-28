### QUESTION 1 ###
#  <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
#  <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>

### brainstorm: 
    # for n < 1000:
    #   add all multiples of 3
    #   add all multiples of 5
    #   subtract all multiples of 15 = 3*5, as the appear in both sets

import numpy as np

