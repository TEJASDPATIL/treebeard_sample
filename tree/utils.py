from tree.models import Category
import json

get = lambda node_id: Category.objects.get(pk=node_id)
def read_file():
    with open('output.json') as f:
        data = json.load(f)
    return data

def tree_data():
    data = read_file()
    # root_name=data[0]["name"]
    # root = Category.add_root(name=root_name)
    tree_data_recursive(data, None)
    

def tree_data_recursive(obj, root):
    for x in obj:
        if x["type"] == "report":
            return
        if root is None:
            new_root = Category.add_root(name=x["name"])
        else:

            new_root = get(root.pk).add_child(name=x["name"])
        if x["type"] == "directory":
            if x.get("contents"):
                tree_data_recursive(x["contents"], new_root)

if __name__ == "__main__":
    tree_data()

