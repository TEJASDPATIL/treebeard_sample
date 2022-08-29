from tree.models import Category
import json
f = open('output.json')
data = json.load(f)
root_name=data[0]["name"]
print("root:",root_name)


def tree_data():
    get = lambda node_id: Category.objects.get(pk=node_id)
    root = Category.add_root(name=root_name)
    for x in data[0]["contents"]:
        if x["type"]=="file":
            child=x["name"]
            get(root.pk).add_child(name=child)
            

        if x["type"]=="directory":
            node=x["name"]
            node1 = get(root.pk).add_child(name=node)
            
            for y in x["contents"]:

                if y["type"]=="file":
                    c1=y["name"]
                    get(node1.pk).add_child(name=c1)
        
                if y["type"]=="directory":
                    n1=y["name"]
                    node2 = get(node1.pk).add_child(name=n1)
                    
    f.close()
