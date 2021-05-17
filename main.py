from tkinter import *
import tkinter.font

effectList = ['a', 'b', 'c', 'd', 'e', 'f']

class mainGUI:
    def __init__(self):
        window = Tk()
        window.geometry("400x600+750+200")
        window.resizable(False, False)
        window.title('건강한 식단 추천')

        font = tkinter.font.Font(window, size=15, weight='bold') # 폰트 설정
        # 라벨1 (알레르기 입력)
        label1 = Label(window, text="알레르기 입력 :", font=font)
        label1.grid(row=0, column=0)
        # 문자열 입력 받기
        allergy = StringVar
        textbox = Entry(window, width=26, textvariable=allergy)
        textbox.grid(row=0, column=1)
        # 라벨2 (특정 효능)
        label2 = Label(window, text="특정 효능 :", font=font)
        label2.grid(row=1, column=0)
        # 리스트박스
        scrollbar = Scrollbar(window)
        scrollbar.grid(row=1, column=2)
        listbox = Listbox(window, font=font, selectmode="extended",
                          width=15, height=1, yscrollcommand=scrollbar.set)
        for i in effectList:
            listbox.insert(END, i)
        scrollbar.config(command=listbox.yview)

        listbox.grid(row=1, column=1)

        '''
        # 상단 프레임
        mainFrame1 = Frame(window)
        mainFrame1.pack()
        # 라벨1 (알레르기 입력)
        label1 = Label(mainFrame1, text="알레르기 입력 :")
        label1.grid(row=0, column=0)
        # 문자열 입력 받기
        allergy = StringVar
        textbox = Entry(mainFrame1, width=12, textvariable=allergy)
        textbox.grid(row=0, column=1)
        # 라벨2 (특정 효능)
        label2 = Label(mainFrame1, text="특정 효능 :")
        label2.grid(row=1, column=0)
        # 리스트박스
        listbox = Listbox(mainFrame1,)'''

        window.mainloop()

mainGUI()
