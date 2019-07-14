# words = (0,1,2,5,6,7,8,9)
# exclusives = (3,4)
# counts = 0
# with open('password.txt','w') as file_object:
#     for n1 in words:
#         if n1 not in exclusives:
#             for n2 in words:
#                 if n2 not in exclusives:
#                     for n3 in words:
#                         if n3 not in exclusives:
#                             for n4 in words:
#                                 if n4 not in exclusives:
#                                     counts = counts + 1
#                                     file_object.write(str(n1) + str(n2) + str(n3) + str(n4))
#                                     if counts % 10 == 0:
#                                         file_object.write("\n")
#                                     else:
#                                         file_object.write("  ")

with open('minus.txt', 'w') as file_object:
    for x in range(11, 20):
        for y in range(7, 10):
            file_object.write(str(x) + " - " + str(y) + " = " + str(x - y))
            file_object.write("\n")
