#!/usr/bin/env python3
"""KaliCMD Academy - Step 3 dashboard/navigation foundation."""
import json
import os
import subprocess

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
from lessons.linux_fundamentals import LINUX_FUNDAMENTALS


def copy_text(text):
    if pyperclip:
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            pass
    if plyer_clip:
        try:
            plyer_clip.copy(text)
            return True
        except Exception:
            pass
    return False


def show_msg(title, text):
    box = BoxLayout(orientation="vertical", padding=10, spacing=10)
    box.add_widget(Label(text=text, text_size=(380, None), halign="left", valign="top"))
    close = Button(text="OK", size_hint=(1, None), height=48)
    box.add_widget(close)
    pop = Popup(title=title, content=box, size_hint=(0.85, 0.6))
    close.bind(on_press=pop.dismiss)
    pop.open()


def title(text, size=22):
    return Label(text=f"[b]{text}[/b]", markup=True, font_size=size,
                 size_hint=(1, None), height=52, halign="center", valign="middle")


class Dashboard(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=12, spacing=8)
        root.add_widget(title("🔥 KaliCMD Academy", 24))
        root.add_widget(Label(
            text="[b]Your Cybersecurity Learning Companion[/b]\nLearn • Practice • Understand",
            markup=True, size_hint=(1, None), height=62, halign="center", valign="middle"))
        root.add_widget(Label(
            text=f"[b]Level 1 — Linux Rookie[/b]\nXP: {app.xp} / 1000    •    Tools: {len(TOOLS)}    •    Favorites: {len(app.favs)}",
            markup=True, size_hint=(1, None), height=72, halign="center", valign="middle"))

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=8, size_hint_y=None, padding=2)
        grid.bind(minimum_height=grid.setter("height"))
        items = [
            ("🎓\nLearning Path", "learning"), ("🛠\nTools", "tools"),
            ("📚\nConcepts", "concepts"), ("🧪\nPractice Labs", "labs"),
            ("🎯\nMissions", "missions"), ("📋\nCheat Sheets", "cheats"),
            ("⭐\nFavorites", "favorites"), ("📈\nProgress", "progress"),
            ("🤖\nAI Tutor", "ai"),
        ]
        for text, section in items:
            b = Button(text=text, size_hint_y=None, height=88, font_size="14sp")
            b.bind(on_press=lambda _b, s=section: app.open_section(s))
            grid.add_widget(b)
        scroll.add_widget(grid)
        root.add_widget(scroll)
        self.add_widget(root)


class Section(Screen):
    DATA = {
        "learning": ("🎓 Learning Path", ["Linux Fundamentals", "Networking", "Recon / OSINT", "Web Security", "Password & Authentication", "Wireless Security", "Windows / Active Directory", "Vulnerability Assessment", "Security Testing", "Digital Forensics", "Reverse Engineering"]),
        "concepts": ("📚 Concepts", ["Linux", "Networking", "Web Fundamentals", "Cryptography", "Security Fundamentals", "Programming"]),
        "labs": ("🧪 Practice Labs", ["Beginner Labs", "Intermediate Labs", "Advanced Labs"]),
        "missions": ("🎯 Missions", ["Daily Mission", "Learning Mission", "Challenge Mission"]),
        "cheats": ("📋 Cheat Sheets", ["Linux Commands", "Networking Commands", "Web Security Commands", "Security Reference"]),
        "progress": ("📈 Progress", ["XP & Levels", "Completed Lessons", "Missions", "Badges", "Learning Streak"]),
        "ai": ("🤖 AI Tutor", ["Explain a concept", "Explain a command", "Get a hint", "Recommend next lesson"]),
    }
    def __init__(self, app, section, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.section = section
        heading, items = self.DATA[section]
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        top = BoxLayout(size_hint=(1, None), height=52, spacing=8)
        back = Button(text="‹ Back", size_hint=(0.25, 1))
        back.bind(on_press=lambda *_: setattr(app.sm, "current", "dashboard"))
        top.add_widget(back); top.add_widget(title(heading, 19)); root.add_widget(top)
        intro = {
            "learning": "A structured path from Linux fundamentals to advanced cybersecurity topics.",
            "concepts": "Learn the concepts behind the tools instead of memorizing commands.",
            "labs": "Practice only in your own systems, CTFs, or intentionally vulnerable training environments.",
            "missions": "Short objectives that turn lessons into practical learning.",
            "cheats": "Quick command and security references.",
            "progress": "Track XP, lessons, missions, badges, and streaks.",
            "ai": "The AI Tutor module will later provide explanations, hints, and recommendations.",
        }[section]
        root.add_widget(Label(text=intro, size_hint=(1, None), height=64, text_size=(420, None), halign="left", valign="top"))
        scroll = ScrollView(); body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=8, padding=4); body.bind(minimum_height=body.setter("height"))
        for item in items:
            b = Button(text=item, size_hint_y=None, height=62)
            b.bind(on_press=lambda _b, name=item: self.select_item(name))
            body.add_widget(b)
        scroll.add_widget(body); root.add_widget(scroll); self.add_widget(root)

    def select_item(self, name):
        if self.section == "learning" and name == "Linux Fundamentals":
            self.app.open_linux_track()
        else:
            show_msg(
                name,
                "This module will be built next.\n\n"
                "Linux Fundamentals is the first connected learning track.",
            )


class LinuxTrack(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)

        top = BoxLayout(size_hint=(1, None), height=50, spacing=6)
        back = Button(text="‹ Back", size_hint=(0.22, 1))
        back.bind(on_press=lambda *_: setattr(app.sm, "current", "learning"))
        top.add_widget(back)
        top.add_widget(title("🐧 Linux Fundamentals", 19))
        root.add_widget(top)

        root.add_widget(Label(
            text=LINUX_FUNDAMENTALS["description"],
            size_hint=(1, None), height=82,
            text_size=(420, None), halign="left", valign="top"
        ))

        scroll = ScrollView()
        body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=8, padding=4)
        body.bind(minimum_height=body.setter("height"))

        for i, lesson in enumerate(LINUX_FUNDAMENTALS["lessons"], 1):
            b = Button(
                text=f"{i}. {lesson['title']}\\n{lesson['difficulty']}",
                size_hint_y=None, height=76
            )
            b.bind(on_press=lambda _b, data=lesson: app.open_linux_lesson(data))
            body.add_widget(b)

        scroll.add_widget(body)
        root.add_widget(scroll)
        self.add_widget(root)


class LinuxLesson(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=6)

        top = BoxLayout(size_hint=(1, None), height=50, spacing=6)
        back = Button(text="‹ Lessons", size_hint=(0.25, 1))
        back.bind(on_press=lambda *_: setattr(app.sm, "current", "linux-track"))
        self.lesson_title = title("Linux Fundamentals", 17)
        top.add_widget(back)
        top.add_widget(self.lesson_title)
        root.add_widget(top)

        self.scroll = ScrollView()
        self.body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=8, padding=4)
        self.body.bind(minimum_height=self.body.setter("height"))
        self.scroll.add_widget(self.body)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def load(self, lesson):
        self.lesson = lesson
        self.lesson_title.text = f"[b]{lesson['title']}[/b]"
        self.body.clear_widgets()

        self.body.add_widget(Label(
            text=f"[b]{lesson['title']}[/b]\\nDifficulty: {lesson['difficulty']}\\n\\n{lesson['objective']}",
            markup=True, size_hint_y=None, height=105,
            text_size=(420, None), halign="left", valign="top"
        ))

        self.body.add_widget(Label(
            text="[b]Concepts[/b]\\n• " + "\\n• ".join(lesson["concepts"]),
            markup=True, size_hint_y=None, height=125,
            text_size=(420, None), halign="left", valign="top"
        ))

        self.body.add_widget(Label(
            text="[b]Commands[/b]", markup=True,
            size_hint_y=None, height=36, halign="left"
        ))

        for item in lesson["commands"]:
            card = BoxLayout(orientation="vertical", size_hint_y=None, height=145, padding=6, spacing=3)
            card.add_widget(Label(
                text=f"[b]{item['name']}[/b]", markup=True,
                size_hint_y=None, height=28, halign="left"
            ))
            card.add_widget(Label(
                text=item["command"], size_hint_y=None, height=40,
                color=(0.6, 0.9, 0.6, 1),
                text_size=(420, None), halign="left", valign="middle"
            ))
            card.add_widget(Label(
                text=item["explanation"], size_hint_y=None, height=44,
                text_size=(420, None), halign="left", valign="top"
            ))
            copy_btn = Button(text="📋 Copy", size_hint_y=None, height=36)
            copy_btn.bind(on_press=lambda _b, c=item["command"]: self.copy_command(c))
            card.add_widget(copy_btn)
            self.body.add_widget(card)

        self.body.add_widget(Label(
            text="[b]Practice[/b]\\n• " + "\\n• ".join(lesson["practice"]),
            markup=True, size_hint_y=None,
            height=max(110, 34 * len(lesson["practice"])),
            text_size=(420, None), halign="left", valign="top"
        ))

        complete = Button(text="✓ Mark Lesson Complete", size_hint_y=None, height=52)
        complete.bind(on_press=lambda *_: self.complete())
        self.body.add_widget(complete)

    def copy_command(self, command):
        if copy_text(command):
            show_msg("Copied", command)
        else:
            show_msg("Copy failed", "Copy manually:\\n\\n" + command)

    def complete(self):
        lesson_id = self.lesson["id"]
        if lesson_id not in self.app.completed_lessons:
            self.app.completed_lessons.add(lesson_id)
            self.app.xp += 100
            self.app.save_data()
        show_msg("Lesson Complete", f"✓ {self.lesson['title']}\\n\\n+100 XP")




class Tools(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs); self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        top = BoxLayout(size_hint=(1, None), height=50, spacing=6)
        back = Button(text="‹ Back", size_hint=(0.22, 1)); back.bind(on_press=lambda *_: setattr(app.sm, "current", "dashboard"))
        top.add_widget(back); top.add_widget(title("🛠 Tools", 20)); root.add_widget(top)
        self.search = TextInput(hint_text="Search tools, descriptions, commands...", multiline=False, size_hint=(1, None), height=46)
        self.search.bind(text=self.search_tools); root.add_widget(self.search)
        row = BoxLayout(size_hint=(1, None), height=48, spacing=6)
        allb = Button(text="All Tools"); favb = Button(text="Favorites")
        allb.bind(on_press=lambda *_: self.rebuild()); favb.bind(on_press=lambda *_: self.rebuild([t for t in TOOLS if t["name"] in app.favs]))
        row.add_widget(allb); row.add_widget(favb); root.add_widget(row)
        self.scroll = ScrollView(); self.grid = GridLayout(cols=2, spacing=8, size_hint_y=None); self.grid.bind(minimum_height=self.grid.setter("height")); self.scroll.add_widget(self.grid); root.add_widget(self.scroll)
        self.add_widget(root); self.rebuild()
    def rebuild(self, tools=None):
        self.grid.clear_widgets(); tools = TOOLS if tools is None else tools
        for t in tools:
            b = Button(text=f'{t["name"]}\n{t["cat"]}', size_hint_y=None, height=78, font_size="12sp")
            b.bind(on_press=lambda _b, tool=t: self.app.open_tool(tool)); self.grid.add_widget(b)
    def search_tools(self, _i, text):
        q = text.strip().lower()
        if not q: self.rebuild(); return
        hits = [t for t in TOOLS if q in (t["name"] + " " + t["cat"] + " " + t["desc"] + " " + " ".join(c for _, c in t["cmds"])).lower()]
        self.rebuild(hits)


class Tool(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs); self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=6)
        top = BoxLayout(size_hint=(1, None), height=48, spacing=6)
        back = Button(text="< Back", size_hint=(0.25, 1)); back.bind(on_press=lambda *_: setattr(app.sm, "current", "tools"))
        self.tool_title = Label(text="", markup=True, size_hint=(0.5, 1), font_size="15sp")
        self.fav = Button(text="☆", size_hint=(0.25, 1)); self.fav.bind(on_press=lambda *_: self.toggle_fav())
        top.add_widget(back); top.add_widget(self.tool_title); top.add_widget(self.fav); root.add_widget(top)
        self.scroll = ScrollView(); self.body = BoxLayout(orientation="vertical", size_hint_y=None, spacing=8); self.body.bind(minimum_height=self.body.setter("height")); self.scroll.add_widget(self.body); root.add_widget(self.scroll); self.add_widget(root)
    def load(self, t):
        self.tool = t; self.tool_title.text = f'[b]{t["name"]}[/b]'; self.fav.text = "★" if t["name"] in self.app.favs else "☆"; self.body.clear_widgets()
        self.body.add_widget(Label(text=t["desc"], size_hint_y=None, height=100, text_size=(420, None), halign="left", valign="top"))
        for i, (desc, cmd) in enumerate(t["cmds"], 1):
            card = BoxLayout(orientation="vertical", size_hint_y=None, height=132, padding=6)
            card.add_widget(Label(text=f"{i}. {desc}", size_hint_y=None, height=28, halign="left"))
            card.add_widget(Label(text=cmd, size_hint_y=None, height=54, text_size=(420, None), halign="left", valign="top"))
            row = BoxLayout(size_hint_y=None, height=42, spacing=6)
            cp = Button(text="Copy"); run = Button(text="Run")
            cp.bind(on_press=lambda _b, c=cmd: self.copy(c)); run.bind(on_press=lambda _b, c=cmd: self.run(c))
            row.add_widget(cp); row.add_widget(run); card.add_widget(row); self.body.add_widget(card)
    def toggle_fav(self): self.app.toggle_fav(self.tool["name"]); self.fav.text = "★" if self.tool["name"] in self.app.favs else "☆"
    def copy(self, cmd):
        ok = copy_text(cmd)
        show_msg("Copied" if ok else "Copy failed", cmd if ok else "Copy manually:\n" + cmd)
    def run(self, cmd):
        if platform == "android":
            show_msg("Sandboxed on Android", "The app cannot run system commands directly.\n\nCopy the command and use it in your authorized Termux/Kali lab:\n\n" + cmd); return
        try:
            r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60); show_msg("Output", (r.stdout + r.stderr)[-1500:] or "[no output]")
        except Exception as e: show_msg("Error", str(e))


class KaliApp(App):
    def build(self):
        self.fav_file = os.path.join(self.user_data_dir, "user_data.json")
        self.favs, self.xp = set(), 0
        self.completed_lessons = set()
        self.load_data()
        self.sm = ScreenManager()
        self.sm.add_widget(Dashboard(self, name="dashboard")); self.sm.add_widget(Tools(self, name="tools")); self.sm.add_widget(Tool(self, name="tool"))
        for s in ["learning", "concepts", "labs", "missions", "cheats", "progress", "ai"]:
            self.sm.add_widget(Section(self, s, name=s))
        self.sm.add_widget(LinuxTrack(self, name="linux-track"))
        self.sm.add_widget(LinuxLesson(self, name="linux-lesson"))
        return self.sm
    def load_data(self):
        try:
            with open(self.fav_file, encoding="utf-8") as f:
                d = json.load(f)
                self.favs = set(d.get("favorites", []))
                self.xp = int(d.get("xp", 0))
                self.completed_lessons = set(d.get("completed_lessons", []))
        except Exception: pass
    def save_data(self):
        try:
            os.makedirs(self.user_data_dir, exist_ok=True)
            with open(self.fav_file, "w", encoding="utf-8") as f:
                json.dump({"favorites": sorted(self.favs), "xp": self.xp, "completed_lessons": sorted(self.completed_lessons)}, f)
        except Exception: pass
    def toggle_fav(self, name):
        self.favs.discard(name) if name in self.favs else self.favs.add(name); self.save_data()
    def open_tool(self, t): self.sm.current = "tool"; self.sm.get_screen("tool").load(t)
    def open_linux_track(self):
        self.sm.current = "linux-track"
    def open_linux_lesson(self, lesson):
        self.sm.current = "linux-lesson"
        self.sm.get_screen("linux-lesson").load(lesson)
    def open_section(self, section):
        if section == "tools":
            self.sm.current = "tools"
        elif section == "favorites":
            self.sm.current = "tools"
            self.sm.get_screen("tools").search.text = ""
            self.sm.get_screen("tools").rebuild([t for t in TOOLS if t["name"] in self.favs])
        else:
            self.sm.current = section

if __name__ == "__main__":
    KaliApp().run()
