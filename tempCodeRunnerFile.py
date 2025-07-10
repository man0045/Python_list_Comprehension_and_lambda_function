class myError(Exception):
 pass
try:
 raise myError("this is custom Erorr")
except myError as e:
 print(e)