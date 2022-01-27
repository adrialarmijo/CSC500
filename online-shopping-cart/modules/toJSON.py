import json
from json import JSONEncoder

f = open("data.json", "rw")
data = json.load(f)

class ItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def toJSON(item) :    
    def genItemNumber(self, number):
        itemNumber = 0
        itemNumber += number
        return self.itemNumber

    def write(self, itemNumber):
        itemName = "item_" + str(self.genItemNumber(itemNumber))
        # itemToJSON = item.setItemName(itemName)
        
        # jsonString = json.dumps(itemToJSON, indent=4, cls=ItemEncoder)

        # with f as outfile:
        #     outfile.write(jsonString)

f.close()