import flask
import os
import openai
import gradio as gr


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The Following Is a Coversation with an AI assistant . The Assistant is helpful,  creative, clever, and very friendly.\n\nHuman: hello, who are you?\nAI: I am an AI created by weybre. How can I help you today?\nHuman; "

def openai_create(prompt):
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" human:", " AI:"]
    )

    return response.choices[0].text


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Weybre Gider Gradio</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Send")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)

if __name__ == '__main__':
    app.run('http://gidergradio.weybre.com/', )
