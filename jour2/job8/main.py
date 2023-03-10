
def String (type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarien et kiwi")
    elif type == "fruit" and saison == "ete":
        print ("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print ("carotte, topinambour,endive")
    elif type == "legume" and saison =="ete":
        print ("artichaud, aubergine,navet")
    else:
        print("plus de fruit et legume pour cette saison")


String ("fruit","printemps")