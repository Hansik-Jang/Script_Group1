from tkinter import *
from tkinter.font import Font
import tkinter.font
from xml.dom.minidom import parseString
from xml.etree import ElementTree
import urllib.request

categoryURL = 'http:/api.nongsaro.go.kr/service/recomentDiet/mainCategoryList'
tableURL = 'http:/api.nongsaro.go.kr/service/recomentDiet/recomendDietList'
infoURL = 'http:/api.nongsaro.go.kr/service/recomentDiet/recomendDietDtl'

effectList = ['없음', 'a', 'b', 'c', 'd', 'e', 'f']
tempList = ['a', 'b', 'c', 'd', 'e', 'f']

class mainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x1000")
        self.window.title('건강한 식단 추천')
        self.window.resizable(False, False)
        self.font = Font(size=13, weight='bold')  # 폰트 설정
        self.font1 = Font(size=11, family='굴림', weight='bold')
        self.initMainFirst()
        self.initMainInfo()

        self.window.mainloop()

    def initMainFirst(self):
        label1 = Label(self.window, text="알레르기 입력 :", font=self.font)
        allergy = StringVar
        textbox = Entry(self.window, width=32, textvariable=allergy)
        allbutton = Button(self.window, text="입력", font=self.font, command=self.allergyEntry)
        label2 = Label(self.window, text="특정 효능 :", font=self.font)
        scrollbar = Scrollbar(self.window)
        listbox = Listbox(self.window, font=self.font, selectmode="extended", width=25, height=1, yscrollcommand=scrollbar.set)
        for i in effectList:
            listbox.insert(END, i)
        scrollbar.config(command=listbox.yview)
        benefitbutton = Button(self.window, text="입력\n완료", font=self.font, width=6, height=3, compound='c', command=self.benefitEntry)

        label1.place(x=60 + 20, y=20)
        textbox.place(x=60 + 20 + 115, y=25)
        #self.allbutton.place(x=80 + 20 + 115 + 200, y=18)
        label2.place(x=60 + 51, y=60)
        listbox.place(x=60 + 60 + 75, y=60)
        scrollbar.place(x=60 + 20 + 115 + 235, y=50)
        benefitbutton.place(x=60 + 20 + 115 + 280, y=22)

    def initMainInfo(self):
        infoScrollbar = Scrollbar(self.window)
        infoList = Listbox(self.window, font=self.font1, width=40, height=20, yscrollcommand=infoScrollbar.set)
        for i in tempList:
            infoList.insert(END, i)
        infoScrollbar.config(command=infoList.yview)

        infoList.place(x=20, y=120)
        infoScrollbar.place(x=400, y=200)



    def allergyEntry(self):
        pass

    def benefitEntry(self):
        pass


mainGUI()

'''
    def allergyEntry(self):
        pass
    def benefitEntry(self):
        pass

    def mainFirstFrame(self):
        font = tkinter.font.
        # 라벨1 (알러지 입력)
        label1 = Label(window, text="알레르기 입력 :", font=font)
        label1.pack()
        label1.place(x=-100,y=20)
        # 문자열 입력 받기
        allergy = StringVar
        textbox = Entry(window, width=26, textvariable=allergy)
        textbox.pack()
        # 알러지 입력 버튼
        allbutton = Button(self.mainFrame1, text="입력", font=font, command=self.allergyEntry)
        allbutton.pack()
        # 라벨2 (특정 효능)
        label2 = Label(self.mainFrame1, text="특정 효능 :", font=font)
        label2.pack()
        # 리스트박스
        scrollbar = Scrollbar(self.mainFrame1)
        listbox = Listbox(self.mainFrame1, font=font, selectmode="extended",
                          width=15, height=1, yscrollcommand=scrollbar.set)
        for i in effectList :
            listbox.insert(END, i)
        scrollbar.config(command=listbox.yview)
        listbox.pack()
        scrollbar.pack()
        # 효능 버튼
        benefitbutton = Button(self.mainFrame1, text="입력", font=font, command=self.benefitEntry)
        benefitbutton.pack()

    def __init__(self):
        window = Tk()
        window.geometry("600x1000")
        window.resizable(False, False)
        window.title('건강한 식단 추천')

        self.mainFrame1 = Frame(window)
        self.mainFirstFrame()
        self.mainFrame1.pack()


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
