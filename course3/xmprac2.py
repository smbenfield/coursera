import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

# Creates object
stuff = ET.fromstring(input)
# Creates list of all instances of user within users
lst = stuff.findall('users/user')
# Prints length of list
print 'User count:', len(lst)

#Loops through list and prints attributes and such of users
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")
