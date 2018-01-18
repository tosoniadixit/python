#comments

### 1. f is of type int set to 0
f =0
print(f)

### 2. f of type string set to "abc"
f="abc"
print(f)

### 3.  Error Different type
# print("string type " + 123)

### 4. convert number to string type
print("string type " + str(123))


### 5. Local variable
def localScopeFunction():
    f = "def"
    print(f)

localScopeFunction()
print(f) # it will print abc because def is function local scope.

### 6. Global variable
def globalScopeFunction():
    global f
    f = "xyz"
    print(f)
globalScopeFunction()
print(f)


### 7. undefined variable
del f
print(f)
