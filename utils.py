import base64

from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage


def get_llm_response(query: str, system_prompt: str, base64_image: bytes) -> str:

    llm = ChatOpenAI(model="gpt-4-turbo", max_tokens=256)

    output = llm.invoke(
        [
            SystemMessage(content=(system_prompt)),
            HumanMessage(
                content=[
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "auto",
                        },
                    },
                ]
            ),
        ]
    )

    return output.content


# Function to encode the image
def encode_image(image_path: str) -> bytes:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
