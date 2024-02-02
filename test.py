import json
from pprint import pprint

"""f = open("./resumecontent/personalinfo.json", "r")
print(f.read())"""

with open("./resumeconfigs/config.json") as json_config:
    e = json.load(json_config)
    print(e)

    g = json.dumps(e)

    num_elements = e["personalinfo"]["contains"][2]
    print(num_elements)

    with open("./resumecontent/personalinfo.json") as json_confff:
        h = json.load(json_confff)
        print(h)

        j = json.dumps(h)

        element = h[num_elements]
        print(element)


with open("./resumecontent/personalinfo.json") as json_personalinfo:
    d = json.load(json_personalinfo)
    print(d)

    y = json.dumps(d)

    name_text = d["name"]["text"]
    print(name_text)
