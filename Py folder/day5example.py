"""
demonstration void vs value-returning
"""
def moreInput(a,b,c,d):
    print(a+d,"is a + d")
    return a+d

result = moreInput(1,2,3,4)
print(result,"is returned.")
print(moreInput(1,2,3,4), "is returned")
