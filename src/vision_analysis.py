# -*- coding: utf-8 -*-
"""
Análisis automático de imagen veterinaria para PetGuard Perú
"""

import json
from datetime import datetime
from transformers import pipeline
from PIL import Image
import numpy as np
from collections import Counter

# --------------------------------------------------------------
# CONFIGURACIÓN: CAMBIA SOLO ESTA LÍNEA
# --------------------------------------------------------------

RUTA_IMAGEN = r"C:\Users\AlumnoCA270117\Pictures\prueba.jpg"   # <-- CAMBIA AQUÍ


# Modelos HuggingFace
MODELO_CLASIFICACION = "google/vit-base-patch16-224"
MODELO_DESCRIPCION = "nlpconnect/vit-gpt2-image-captioning"
MODELO_OCR = "microsoft/trocr-base-printed"

# --------------------------------------------------------------
# FUNCIONES
# --------------------------------------------------------------

def inferir_especie(label):
    label = label.lower()
    if "cat" in label:
        return "gato"
    if "dog" in label:
        return "perro"
    if any(x in label for x in ["bird", "parrot"]):
        return "ave"
    if "horse" in label:
        return "caballo"
    if any(x in label for x in ["rabbit", "hare"]):
        return "conejo"
    if any(x in label for x in ["monkey", "tiger", "leopard", "lion", "hamster", "ferret"]):
        return "animal exótico"
    return "no identificado"


def colores_dominantes(img, k=3):
    img = img.resize((80, 80))
    datos = np.array(img).reshape(-1, 3)
    counts = Counter([tuple(px) for px in datos])
    comunes = counts.most_common(k)
    
    resultado = []
    total = sum(counts.values())
    for color, cnt in comunes:
        r, g, b = color
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        resultado.append({
            "rgb": {"r": r, "g": g, "b": b},
            "hex": hex_color,
            "proporcion": round(cnt / total, 3)
        })
    return resultado


# --------------------------------------------------------------
# CARGA DE MODELOS
# --------------------------------------------------------------

print("Cargando modelos, espera un momento...")

clasificador = pipeline("image-classification", model=MODELO_CLASIFICACION)
descripcionador = pipeline("image-to-text", model=MODELO_DESCRIPCION)
ocr_reader = pipeline("image-to-text", model=MODELO_OCR)

# --------------------------------------------------------------
# PROCESAMIENTO DE LA IMAGEN
# --------------------------------------------------------------

imagen = Image.open(RUTA_IMAGEN).convert("RGB")

# 1. CLASIFICACIÓN
pred = clasificador(imagen)[0]
label = pred['label']
score = float(pred['score'])
especie = inferir_especie(label)

# 2. DESCRIPCIÓN
descripcion = descripcionador(imagen)[0]["generated_text"]

# 3. OCR
texto = ocr_reader(imagen)[0]["generated_text"]

# 4. COLORES
colores = colores_dominantes(imagen)

# --------------------------------------------------------------
# JSON CLÍNICO
# --------------------------------------------------------------

json_clinico = {
    "clinica": "PetGuard Perú",
    "fecha": datetime.now().isoformat(),
    "imagen": RUTA_IMAGEN,
    "resultados": {
        "especie_probable": especie,
        "label_original": label,
        "confianza_label": round(score, 3),
        "descripcion_automatica": descripcion,
        "texto_detectado": texto,
        "colores_dominantes": colores
    }
}

print("\n=== RESULTADO JSON CLÍNICO ===\n")
print(json.dumps(json_clinico, indent=2, ensure_ascii=False))

# Guardar JSON
with open("resultado_petguard.json", "w", encoding="utf-8") as f:
    json.dump(json_clinico, f, indent=2, ensure_ascii=False)

print("\nArchivo guardado como resultado_petguard.json")
