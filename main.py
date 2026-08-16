#!/usr/bin/env python3
"""KaliCMD Toolkit — Kivy/Android edition"""
import json, os, subprocess
from kivy.app import App
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

try:
    import pyperclip
except ImportError:
    pyperclip = None
try:
    from plyer import clipboard as plyer_clip
except ImportError:
    plyer_clip = None

from tools_data import TOOLS

CATS = []
for t in TOOLS:
    if t["cat"] not in CATS:
        CATS.append(t["cat"])

def copy_text(text):
    if pyperclip:
        try:
            pyperclip.copy(text); return True
        except Exception: pass
    if plyer_clip:
        try:
            plyer_clip.copy(text); return True
        except Exception: pass
    return False

def show_msg(title, text):
    box = BoxLayout(orientation="vertical", padding=10, spacing=10)
    lb = Label(text=text, text_size=(380, None), halign="left", valign="top")
    box.add_widget(lb)
    close = Button(text="OK", size_hint=(1, None), height=48)
    box.add_widget(close)
    pop = Popup(title=title, content=box, size_hint=(0.85, 0.6))
    close.bind(on_press=pop.dismiss)
    pop.open()

class HomeScreen(Screen):
    def __init__(self, app, **kw):
        super().__init__(**kw)
        self.app = app
        root = BoxLayout(orientation="vertical", spacing=8, padding=10)
        root.add_widget(Label(text="[b]KaliCMD Toolkit[/b]", markup=True,
                              size_hint=(1, None), height=44, font_size=22))
        self.search = TextInput(hint_text="Search tools, commands...", multiline=False,
                                size_hint=(1, None), height=44)
        self.search.bind(text=self.on_search)
        root.add_widget(self.search)
        btn_row = BoxLayout(size_hint=(1, None), height=48, spacing=6)
        b_all = Button(text="All Tools")
        b_fav = Button(text="Favorites")
        b_all.bind(on_press=lambda *a: self.show_list("all"))
        b_fav.bind(on_press=lambda *a: self.show_list("fav"))
        btn_row.add_widget(b_all); btn_row.add_widget(b_fav)
        root.add_widget(btn_row)
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=2, spacing=8, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        root.add_widget(self.scroll)
        self.add_widget(root)
        self.rebuild()

    def rebuild(self, tools=None):
        self.grid.clear_widgets()
        tools = tools if tools is not None else TOOLS
        for t in tools:
            b = Button(text="%s\n%s" % (t["name"], t["cat"]),
                       size_hint_y=None, height=74,
                       halign="center", valign="middle", font_size="12sp")
            b.bind(on_press=lambda *a, tt=t: self.app.open_tool(tt))
            self.grid.add_widget(b)

    def on_search(self, inst, text):
        q = text.strip().lower()
        if not q:
            self.rebuild(); return
        hits = []
        for t in TOOLS:
            hay = (t["name"] + " " + t["desc"] + " " +
                   " ".join(c for _, c in t["cmds"])).lower()
            if q in hay:
                hits.append(t)
        self.rebuild(hits)

    def show_list(self, kind):
        self.search.text = ""
        if kind == "fav":
            self.rebuild([t for t in TOOLS if t["name"] in self.app.favs])
        else:
            self.rebuild()

class ToolScreen(Screen):
    def __init__(self, app, **kw):
        super().__init__(**kw)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=6)
        top = BoxLayout(size_hint=(1, None), height=48, spacing=6)
        back = Button(text="< Back", size_hint=(0.25, 1))
        back.bind(on_press=lambda *a: setattr(self.app.sm, "current", "home"))
        self.title = Label(text="", markup=True, size_hint=(0.5, 1), font_size="15sp")
        self.fav_btn = Button(text="☆", size_hint=(0.25, 1))
        self.fav_btn.bind(on_press=lambda *a: self.toggle_fav())
        top.add_widget(back); top.add_widget(self.title); top.add_widget(self.fav_btn)
        root.add_widget(top)
        self.scroll = ScrollView()
        self.body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=8)
        self.body.bind(minimum_height=self.body.setter("height"))
        self.scroll.add_widget(self.body)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def load(self, t):
        self.tool = t
        self.title.text = "[b]%s[/b]" % t["name"]
        self.fav_btn.text = "★" if t["name"] in self.app.favs else "☆"
        self.body.clear_widgets()
        self.body.add_widget(Label(text=t["desc"], size_hint_y=None, height=90,
                                   text_size=(420, None), halign="left", valign="top"))
        for i, (desc, cmd) in enumerate(t["cmds"], 1):
            card = BoxLayout(orientation="vertical", size_hint_y=None, height=130, padding=6)
            card.add_widget(Label(text="%d. %s" % (i, desc), size_hint_y=None, height=28,
                                  halign="left"))
            card.add_widget(Label(text=cmd, size_hint_y=None, height=52, color=(0.6, 0.9, 0.6, 1),
                                  text_size=(420, None), halign="left", valign="top"))
            row = BoxLayout(size_hint_y=None, height=42, spacing=6)
            b_copy = Button(text="Copy"); b_run = Button(text="Run")
            b_copy.bind(on_press=lambda *a, c=cmd: self.do_copy(c))
            b_run.bind(on_press=lambda *a, c=cmd: self.do_run(c))
            row.add_widget(b_copy); row.add_widget(b_run)
            card.add_widget(row)
            self.body.add_widget(card)

    def toggle_fav(self):
        self.app.toggle_fav(self.tool["name"])
        self.fav_btn.text = "★" if self.tool["name"] in self.app.favs else "☆"

    def do_copy(self, cmd):
        if copy_text(cmd):
            show_msg("Copied to clipboard", cmd)
        else:
            show_msg("Copy failed", "Copy manually:\n" + cmd)

    def do_run(self, cmd):
        if platform == "android":
            show_msg("Sandboxed on Android",
                     "The app can't run system commands directly (Android sandbox).\n\n"
                     "Tap Copy, then paste into Termux and run there:\n\n" + cmd)
            return
        try:
            out = subprocess.run(cmd, shell=True, capture_output=True,
                                 text=True, timeout=60)
            show_msg("Output", (out.stdout + out.stderr)[-1500:] or "[no output]")
        except Exception as e:
            show_msg("Error", str(e))

class KaliApp(App):
    def build(self):
        self.fav_file = os.path.join(self.user_data_dir, "favs.json")
        try:
            self.favs = set(json.load(open(self.fav_file)))
        except Exception:
            self.favs = set()
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(self))
        self.sm.add_widget(ToolScreen(self))
        return self.sm

    def open_tool(self, t):
        self.sm.current = "tool"
        self.sm.get_screen("tool").load(t)

    def toggle_fav(self, name):
        if name in self.favs:
            self.favs.discard(name)
        else:
            self.favs.add(name)
        try:
            json.dump(sorted(self.favs), open(self.fav_file, "w"))
        except Exception:
            pass

if __name__ == "__main__":
    KaliApp().run()