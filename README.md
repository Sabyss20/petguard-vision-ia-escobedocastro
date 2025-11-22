# 🐾 PetGuard Visión IA - Análisis Automático de Imágenes Veterinarias

## 🎯 Objetivo del Proyecto

[cite_start]Este proyecto implementa el análisis automático de imágenes veterinarias (fotos de mascotas, radiografías, etc.) [cite: 14] [cite_start]utilizando modelos de **HuggingFace** en Python (Spyder)[cite: 16].

[cite_start]El objetivo principal es extraer automáticamente la siguiente información clave de la imagen[cite: 23, 24]:

* [cite_start]Especie del animal (si es posible inferir)[cite: 24].
* [cite_start]Descripción de la imagen[cite: 24].
* [cite_start]Texto detectado (si lo hay)[cite: 24].
* [cite_start]Colores dominantes (opcional)[cite: 24].

[cite_start]Esta información será utilizada para la estandarización de datos en un **JSON clínico**[cite: 15].

## 🛠️ Dependencias y Versiones

[cite_start]El proyecto fue desarrollado utilizando un entorno virtual de Conda con Python 3.10[cite: 26]. Las librerías principales utilizadas son:

* [cite_start]**Python:** 3.10 [cite: 26]
* [cite_start]**torch / torchvision / torchaudio** [cite: 28]
* [cite_start]**transformers** [cite: 29]
* [cite_start]**huggingface_hub** [cite: 29]
* **pillow** [cite: 29]
* [cite_start]**timm** [cite: 29]
* [cite_start]**matplotlib** [cite: 30]

## 🚀 Instrucciones de Ejecución

Siga estos pasos en su entorno Conda y Spyder para replicar el análisis:

### 1. Configuración del Entorno

1.  Cree y active el entorno virtual:
    ```bash
    [cite_start]conda create -n petguard python=3.10 –y [cite: 26]
    [cite_start]conda activate petguard [cite: 27]
    ```

2.  Instale las librerías necesarias:
    ```bash
    [cite_start]pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu) [cite: 28]
    [cite_start]pip install transformers huggingface_hub pillow timm [cite: 29]
    [cite_start]pip install matplotlib [cite: 30]
    ```

3.  Instale y ejecute Spyder:
    ```bash
    [cite_start]conda install spyder -y [cite: 31]
    [cite_start]spyder [cite: 32]
    ```

### 2. Ejecución del Script

1.  [cite_start]Guarde la imagen a analizar en la carpeta `/assets`[cite: 37].
2.  [cite_start]Guarde el script de análisis (por ejemplo, `vision_analysis.py`) en la carpeta `/src`[cite: 36].
3.  Abra el script en Spyder.
4.  Asegúrese de que el script cargue la imagen de `/assets`.
5.  Ejecute el script. [cite_start]Este procesará la imagen con el modelo de HuggingFace seleccionado [cite: 22] y generará el JSON con la información extraída.

---

Una vez que termine de escribir el contenido en el editor de GitHub, haga clic en el botón verde **"Commit changes..."** para guardar el archivo.

[cite_start]¿Necesitas ayuda con el contenido específico para las instrucciones de ejecución o el código Python, o quieres continuar con el **Punto 3: Diseño de un agente/bot veterinario**[cite: 43]?
