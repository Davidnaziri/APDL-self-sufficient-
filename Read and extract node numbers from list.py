# Read and extract node numbers from the uploaded file
node_list = []

with open("/mnt/data/list of nodes which should have zero displacement in all three dimentions.txt", "r") as file:
    for line in file:
        stripped = line.strip()
        if stripped and stripped[0].isdigit():
            node = stripped.split()[0]
            if node.isdigit():
                node_list.append(int(node))

print(node_list)
