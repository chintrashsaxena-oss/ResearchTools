# from langchain_huggingfacehub import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )
# model= ChatHuggingFace(llm=llm)
# st.header('Research tool')
# user_input= st.text_input("Enter your prompts")

# if st.button("Summarize"):
#     result=model.invoke(user_input)
#     st.write(result.content)



# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st

# # Load environment variables
# load_dotenv()

# # Create LLM endpoint
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     max_new_tokens=200,
#     temperature=0.5
# )

# # Wrap in chat model
# model = ChatHuggingFace(llm=llm)

# # Streamlit UI
# st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

# if st.button("Summarize"):
#     if user_input.strip():
#         result = model.invoke(user_input)
#         st.write(result.content)
#     else:
#         st.warning("Please enter a prompt.")

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

api_token = os.getenv("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")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation",
    temperature=0.5,
    huggingfacehub_api_token="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"
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)