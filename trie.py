import pandas as pd
from collections import deque 

class TrieNode:
    def __init__(self):
        self.children = [None] * 144
        self.isCocktail = False


def insert(root, ingrs):
    curr = root
    for c in ingrs:
        index = ingredientLookUp[c]
        if curr.children[index] is None:
            new_node = TrieNode()
            curr.children[index] = new_node
        curr = curr.children[index]
    curr.isCocktail = True

def search(root, ingrs):
    curr = root
    for c in ingrs:
        index = ingredientLookUp[c]
        if curr.children[index] is None:
            return False
        curr = curr.children[index]
    return curr.isCocktail

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

# for c in cocktails:
#     print(str(c) + " " + str(cocktails[c]))

# print(ingredientLookUp)

root = TrieNode()
for cock in cocktails:
    insert(root, cocktails[cock])
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
    print(search(root, test[cock]))