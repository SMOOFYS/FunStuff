# import all of the code from wizardlib.py
from wizardlib import *
# Store add image function to a variable "dog_image"
dog_image = add_image("dog-1.jpg", 100)
# add position to dog_image via position_element(variable, x, y)
position_element(dog_image, 400, 100)
# rotating images via rotate_element(variable, degrees)