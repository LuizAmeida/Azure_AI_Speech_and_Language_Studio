# =========================================================
# PROJETO: Azure AI Multi-Service (Speech & Language)
# ANALISTA: Luiz (Teteo)
# DESCRIÇÃO: Integração de serviços de IA para Texto e Voz.
# =========================================================

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
from azure.core.credentials import AzureKeyCredential

# --- CONFIGURAÇÃO DE LINGUAGEM ---
def analyze_text_features(text):
    print(f"\n--- Analisando Texto ---")
    endpoint = "SEU_ENDPOINT_LANGUAGE"
    key = "SUA_CHAVE_LANGUAGE"
    
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    response = client.analyze_sentiment(documents=[text])[0]
    
    print(f"Sentimento: {response.sentiment}")
    print(f"Confiança: P:{response.confidence_scores.positive} N:{response.confidence_scores.negative}")

# --- CONFIGURAÇÃO DE FALA (SPEECH) ---
def recognize_speech_from_mic():
    print(f"\n--- Analisando Voz (Speech-to-Text) ---")
    speech_key = "SUA_CHAVE_SPEECH"
    service_region = "eastus" # Exemplo

    speech_config = SpeechConfig(subscription=speech_key, region=service_region)
    speech_recognizer = SpeechRecognizer(speech_config=speech_config)

    print("Diga algo no microfone...")
    result = speech_recognizer.recognize_once()
    
    if result.reason == result.reason.RecognizedSpeech:
        print(f"Texto Reconhecido: {result.text}")
    else:
        print("Não foi possível reconhecer a fala.")

if __name__ == "__main__":
    # Simulação para o laboratório
    texto_exemplo = "A tecnologia de IA da Microsoft é impressionante e facilita o trabalho do analista."
    analyze_text_features(texto_exemplo)
    
    # Nota: A função de voz requer hardware e assinatura ativa.
    print("\n[INFO] Módulo de Voz pronto para integração via SDK.")