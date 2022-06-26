A = int(input())
print(A)
note100 = A // 100
A = A - (note100 * 100)
print(f"{note100} nota(s) de R$ 100,00")
note50 = A // 50
A = A - (note50 * 50)
print(f"{note50} nota(s) de R$ 50,00")
note20 = A // 20
A = A - (note20 * 20)
print(f"{note20} nota(s) de R$ 20,00")
note10 = A // 10
A = A - (note10 * 10)
print(f"{note10} nota(s) de R$ 10,00")
note5 = A // 5
A = A - (note5 * 5)
print(f"{note5} nota(s) de R$ 5,00")
note2 = A // 2
A = A - (note2 * 2)
print(f"{note2} nota(s) de R$ 2,00")
note1 = A // 1
A = A - (note100 * 1)
print(f"{note1} nota(s) de R$ 1,00")
