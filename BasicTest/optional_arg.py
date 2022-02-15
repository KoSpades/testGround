def testfunc(arg1, arg2=True, arg3="hello"):
    print(arg1)
    print(arg2)
    print(arg3)


print("First run:")
testfunc("gay")

print("Second run:")
testfunc("gay", 1)

print("Third run:")
testfunc("gay", False, "not hello")

print(None)