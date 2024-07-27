## Resources
- [Local LLM](https://python.langchain.com/v0.2/docs/how_to/local_llms/)
- [Local RAG](https://python.langchain.com/v0.2/docs/tutorials/local_rag/)
- [Conversational RAG](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)
- [Nvidia Embedding Models](https://build.nvidia.com/search?term=Embeddings)
- [Nvidia LLMs](https://build.nvidia.com/search?term=Chat)

# Runtimes

## Embedding Models
| Model                                 | Avg Time (millisec) |
|---------------------------------------|---------------------|
| all-mpnet-base-v2                     | 94.50               |
| paraphrase-multilingual-MiniLM-L12-v2 | 33.90               |
| all-MiniLM-L6-v2                      | 17.50               |
| LaBSE                                 | 91.50               |
| distiluse-base-multilingual-cased-v1  | 55.72               |
| stsb-distilbert-base                  | 48.37               |
| all-MiniLM-L12-v2                     | 30.28               |
| all-distilroberta-v1                  | 56.26               |
| multi-qa-mpnet-base-dot-v1            | 91.20               |
| multi-qa-distilbert-cos-v1            | 49.13               |
| multi-qa-MiniLM-L6-cos-v1             | 16.02               |
| paraphrase-multilingual-mpnet-base-v2 | 108.86              |
| paraphrase-albert-small-v2            | 36.49               |
| paraphrase-MiniLM-L3-v2               | 9.17                |
| distiluse-base-multilingual-cased-v2  | 56.03               |

## LLMs
### Hardware Config (CPU Only)
| Model    | RAM (Gb) | Cpu Cores | KV_cache (Gb) | Cpu blocks | Time Per Prompt |
|----------|----------|-----------|---------------|------------|-----------------|
| gemma-2b | 32       | 8         | 4             | 14563      | 2.15            |
| gemma-2b | 32       | 8         | 5             | 18240      | 2.09            |
| gemma-2b | 32       | 8         | 8             | 29127      | 2.16            |
| gemma-2b | 32       | 32        | 4             | 14563      | 2.12            |
| gemma-2b | 32       | 32        | 8             | 29127      | 2.08            |
| gemma-2b | 32       | 32        | 10            | 36408      | 2.13            |
| gemma-2b | 32       | 32        | 16            | 58254      | Killed          |
| gemma-2b | 64       | 8         | 4             | 14563      | 2.09            |
| gemma-2b | 64       | 32        | 4             | 14563      | 2.11            |
| gemma-2b | 64       | 32        | 8             | 29127      | 2.07            |
| gemma-2b | 64       | 32        | 10            | 36408      | 2.07            |
| gemma-2b | 128      | 32        | 4             | 14563      | 2.12            |
| gemma-2b | 128      | 32        | 10            | 36408      | 2.08            |
| gemma-2b | 128      | 32        | 12            | 43690      | 2.08            |
| gemma-2b | 128      | 32        | 16            | 58254      | 2.08            |
| gemma-2b | 128      | 32        | 20            | 72817      | 2.08            |
| gemma-2b | 128      | 32        | 24            | 87381      | 2.07            |
| gemma-2b | 128      | 32        | 30            | 109226     | 2.16            |

### CPU Only
|           Model          | Parameters (B) | Answer Quality | Time per Prompt |
|--------------------------|----------------|----------------|-----------------|
| Mistral                  | 7              | Good           | 8 min           |
| Meta-Llama-3-8B-Instruct | 8              | Good           | 6.21 min        |
| gpt2                     | 1.5            | Bad            | 6 sec           |
| Qwen2-0.5B               | 0.5            | Bad            | 10 sec          |
| DialoGPT-medium          | 0.147          | Bad            | 12 sec          |
| distilgpt2               | 0.08           | Bad            | 3 sec           |
| pythia-160m              | 0.16           | Bad            | 8 sec           |
| pythia-410m              | 0.41           | Bad            | 23 sec          |
| bloom-560m               | 0.56           | Bad            | 23 sec          |

### RTX 6000 GPU
|           Model          | # of Parameters (B) | Answer Quality (/10) |     Time Avg    |
|--------------------------|---------------------|----------------------|-----------------|
| Mistral-7B-Instruct-v0.3 | 7                   |                      | out of memory   |
| Meta-Llama-3-8B-Instruct | 8                   | 6                    | 4 sec           |
| gpt2                     | 1.5                 | 1                    | 0 sec           |
| Qwen2-0.5B               | 0.5                 | 1                    | 0 sec           |
| Yi-1.5-6B-Chat           | 6                   | 8                    | 6 sec           |
| internlm2_5-7b-chat      | 7                   |                      | out of memory   |
| Qwen2-7B-Instruct        | 7                   |                      | out of memory   |
| Llama-3-6.3b-v0.1        | 6.3                 | 8                    | 3 sec           |
| Mistral-v0.3-6B          | 6                   | 7                    | 3 sec           |
| Llama-3-8B-Instruct-v0.8 | 8                   | 7                    | 4 sec           |
| L3-8B-Stheno-v3.2        | 8                   | 8 seems good         | 4 sec           |
| blossom-v5.1-9b          | 9                   |                      | out of memory   |
| gemma-2-9b-it            | 9                   |                      | Gemma2 not supp |
| Yi-1.5-9B-Chat-16K       | 9                   | 8                    | 5 sec           |
| openchat-3.6-8b-20240522 | 8                   | 1                    | 1 sec           |
| orca_mini_v7_7b          |                     |                      |                 |
| neural-chat-7b-v3-2      |                     |                      |                 |
