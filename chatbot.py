import json
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cdist

def load_and_prepare_data(file_path="intents.json"):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None, None
    
    faq_database = {}
    pattern_to_tag_map = {}
    
    for intent in data['intents']:
        tag = intent['tag']
        faq_database[tag] = intent['responses'][0]
        
        if tag not in ["fallback"]:
            all_patterns = intent['patterns'] + [tag.replace("_", " ")]
            for pattern in all_patterns:
                if pattern:
                    pattern_to_tag_map[pattern.lower()] = tag

    return faq_database, pattern_to_tag_map

def load_similarity_model():
    print("Loading the sentence similarity model... (This may take a moment on first run)")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded successfully!")
    return model

def precompute_pattern_embeddings(model, patterns):
    print("Pre-computing embeddings for all patterns...")
    pattern_embeddings = model.encode(patterns)
    print("Embeddings computed.")
    return pattern_embeddings

def get_intent_from_similarity(user_query, model, patterns, pattern_embeddings, p_to_t_map, similarity_threshold=0.6):
    query_embedding = model.encode([user_query])
    
    similarities = 1 - cdist(query_embedding, pattern_embeddings, 'cosine')[0]
    
    best_match_index = similarities.argmax()
    
    best_score = similarities[best_match_index]
    best_pattern = patterns[best_match_index]
    
    final_intent_tag = p_to_t_map[best_pattern]
    
    print(f"(Debug: Best pattern is '{best_pattern}' -> maps to '{final_intent_tag}' with similarity score {best_score:.2f})")
    
    if best_score < similarity_threshold:
        return "fallback"
        
    return final_intent_tag

def run_chatbot():
    faq_database, pattern_to_tag_map = load_and_prepare_data()
    if not faq_database or not pattern_to_tag_map:
        print("Could not start chatbot due to data loading issues.")
        return
        
    model = load_similarity_model()
    
    patterns_list = list(pattern_to_tag_map.keys())
    pattern_embeddings = precompute_pattern_embeddings(model, patterns_list)

    print("\n--- Real Estate AI Assistant (Sentence Similarity Model) ---")
    print("Ask me anything about our services! (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Glad to help. Have a great day!")
            break
            
        intent = get_intent_from_similarity(user_input, model, patterns_list, pattern_embeddings, pattern_to_tag_map)
        
        response = faq_database.get(intent, faq_database.get("fallback"))
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_chatbot()