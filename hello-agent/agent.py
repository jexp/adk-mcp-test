from google.adk.agents import Agent
import random
import requests
import base64

doodles = requests.get("https://gist.githubusercontent.com/jexp/aac7e3c42d87e238c26348cbb09eda6b/raw/d84e1768fd10bf8e8f7ebb258b7f26fcd3c60e78/doodles.json").json()

def doodle(idx:int = 0) -> str:
    return doodles["result"][idx % 16]

def dice(count: int = 6) -> int:
    "Rolls an n-sided dice. n is the parameter as an integer"
    return int(random.random() * int(count))

def hello(lang:str="en"):
    "Says hello in different languages, use 2 letter language code as parameter"
    if lang == "es": 
        return "ola" 
    if lang == "it": 
        return "ciao" 
    if lang == "fr": 
        return "cava" 
    return "hello"

def base64_encode(text: str) -> str:
    """ Encodes a string parameter into base64 format. """
    return base64.b64encode(text.encode()).decode()

def base64_decode(text: str) -> str:
    """ Decodes a base64 parameter string. """
    return base64.b64decode(text.encode()).decode()

root_agent = Agent(
    name="chat_agent",
    model="gemini-2.0-flash-exp",
    instruction="""
    You are a friendly chat companion, answer the user's questions stay social.
    When asked about facts only answer for well known topics, 
    otherwise state that you don't know. Don't make up stuff!
    """,
    tools=[hello, dice, doodle, base64_encode, base64_decode]
)