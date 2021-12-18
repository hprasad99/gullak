import json

# file = open('input.json')
# input = json.loads(file)

# for i in input['sms']:
#     print(i)

# file.close()
file_path = 'C:\Users\Himanshu J Prasad\Desktop\Gullak\input.json'
with open('C:\Users\Himanshu J Prasad\Desktop\Gullak\input.json','r') as f:
    data = json.loads(f.read())
    print(data[0]['text'])