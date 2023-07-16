# def strcounter(string): #сложность О(n**2)
#     for symvol in string:
#         counter = 0
#         for sub_symvol in string:
#             if symvol == sub_symvol:
#                 counter += 1
#         print(symvol,counter)

# strcounter('aaaabbcdee')


# def strcounter(string): #сложность O(n*m)
#     for symvol in set(string):
#         counter = 0
#         for sub_symvol in string:
#             if symvol == sub_symvol:
#                 counter += 1
#         print(symvol,counter)


# strcounter('aaaabbcdee')

def strcounter(string): #сложность O(n)
    syms_counter = {}
    for symvol in string:
        syms_counter[symvol] = syms_counter.get(symvol,0)+1
    print(syms_counter)

strcounter('aaaabbcdee')