from tree.models import Category
import json
f = open('output.json')
data = json.load(f)
root_name=data[0]["name"]
print("root:",root_name)


def tree_data():
    get = lambda node_id: Category.objects.get(pk=node_id)
    print(f"get = lambda node_id: Category.objects.get(pk=node_id)")
    root = Category.add_root(name=root_name)
    print(f"root = Category.add_root(name={root_name})")

    for x in data[0]["contents"]:
        if x["type"]=="file":
            print("child1:",x["name"])
            # child_list_l1.append(x["name"])
            child=x["name"]
            get(root.pk).add_child(name=child)
            print(f"get(root.pk).add_child(name={child}))")
            

        if x["type"]=="directory":
            print("node1 of:",root_name,"::",x["name"])
            node=x["name"]
            node1 = get(root.pk).add_child(name=node)
            print(f"node1 = get(root.pk).add_child(name={node})")
            # print(x["name"],"::",x["contents"])
            for y in x["contents"]:
                # print(x["name"],":",y["name"])
                if y["type"]=="file":
                    print("file child2 of:",x["name"],"::",y["name"])
                    c1=y["name"]
                    get(node1.pk).add_child(name=c1)
                    print(f"get(node1.pk).add_child(name={c1})")
                if y["type"]=="directory":
                    n1=y["name"]
                    print("directory node2 of:",x["name"],"::",y["name"])
                    node2 = get(node1.pk).add_child(name=n1)
                    print(f"node2 = get(node1.pk).add_child(name={n1})")

    f.close()
