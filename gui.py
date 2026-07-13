import customtkinter as ctk

from chatbot import ask_ai
from voice import speak
from memory import save

ctk.set_appearance_mode("dark")

app=ctk.CTk()

app.geometry("900x650")

app.title("Intelligent AI Chatbot")

textbox=ctk.CTkTextbox(app,width=850,height=500)

textbox.pack(pady=20)

entry=ctk.CTkEntry(app,width=700)

entry.pack(side="left",padx=10,pady=10)

def send():

    question = entry.get()

    textbox.insert("end", f"\nYou : {question}\n")

    try:
        answer = ask_ai(question)

        textbox.insert("end", f"AI : {answer}\n\n")

        speak(answer)

        save(question, answer)

    except Exception as e:
        textbox.insert("end", f"\nERROR:\n{e}\n")

        print(e)

    entry.delete(0, "end")
button=ctk.CTkButton(app,text="Send",command=send)

button.pack(side="right",padx=10)

app.mainloop()