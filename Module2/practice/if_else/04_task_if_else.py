# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
x = int(input("x="))
if x // 3:
    print("Foo")
elif x / 5:
    print("Bar")
elif x / 3 and x / 5:
    print("Foobar")
