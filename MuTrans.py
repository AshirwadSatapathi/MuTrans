from tkinter import *
from tkinter import messagebox
from googletrans import Translator
from textblob import TextBlob
root = Tk()
root.title("MuTrans")
translator = Translator()
b = ""
lang = ""
def input():
    global inputRes
    inputRes= message.get("1.0","end-1c")
    return inputRes
def about():
    messagebox.showinfo("About us","Made by Madhuri and Team")
def trans():
    text=input()
    print(text)
    TransText = translator.translate(text)
    print("Source Language is "+TransText.src)
    print("Original Text is "+text)
    print("Translated Text is "+TransText.text)
    #return TransText.text
    global b
    b = TransText.text
    global lang
    lang = TransText.src
    result.delete(0.0,END)
    result.insert(END,b)
def sentiment():
    wiki = TextBlob(b)
    a=wiki.sentiment.polarity
    print(a)
    print(b)
    messagebox.showinfo("Sentiment Score","The polarity of the message is "+str(a))
def Lang():
    messagebox.showinfo("Source Language","The Language code is "+lang)
#def set():
# b = trans()
# result.delete(0.0, END)
# result.insert(END,b)
# Title label
instruction = Label(root, text = "MuTrans", font=("arial",17,"bold"))
instruction.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = W)
# Message label

# Message entry
message = Text(root, width = 45, height = 6)
message.grid(row = 5, column = 0, columnspan = 3, padx = 5, sticky = W)

# Submit
submit = Button(root, text = "Translate", command = trans)
submit.grid(row = 8, column = 1, padx = 5)

# Result label
instruction = Label(root, text = "Result", font=("arial",14,"bold"))
instruction.grid(row = 9, column = 0, columnspan = 2, padx = 5, sticky = W)
# Result
result = Text(root, width = 45, height = 6, wrap = WORD)
result.grid(row = 10, column = 0, columnspan = 3, padx = 5, sticky = W)
Language = Button(root, text = "Language", command = Lang)
Language.grid(row = 11, column = 0, padx = 5, sticky = W)
Sentiment = Button(root, text = "Sentiment", command = sentiment)
Sentiment.grid(row = 11, column = 1, padx = 5)
About = Button(root, text = "About us", command = about)
About.grid(row = 11, column = 2, padx = 5, sticky = E)
root.mainloop()
