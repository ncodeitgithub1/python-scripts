formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % ("i had this thing",
                   "that you could type up right",
                   "but it didnt sing",
                   "spo i said good night"
)