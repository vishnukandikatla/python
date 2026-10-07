dict = {
    "name": "vishnu",
    " marks" : { "chem" : 99,
                "phy" : 88,
                "maths" : 100,
                "eng" : 100
    }
}
dict[" marks"].update({"chem": 0})
 
import json 
dump = json.dumps(dict)
print(dump)