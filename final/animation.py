import numpy as np
from lib.generate import generate

# ###########################################################################
#  func animation
# ###########################################################################

from lib.func_animation import generate_animation

def gen(frame_id, frn):
    return generate(lambda x: np.exp(x + frame_id / frn * np.pi / 2 * 1j), lambda x: np.exp(-x), du=1.5, dv=np.pi, step=0.2)

generate_animation(gen, out='out.gif', out_fps=20)

# ###########################################################################
#  rotate animation
# ###########################################################################

# from lib.rotate_animation import generate_animation

# def gen():
#     return generate(lambda z: 1j * np.exp(z), lambda x: np.exp(-x), du=1.5, dv=np.pi, step=0.2)

# generate_animation(gen, sec=2, fps=120)