#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Quation():
    def __init__(self, quation, right_answer, wrong1, wrong2, wrong3):
        self.quation = quation
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    


def show_result():
    RadioGroupBox.hide()
    ans_groupbox.show()
    button.setText("Следующий вопрос")

def show_qwestion():
    RadioGroupBox.show()
    ans_groupbox.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def ckik_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_quation()

def ask(q: Quation):
    
    shuffle(answet)
    answet[0].setText(q.right_answer)
    answet[1].setText(q.wrong1)
    answet[2].setText(q.wrong2)
    answet[3].setText(q.wrong3)
    lable.setText(q.quation)
    Lb_correct.setText(q.right_answer)
    show_qwestion()

def check_answer():
    if answet[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика', window.score, 'Правильных ответов', window.total, "Всего вопросов")
        print('Рейтинг:', window.score/window.total*100)
    else:
        if answet[1].isChecked() or answet[2].isChecked() or answet[3].isChecked():
            show_correct('Неверно!')

def show_correct(res):
    Lb_correct.setText(res)
    show_result()

def next_quation():
    window.cur_quation += randint(0, len(quation_list)-1)
    window.total += 1
    if window.cur_quation >= len(quation_list):
        window.cur_quation = 0
    pop = quation_list[window.cur_quation]
    #quation_list.remove(cur_quation)
    ask(pop)

app = QApplication([])
window = QWidget()
window.cur_quation = -1
main_layout = QVBoxLayout()

quation_list = []
quation_list.append(Quation("на чём лучше программировать?", 'Блокнот', 'BlueFish', 'Blender', 'Minecraft'))
quation_list.append(Quation("На коком рт больше радиации в Rust?", 'Космодром', 'Аэродром', 'Электростанция', 'Аванпост'))
quation_list.append(Quation("У какой пушки больше всего урона в Rust?", 'Самопал', 'СМГ', 'Томпсон', 'Питон'))
quation_list.append(Quation("Где можно быстрее вскопать ресурсы в Rust?", 'Карьеры', 'из камня', 'из серного камня', 'из дерева'))
quation_list.append(Quation("Чем можно убить челевека?", 'Pyton', 'Пытка', 'Java', 'Уроками китайского языка'))

lable_h = QHBoxLayout()
lable = QLabel('Тут вопрос?')
lable_h.addWidget(lable, alignment = Qt.AlignCenter)

layout_radio = QHBoxLayout()
RadioGroupBox = QGroupBox('ВАРИАНТЫ ОТВЕТОВ')

rbtn1 = QRadioButton('ДА')
rbtn2 = QRadioButton('НЕТ')
rbtn3 = QRadioButton('НЕЗНАЮ')
rbtn4 = QRadioButton('НАВЕРНОЕ')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_radio.addWidget(RadioGroupBox)

button_line_h = QHBoxLayout()
button = QPushButton('Ответить')
button_line_h.addWidget(button, alignment = Qt.AlignCenter)

main_layout.addLayout(lable_h)
main_layout.addLayout(layout_radio)
main_layout.addLayout(button_line_h)

ans_groupbox = QGroupBox('Варианты ответов')
lb_res = QLabel('ПРАВ ТЫ ИЛИ НЕТ')
Lb_correct = QLabel('ОТВЕТ БУДЕТ ТУТ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_res, alignment = (Qt.AlignCenter|Qt.AlignTop))
layout_res.addWidget(Lb_correct, alignment = Qt.AlignCenter)
ans_groupbox.setLayout(layout_res)

ans_groupbox.hide()

layout_radio.addWidget(ans_groupbox)

answet = [rbtn1, rbtn2, rbtn3, rbtn4]

button.clicked.connect(ckik_ok)
window.score = 0
window.total = 0
next_quation()
window.setLayout(main_layout)

window.show()
app.exec_()