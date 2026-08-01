import trimesh

# 1. Create a cube with custom width, height, depth
width  = 2.0
height = 1.0
depth  = 2.0
mesh = trimesh.creation.box(extents=[width, height, depth])

# 2. Set colour (R, G, B, Alpha)
mesh.visual.face_colors = [100, 100, 200, 255]

# 3. Print basic properties
print("Vertices:", mesh.vertices.shape)
print("Faces:", mesh.faces.shape)
print("Volume:", mesh.volume)
print("Bounding box size:", mesh.bounding_box.extents)

# 4. Check if the mesh is watertight
print("Is watertight?", mesh.is_watertight)

# 5. Visualize the mesh
mesh.show()