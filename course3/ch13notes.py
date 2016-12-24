import xml.etree.ElementTree as ET

# XML = extensible markup language
data = '''
<people>
    <person>
        <name>Chuck</name>
        <phone type="intl">303 4456</phone>
        <email hide="yes"/> #Self closing tag
    </person>
    <person>
        <name>Noah</name>
        <phone>622 7421</phone>
    </person>
</people>
'''

# Deserialization/Parsing/Making into an object
tree = ET.fromstring(data)
# Calling methods on item from above
print 'Name:', tree.find('name').text
# Calling methods to get the value of hide
print 'Attr:', tree.find('email').get('hide')
