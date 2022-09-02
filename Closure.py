def peru(name):
    print("ayya en peru ", name)
    def innoru_peru():
        print("ennaku innoru peru iruku {} Bashaa!".format(name[:5]))
    return innoru_peru
rajini = peru("Manikam")
print(rajini)

rajini()

#deleting manikam(outer method)
del peru
rajini()