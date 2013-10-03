__author__ = 'nathan'

import sh
import tablib

def run_opencfu(i, a=True, m='auto', d='bil', t=False, l=False, r=False, R=False, c=False, C=False):
    options = {('-i %s' % i): True}
    if a:
        options["-a"] = True
    if m:
        options["-m %s" % m] = True
    if d:
        options["-d %s" % d] = True
    if t:
        options["-t %s" % t] = True
    if l:
        options["-l %s" % l] = True
    if r:
        options["-r %s" % r] = True
    if R:
        options["-R %s" % R] = True
    if c:
        options["-c %s" % c] = True
    if C:
        options["-C %s" % C] = True
    result = tablib.Dataset()
    result.csv = sh.opencfu(*options)
    return result