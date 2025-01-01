import hashlib
code = "3cc6520a6890b92fb55a6b3d657fd1f6"
for i in range(100000,1000000):
    result = hashlib.md5(str(i).encode()).hexdigest()
    if result == code:
        print(i)
        break



