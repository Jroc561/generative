from p5 import *

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)
    circle_size = random_uniform(low=10, high=80)
    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

def random_list_value(val_list):
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
def random_centered(value_og, offset=5):
    value = random(value_og-offset, value_og+offset)
    return value

def random_gaussian_limit(min_val, max_val):
    new_val = max_val*randomGaussian()+min_val
    if new_val < min_val:
        new_val = min_val
    elif new_val > max_val:
        new_val = max_val
    return new_val

def print_string_stack(string_stack='TESt', w_offset=100, h_offset=100):
    for c in string_stack:
        text(c, w_offset, h_offset)
       
def create_filename(word, num_list=[]):
    filename = word
    for number in num_list:
        filename = filename + '_{:04}'.format(int(number))
    filename = filename + '.png'
    return filename

run()