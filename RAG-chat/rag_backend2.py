#   #1 Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
# • #2. Define the data source and load data with PDFLoader(https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf)
# • #3. Split the Text based on Character, Tokens etc. - Recursively split by character - ["\n\n", "\n", " ", ""]
# • #4. Create Embeddings -- Client connection
# • #5à Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
# • #5b Create index for HR Report
# • #5c. Wrap within a function
# • #6a. Write a function to connect to Bedrock Foundation Model
# • #6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.
# • # Index creation --> https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html