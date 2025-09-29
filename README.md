AIM:
The aim of this project is to design and develop an intelligent, NLP-powered chatbot to automate responses to frequently asked questions (FAQs) for a real estate agency. The system leverages modern sentence-embedding models to understand and classify user queries based on semantic meaning rather than just keywords.

OBJECTIVE:
The primary objectives to achieve the project's aim were:
1. To curate a comprehensive knowledge base of real estate FAQs and structure it in a machinereadable intents.json format.
2. To implement a modern NLP model (sentence-transformers) to convert both user queries and predefined questions into meaningful numerical vectors (embeddings).
3. To develop a robust intent classification system by calculating the cosine similarity between user input and the known question patterns.
4. To create an interactive command-line interface (CLI) that allows a user to converse with the chatbot in real-time.
5. To implement a fallback mechanism to gracefully handle out-of-scope or misunderstood questions, ensuring a user-friendly experience.

OUTCOMES:
The project successfully resulted in the following outcomes:
1. A functional, interactive AI chatbot that runs in the command line.
2. The system accurately classifies a wide variety of user queries, including those phrased conversationally or informally, by matching them to the correct intent.
3. The chatbot demonstrates a strong understanding of semantic meaning, correctly identifying user intent even when no keywords overlap (e.g., mapping "I've never bought a home before..." to the buyer_process_overview intent).
4. A structured and easily expandable knowledge base (intents.json) was created, allowing the agency to add, remove, or modify questions and answers without changing the core program code.
5. The project serves as a successful proof-of-concept, demonstrating the effectiveness of sentence embeddings and cosine similarity as a superior alternative to basic keyword matching for building intelligent FAQ systems.

Chatbot Testing: 
<img width="994" height="476" alt="image" src="https://github.com/user-attachments/assets/f98c399c-2142-43a5-a4ce-fe444d7d3bbc" />
Fallbacks:
<img width="996" height="189" alt="image" src="https://github.com/user-attachments/assets/2dffed92-d83a-43bd-9752-857a11b1cf65" />

CONCLUSION:
In conclusion, this project successfully delivered a functional AI chatbot for the real estate industry. By leveraging a sentence-transformer model for semantic similarity, the chatbot accurately interprets user intent from natural language, going beyond simple keyword matching to understand the true meaning behind queries. The system's modular design ensures easy maintenance and provides a strong foundation for future enhancements, such as web deployment and more advanced conversational capabilities.

