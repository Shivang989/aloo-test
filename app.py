import subprocess, time, urllib.request, gradio as gr

subprocess.run(["npm", "install"], check=True)
subprocess.run(["npm", "run", "build"], check=True)
subprocess.Popen(["npm", "start"])
time.sleep(2)

def check_ts():
    try:
        return urllib.request.urlopen("http://127.0.0.1:3000", timeout=2).read().decode()
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## TypeScript + Gradio Test")
    out = gr.Textbox(value=check_ts, label="TypeScript Backend Status")
    gr.Button("Refresh").click(fn=check_ts, outputs=out)

demo.launch(server_name="0.0.0.0", server_port=7860)
