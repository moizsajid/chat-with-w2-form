from dotenv import load_dotenv

load_dotenv()

import os
import tempfile

import streamlit as st
from pdf2image import convert_from_path

from utils import get_llm_response, encode_image


with open("resources/system_prompt.txt", "r") as file_input:
    system_prompt = file_input.read()

st.title("Chat with your W-2 form!")
st.subheader("Get all your queries answered about your W-2 form!")

pdf = st.file_uploader("Upload your W-2 form!", type="pdf")

if pdf is not None:
    temp_dir = tempfile.mkdtemp()
    pdf_file_path = os.path.join(temp_dir, pdf.name)
    with open(pdf_file_path, "wb") as f:
        f.write(pdf.getvalue())

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file_path)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(pdf_file_path.split(".")[0] + ".jpg", "JPEG")

    # Path to your image
    image_path = pdf_file_path.split(".")[0] + ".jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "What is your question regarding your W-2 form?",
            }
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        output = get_llm_response(prompt, system_prompt, base64_image)

        st.session_state.messages.append({"role": "assistant", "content": output})
        st.chat_message("assistant").write(output)
