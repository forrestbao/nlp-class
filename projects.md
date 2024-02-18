# Project (Spring 2024): RAG

(Draft. To be updated.)

Retrieval-augmented generation (RAG) is a framework to give generative models knowledge without finetuning themselves. In this way, an LLM can adapt to new tasks quickly with the presence of new documents. 

In this project, you will build a demo RAG system of the following features: 
1. Upload/Add PDF files to a RAG platform/pipeline
2. Index the PDF files (chunk the content of the PDF files, embed them, and store them in a vector database), if applicable 
3. Query to the RAG system with a question and expect an answer based on the PDFs uploaded
4. Build a GUI app for all steps above. 
5. [Bonus] Delete a PDF file from the RAG system

An example demo using the Vectara AI platform is [here](https://github.com/forrestbao/vectara-python-cli)

You will be randomly assigned to pick one RAG solution and one UI solution to build the demo. 

## Steps of RAG
1. Ingest (optional): Filters and extracts useful text from the data uploaded, e.g., ignore page numbers in PDF. 
2. Chunk: Chunks the text into smaller pieces.
3. Embed the chunks and store them in, e.g., a vector database or as simple as the computer's RAM. 
4. Embed a query 
5. Retrieval: Retrieve the top-k documents -- get a rough but fast ranking using dot-product
6. Rerank (optional): Rerank the top-k documents based on the similarity between the query and the document, resulting in top-p documents where p < k
7. Generate: Generate an answer based on the top-p documents.

## RAG solutions to pick from (to be expanded)
* Google Vertex AI
* LangChain
* LlamaIndex

## App UI systems to pick from
* Streamlit
* Gradio
* Dash
* Funix.io

## Key challenges
1. How to chunk the text? Please experiment with different chunk sizes for the optimal solution. For example, 100-word chunks, 200-word chunks, etc. Be sure to overlap two consecutive chunks by 25% to avoid missing information.
2. How many chunks to retrieve and feed into an LLM? Let's make it simple by using top 5. 

## How to submit
1. An open-source GitHub repo with the RAG and UI solutions integrated. 
2. The Github repo shall include a README file with instructions on how to run the demo.
3. Instructions and video clips to show the usage and completion of 
3. A 5-minute video demo of the RAG system and the UI app.
4. [Bonus] Deploy your demo to a cloud platform for public access to test your demo. 

## Milestones
* Feb. 28: Github repo set up. 
* March 7: PDF upload and indexing via command line done. Include README file and a short video demo to show the usage and completion of your command line tool. 
* March 30: Answer generation based on user queries via command line finish. Include README file and a short video demo to show the usage and completion of your query tool.
* April 20: Build a GUI app for all steps above. Include README file and a short video demo to show the usage and completion of your GUI app.

## Tips
* For answer generation, use a small language model, like GPT-2. HuggingFace has free GPT-2 inference points. You can use HF_API instead of raw REST requests. 

## References
* https://python.langchain.com/docs/modules/data_connection/
* https://cloud.google.com/blog/products/ai-machine-learning/rags-powered-by-google-search-technology-part-1
* https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts 
* The instructor's demo of semantic search: https://github.com/forrestbao/pebble/blob/master/NLP/semantic_search.ipynb
