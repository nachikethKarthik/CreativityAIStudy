import os
from revChatGPT.V1 import Chatbot
import streamlit as st
from streamlit_chat import message
import requests

# Chat GPT session
chatbot = Chatbot(config={
  "email": "herr.nachiketh@gmail.com", 
  "password": "Tasmaniandevil900"
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

def query_chatgpt(user_input):
    gpt_feedback = chatbot.ask(user_input) 
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
    return input_text 

# users_input = get_text() 
# print(users_input) 

st.header("Chat GPT")
user_input = get_text()

if user_input:
    print("user give some input:",user_input)
    output = query_chatgpt(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# message(user_input)
    # st.write(prev_text)
    # print("getting new output")
    # print(prev_text)

    # print()



    # output = query({
    #     "inputs": {
    #         "past_user_inputs": st.session_state.past,
    #         "generated_responses": st.session_state.generated,
    #         "text": user_input,
    #     },"parameters": {"repetition_penalty": 1.33},
    # })

    # st.session_state.past.append(user_input)

    # st.session_state.generated.append(output["generated_text"])

# if st.session_state['generated']:


    # for i in range(len(st.session_state['generated'])-1, -1, -1):
    #     message(st.session_state["generated"][i], key=str(i))
    #     message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

# st.set_page_config(page_title="Brainstorming Buddy")

# html_temp = """
#                 <div style="background-color:{};padding:1px">
                
#                 </div>
#                 """

# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )