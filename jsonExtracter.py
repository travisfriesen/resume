import json


#gets the number of elements in the resume from config>personalinfo>num_elements
def get_num_elements(filename):
    with open("./resumeconfigs/" + filename + ".json") as json_config:
        e = json.load(json_config)
        g = json.dumps(e)

        num_elements = e["personalinfo"]["num_elements"]

        num_elements = int(num_elements) + 1
        return num_elements


#gets the header element from config>personalinfo>contains
def get_header_element(number):
    with open("./resumeconfigs/config.json") as json_config:
        e = json.load(json_config)

        num_elements = e["personalinfo"]["contains"][number]

        with open("./resumecontent/personalinfo.json") as json_personalinfo:
            d = json.load(json_personalinfo)

            result = [0, 0, 0]
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


#gets the all the elements (except personal info) and their types from the config file
def get_catagory_type(filename):
    with open("./resumeconfigs/" + filename + ".json") as json_config:
        e = json.load(json_config)
        elements = list(e)

        if "personalinfo" in elements:
            elements.remove("personalinfo")

        element_type = []
        for i in range(len(elements) - 1):
            element_type.append(e[elements[i]]["type"])

    return elements, element_type


#gets the filepath of the element from the config file
def get_filepath(element, filename):
    with open("./resumeconfigs/" + filename + ".json") as json_config:
        e = json.load(json_config)
        filepath = e[element]["filepath"]

    return filepath
