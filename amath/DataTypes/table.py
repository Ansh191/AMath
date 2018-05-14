class table:
    def __init__(self, x=None, y=None):
        if x is None:
            x = []
        if y is None:
            y = []

        try:
            self.x = [i for i in x]
        except TypeError:
            raise TypeError("x must be a list, set, tuple, or frozenset")

        try:
            self.y = [i for i in y]
        except TypeError:
            raise TypeError("y must be a list, set, tuple, or frozenset")

    def __repr__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def plot(self, format='b-', **kwargs):
        import matplotlib.pyplot as plt
        agg_filter = kwargs.get("agg_filter")
        alpha = kwargs.get("alpha")
        animated = kwargs.get("animated")
        aa = kwargs.get('antialiased')
        axes = kwargs.get('axes')
        clip_box = kwargs.get('clip_box')
        clip_on = kwargs.get('clip_on')
        clip_path = kwargs.get('clip_path')
        color = kwargs.get('color')
        contains = kwargs.get('contains')
        dash_capstyle = kwargs.get('dash_capstyle')
        dash_joinstyle = kwargs.get('dash_joinstyle')
        dashes = kwargs.get('dashes')
        drawstyle = kwargs.get('drawstyle')
        figure = kwargs.get('figure')
        fillstyle = kwargs.get('fillstyle')
        gid = kwargs.get('gid')
        label = kwargs.get('label')
        linestyle = kwargs.get('linestyle')
        linewidth = kwargs.get('linewidth')
        marker = kwargs.get('marker')
        markeredgecolor = kwargs.get('markeredgecolor')
        markeredgewidth = kwargs.get('markeredgewidth')
        markerfacecolor = kwargs.get('markerfacecolor')
        markerfacecoloralt = kwargs.get('markerfacecoloralt')
        markersize = kwargs.get('markersize')
        markevery = kwargs.get('markevery')
        path_effects = kwargs.get('path_effects')
        picker = kwargs.get('picker')
        pickradius = kwargs.get('pickradius')
        rasterized = kwargs.get('rasterized')
        sketch_params = kwargs.get('sketch_params')
        snap = kwargs.get('snap')
        solid_capstyle = kwargs.get('solid_capstyle')
        solid_joinstyle = kwargs.get('solid_joinstyle')
        transform = kwargs.get('transform')
        url = kwargs.get('url')
        visible = kwargs.get('visible')
        zorder = kwargs.get('zorder')

        plt.plot(self.x, self.y, format)
        #          agg_filter=agg_filter, alpha=alpha, animated=animated, aa=aa, axes=axes,
        #          clip_box=clip_box, clip_on=clip_on, clip_path=clip_path, color=color, contains=contains,
        #          dash_capstyle=dash_capstyle, dash_joinstyle=dash_joinstyle, dashes=dashes, drawstyle=drawstyle,
        #          figure=figure, fillstyle=fillstyle, gid=gid, label=label, linestyle=linestyle, linewidth=linewidth,
        #          marker=marker, markeredgecolor=markeredgecolor, markeredgewidth=markeredgewidth,
        #          markerfacecolor=markerfacecolor, markerfacecoloralt=markerfacecoloralt, markersize=markersize,
        #          markevery=markevery, path_effects=path_effects, picker=picker, pickradius=pickradius,
        #          rasterized=rasterized, sketch_params=sketch_params, snap=snap, solid_capstyle=solid_capstyle,
        #          solid_joinstyle=solid_joinstyle, transform=transform, url=url, visible=visible, zorder=zorder)

        plt.show()
