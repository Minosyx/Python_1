from gi.repository import Gtk


class Okno:
    def __init__(self):
        self.o = Gtk.Window()
        self.o.resize(400, 400)
        self.b1 = Gtk.Button("Hide")
        self.o.connect('delete-event', lambda *args: Gtk.main_quit())
        self.b1.connect('button-press-event', lambda *args: self.o.set_opacity(0))
        self.b1.connect('button-release-event', lambda *args: self.o.set_opacity(1))
        self.o.add(self.b1)
        self.o.show_all()


ok = Okno()
Gtk.main()
