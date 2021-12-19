import json
import re

def toCategorize(text,item):
    obj = {}
    category = ""
    smsArray = []
    totalAmount = 0
    if(re.search("[a-z]+\s@[a-z]+",text)):
        category="Food"
        val = "".join(extractAmount(text))
        totalAmount += float(val)
        time = item['time']
        sender = item['sender']
        text = item['text']
        newbalance = item['New balance']
        smsArray.append({"time":time,"sender":sender,"text":text,"New balance":newbalance})
        obj["category"]=category
        obj["totalAmount"]=totalAmount
        obj["smsArray"] = smsArray
    elif(re.search("[A-Z]+",text)): 
        totalAmount = 0
        category="Bill Payment"
        val = "".join(extractAmount(text))
        totalAmount += float(val)
        time = item['time']
        sender = item['sender']
        text = item['text']
        newbalance = item['New balance']
        smsArray.append({"time":time,"sender":sender,"text":text,"New balance":newbalance})
        obj["category"]=category
        obj["totalAmount"]=totalAmount
        obj["smsArray"] = smsArray
    return obj
    
def extractAmount(text):
    amount = 0
    if(re.search("[0-9]+[0-9]*\.[0-9]+",text)):
        amount = re.findall("[0-9]+[0-9]*\.[0-9]+",text)
    return amount

if __name__== "__main__":
    file_path = 'input.json'
    summary = []
    main = {}
    with open(file_path,'r') as f:
        data = json.loads(f.read())
    
    for item in data['sms']:
        text = item['text'];
        # extracted text to be categorized
        summary.append(toCategorize(text,item))
        main["summary"] = summary
        
json_object = json.dumps(main,indent = 4)
        
#writing to out.json file
with open("out.json","w") as outfile:
    outfile.write(json_object)



