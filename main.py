#!/usr/bin/env python3
"""KaliCMD Academy — Step 8 Part 2.

Adds Practice Labs to the Academy UI.
Use labs only on your own device, local training VMs, CTFs, or systems
where you have explicit authorization.
"""

import json
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from tools_data import TOOLS
from concepts_data import CONCEPTS
from labs_data import LABS
from missions_data import MISSIONS


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


def make_title(text, size=20):
    return Label(
        text=f"[b]{text}[/b]", markup=True,
        font_size=f"{size}sp", size_hint_y=None, height=48
    )


class Dashboard(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        root = BoxLayout(orientation="vertical", padding=10, spacing=8)
        root.add_widget(make_title("🎓 KaliCMD Academy", 24))
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
            ("🧪 Practice Labs", "labs"),
            ("🎯 Missions", "missions"),
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
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(make_title("📚 Concepts", 20))
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
        self.heading = make_title("Concept", 19)
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
        for heading_text, text in [
            ("What is it?", c["what"]),
            ("Why does it matter?", c["why"]),
            ("Simple example", c["example"]),
        ]:
            self.body.add_widget(Label(
                text=f"[b]{heading_text}[/b]\n{text}",
                markup=True, size_hint_y=None, height=105,
                text_size=(420, None), halign="left", valign="top"
            ))

        self.body.add_widget(Label(
            text="[b]Related commands[/b]", markup=True,
            size_hint_y=None, height=38
        ))
        for cmd in c.get("related_commands", []):
            row = BoxLayout(size_hint_y=None, height=48, spacing=6)
            row.add_widget(Label(text=cmd, size_hint_x=.78))
            b = Button(text="Copy", size_hint_x=.22)
            b.bind(on_press=lambda _, x=cmd: self.copy(x))
            row.add_widget(b)
            self.body.add_widget(row)

        self.body.add_widget(Label(
            text="[b]Quick Quiz[/b]", markup=True,
            size_hint_y=None, height=42
        ))
        for i, q in enumerate(c.get("quiz", []), 1):
            self.add_quiz(i, q)

    def copy(self, text):
        ok = copy_text(text)
        popup("Copied" if ok else "Copy failed",
              text if ok else f"Copy manually:\n{text}")

    def add_quiz(self, number, q):
        box = BoxLayout(
            orientation="vertical", size_hint_y=None, height=190,
            spacing=5, padding=5
        )
        box.add_widget(Label(
            text=f"{number}. {q['q']}",
            size_hint_y=None, height=48, halign="left"
        ))
        for option in q["options"]:
            b = Button(text=option, size_hint_y=None, height=40)
            b.bind(on_press=lambda _, selected=option, answer=q["answer"]:
                    self.quiz_result(selected, answer))
            box.add_widget(b)
        self.body.add_widget(box)

    def quiz_result(self, selected, answer):
        if selected == answer:
            self.app.add_xp(25)
            popup("Correct! 🎯", "Great job! +25 XP")
        else:
            popup("Not quite", f"Correct answer: {answer}")


class LabsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=10, spacing=7)

        top = BoxLayout(size_hint_y=None, height=50, spacing=6)
        back = Button(text="‹ Back", size_hint_x=.22)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "dashboard"))
        top.add_widget(back)
        top.add_widget(make_title("🧪 Practice Labs", 20))
        root.add_widget(top)

        self.search = TextInput(
            hint_text="Search labs...",
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

        for lab in LABS:
            hay = (
                lab["title"] + " " + lab["category"] + " " +
                lab["level"] + " " + lab["objective"]
            ).lower()
            if q and q not in hay:
                continue

            completed = lab["id"] in self.app.completed_labs
            status = "✅ Completed" if completed else f"⭐ {lab['xp']} XP"
            b = Button(
                text=f"{lab['title']}\n"
                     f"{lab['category']} • {lab['level']} • {status}",
                size_hint_y=None, height=82
            )
            b.bind(on_press=lambda _, data=lab:
                   self.app.open_lab(data))
            self.grid.add_widget(b)

        if not self.grid.children:
            self.grid.add_widget(Label(
                text="No labs found.", size_hint_y=None, height=50
            ))


class LabDetail(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.lab = None

        root = BoxLayout(orientation="vertical", padding=10, spacing=7)
        top = BoxLayout(size_hint_y=None, height=50, spacing=6)
        back = Button(text="‹ Labs", size_hint_x=.25)
        back.bind(on_press=lambda *_:
                  setattr(app.sm, "current", "labs"))
        top.add_widget(back)
        self.heading = make_title("Lab", 19)
        top.add_widget(self.heading)
        root.add_widget(top)

        self.scroll = ScrollView()
        self.body = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing=9, padding=5
        )
        self.body.bind(minimum_height=self.body.setter("height"))
        self.scroll.add_widget(self.body)
        root.add_widget(self.scroll)
        self.add_widget(root)

    def load(self, lab):
        self.lab = lab
        self.body.clear_widgets()
        done = lab["id"] in self.app.completed_labs
        self.heading.text = f"[b]{lab['title']}[/b]"

        self.add_text(
            f"[b]{lab['title']}[/b]\n"
            f"{lab['category']} • {lab['level']} • {lab['xp']} XP",
            70
        )
        self.add_text(f"[b]Objective[/b]\n{lab['objective']}", 110)
        self.add_text(f"[b]Scenario[/b]\n{lab['scenario']}", 120)

        self.add_text("[b]Tasks[/b]", 40)
        for i, task in enumerate(lab["tasks"], 1):
            self.add_text(f"{i}. {task}", 65)

        self.add_text("[b]Hints[/b]", 40)
        for i, hint in enumerate(lab["hints"], 1):
            self.add_text(f"Hint {i}: {hint}", 75)

        self.add_text(
            f"[b]Expected learning[/b]\n{lab['expected_learning']}", 120
        )
        self.add_text(
            f"[b]Completion criteria[/b]\n{lab['completion']}", 120
        )

        self.body.add_widget(Button(
            text="🔄 Mark as Completed" if not done else "✅ Completed",
            disabled=done, size_hint_y=None, height=58
        ))
        button = self.body.children[0]
        button.bind(on_press=lambda *_: self.complete())

    def add_text(self, text, height):
        self.body.add_widget(Label(
            text=text, markup=True, size_hint_y=None, height=height,
            text_size=(420, None), halign="left", valign="top"
        ))

    def complete(self):
        if not self.lab or self.lab["id"] in self.app.completed_labs:
            return
        self.app.completed_labs.add(self.lab["id"])
        self.app.add_xp(self.lab["xp"])
        self.app.save_state()
        popup(
