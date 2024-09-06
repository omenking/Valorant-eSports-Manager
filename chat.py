import os
from llama_index.llms.bedrock import Bedrock
# from llama_index.embeddings import CohereBedrock
from llama_index.core import Settings
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler, TokenCountingHandler

debug_handler = LlamaDebugHandler()
token_counter = TokenCountingHandler()
callback_manager = CallbackManager([debug_handler, token_counter])

# Amazon Bedrock Model IDs
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html

# Amazon Bedrock parametres
# > The LlamaIndex docs don't show them so we have go into the code
# https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-bedrock/llama_index/llms/bedrock/base.py
#
# model: The modelId of the Bedrock model to use.
# temperature: The temperature to use for sampling.
# max_tokens: The maximum number of tokens to generate.
#  - 4096 max for Command Light
# context_size: The maximum number of tokens available for input.
#  - 4096 max for Command Light

llm = Bedrock(
  model="cohere.command-light-text-v14",
  context_size=4096,
  max_token=400,
  callback_manager=callback_manager
)

# Initialize Cohere embeddings through Amazon Bedrock
# embed_model = CohereBedrock(
#     model_name="embed-english-light-v3.0",
#     client_name="bedrock"
# )

# Configure LlamaIndex to use our models
Settings.llm = llm
Settings.callback_manager = callback_manager
# Settings.embed_model = embed_model

def chatbot():
  print(">>>")

  while True:
    user_input = input("User: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
      print("Agent: Exiting...")
      break
    
    # Use the LLM directly for response generation
    response = llm.complete(user_input)
    print(f"Agent: {response.text.strip()}")
    print(
      "Embedding Tokens: ",
      token_counter.total_embedding_token_count,
      "\n",
      "LLM Prompt Tokens: ",
      token_counter.prompt_llm_token_count,
      "\n",
      "LLM Completion Tokens: ",
      token_counter.completion_llm_token_count,
      "\n",
      "Total LLM Token Count: ",
      token_counter.total_llm_token_count,
      "\n",
    )

if __name__ == "__main__":
  chatbot()