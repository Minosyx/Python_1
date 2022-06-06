from gi.repository import Gtk


class Okno:
    def __init__(self):
        self.o = Gtk.Window()
        self.o.move(500, 500)  # self.o.get_position()
        self.o.resize(400, 300)  # self.o.get_size()
        self.o.set_title("Hello")  # self.o.get_title()
        self.o.set_opacity(.75)  # self.o.get_opacity()
        self.b1 = Gtk.Button("OK")
        self.b2 = Gtk.Button("Cancel")
        self.e = Gtk.Entry()
        self.tv = Gtk.TextView()
        self.hb = Gtk.HBox()
        self.hb.pack_start(self.b1, False, False, 10)  # expand, fill, padding
        self.hb.pack_start(self.b2, True, True, 0)
        self.hb.pack_start(self.e, True, True, 0)
        self.hb.pack_start(self.tv, True, True, 0)
        self.o.add(self.hb)
        self.o.show_all()


ok = Okno()
Gtk.main()
