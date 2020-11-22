

def cakes(recipe, available):
    tot = list()
    for ing,cant in recipe.items():
        tot.append(available.get(ing,0)//cant)
    
    return min(tot) if tot else 0




recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
assert (cakes(recipe, available) == 2)
print("funciono!")
