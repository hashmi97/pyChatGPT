import openai
from dotenv import load_dotenv
import os


load_dotenv()


class openai_conn():
    def __init__(self) -> None:
        openai.organization = os.getenv("ORGANIZATION")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self._model = "gpt-3.5-turbo"

    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if new_model not in ['gpt-3.5-turbo', 'gpt-3.5-turbo-0301']:
            raise Exception("The model name you selected is not supported")
        else:
            self._model = new_model

    @staticmethod
    def update_api_key(new_api_key):
        openai.api_key = new_api_key

    @staticmethod
    def update_api_organization(new_org):
        openai.organization = new_org

    def create_chat(self, messages, **kwargs):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            **kwargs # TODO: Document the kwargs that are available
        )
        # To get the message only, you parse the response: response['choices'][0]['message']['content'],
        return response




if __name__ == "__main__":
    params = {"Starting Date": "20/03/2023",
              "Employer": "PhazeRo",
              "Employee": "Hisham Al Hashmi",
              "Country": "Oman"}
    m = [
        {"role": "system", "content": "You are a lawyer writing a document."},
        {"role": "user",
         "content": "with referencing the following data, write an employment agreement document"},
        {"role": "user", "content": str(params)}
    ]

    response = openai_conn().create_chat(messages=m)
    with open(f"sample_response.txt", "w") as f:
        print(response['choices'][0]['message']['content'], file=f)
