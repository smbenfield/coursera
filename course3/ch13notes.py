import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

# Creates object
tree = ET.fromstring(data)
# Calls method find on object to retrieve text
print 'Name:',tree.find('name').text
# Calls find and get to retrieve status of hide
print 'Attr:',tree.find('email').get('hide')
