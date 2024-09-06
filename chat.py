import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import Bedrock
from llama_index.embeddings import CohereBedrock

# Set up AWS credentials (make sure you have the necessary permissions)
os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_access_key"
os.environ["AWS_DEFAULT_REGION"] = "your_aws_region"

# Initialize Bedrock LLM
# https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html
llm = Bedrock(model_id="cohere.command-light-text-v14")

# Initialize Cohere embeddings through Amazon Bedrock
embed_model = CohereBedrock(
    model_name="embed-english-light-v3.0",
    client_name="bedrock"
)

# Load documents (replace 'data' with your document directory)
documents = SimpleDirectoryReader('data').load_data()

# Create index
index = VectorStoreIndex.from_documents(
    documents,
    llm=llm,
    embed_model=embed_model
)

# Create query engine
query_engine = index.as_query_engine()

def chatbot(query):
    response = query_engine.query(query)
    return response.response

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)