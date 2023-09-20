import sys
import importlib

# Define the path to the module
path = r'D:\jaw_utils'

# Remove the module from sys.modules if it's already imported
if 'jaw_utils3' in sys.modules:
    del sys.modules['jaw_utils3']

# Add the path to sys.path if it's not already there
if path not in sys.path:
    sys.path.append(path)

# Now you can import the module using importlib
jaw_utils3 = importlib.import_module('jaw_utils3')

# Call the functions from the jaw_utils module
jaw_utils3.createGuides(number=8)


jaw_utils3.build()
jaw_utils3.createJawPin()





    
    
    
    
    
    