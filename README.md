# Retrieval-Augmented Generation for Smarter LLM's
> This repository contains notes and source code provided during Dr. Mohammad Al Shaer's webinar entitled "The RAG Approach to Smarter Language Models".
> The webinar was organized by Dr. Ihab Sbeity on Monday, April 14, 2025.

## 1. Introduction & General Overview
**RAG**, or Retrieval-Augmented Generation, is a hybrid AI architecture that combines the strengths of retrieval-based and generative models. 
It enhances the capabilities of language models by integrating external knowledge sources, allowing them to generate more accurate and contextually relevant responses. 
This architecture is particularly useful in scenarios where the model needs to access up-to-date information or specialized knowledge that may not be present in its training data (for example, in legal or medical document analysis, or in enterprise knowledge management).

Such an architecture can also be used to address other major limitations of traditional language models, such as AI hallucination, by providing a mechanism for the model to verify its responses against reliable sources.

## 2. The RAG Architecture
The RAG architecture consists of the following components:
- **Chunker**: Divides the input text into smaller, more manageable bits
- **Embedder**: Converts the text chunks into vector representations
- **Vector Store**: Database optimized for similarity search
- **Retriever**: Searches the vector store for relevant chunks based on the input query
- **Generator**: LLM that uses the retrieved chunks to generate a response

## 3. Vector Embeddings and Vector Search
**Text Embeddings:** 
Vector embeddings are numerical representations of text that capture the semantic meaning of the text.
Words and phrases are converted into high-dimensional vectors, allowing for efficient similarity comparisons:
Those that have similar meanings will be positioned closer together.

**Vector Search:** 
Relationships/distances are defined by what we call 'similarity metrics', which are mathematical functions that measure the similarity between two vectors.
- **Cosine Similarity:** Measures the angle between two vectors 
- **Euclidean Distance:** Measures the straight-line distance between two points
- **Dot Product:** Calculates the product of vector elements

## 4. RAG Implementation
[]

## 5. Advanced RAG Techniques
RAG can be further enhanced by using the following advanced techniques: 

### 5.1. Query Transformation
The first technique we can look at is **query transformation**, which involves modifying the input query to improve the retrieval process.
We can do this via query expansion (enhancing queries with related terms) or query decomposition (breaking complex queries into simpler sub-queries).

### 5.2. Contextual Compression
The second technique we can look at is **contextual compression**, which aims to get rid of irrelevant information (aka additional unnecessary workload) in the retrieved documents.
This technique works by filtering irrelevant information from the retrieved documents and summarizing the document before the LLM begins processing information.
These steps ensure that the LLM is only processing relevant information, which can significantly improve the performance of the RAG model.

### 5.3. Ensemble Retrieval
The third technique is **ensemble retrieval**, which involves using multiple retrievers to gather information from different sources.
This technique can be useful when the information is spread across multiple sources or when the retriever needs to access different types of data (e.g., structured and unstructured data).
This technique can be used to improve the performance of the RAG model by ensuring that the LLM has access to a wider range of information.
This can be done by using different retrievers for different types of data or by using multiple retrievers to gather information from different sources.

### 5.4 Self-RAG and Adaptive Retrieval
[]

## 6. Evaluation Metrics
Once the output is generated, we are able to evaluate the performance of the RAG model to ensure its efficiency and accuracy. Typically, we look at two things:
1. Content Quality, and
2. Retrieval Performance

### 6.1. Content Quality
The content needs to be useful to the end user. This can be evaluated by looking at the following:
1. **Factual Correctness:** Is the content generated factually correct? Are there any faults, gaps in knowledge, or fallacies found in the generated results?
2. **Hallucination Rate:** How often does the model generate information that is not present in the retrieved documents? Is any information outputted fabricated by the model?
3. **Relevance:** Is the content relevant to the query? Does it answer the question asked?

### 6.2. Retrieval Performance
The retrieval performance can be evaluated by looking at the recall and precision of the output.
- Recall (proportion of relevant documents retrieved): ```Recall k = (number of relevant documents retrieved in top k) / (total number of relevant documents)```
- Precision (proportion of relevant documents retrieved): ```Precision k = (number of relevant documents in top k) / (k)```

## 7. Demo
A demonstration of a real-life application of RAG is provided in this repository.
To view the source code, head into the ```@/src``` directory. 

## 8. License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/myrmlbst/RAG-for-smarter-LLMs/blob/main/LICENSE) file for details.

## 9. Credits
Speaker: Mohammad Al Shaer, PhD, Software and Data Engineer
