import json
import re

categoryMapping = {'upiswiggy':"Food","BBPSBP":"Bill Payment"}
def toCategorize(text):
    #obj = {}
    category = ""
    #smsArray = []
    totalAmount = 0
    if(re.search("[a-z]+\s@[a-z]+",text)):
        category="Food"
        val = "".join(extractAmount(text))
        totalAmount += float(val)
        # time = item['time']
        # sender = item['sender']
        # text = item['text']
        #newbalance = item['New balance']
        # smsArray.append({"time":time,"sender":sender,"text":text,"New balance":newbalance})
        # obj["category"]=category
        # obj["totalAmount"]=totalAmount
        # obj["smsArray"] = smsArray
    elif(re.search("[A-Z]+",text)): 
        totalAmount = 0
        category="Bill Payment"
        val = "".join(extractAmount(text))
        totalAmount += float(val)
        # time = item['time']
        # sender = item['sender']
        # text = item['text']
        #newbalance = item['New balance']
        # smsArray.append({"time":time,"sender":sender,"text":text,"New balance":newbalance})
        # obj["category"]=category
        # obj["totalAmount"]=totalAmount
        # obj["smsArray"] = smsArray
    return totalAmount,category
    
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
            tmpObj['totalAmount']+=amount
            tmpObj['smsArray'].append(sms)
        else:
            summary.append({'category':category,'totalAmount':amount,'smsArray':[sms]})    
    output["summary"] = summary
        
json_object = json.dumps(output,indent = 4)
        
#writing to out.json file
with open("out.json","w") as outfile:
    outfile.write(json_object)



