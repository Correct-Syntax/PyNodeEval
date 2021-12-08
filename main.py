

from nodes import ImageNode, MixNode, OutputNode
from renderer import Renderer


# Init renderer
renderer = Renderer(None)

# Init nodes with ids
img_nd1 = ImageNode(1)
img_nd2 = ImageNode(2)
mix_nd = MixNode(3)
output_nd = OutputNode(4)

# Create a dict of nodes which the renderer accepts
nodes = {
    "img_nd1": img_nd1, 
    "img_nd2": img_nd2, 
    "mix_nd": mix_nd, 
    "output_nd": output_nd
}

# Edit the values (properties) and connections (parameters) of the nodes
img_nd1.EditProperty("file_path", "./test1.jpg")
img_nd2.EditProperty("file_path", "./test2.jpg")
mix_nd.EditParameter("image_1", img_nd1)
mix_nd.EditParameter("image_2", img_nd2)
output_nd.EditParameter("image", mix_nd)


# Render 1

mix_nd._dirty_flag = True
mix_nd.EditProperty("blend_mode", 1)

print("Render result 1: ", renderer.Render(nodes))


# Render 2

mix_nd._dirty_flag = True
mix_nd.EditProperty("blend_mode", 10)

print("Render result 2: ", renderer.Render(nodes))


# Render 3

mix_nd._dirty_flag = True
mix_nd.EditProperty("blend_mode", 1)

print("Render result 3: ", renderer.Render(nodes))
