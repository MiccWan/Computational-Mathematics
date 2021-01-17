import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .complex_int import complex_integrate
from .generate import generate

def generate_animation(gen, sec=2, fps=20, cmap='viridis', edgecolor='none', out=None, out_fps=80):
    frn = sec*fps

    def update_plot(frame_id, plot):
        plot[0].remove()
        plot[0] = ax.plot_surface(*gen(frame_id, frn), cmap=cmap, edgecolor=edgecolor)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plot = [ax.plot_surface(*gen(0, frn), color='0.75', rstride=1, cstride=1)]
    ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(plot,), interval=1000/fps)

    if out:
        ani.save(out, writer='imagemagick', fps=out_fps)
    else:
        plt.show()


if __name__ == '__main__':
    def gen(frame_id, frn):
        return generate(lambda x: np.exp(x + frame_id / frn * np.pi / 2 * 1j), lambda x: np.exp(-x))
    generate_animation(gen)