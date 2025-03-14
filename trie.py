import pandas as pd
from collections import deque 

class TrieNode:
    def __init__(self):
        self.children = [None] * 144
        self.cocktailName = ''
        self.isCocktail = False


def insert(root, cock, ingrs):
    curr = root
    for c in ingrs:
        index = ingredientLookUp[c]
        if curr.children[index] is None:
            new_node = TrieNode()
            curr.children[index] = new_node
        curr = curr.children[index]
    curr.isCocktail = True
    curr.cocktailName = cock

def search(root, ingrs):
    curr = root
    for c in ingrs:
        index = ingredientLookUp[c]
        if curr.children[index] is None:
            return {
                "isCocktail": False, 
                "cocktailName": ''
            }
        curr = curr.children[index]
    return {
                "isCocktail": curr.isCocktail, 
                "cocktailName": curr.cocktailName
            }

# -- END OF TRIE LOGIC --


pd.options.display.max_rows = 9999
df = pd.read_csv('savoy.csv')

cocktails = {}
ingredientLookUp = {}

cols = df.columns
for ind, c in enumerate(cols):
    ingredientLookUp[c] = ind


for index, row in df.iterrows():
    
    ingrs = deque([])

    for c in cols:
        if not pd.isnull(row[c]):
            ingrs.append(c)
    ingrs.popleft()
    cocktails[row['Cocktail']] = list(ingrs)

root = TrieNode()
for cock in cocktails:
    insert(root, cock, cocktails[cock])
test = {
 'Waterbury': ['Sugar / Simple Syrup', 'Lemon', 'Egg', 'Cognac', 'Grenadine'],
 'Tulip': ['Sweet (Italian) Vermouth', 'Lemon', 'Apricot Brandy / Abricotine / Pricota*', 'Calvados'],
 'Swizzles': ['London Dry Gin', 'Angostura Bitters', 'Sugar / Simple Syrup', 'Lime', 'Swizzle Stick*'],
 'FakeDrink': ['London Dry Gin', 'Swizzle Stick*']
}
# True
# True
# True
# False
for cock in test:
    res = search(root, test[cock])
    if res['isCocktail']:
        print(str(res['isCocktail']) + " " + str(res['cocktailName']))
    else:
        print(str(res['isCocktail']) +  " not a cocktail")