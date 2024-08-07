import time
from openai import OpenAI
import logging

class ChatgptApiService:
    def __init__(self, api_key: str, model: str, max_retries: int = 3):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_retries = max_retries
        self.logger = logging.getLogger(__name__)

    def send_prompt_to_api(self, system_message: str, text: str) -> str:
        messages = [{"role": "system", "content": system_message}, {"role": "user", "content": text}]
        self.logger.info(f"Sending prompt to chatgpt:\n {text} with context:\n {system_message}")
        
        retries = 0
        while retries <= self.max_retries:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
                return response["choices"][0]["message"]["content"]
            except Exception as e:
                self.logger.error(f"Error occurred: {e}")
                retries += 1
                if retries <= self.max_retries:
                    self.logger.info(f"Retrying... ({retries}/{self.max_retries})")
                    time.sleep(2 ** retries)  # Exponential backoff
                else:
                    self.logger.error("Max retries reached. Failing the request.")
                    raise