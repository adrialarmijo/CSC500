import Item
import json
from json import JSONEncoder

f = open("data.json", "rw")
data = json.load(f)

class ItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class ItemToPurchase(Item) :
    def __init__(self):
         self.item = Item
         self.itemNumber = 0

    def genItemNumber(self, number):
        self.itemNumber += number
        return self.itemNumber

    def write(self, itemNumber):
        item = "item_" + str(self.genItemNumber(itemNumber))
        itemToPurchase = ItemToPurchase(item)
        
        jsonString = json.dumps(itemToPurchase, indent=4, cls=ItemEncoder)

        with f as outfile:
            outfile.write(jsonString)

f.close()