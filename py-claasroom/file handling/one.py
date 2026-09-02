import json
fp1=open('data.text','r')
employee=json.load(fp1)
malecount=0
femalecount=0

for emp in employee:
    if emp['gender']=='male':
        malecount =+1
    else femalecount =+1
print('malecount(male) femalecount(female)')






