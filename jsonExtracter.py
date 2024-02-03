import json

def getNumElements(filename):
    with open("./resumeconfigs/" + filename + ".json") as json_config:
        e = json.load(json_config)
        g = json.dumps(e)

        num_elements = e["personalinfo"]["num_elements"]
        return num_elements

def getHeaderElement(number):
    with open("./resumeconfigs/config.json") as json_config:
        e = json.load(json_config)
        print(e)

        g = json.dumps(e)

        num_elements = e["personalinfo"]["contains"][number]
        print(num_elements)

        with open("./resumecontent/personalinfo.json") as json_personalinfo:
            d = json.load(json_personalinfo)
            print(d)

            y = json.dumps(d)

            result = []
            type = d[num_elements]["type"]
            if (type == "text"):
                result[0] = "text"
                result[1] = d[num_elements]["text"]
            elif (type == "email"):
                result[0] = "email"
                result[1] = d[num_elements]["text"]
                result[2] = "mailto:" + d[num_elements]["text"]
            elif (type == "link"):
                result[0] = "link"
                result[1] = d[num_elements]["text"]
                result[2] = d[num_elements]["url"]
            return result



