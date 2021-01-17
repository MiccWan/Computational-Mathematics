import matplotlib.pyplot as plt

def basic_plot(x, y, z, cmap='viridis', edgecolor='none'):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("auto")
    ax.plot_surface(x, y, z, cmap=cmap, edgecolor=edgecolor)
    plt.show()
