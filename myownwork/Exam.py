import numpy as np
def degreetoFar (TC):
    TF = 9/5*TC+32
    return (TF)
TC= float(input("Enter degrees:"))
TF= degreetoFar(TC)
print(f"the deg into Far is {TF:0.2f}")