import requests
import json
import io
from ollama import Client
import os

INVALID_API_KEY_MESSAGE = (
    "Invalid API key. Please generate a new API key"
)


class BitPoetOllamaLLMNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "Hello",
                    "placeholder": "Enter your prompt here..."
                }),
                "model": ("STRING", {
                    "multiline": False,
                    "default": "gemma3:4b",
                    "placeholder": "Model name"
                }),
            },
            "optional": {
                "use_cloud": ("BOOLEAN", {
                    "default": False
                }),
           }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_text"
    CATEGORY = "LLM/Ollama"
    
   
    def generate_text(self, prompt, model="gemma3", use_cloud=False):
        print ("generate_text started")
        try:
            messages = [
                {"role": "user", "content": prompt}
            ]
 
            if use_cloud:
                if os.environ.get('OLLAMA_API_KEY') is None:
                    return ("Error: OLLAMA_API_KEY is not set!",)
 
                client = Client(
                    host='https://ollama.com',
                    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
                )
            else:
                client = Client()

            print ("Running inference on Ollama")

            content = ""
 
            for part in client.chat(model=model, messages=messages, stream=True):
                print (part)
                content += part.message.content

            return (content,)
            
        except Exception as e:
            return (f"Error: {str(e)}",)
            

