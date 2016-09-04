import time
from math import sqrt
import decimal
res=0

def fiblogic(inp):
    res = 0
    n=inp.encode("utf-8")
    n=int(n)
    start_time = time.time()
    s5 = decimal.Decimal(5).sqrt()
    res = round(((1 + s5) ** n - (1 - s5) ** n) / (2 ** n * s5))
    timetaken =("%s seconds" % (time.time() - start_time))
    print res
    return res,timetaken


