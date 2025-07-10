from transformers import pipeline

# Use smaller models to save memory
ner_pipeline = pipeline("token-classification", model="Davlan/distilbert-base-multilingual-cased-ner-hrl", aggregation_strategy="simple")
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)


def ner(text):
    return ner_pipeline(text)

def sentiment(text):
    try:
        return [sentiment_pipeline(text)]
    except Exception as e:
        return {"error": str(e)}

def emotion(text):
    result = emotion_pipeline(text)
    # ✅ Fix: return inner list directly
    if isinstance(result, list) and len(result) == 1 and isinstance(result[0], list):
        return result[0]
    return result

