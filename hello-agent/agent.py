from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
import random
import requests
import base64

# doodles = requests.get("https://gist.githubusercontent.com/jexp/aac7e3c42d87e238c26348cbb09eda6b/raw/d84e1768fd10bf8e8f7ebb258b7f26fcd3c60e78/doodles.json").json()

# def doodle(idx:int = 0) -> str:
#    return doodles["result"][idx % 16]

def dice(count: int = 6) -> int:
    "Rolls an n-sided dice. n is the parameter as an integer"
    return int(random.random() * int(count))

def hello(lang: str = "en"):
    "Says hello in different languages, use 2 letter language code as parameter"
    greetings = {
        "en": "hello",
        "es": "hola",
        "it": "ciao",
        "fr": "salut",
        "de": "hallo",
        "pt": "olá",
        "ru": "привет",
        "zh": "你好",
        "ja": "こんにちは",
        "ko": "안녕하세요",
        "ar": "مرحبا",
        "hi": "नमस्ते",
        "tr": "merhaba",
        "nl": "hallo",
        "sv": "hej",
        "no": "hallo",
        "da": "hej",
        "fi": "hei",
        "pl": "cześć",
        "cs": "ahoj",
        "el": "γεια",
        "he": "שלום",
        "th": "สวัสดี",
        "vi": "xin chào",
        "id": "halo"
    }
    return greetings.get(lang, "hello")

def base64_encode(text: str) -> str:
    """ Encodes a string parameter into base64 format. """
    return base64.b64encode(text.encode()).decode()

def base64_decode(text: str) -> str:
    """ Decodes a base64 parameter string. """
    return base64.b64decode(text.encode()).decode()

root_agent = Agent(
    name="chat_agent",
    model="gemini-2.5-flash",
    # model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    instruction="""
    You are a friendly chat companion, answer the user's questions stay social.
    When asked about facts only answer for well known topics, 
    otherwise state that you don't know. Don't make up stuff!
    """,
    tools=[hello, dice] # , base64_encode, base64_decode, doodle
)