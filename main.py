from difflib import get_close_matches
from collections import defaultdict


def get_best_match(user_question: str, knowledge: dict, context: str) -> str | None:
    question = list(knowledge.keys())
    # Handle synonyms by checking alternative phrases in the context
    matches = get_close_matches(user_question, question, n=1, cutoff=0.6)

    if not matches and context:
        # Use context as fallback if no match found
        matches = get_close_matches(context, question, n=1, cutoff=0.6)

    if matches:
        return matches[0]
    return None


def update_context(user_input: str, context: str) -> str:
    """
    Updates the context based on the user input. This could be enhanced further for context management.
    """
    if 'how are you' in user_input.lower():
        return 'how are you'
    elif 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
        return 'goodbye'
    elif 'help' in user_input.lower():
        return 'help'
    return context


def run_chatBot(knowledge: dict) -> None:
    context = ''
    while True:
        user_input: str = input('You: ')

        # Update the context based on the user's input
        context = update_context(user_input, context)

        best_match: str | None = get_best_match(user_input, knowledge, context)

        if best_match:
            response: str = knowledge.get(best_match, 'I am sorry, I don\'t understand.')
            print(f'Bot: {response}')
        else:
            print(f'Bot: I don\'t understand... Can you rephrase?')


def main() -> None:
    brain: dict[str, str] = {
        'hello': 'Hey there! How can I assist you today?',
        'hi': 'Hello! How can I help you?',
        'how are you': 'I\'m doing great, thank you for asking! How about you?',
        'bye': 'Goodbye! Have a great day! Don\'t hesitate to reach out again.',
        'goodbye': 'See you soon! Take care!',
        'thanks': 'You\'re welcome! Feel free to ask me anything else.',
        'thank you': 'It\'s my pleasure! Let me know if you need anything else.',
        'help': 'Sure! I can assist with various topics like your account, services, and more. What do you need help with?',
        'what is your name': 'I am your friendly chatbot! How can I assist you today?',
        'who are you': 'I am a chatbot here to help you with your queries. Just let me know what you need!',
        'tell me a joke': 'Why don\'t skeletons fight each other? They don\'t have the guts!',
        'what can you do': 'I can help with a wide range of tasks like answering questions, providing information, and assisting with specific requests. What do you need help with?',
        'how can I contact support': 'You can reach support by emailing support@company.com or calling 1-800-123-4567.',
        'price of product': 'I can help with product prices. Please provide the product name or category.',
        'product availability': 'Let me know the product name or category, and I can check availability for you.',
        'order status': 'Can you provide your order ID? I can check the status for you.',
        'how to reset password': 'To reset your password, go to the settings page and click on "Reset Password". You will receive an email with instructions.',
        'weather': 'I can help you with weather updates! What location are you looking for?',
        'yes': 'Got it! How else can I assist you?',
        'no': 'Okay, feel free to ask if you change your mind!',
        'error': 'I\'m sorry, I didn\'t understand that. Could you please rephrase or ask something else?',
    }

    run_chatBot(knowledge=brain)


if __name__ == '__main__':
    main()
