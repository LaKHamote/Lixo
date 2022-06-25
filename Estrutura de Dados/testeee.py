from shutil import ExecError


def asc(v):
    if v < 4:
        return v
    raise Exception("Mcaca")
a = 44444444444444    
try:
    a = asc(5)
    print(1, a)
except Exception as e:
    print(e)
    print(2, a)
