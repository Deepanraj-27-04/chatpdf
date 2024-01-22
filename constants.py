# Number of snippets that will be added to the prompt. Too many snippets and you risk both the prompt going over the
# token limit, and the model not being able to find the correct answer
prompt_number_snippets = 3

# GPT related constants
# use gpt gpt-3.5-turbo for faster results
gpt_model_to_use = 'gpt-3.5-turbo'
gpt_max_tokens = 1000

# Number of past user messages that will be used to search relevant snippets
search_number_messages = 4

# PDF Chunking constants
chunk_size = 500
chunk_overlap = 50

# Number of snippets to be retrieved by FAISS
number_snippets_to_retrieve = 3
