from lxml import etree

# 创建元素
root = etree.Element('html')
print(type(root))
print(root.tag)

body = etree.Element('body')
root.append(body)

print(etree.tostring(root))

# 创建子元数
sub = etree.SubElement(body, 'child1')
print(type(sub))
sub = etree.SubElement(body, 'child2')

print(etree.tostring(root, pretty_print=True).decode())

