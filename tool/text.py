import random
import sys
import time
def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.07)
type('Pursue perfection then success will come to you ||  Learn what you like then you will easily understand - ERR0R.')
