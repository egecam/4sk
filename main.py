import sys
import os
import datetime as dt
from gpt4all import GPT4All


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def display_welcome():
    welcome_text = """
     ....-    ...     -.- 
    
    ██╗  ██╗███████╗██╗  ██╗
    ██║  ██║██╔════╝██║ ██╔╝
    ███████║███████╗█████╔╝ 
    ╚════██║╚════██║██╔═██╗ 
         ██║███████║██║  ██╗
         ╚═╝╚══════╝╚═╝  ╚═╝
                        
    """
    print("\033[91m" + welcome_text + "\033[0m")  # Red color
    print(
        f"{bcolors.BOLD}Welcome to 4SK - Free & Open Source AI Assistant Client for Everyone!{bcolors.ENDC}"
    )  # Bold
    print("Version: 1.0")
    print("Type 'quit' to exit the chat.")
    print("\nInitializing AI model...")


def load_model(model_name):
    try:
        return GPT4All(model_name=model_name)
    except Exception as e:
        print(f"{bcolors.WARNING}Error loading model:{bcolors.ENDC} {e}")
        sys.exit(1)


def count_tokens(text):
    return len(text.split())


def truncate_history(history, max_tokens=1000):
    tokens = history.split()
    if len(tokens) > max_tokens:
        return history
    return " ".join(tokens[-max_tokens:])


def generate_response(
    model,
    prompt,
    conversation_history,
    system_template,
    prompt_template,
    temp,
    max_tokens=1000,
):
    try:
        truncated_history = truncate_history(conversation_history, max_tokens)
        full_prompt = (
            system_template + "\n" + truncated_history + prompt_template.format(prompt)
        )
        with model.chat_session():
            response = ""
            for token in model.generate(prompt=full_prompt, streaming=True, temp=temp):
                response += token
                print(token, end="", flush=True)
            print()
            return response
    except Exception as e:
        print(f"Failed to generate response: {e}")
        return None


def main():
    display_welcome()

    # model_name = "wizardlm-13b-v1.2.Q4_0.gguf" # Largest, most capable
    model_name = "mistral-7b-openorca.Q4_0.gguf"  # Larger, more capable
    # model_name = "orca-mini-3b-gguf2-q4_0.gguf"  # Smaller, faster

    temp = 0.7
    system_template = "You are a helpful AI assistant capable of translation, calculations, and code debugging. Respond based on the entire conversation history provided. Your nickname is '4SK'.\n"
    prompt_template = "USER: {0}\nASSISTANT: "

    model = load_model(model_name)
    print("\nAI model loaded successfully. Ready for you questions!\n")

    conversation_history = ""

    while True:
        user_input = input("\n\033[94mYOU:\033[0m ")
        if user_input.startswith("/"):
            if user_input == "/help":
                print("\nCommands:")
                print(f"{bcolors.OKCYAN}/help{bcolors.ENDC} - Show this help message")
                print(
                    f"{bcolors.OKCYAN}/clear{bcolors.ENDC} - Clear conversation history"
                )
                print(
                    f"{bcolors.OKCYAN}/load{bcolors.ENDC} {filepath} - Load conversation history from a local source"
                )
                print(
                    f"{bcolors.OKCYAN}/save{bcolors.ENDC} - Save conversation history to a local source"
                )
                print(f"{bcolors.OKCYAN}/model{bcolors.ENDC} - Show current model")
                print(
                    f"{bcolors.OKCYAN}/model{bcolors.ENDC} {model} - Change model to the specified model"
                )
                print(
                    f"{bcolors.OKCYAN}/reload{bcolors.ENDC} - Reload 4SK. Useful after changing the model. {bcolors.WARNING}Warning:{bcolors.ENDC} This will clear the conversation history, back up first by '/save' if needed."
                )
                print(f"Type {bcolors.OKCYAN}'quit'{bcolors.ENDC} to exit the chat.")

            elif user_input == "/clear":
                conversation_history = ""
                print("Conversation history cleared.")

            elif user_input == "/load {filepath}":
                try:
                    with open(user_input.split()[1], "r") as f:
                        conversation_history = f.read()
                    print(
                        "Conversation history loaded from a local source successfully."
                    )
                except Exception as e:
                    print(
                        f"{bcolors.WARNING}Error loading conversation history:{bcolors.ENDC} {e}"
                    )

            elif user_input == "/save":
                try:
                    script_dir = os.path.dirname(__file__)
                    now = dt.datetime.now()
                    rel_path = (
                        f"conversation_history_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
                    )
                    abs_file_path = os.path.join(script_dir, rel_path)
                    print("Conversation history saved to a local source successfully.")
                except Exception as e:
                    print(
                        f"{bcolors.WARNING}Error saving conversation history:{bcolors.ENDC} {e}"
                    )

            elif user_input == "/model":
                print(f"Current model: {model_name}")

            elif user_input == "/model {model}":
                try:
                    model_name = user_input.split()[1]
                    model = load_model(model_name)
                    print(f"Model changed to {model_name}")
                except Exception as e:
                    print(f"{bcolors.WARNING}Error loading model:{bcolors.ENDC} {e}")

            elif user_input == "/reload":
                try:
                    os.execl(sys.executable, sys.executable, *sys.argv)
                except Exception as e:
                    print(f"{bcolors.WARNING}Error reloading 4SK:{bcolors.ENDC} {e}")

            else:
                print("Unknown command. Type '/help' for assistance.")
            continue

        if user_input == "":
            print("Please ask me something.")
            continue

        if user_input.lower() == "quit":
            print("\033[91m Thank you for using 4SK. Goodbye! \033[0m")
            break

        print("\033[91m 4SK: \033[0m ", end="", flush=True)

        response = generate_response(
            model,
            user_input,
            conversation_history,
            system_template,
            prompt_template,
            temp,
        )
        if response is None:
            print("Sorry, I couldn't generate a response. Please try again.")
        else:
            conversation_history += f"USER: {user_input}\nASSISTANT: {response}\n"


if __name__ == "__main__":
    main()
