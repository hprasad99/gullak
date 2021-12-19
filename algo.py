import json
import re

categoryMapping = {'upiswiggy':"Food","BBPSBP":"Bill Payment"}

def toCategorize(text):
    category = ""
    textToSearch = text.split(' ')[11]
    val = "".join(extractAmount(text))
    category = categoryMapping[textToSearch]
    return val,category
    
def extractAmount(text):
    amount = 0
    if(re.search("[0-9]+[0-9]*\.[0-9]+",text)):
        amount = re.findall("[0-9]+[0-9]*\.[0-9]+",text)
    return amount

if __name__== "__main__":
    file_path = 'input.json'
    summary = []
    output = {}
    with open(file_path,'r') as f:
        data = json.loads(f.read())
    
    for sms in data['sms']:
        text = sms['text'];
        # extracted text to be categorized
        #summary.append(toCategorize(text,item))
        amount,category = toCategorize(text)
        # get index from summary where category is smscategory
        if any(obj['category'] == category for obj in summary):
            tmpObj = [ele for ele in summary if ele['category']==category][0]
            tmpObj['totalAmount']+=float(amount)
            tmpObj['smsArray'].append(sms)
        else:
            summary.append({'category':category,'totalAmount':float(amount),'smsArray':[sms]})    
    output["summary"] = summary
        
json_object = json.dumps(output,indent = 4)
        
#writing to out.json file
with open("out.json","w") as outfile:
    outfile.write(json_object)



