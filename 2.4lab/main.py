# а) 
def capitalize_words(text, separator=" "):
    words = text.split(separator)
    result = ""
    for word in words:
        result = result + word.capitalize() + separator
    return result[:-1]
# б) 
def filter_elements(list1, list2, filter_function=None):
    result = []
    for x in list1:
        if filter_function == None:
            result.append(x)
        else:
            if filter_function(x):
                result.append(x)
    for x in list2:
        if filter_function == None:
            result.append(x)
        else:
            if filter_function(x):
                result.append(x)
    return result
# в) 
def merge_dictionaries(dict1, dict2, dict3=None, dict4=None):
    result = {}
    for d in (dict1, dict2, dict3, dict4):
        if d != None:
            for key in d:
                result[key] = d[key]
    return result
# г) 
def unique_keys(dict1, dict2):
    result = {}
    for key in dict1:
        if key not in dict2:
            result[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]
    return result
