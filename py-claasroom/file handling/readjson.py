import json
fp1=open('data.text','r')
employee_list=json.load(fp1)
print(len(employee_list))