# Placeholder for BERT model
# In a real project, this would load a trained BERT model
def predict_anxiety(text):
    if "nervous" in text or "scared" in text:
        return "High"
    elif "worried" in text:
        return "Moderate"
    else:
        return "Low"
