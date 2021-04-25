fname='onedrive.ignore'
regname='onedriveignore.reg'
items=open(fname,'r').readlines()
regfile=open(regname,'w')

title='''Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\OneDrive\EnableODIgnoreListFromGPO]
'''
regfile.write(title)
for item in items:
    item=item.strip()
    regfile.write('"'+item+'"="'+item+'"\n')

regfile.close()
