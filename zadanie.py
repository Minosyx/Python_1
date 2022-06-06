from gi.repository import Gtk
from p10 import stolica as c


class Okno:
    def __init__(self):
        self.o = Gtk.Window()
        self.o.resize(400, 400)
        self.tv = Gtk.TextView()
        self.tb = Gtk.TextBuffer()
        self.en = Gtk.Entry()
        self.b1 = Gtk.Button('OK')
        self.b2 = Gtk.Button('Cancel')
        self.box = Gtk.VBox()
        self.v1 = Gtk.VBox()
        self.v2 = Gtk.VBox()
        self.h1 = Gtk.HBox()
        self.tv.set_buffer(self.tb)
        self.tv.set_editable(False)
        self.tx = ''
        self.v1.pack_start(self.tv, True, True, 0)
        self.h1.pack_start(self.en, True, True, 0)
        self.h1.pack_start(self.b1, False, False, 0)
        self.h1.pack_start(self.b2, False, False, 0)
        self.v2.pack_start(self.h1, False, False, 0)
        self.box.pack_start(self.v1, True, True, 0)
        self.box.pack_start(self.v2, False, False, 0)
        self.o.add(self.box)
        self.o.show_all()
        self.en.grab_focus()

        self.o.connect('delete-event', self.de)
        #self.b1.connect('button-press-event', lambda *args: print("OK"))
        #self.b2.connect('button-press-event', lambda *args: print("Cancel"))
        self.b1.connect('button-press-event', self.bpe)
        self.b2.connect('button-press-event', self.bpe)
        self.b1.connect('button-release-event', self.bre)
        self.b2.connect('button-release-event', self.bre)
        self.o.connect('configure-event', self.ce)
        self.o.connect('key-press-event', self.kpe)
        self.o.connect('key-release-event', lambda *args: print("Puszczono"))

    def bpe(self, b, e):
        if b == self.b1:
            x = c(self.en.get_text())
            self.tx += x + '\n'
            self.tb.set_text(f"{self.tx}")
        self.en.set_text("")

    def bre(self, *args):
        self.en.grab_focus()

    def de(*args):
        Gtk.main_quit()
        return 1  # blokuje zachowanie domyślne

    def ce(*args):
        args[0].o.set_title(f"{args[2].x} {args[2].y} {args[2].height} {args[2].width}")
        print(args[2].x, args[2].y, args[2].height, args[2].width)

    def kpe(self, o, k):
        if k.keyval == 65421:
            self.bpe(self.b1, 0)
        elif k.keyval == 65307:
            self.bpe(self.b2, 0)



ok = Okno()
Gtk.main()


# Gtk.Entry -> set_text, get_text, grab_focus
# Gtk.TextView -> set_editable, set_buffer(Gtk.TextBuffer)
# Gtk.TextBuffer -> set_text
# enter = ok, cancel = escape, mozna przez lambde
