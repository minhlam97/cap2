import openai 
import streamlit as st 
import config 

openai.api_key = config.API_KEY 

def generate_response(prompt):
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=1000,
                                          temperature=0.3) 
    message = completion.choices[0].text 
    return message 

st.title("""
        Chatbot - MR
         """)

def get_text():
    input_text = st.text_input("Nhập câu hỏi: ",)
    return input_text 

user_input = get_text()

if user_input:
    st.text_area("Câu trả lời:", value=generate_response(user_input), height=600, max_chars=None)
else:
    st.text_area("Câu trả lời:", value="Xin mời nhập vào!!!", height=600, max_chars=None)