import xml.etree.ElementTree as ET

mytree = ET.parse('date.xml')
myroot = mytree.getroot()

print(myroot.tag)


for n in  myroot.findall(".//rank/..[@name='Panama']"): # 
    print(n.attrib['name'])
    print(len(n.items()))
    for it in n.iter():
        print(it.tag, it.text)

i = 0
for g in myroot.findall("./*"):
    i+=1
print("Count is ", i)

# ""Print an xml file in heirarchical format, with element name and its attributes, if any, on same line and children indented
"""
<data>
  <Subject name="science">
    <Books>
      <Book type="theory">Something1</Book>
      <Book type="workshop">Something2</Book>
    </Books>
  </Subject>
  <Subject name="maths" class="sdflkajf"/>
</data>

data:
  Subject: name=science
    Books:
      Book: type=theory
        Something1
      Book: type=workshop
        Something2
  Subject: name=maths
"""


*#
