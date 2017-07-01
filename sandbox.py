
from RestrictedPython import compile_restricted #for compiling the code safely
from RestrictedPython.Guards import safe_builtins#the builtins that are safe
from RestrictedPython.Guards import full_write_guard#never lets restricted code modify (assign, delete an attribute or item) it shouldn't to
import sys#for manipulating the parameters recieved
import ast
"""preparing the safe_builtins"""
safe_builtins["_getiter_"]= list
safe_builtins["type"]= __builtins__.type
safe_builtins["_getattr_"]= getattr
safe_builtins["_write_"]= full_write_guard

SliceType = type(slice(0))
DisallowedObject = []

class AccessDenied (Exception):
    pass

def guarded_getitem(ob, index):
    if type(index) is SliceType and index.step is None:
        start = index.start
        stop = index.stop
        if start is None:
            start = 0
        if stop is None:
            v = ob[start:]
        else:
            v = ob[start:stop]
    else:
        v = ob[index]
    if v is DisallowedObject:
        raise AccessDenied
    return v

safe_builtins["_getitem_"]= guarded_getitem


restricted_globals = dict(__builtins__ = safe_builtins)#
"""open the plugin for retrieving the code as a string"""
with open(sys.argv[1], 'r') as plugin:
    data=plugin.read()
loc = {}#the locals for the sandboxed environment
"""compling the code with the restricted funcionalities such as import, using names starting with underscore _, etc"""
byte_code = compile_restricted(data, sys.argv[1], 'exec')
"""executing the byte code with the restricted globals"""
exec(byte_code, restricted_globals, loc)
"""updating the globals"""
restricted_globals.update(loc)
for nombre, value in restricted_globals.items():
    globals()[nombre] = value
"""executes the function in sanbox.py environment, by this point the code should be safe"""
if (sys.argv[2]=="name"):
    print restricted_globals[sys.argv[2]]()
else:
    """parsing the parameters"""
    roll_no = ast.literal_eval(sys.argv[3])
    dice = ast.literal_eval(sys.argv[4])
    bonus = ast.literal_eval(sys.argv[5])
    players =ast.literal_eval(sys.argv[6])
    scoresheets = ast.literal_eval(sys.argv[7])
    """executing the play"""
    print restricted_globals["play"](roll_no,dice,bonus,players,scoresheets)