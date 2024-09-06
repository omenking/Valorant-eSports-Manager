import boto3
import json

# Amazon Bedrock Model IDs
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html

# Cohere Request Body Parameters
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere-command.html

bedrock = boto3.client(
  service_name='bedrock-runtime'
)
# Initialize Cohere embeddings through Amazon Bedrock
# embed_model = CohereBedrock(
#     model_name="embed-english-light-v3.0",
#     client_name="bedrock"
# )

def generate_response(prompt, max_tokens=256):
    body = json.dumps({
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.7,
        "p": 0.75,
        "k": 0,
        "stop_sequences": [],
        "return_likelihoods": "NONE"
    })
    
    response = bedrock.invoke_model(
        body=body,
        modelId='cohere.command-light-text-v14',
        accept='application/json',
        contentType='application/json'
    )
    
    response_body = json.loads(response.get('body').read())
    return response_body.get('generations')[0].get('text').strip()

def count_tokens(text):
    # This is a very rough estimate. Actual token count may vary.
    return len(text.split())

def chatbot():
    print(">>>")
    
    conversation_history = []
    total_prompt_tokens = 0
    total_completion_tokens = 0
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Agent: Exiting")
            break
        
        conversation_history.append(f"User: {user_input}")
        prompt = "\n".join(conversation_history[-10:])  # Use last 10 exchanges
        
        prompt_tokens = count_tokens(prompt)
        response = generate_response(prompt)
        completion_tokens = count_tokens(response)
        
        print(f"Agent: {response}")
        
        conversation_history.append(f"AI: {response}")
        total_prompt_tokens += prompt_tokens
        total_completion_tokens += completion_tokens
        
        print(f"\nTokens used in this exchange - Prompt: {prompt_tokens}, Completion: {completion_tokens}")
        print(f"Total tokens used so far - Prompt: {total_prompt_tokens}, Completion: {total_completion_tokens}")

    print(f"\nTotal tokens used in the entire conversation:")
    print(f"Prompt tokens: {total_prompt_tokens}")
    print(f"Completion tokens: {total_completion_tokens}")
    print(f"Total tokens: {total_prompt_tokens + total_completion_tokens}")

if __name__ == "__main__":
    chatbot()