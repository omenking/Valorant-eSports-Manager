# Model Cost Analysis

> All costs are in USD

https://aws.amazon.com/bedrock/pricing/?refid=8228be07-d2ee-417f-b236-33eb068829a6

We need to determine the base cost to use these models served by Amazon Bedrock.

- Amazon Titan Premier
- Amazon Titan Lite
- Command
- Command R
- Command R+
- Command Light


| Models | Price per 1,000 input tokens	| Price per 1,000 output tokens |
|---|---|---|
| Amazon Titan Premier | $0.0005 | $0.0015 |
| Command | $0.0015 | $0.0020 |
| Command-Light | $0.0003 | $0.0006 |
| Command R	| $0.0005 | $0.0015 |
| Command R+ | $0.0030 | $0.0150 |
| Embed - English | $0.0001 | N/A |
| Embed - Multilingual | $0.0001 | N/A |

- Why is Command R so close in cost effectiveness? Is it better than Command Light?

## Command R vs Command Light vs Titan Prem

https://docs.cohere.com/docs/models
https://aws.amazon.com/bedrock/titan/

| Feature | Command R | Command Light | Amazon Titan Prmier |
|---|---|---|
Context Length | 128K | 4K | 32K |
Maximum Output Token | 4K | 4K | 4K |
## Cost Analysst of Resource Management

### How much would a team spend on a eSports Manager tool?

| Range | Size of Team |
|---|---|
| $500 | Entry-Level or Smaller |
| $10K  | Mid-Tier |
| $50K | Top-Tier |

> Resource as in humans

### eSports Manager

The cost of a eSports Manager

| Range | Size of Team |
|---|---|
| $30K - $50K | Entry-Level or Smaller |
| $50K - $80K  | Mid-Tier |
| $80K - $120K | Top-Tier |

### Team Members Costs

The cost of a team member

| Player Level  | Monthly  |  Yearly  |  Recruitment Costs |
|---|---|---|---|
| Entry-Level   | $1K - $5K   | $12K - $60K  | Low (minimal) |
| Mid-Tier | $5L - $10K | $60K - $120K  | Moderate  |
| Top-Tier | $10K - $25K | $120K - $300K | $20K - $500K+               |

## Custom Model Costs

> We are excluding Cohere Command R because it cannot be trained.

> We are excluding Amazon Titan Premier because it cannot be customized currently.

Custom models have their own inference cost per hour.
Id compute can scale zero when not used, than this option based on the value it provides could be worth it. But we need to understand the value propostion in monterary terms to a team.


### Cohere Command-Light	
- $0.001	 Price to train 1,000 tokens
- $1.95 Price to store each custom model per month
- $8.56 Price to infer from a custom model per model unit per hour (with no-commit Provisioned Throughput pricing)

### Amazon Titan Lite

- $0.0004 Price to train 1,000 tokens*	
- $1.95 Price to store each custom model per month

Amazon Titan Text Lite:
- 7.10 per hour (provisioned throughput to serve custom model, same cost if you didn't train it)

## Token Usage

To track usage server-side is challenging because we don't have a way to scope the logs in cloudwatch based on per conversation or event any agent. So if multiple LLMs are being used for multiple projects it can be difficult to infer.

We cannot use LlamaIndex to track token input and output count clients side because Amazon Bedrock module is not coded to pass that information forward.

We could try and control usage by setting the context length, however I tried an experiment where I set the context length to 100, but the API did not care and counitued beyond, so I think the context length is for specific models and maybe its not an option for Cohere's model to limit the context windoe.

## Conclusions

### Amazon Titan Premier

We can only use RAG and Prompt Engineering to improve is response. This model is very cost effective, however RAG and Prompt Engineering might not be enough to get the level intelligence and reasoning we want.

### Amazon Titan Lite

If we have to fine-tuning model than this is the most cost effective model for inference. But not by much compared to Cohere Llight for inference. This model has two options:
- Fine Tuning
- Contiued Pre Training


### Cohere Command Light

This model provides the most flexibility it is very cost effective, if we were to fine-tune the model and we dont have to pay per token cost (assuming that is now using only Provisioned Throughout because custom models have to be served) than it might be better than Amazon Titan Lite

### Cohere Command R

This model will perform better than Amazon Premier Titan, but is the most costly option. But its level of comphresion maybe may it worth it.