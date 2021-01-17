import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from .complex_int import complex_integrate
from .generate import generate

def generate_animation(gen, sec=2, fps=20, angle=360, cmap='viridis', edgecolor='none'):
    apf = angle / (sec * fps)

    fig = plt.figure()
    ax = Axes3D(fig)

    def init_plot():
        ax.plot_surface(*gen(), color='0.75', rstride=1, cstride=1, cmap=cmap, edgecolor=edgecolor)
        return fig,
    # init_plot()
    def update_plot(frame_id):
        ax.view_init(elev=30, azim=apf*frame_id)
        return fig,

    ani = animation.FuncAnimation(fig, update_plot, frames=sec*fps, init_func=init_plot, interval=1000/fps)

    ani.save('out.gif', writer='imagemagick', fps=fps)

    plt.show()


if __name__ == '__main__':
    def gen(frame_id, frn):
        return generate(lambda x: np.exp(x + frame_id / frn * np.pi / 2 * 1j), lambda x: np.exp(-x))
    generate_animation(gen)