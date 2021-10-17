# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
from json_parser import build_Yenachi_convos, build_json_list
import openai
import os
from dotenv import load_dotenv

load_dotenv()
FINE_TUNED_MODEL = os.getenv('YENACH_GPT_MODEL')
openai.api_key = os.getenv('OPENAI_API_KEY')
# print("model = " + str(FINE_TUNED_MODEL))
# Gets a GPT-3 Curie fine-tuned model response to a query
def get_response_gpt(question):
    question = question + '\n\n###\n\n' # weird characters to indicate end of prompt
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = question,
        stop = '***') # '***' signifies end of completion
    text = response['choices'][0]['text']
    return text

if __name__ == "__main__":
    print(get_response_gpt("Yenach how is laura"))








#CHATTERBOT GRAVEYARD AHEAD

# bot = ChatBot(
#         'Buddy',  
#         logic_adapters=[
#             'chatterbot.logic.BestMatch',
#             'chatterbot.logic.TimeLogicAdapter'],
#     )
# def build_bot():
#     Yenachi_convos = build_Yenachi_convos()
#     Yenachi_trainer = ListTrainer(bot)
#     for i in range(len(Yenachi_convos)):
#         Yenachi_trainer.train(Yenachi_convos[i])

# def get_response(question):
#     response = bot.get_response(question)
#     return response