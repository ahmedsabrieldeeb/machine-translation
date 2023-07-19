import gradio as gr
from model.model import Translate

model_path = "model/model.h5"

def translate_sentence(english_sentence):
    translator = Translate(model_path)
    french_sentence = translator.translate(english_sentence)
    return french_sentence

english_input = gr.inputs.Textbox(label="English Sentence", placeholder="Enter your sentence here")
french_output = gr.outputs.Textbox(label="French Translation")

iface = gr.Interface(fn=translate_sentence, inputs=english_input, outputs=french_output)

iface.launch(share=True)