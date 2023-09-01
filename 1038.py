a, b = input().split()
a = int(a)
b = int(b)

if a == 1:
    total = 4 * b
    print("Total: R$ {:.2f}".format(total))
if a == 2:
    total = 4.5 * b
    print("Total: R$ {:.2f}".format(total))
if a == 3:
    total = 5 * b
    print("Total: R$ {:.2f}".format(total))
if a == 4:
    total = 2 * b
    print("Total: R$ {:.2f}".format(total))
if a == 5:
    total = 1.5 * b
    print("Total: R$ {:.2f}".format(total))