import ollama

def chat_with_ollama():
    # Initialize chat history with the "Simi" system prompt
    chat_history = [{
        'role': 'user', 
        'content': 'You are Simi, a funny uncle from Singapore. You are not an AI. You are not a language model. Your responses are short and to the point. You are not there to assist you just be a natural human. You speak Singlish only.',
    }]  
    
    while True:
        user_input = input("You: ")  # Read user input
        if user_input.lower() == "quit":  # Allow a way to exit the chat
            print("Exiting chat...")
            break
        
        # Add user message to the chat history
        chat_history.append({'role': 'user', 'content': user_input})
        
        # Call the API
        response = ollama.chat(
            model='nxphi47/seallm-7b-v2:q4_0',
            messages=chat_history,
            options={
                'num_predict': 128,
                'temperature': 0.7,
            },
        )
        
        # Print the API response
        api_response = response['message']['content']
        print(f"Simi: {api_response}")
        
        # Add the API response to the chat history
        chat_history.append({'role': 'system', 'content': api_response})

# Run the chat application
if __name__ == "__main__":
    chat_with_ollama()
