# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 14:39:24 2025

@author: ayush
"""

# Enhanced Customer Support Chatbot using Python

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Predefined responses for common customer queries
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I assist you with?",
        "how are you": "I'm here to help! What do you need assistance with?",
        "what is your name": "I'm your customer support assistant.",
        "services": "We provide product support, order tracking, refunds, technical help, and more.",
        "refund": "Sure, I can help with that. Please share your order ID.",
        "return policy": "Our return policy allows returns within 10 days of delivery.",
        "delivery status": "Please provide your order ID to check the delivery status.",
        "track order": "Sure, just share your order number to track it.",
        "payment methods": "We accept credit/debit cards, UPI, wallets, and net banking.",
        "cancel order": "Please provide your order ID so I can assist you with cancellation.",
        "technical issue": "Can you describe the issue? I’ll try to help or escalate it.",
        "warranty": "Our products come with a 1-year warranty from the date of purchase.",
        "working hours": "We are available 9 AM to 6 PM, Monday to Saturday.",
        "contact support": "You can call us at 1800-123-4567 or email support@example.com.",
        "bye": "Thank you for chatting with us. Have a great day!",
        "thank you": "You're welcome! Let me know if there's anything else I can help with.",
        "thanks": "Glad to help! Do you need anything else?"
    }

    # Search for a matching keyword in user input
    for question, answer in responses.items():
        if question in user_input:
            return answer

    # Fallback message for unknown queries
    return "I'm not sure about that. Would you like to get a call from customer service?"

# Chat function
def chat():
    print("🤖 Welcome to Customer Support Chatbot!")
    print("Type your question below (or type 'bye' to exit):\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Thank you for chatting with us. Goodbye!")
            break
        reply = chatbot_response(user_input)
        print("Bot:", reply)

# Run the chatbot
if __name__ == "__main__":
    chat()

