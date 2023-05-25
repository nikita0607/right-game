import json
import random

from widgets import Widget, TextWidget
from window import Window

from utils import oemc, oemw



class Manager:
    def __init__(self, window):
        window.clear_widgets()
        self.window = window

        self.do_question(0)

    def do_question(self, quest_id):
        window = self.window
        with open('./tasks.json') as file:
            questions = json.load(file)

        quest_id = quest_id % len(questions)
        quest = questions[quest_id]
        textw = TextWidget(window, 'textw', *oemc(50, 10), 24, quest['text'])
        textw.move_center2cords()

        x0 = 30
        y0 = 40

        ids = [i for i in range(len(quest['answers']))]
        random.shuffle(ids)
        for pos in range(len(ids)):
            x = x0 if pos % 2 == 0 else 70
            y = (pos//2)*30 + y0

            _id = ids[pos]
            ans_id = f'answer{_id}' if _id > 0 else f'good_answer{quest_id}'
            text = quest['answers'][_id]

            ans = Widget(window, ans_id, *oemc(x, y), img='answer.png', callback=self.answer)
            ans.move_center2cords()

            anst = TextWidget(window, ans_id, *ans.get_center(), 24, text=text, callback=self.answer)
            anst.move_center2cords()

            window.add_widget(ans)
            window.add_widget(anst)

        window.add_widget(textw)

    def answer(self, widget: Widget):
        if 'good_answer' in widget.id:
            self.window.clear_widgets()
            next_quest_id = int(widget.id.replace('good_answer', ''))+1

            self.do_question(next_quest_id)

        else:
            self.window.del_widgets_by_id(widget.id)