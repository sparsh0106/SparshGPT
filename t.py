import customtkinter as ctk
import requests
import json

model = "gpt-4o-mini"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDAyNzRAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.EXQ2jMCIT-QnLGiWuu0jYhru6YgwBB5xkqQiMnng4O8"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("1600x900")
root.title("SparshGPT")

label = ctk.CTkLabel(root, text="Welcome to the SparshGPT (powered by ClosedAI)", font=("Arial", 20))
label.pack(pady=20)

#############################################################################################

def TEXT():

    def Generate_Text():

        a = entry_text.get()

        model = "gpt-4o-mini"
        messages = [
            {
                "role":"system",
                "content":"answer"
            },
            {
                "role":"user",
                "content": a
            }
        ]

        data = {
            "model":model,
            "messages":messages
        }

        headers = {
            "Content-Type":"application/json",
            "Authorization":f"Bearer {api_key}"
        }

        response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers = headers, data = json.dumps(data))
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        
    
        answer_label = ctk.CTkLabel(root_text, text = answer, font = ('Arial',14), wraplength=500)
        answer_label.pack(pady = 10)

    root_text = ctk.CTk()
    root_text.geometry("800x450")
    root_text.title("TextGPT")
    
    label_text = ctk.CTkLabel(root_text, text = "TextGPT", font = ('Arial',20))
    label_text.pack(pady = 20)

    entry_text = ctk.CTkEntry(root_text, placeholder_text = "Enter your text")
    entry_text.pack(pady = 10, padx = 20)

    generate_button = ctk.CTkButton(root_text, text = "Gnerate", command = Generate_Text)
    generate_button.pack(pady = 20)

    root_text.mainloop()

#############################################################################################

def IMAGE():

    def Generate_Insights():
        url = image_link_text.get()
        c = caption.get()
        headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
        }

        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": c
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "detail": "low",
                                "url": url
                            }
                        }
                    ]
                }
            ]
        }

        response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)

        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        
        

        answer_label = ctk.CTkLabel(root_image, text = answer, font = ('Arial',14), wraplength=500)
        answer_label.pack(pady = 10)

    root_image = ctk.CTk()
    root_image.geometry("800x450")
    root_image.title("ImageGPT")

    label_text = ctk.CTkLabel(root_image, text = "ImageGPT", font = ('Arial',20))
    label_text.pack(pady = 20)

    image_link_text = ctk.CTkEntry(root_image, placeholder_text = "Enter Image Link")
    image_link_text.pack(pady = 10, padx = 20)

    caption = ctk.CTkEntry(root_image, placeholder_text = "Enter image caption")
    caption.pack(pady = 10, padx = 20)

    generate_button = ctk.CTkButton(root_image, text = "Gnerate", command = Generate_Insights)
    generate_button.pack(pady = 20)
    
    root_image.mainloop()


text_button = ctk.CTkButton(root, text="Text", command = TEXT)
text_button.pack(pady = 20)

image_button = ctk.CTkButton(root, text = "Image", command = IMAGE)
image_button.pack(pady = 20)


root.mainloop()

