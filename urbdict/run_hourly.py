import urllib
from lxml import etree

page = urllib.urlopen('http://www.urbandictionary.com/random.php?')
# print page.geturl()
content = page.read()
parser = etree.XMLParser(recover=True)
tree = etree.fromstring(content, parser=parser)

word = tree.xpath("//a[@class='word']")[0].text
node = tree.xpath("//div[@class='meaning']")[0]
meaning_str = ' '.join(node.itertext())

print word.strip()
print
print 'Definition: ',meaning_str.strip()