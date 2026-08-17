#!/usr/bin/env python3
"""KaliCMD Academy — Step 7 Part 2.

Connects the Concepts database to the Kivy app.
Educational use only: run security commands only on systems/labs you own
or are explicitly authorized to test.
"""

import json
import os
import subprocess

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.utils import platform

from tools_data import TOOLS
from concepts_data import CONCEPTS


def copy_text(text):
    try:
        from plyer import clipboard
        clipboard.copy(text)
        return True
    except Exception:
        try:
            import pyperclip
            pyperclip.copy(text)
            return True
        except Exception:
            return False


def popup(title_text, message):
    box = BoxLayout(orientation="vertical", padding=10, spacing=10)
    label = Label(
        text=message, text_size=(None, None),
        halign="left", valign="top"
    )
    box.add_widget(label)
    close = Button(text="OK", size_hint_y=None, height=48)
    box.add_widget(close)
    pop = Popup(title=title_text, content=box, size_hint=(0.88, 0.72))
    close.bind(on_press=pop.dismiss)
    pop.open()


def title(text, size=20):
    return Label(
        text=f"[b]{text}[/b]", markup=True,
        font_size=f"{size}sp", size_hint_y=None, height=48
    )


class Dashboard(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        root.add_widget(title("🎓 KaliCMD Academy", 24))
        root.add_widget(Label(
            text="Learn Linux • Networking • Cybersecurity",
            size_hint_y=None, height=34
        ))

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=8, padding=4, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        items = [
            ("🎓 Learning Path", "learning"),
            ("📚 Concepts", "concepts"),
            ("🛠 Tools", "tools"),
            ("📈 Progress", "progress"),
            ("⭐ Favorites", "favorites"),
        ]
        for text, section in items:
            b = Button(text=text, size_hint_y=None, height=78)
            b.bind(on_press=lambda _, s=section: self.app.open_section(s))
            grid.add_widget(b)

        scroll.add_widget(grid)
        root.add_widget(scroll)
        self.add_widget(root)


class ConceptsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        root = BoxLayout(orientation="vertical", padding=10, spacing=7)
        top = BoxLayout(size_hint_y=None, height=50, spacing=6)
        back = Button(text="‹ Back", size_hint_x=.22)
        back.bind(on_press=lambda *_: setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(title("📚 Concepts", 20))
        root.add_widget(top)

        self.search = TextInput(
            hint_text="Search concepts...",
            multiline=False, size_hint_y=None, height=46
        )
        self.search.bind(text=lambda *_: self.rebuild())
        root.add_widget(self.search)

        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=7, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def rebuild(self):
        self.grid.clear_widgets()
        q = self.search.text.strip().lower()
        concepts = [
            c for c in CONCEPTS
            if not q or q in (
                c["title"] + " " + c["category"] + " " +
                c["what"] + " " + c["why"]
            ).lower()
        ]

        categories = []
        for c in concepts:
            if c["category"] not in categories:
                categories.append(c["category"])

        for category in categories:
            self.grid.add_widget(Label(
                text=f"[b]{category}[/b]",
                markup=True, size_hint_y=None, height=38,
                halign="left"
            ))
            for c in [x for x in concepts if x["category"] == category]:
                b = Button(
                    text=f"{c['title']}\n{c['level']}",
                    size_hint_y=None, height=72
                )
                b.bind(on_press=lambda _, data=c:
                       self.app.open_concept(data))
                self.grid.add_widget(b)

        if not concepts:
            self.grid.add_widget(Label(
                text="No concepts found.",
                size_hint_y=None, height=50
            ))


class ConceptDetail(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        root = BoxLayout(orientation="vertical", padding=10, spacing=7)
        top = BoxLayout(size_hint_y=None, height=50, spacing=6)
        back = Button(text="‹ Concepts", size_hint_x=.25)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "concepts"))
        top.add_widget(back)
        self.heading = title("Concept", 19)
        top.add_widget(self.heading)
        root.add_widget(top)

        self.scroll = ScrollView()
        self.body = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing=10, padding=5
        )
        self.body.bind(minimum_height=self.body.setter("height"))
        self.scroll.add_widget(self.body)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def load(self, c):
        self.body.clear_widgets()
        self.heading.text = f"[b]{c['title']}[/b]"
        self.body.add_widget(Label(
            text=f"[b]{c['title']}[/b]\n{c['category']} • {c['level']}",
            markup=True, size_hint_y=None, height=70,
            text_size=(420, None), halign="left"
        ))
        sections = [
            ("What is it?", c["what"]),
            ("Why does it matter?", c["why"]),
            ("Simple example", c["example"]),
        ]
        for heading_text, text in sections:
            self.body.add_widget(Label(
                text=f"[b]{heading_text}[/b]\n{text}",
                markup=True, size_hint_y=None, height=105,
                text_size=(420, None), halign="left", valign="top"
            ))

        self.body.add_widget(Label(
            text="[b]Related commands[/b]",
            markup=True, size_hint_y=None, height=38
        ))
        for cmd in c.get("related_commands", []):
            row = BoxLayout(size_hint_y=None, height=48, spacing=6)
            row.add_widget(Label(
                text=cmd, size_hint_x=.78, halign="left"
            ))
            b = Button(text="Copy", size_hint_x=.22)
            b.bind(on_press=lambda _, x=cmd: self.copy(x))
            row.add_widget(b)
            self.body.add_widget(row)

        self.body.add_widget(Label(
            text="[b]Quick Quiz[/b]",
            markup=True, size_hint_y=None, height=42
        ))
        for i, q in enumerate(c.get("quiz", []), 1):
            self.add_quiz(i, q)

    def copy(self, text):
        popup(
            "Copied" if copy_text(text) else "Copy failed",
            text if copy_text(text) else f"Copy manually:\n{text}"
        )

    def add_quiz(self, number, q):
        box = BoxLayout(
            orientation="vertical", size_hint_y=None, height=190,
            spacing=5, padding=5
        )
        box.add_widget(Label(
            text=f"{number}. {q['q']}",
            size_hint_y=None, height=48,
            halign="left"
        ))
        for option in q["options"]:
            b = Button(text=option, size_hint_y=None, height=40)
            b.bind(
                on_press=lambda _, selected=option, answer=q["answer"]:
                    self.quiz_result(selected, answer)
            )
            box.add_widget(b)
        self.body.add_widget(box)

    def quiz_result(self, selected, answer):
        if selected == answer:
            self.app.add_xp(25)
            popup("Correct! 🎯", "Great job! +25 XP")
        else:
            popup("Not quite", f"Correct answer: {answer}")


class ToolsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=7)
        top = BoxLayout(size_hint_y=None, height=50, spacing=6)
        back = Button(text="‹ Back", size_hint_x=.22)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(title("🛠 Tools", 20))
        root.add_widget(top)

        self.search = TextInput(
            hint_text="Search tools...",
            multiline=False, size_hint_y=None, height=46
        )
        self.search.bind(text=lambda *_: self.rebuild())
        root.add_widget(self.search)

        self.scroll = ScrollView()
        self.grid = GridLayout(cols=2, spacing=7, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        self.scroll.add_widget(self.grid)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def rebuild(self):
        self.grid.clear_widgets()
        q = self.search.text.strip().lower()
        for t in TOOLS:
            hay = (
                t.get("name", "") + " " + t.get("cat", "") + " " +
                t.get("desc", "")
            ).lower()
            if q and q not in hay:
                continue
            b = Button(
                text=f"{t['name']}\n{t['cat']}",
                size_hint_y=None, height=72
            )
            b.bind(on_press=lambda _, data=t: self.show_tool(data))
            self.grid.add_widget(b)

    def show_tool(self, t):
        lines = [t.get("desc", "")]
        for desc, cmd in t.get("cmds", []):
            lines.append(f"\n{desc}\n$ {cmd}")
        popup(t["name"], "\n".join(lines))


class ProgressScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        top = BoxLayout(size_hint_y=None, height=50)
        back = Button(text="‹ Back", size_hint_x=.22)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(title("📈 Progress", 20))
        root.add_widget(top)
        self.info = Label(
            text="", text_size=(420, None), halign="left",
            valign="top"
        )
        root.add_widget(self.info)
        self.add_widget(root)

    def refresh(self):
        self.info.text = (
            f"[b]KaliCMD Academy Progress[/b]\n\n"
            f"XP: {self.app.xp}\n"
            f"Concept quiz XP: earned by correct answers\n"
            f"Concepts available: {len(CONCEPTS)}\n"
            f"Tools available: {len(TOOLS)}\n\n"
            "Next modules will add learning-path completion, "
            "missions, labs, achievements and streaks."
        )
        self.info.markup = True


class LearningScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        top = BoxLayout(size_hint_y=None, height=50)
        back = Button(text="‹ Back", size_hint_x=.22)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(title("🎓 Learning Path", 20))
        root.add_widget(top)
        scroll = ScrollView()
        box = BoxLayout(orientation="vertical", size_hint_y=None, spacing=7)
        box.bind(minimum_height=box.setter("height"))
        paths = [
            "Linux", "Networking", "Recon", "Web Security",
            "Passwords", "Wireless", "Windows / AD",
            "Vulnerability", "Exploitation", "Forensics",
            "Reverse Engineering",
        ]
        for item in paths:
            b = Button(
                text=item + "\nComing next",
                size_hint_y=None, height=70
            )
            b.bind(on_press=lambda _, x=item:
                   popup(x, "This learning path will be connected in the next build."))
            box.add_widget(b)
        scroll.add_widget(box)
        root.add_widget(scroll)
        self.add_widget(root)


class KaliAcademy(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xp = 0
        self.favs = set()
        self.data_file = os.path.join(self.user_data_dir, "academy.json")
        self.load_state()
        self.sm = ScreenManager()

    def build(self):
        self.sm.add_widget(Dashboard(self, name="dashboard"))
        self.sm.add_widget(ConceptsScreen(self, name="concepts"))
        self.sm.add_widget(ConceptDetail(self, name="concept-detail"))
        self.sm.add_widget(ToolsScreen(self, name="tools"))
        self.sm.add_widget(ProgressScreen(self, name="progress"))
        self.sm.add_widget(LearningScreen(self, name="learning"))
        self.sm.current = "dashboard"
        self.sm.get_screen("concepts").rebuild()
        self.sm.get_screen("tools").rebuild()
        return self.sm

    def open_section(self, section):
        self.sm.current = section
        if section == "concepts":
            self.sm.get_screen("concepts").rebuild()
        elif section == "tools":
            self.sm.get_screen("tools").rebuild()
        elif section == "progress":
            self.sm.get_screen("progress").refresh()

    def open_concept(self, concept):
        self.sm.current = "concept-detail"
        self.sm.get_screen("concept-detail").load(concept)

    def add_xp(self, amount):
        self.xp += amount
        self.save_state()

    def load_state(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.xp = int(data.get("xp", 0))
            self.favs = set(data.get("favorites", []))
        except Exception:
            self.xp = 0
            self.favs = set()

    def save_state(self):
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump({
                    "xp": self.xp,
                    "favorites": sorted(self.favs),
                }, f)
        except Exception:
            pass


if __name__ == "__main__":
    KaliAcademy().run()
    
