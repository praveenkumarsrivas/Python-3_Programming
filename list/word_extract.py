l=list()
l=['mango','banana','grapes','papaya']
s='mangograpesbananapapaya'
ss=""
for x in range(len(s)):
    ss+=s[x]
    if(ss in l):
        print(ss)
        ss=""
        
        
 '''
It's just a demo need to write a python script which can extract meaningful words from any random string.
eg:
giving random raw string="knnknitkliwnsurathkal"
output: nitk
        surathkal
'''
