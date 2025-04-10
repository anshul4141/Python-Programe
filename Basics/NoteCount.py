amount = 4700

notes500 = amount // 500
amount = amount % 500

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100

print("500 = ", notes500)
print("200 = ", notes200)
print("100 = ", notes100)