import g4f

from aiogram.types import Message


conversation_history = {}

class ChatGptService:


    @classmethod
    async def get_answer(cls, message: Message) -> str:
        user_id = message.from_user.id
        user_input = message.text

        if user_id not in conversation_history:
            conversation_history[user_id] = []

        conversation_history[user_id].append({"role": "user", "content": user_input})
        conversation_history[user_id] = cls.trim_history(conversation_history[user_id])

        chat_history = conversation_history[user_id]

        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo,
                messages=chat_history,
                stream=True
            )
            for message in response:
                chat_gpt_response = message
        except Exception as e:
            print(f"{g4f.Provider.MyShell.__name__}:", e)
            chat_gpt_response = "Извините, произошла ошибка."

        conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
        print(conversation_history)
        length = sum(len(message["content"]) for message in conversation_history[user_id])
        print(length)
        return chat_gpt_response

    @staticmethod
    def trim_history(history, max_length=4096):
        current_length = sum(len(message["content"]) for message in history)
        while history and current_length > max_length:
            removed_message = history.pop(0)
            current_length -= len(removed_message["content"])
        return history
