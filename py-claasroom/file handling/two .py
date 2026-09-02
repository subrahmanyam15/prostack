import json
fp1 =open('users.json1','r')
users=json.load(fp1)

male_users=[]
female_users=[]
for user in users:
    if user['gender']=='male':
        male_users.append(user)
    elif user['gender']=='female':
        female_users.append(user)

fp2=open('male.json','w')
fp3=open('female.json','w')
json.dump(male_users,fp2)
json.dump(female_users,fp3)
print("new json file created sucessfully")
fp1.close()
fp2.close()
fp3.close()
