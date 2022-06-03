import re
############ Our String Here
st = "this is the string that we want to programming and processing \n this is newLine    with multispace   and tab _ - 1 2 3 ! # @ sing tell me killed hime"

############ Tokeniztion of String Here
token = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", st) ###### print(st.split())

############ Stemming of String Here
with open("stopWords.txt", "r") as txt_file:
    stopWords = re.findall(r"\w+", txt_file.read())

token = [i for i in token if i not in stopWords]

text = "sing"

def strip_suffixes(s,suffixes): 
    for suf in suffixes: 
        if s.endswith(suf): 
            return s.rstrip(suf) 
    return s 

# text = strip_suffixes('sing',['s','es','er','r','ed', 'ing']) 

with open("suffix.txt", "r") as txt_file:
    stopWords = re.sub(r"\d+", ' ', txt_file.read())
print(stopWords.split())