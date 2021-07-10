import xml.etree.ElementTree as ET

class mytree:
    def __init__(self,xml_file):
        self.tree = ET.parse(xml_file)
        self.root =  self.tree.getroot()
        self.apple = []
    def val_leaves(self, node):
        children = []
        for child in node:
            children.append(child)
        if len(children) == 0:
            return True
        else:
            return False

    def get_children(self, node):
        children = []
        for child in node:
            children.append(child)
        return children

    def grow_apple(self, node, firstgid, differ):
        if self.val_leaves(node):
            pass
        else:
            children = self.get_children(node)
            
            for child in children:
                if self.val_leaves(child):
                    if child.attrib.__contains__('gid') and int(child.attrib['gid']) >= firstgid:
                        child.attrib['gid'] = str(int(child.attrib['gid']) - differ)
                else:
                    self.grow_apple(child, firstgid, differ)
            
    def get_apple(self, firstgid, differ):
        self.grow_apple(self.root, firstgid, differ)
        
        return self.apple

if __name__ == "__main__":
    file = "Level_Home.tmx"
    mytree = mytree(file)
    
    invaild_gids = [7169, 6657, 6145, 5633, 5121, 4097]
    differ_list = [7169-1025, 6657-2561, 6145-1537, 5633-3073, 5121-2049, 4097-1]
    for index in range(6):
        mytree.get_apple(invaild_gids[index], differ_list[index])

    ET.dump(mytree.tree)

