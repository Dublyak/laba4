import modul6

N = int(input("Введите количество чисел в списке: "))
A = []
for i in range(N):
    number = float(input(f"Введите число {i+1}: "))
    A.append(number)

K = int(input("Введите порядковый номер элемента для удаления: ")) - 1

updated_list = modul6.remove_element(A, K)
print(f"Измененный список: {updated_list}")
print(modul6.module_description())
