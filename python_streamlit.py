import os
from revChatGPT.V1 import Chatbot
import streamlit as st
from streamlit_chat import message
import requests
from datetime import datetime
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



start_time = time.time()
# Chat GPT session
chatbot = Chatbot(config={
  "email": "duan92@purdue.edu", 
  "password": "CDesign2023"
})

print("Chatbot: ")



# prev_text = ""
# for data in chatbot.ask(
#     "Give me some ",
# ):
#     message = data["message"][len(prev_text) :]
#     print(message, end="", flush=True)
#     prev_text = data["message"]
# print()

## Streamlit Session 



# st.set_page_config(
#     page_title="Streamlit Chat - Demo",
#     page_icon=":robot:"
# )

# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
# headers = {"Authorization": st.secrets['api_key']}

# st.header("Streamlit Chat - Demo")
# st.markdown("[Github](https://github.com/ai-yash/st-chat)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query_chatgpt(user_query):
    gpt_feedback = chatbot.ask(user_query)
    prev_text = ""
    for data in gpt_feedback:
        # print(data)
        # print('len(prev_text)',len(prev_text))
        message = data["message"][len(prev_text) :]
        
        # st.write("You entered: ", text_input)
        # st.text_area(message)
        # print(message, end="", flush=True)
        prev_text = data["message"]

    return prev_text

def get_text():
    input_text = st.text_input("You: ",placeholder="Please type in your query")
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    return input_text, current_time

# users_input = get_text() 
# print(users_input) 

# hide remining part of the website until the user inputs a name
nameEntered = False
if(nameEntered ==False):
    user_name = st.text_input("Please type in you name before start:",placeholder="Please type in your name(do this first or else the code breaks)")
    nameEntered =True

# print(dummy_input)
# clicked = st.button("START")

# if clicked and dummy_input:
st.header("Chat GPT Assistant")
user_input, timeC = get_text()


if user_input:
    print("user give some input:",user_input)
    output = query_chatgpt(user_input)
    end_time = time.time()
    execute_time = end_time - start_time
    file_data = "User name: " + user_name + "\ninput text: " + user_input + "\n@Time: " + str(timeC) + "\n@Execution Time: " + str(round(execute_time, 2)) + "s\n" + output

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

    # filename = f"ChatGPT"{str(datetime.today)}.txt"
    filename = f"{user_name}.txt"
    print(filename)

    f=open(filename, "a+")
    f.write(file_data)
    f.close()

if st.button('End Session ?'):
    # # Saving file to google drive
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    file_to_upload = filename

    f=open(filename, "r+")
    file_content = f.read()
    f.close()

    file1 = drive.CreateFile({'title': filename})  # Create GoogleDriveFile instance with title filename.
    file1.SetContentString(file_content) # Set content of the file from given string.
    file1.Upload()

    # delete users file after uploading 
    os.remove(filename)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


