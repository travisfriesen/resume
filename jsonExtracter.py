import json

def getNumElements(filename):
    with open("./resumeconfigs/" + filename + ".json") as json_config:
        e = json.load(json_config)
        g = json.dumps(e)

        num_elements = e["personalinfo"]["num_elements"]
        return num_elements

def getHeaderElement(object):
    with open("./resumecontent/personalinfo.json") as json_info:
        pi = json.load(json_info)
        pid = json.dumps(pi)

        element = pi[num_elements]
        print(element)



