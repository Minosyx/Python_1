from gi.repository import Gtk, Gdk


class Okno:
    def __init__(self):
        self.o = Gtk.Window()
        self.o.move(200, 200)
        self.o.resize(400, 400)
        self.o.connect('delete-event', self.de)
        self.o.connect('key-press-event', self.kpe)
        self.o.show_all()

    def de(*args):
        Gtk.main_quit()
        return 1

    def kpe(self, o, k):
        position = list(self.o.get_position())
        size = list(self.o.get_size())
        shift = (k.state & Gdk.ModifierType.SHIFT_MASK)
        if shift:
            if k.keyval == 65361:
                size[0] -= 10
            elif k.keyval == 65363:
                size[0] += 10
            elif k.keyval == 65362:
                size[1] -= 10
            elif k.keyval == 65364:
                size[1] += 10
        else:
            if k.keyval == 65361:
                position[0] -= 10
            elif k.keyval == 65363:
                position[0] += 10
            elif k.keyval == 65362:
                position[1] -= 10
            elif k.keyval == 65364:
                position[1] += 10
        self.o.move(*position)
        self.o.resize(*size)


ok = Okno()
Gtk.main()
