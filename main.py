import pyttsx4

engine = pyttsx4.init()

# Configurar a voz (usando índice ou ID)
voices = engine.getProperty('voices')

# Alterar para uma voz específica (exemplo: primeira voz da lista)
engine.setProperty('voice', voices[0].id)

# Ajustar outras propriedades (opcional)
engine.setProperty('rate', 150)  # Velocidade
engine.setProperty('volume', 0.8)  # Volume (0.0 a 1.0)

engine.say("Olá, mundo! Estou usando pyttsx4.")
engine.runAndWait()
