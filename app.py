import gradio as gr
from langflow import start_langflow

# Titel und kurze Beschreibung für dein Space
title = "RPG Agent DEMO"
description = "Ein einfacher Langflow-Agent, der als RPG-Character agiert."

# Funktion die Langflow startet
def launch_langflow():
  # Startet die Langflow-Oberfläche dierkt im Space
  start_langflow()

# Gradio Interface (Button zum Starten)
with gr.Blocks() as demo:
  gr.Markdown(f"# {title}\n{description}")
  gr.Button("Starte Langflow").click(fn=launch_langflow)

if __name__ == "__main__":
  demo.launch()
