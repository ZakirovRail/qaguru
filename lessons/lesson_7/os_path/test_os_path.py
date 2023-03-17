import os

os.path.abspath(__file__)
print(os.path.abspath(__file__))

os.path.dirname(__file__)
print(os.path.dirname(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

current_dir = os.path.dirname(os.path.abspath(__file__))

resources = os.path.join(current_dir, "resources")
print(resources)

resources = os.path.join(current_dir, "..", "resources")
print(os.path.abspath(resources))
