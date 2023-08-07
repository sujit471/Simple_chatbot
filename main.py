from conversations.differentclass import chat_conversation
from conversations.selectoptions import mapping as mapping_func


def main():
    chat_conversation.greeting()
    while True:
        data = input(f'User: ')
        mapping_func(("Bot :",data))
    

if __name__ == "__main__":
    main()
