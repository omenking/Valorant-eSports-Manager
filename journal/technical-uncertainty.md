# Technical Uncertainty

Its important that we define technical goals where there is a chance of uncertainty (a result of failure).
This will help us measure whether we have gained any technical domain knowledge at the end of this project.


## IaC AI Limits

Try and use IaC to stand up the project in one command in an AWS Account

- How much of the GenAI services can be provisioned via CFN?
- Can model's from the model catalog be provisioned via CFN?
- What should and shouldn't live in IaC for GenAI Infrastructure?

## Developer Productivty with Q

Try and use Amazon Developer Q to expediate the writing of IaC, UI, and other standard code.
The goal is just to get familar with newer Amazon Developer Q features like having project wide context.

- There may be a lack of code examples for the LLMs to pull from so I may have to write much by hand.

## Determining Cost

There is lack of understanding of the total cost to operate an GenAI project as a MVP and at scale.

Here are possible GenAI costs:
- Token costs for LLMs
    - How do we track input and ouput tokens?
    - How much will our chats generally cost in tokens for our use-case?
- Real-time inference cost
- Training-time cost
- Custom Model inference cost?
- Serverless LLMs vs Provisioend LLMs cost
- Session Management Cost
- Vectostore stroage and access costs
- Other types of search costs
- Knowledge graph (graph database costs)
- **What does the scale path look like for this GenAI app?

> There are other traditional costs for hosting the UI which will omit since those costs are well known.


## Model Evaluations

There are many models to choose from.
There are many ways to optimize specific models.

- What Evaluation/Performance metrics can we use to determine if our model(s) is perform well?
- How would we programmatically operate evaluations or do we use a cloud services?
- Is there any easy way to swap out models maybe via a framework like using LlamaIndex, or AWS SDK for Bedrock?

[Update 1]
AWS allows us to fine tune and do Continued Pre Training.
Titan can do both
Cohere Light can do fine tuning.

- How good can we make Titan express through custom models?

[Update 2]

- What is a small model for Chat completion?
    - Cohere Light is a chat completion model can be fined tune.
    - What is the difference (smartness vs cost) between the four Command Models?
        - Command
        - Command R
        - Command R+
        - Command Light
- Do we want to leverage completion models (fine tune them)?
    - Do we even know which are completion models?

## Programmatic Workflow for LLMs

- Is it all going to be the AWS and Bedrock SDK
- Can we leverage LlamaIndex or Ollama.

## Data Use

RAG is a very popular way to provide relevant information to the Agent.
Amazon Bedrock (I think) has built in RAG offering.
However there are many strategies for RAG.

- What limitations does this Amazon Bedrock RAG offering have?

There is multiple Vectorstore options on AWS.
- DocumentDB
- Postgres
- Amazon OpenSearch (might store index data)

Which one should we use?

There are multiple ways to search for data.
- Semantic Ranking
- HNSW
- Reranking

- Which should we use?

Knowledge Graphs leverage Graph databases for better results.
I don't know anything about how these can enhance data retrieval

- General research required

SageMaker has multiple services for data wrangling, data pre processing
and other steps in the data pipeline.

- Is our dataset so small we do not require these SageMaker service feature offerings?
- Does Amazon Bedrock have some kind of simplied offering so we don't have to use SageMaker?

## Automatic Reasoning and Tool Use

Should I include this?

Tool use could be going on and using the internet, searching google. eg. SerpAI

## Judges Evaluating Project

We may not be able to use custom models due to the judging process.

- If we chose to use a custom model which we think requires provision throughly hourly, will we need to have a means to launch and then stop the compute for the duration of the evaluations of judeges
- If compute has to provisioned how long would it take? Because it might take too long for judges to consider.
