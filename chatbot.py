from dotenv import load_dotenv
import os
import gradio as gr
import importlib
import requests
import time

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVUS_API_KEY = os.getenv("TAVUS_API_KEY")

# Check for API keys to ensure they're loaded
if not GROQ_API_KEY or not TAVUS_API_KEY:
    raise ValueError("One or more API keys are missing. Please set them in your .env file.")

# Import and set up models and classes dynamically
modules = {
    'GroqModel': 'swarmauri.standard.llms.concrete.GroqModel',
    'SystemMessage': 'swarmauri.standard.messages.concrete.SystemMessage',
    'SimpleConversationAgent': 'swarmauri.standard.agents.concrete.SimpleConversationAgent',
    'MaxSystemContextConversation': 'swarmauri.standard.conversations.concrete.MaxSystemContextConversation',
}
for class_name, module_path in modules.items():
    module = importlib.import_module(module_path)
    globals()[class_name] = getattr(module, class_name)

# Initialize variables
llm = GroqModel(api_key=GROQ_API_KEY)
allowed_models = llm.allowed_models if llm.allowed_models else ["default-model"]
conversation = MaxSystemContextConversation()

# Function to load the selected model
def load_model(selected_model):
    try:
        return GroqModel(api_key=GROQ_API_KEY, name=selected_model)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Generate video from Tavus API
def generate_avatar_video(text):
    try:
        url = "https://tavusapi.com/v2/videos"
        payload = {"replica_id": "rcefb7292e", "script": text}
        headers = {"x-api-key": TAVUS_API_KEY, "Content-Type": "application/json"}
        
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        
        if response_data.get("status") != "queued":
            print("Failed to queue video generation.")
            return None, None

        video_id = response_data.get("video_id")
        video_check_url = f"https://tavusapi.com/v2/videos/{video_id}"
        return video_id, video_check_url

    except Exception as e:
        print(f"Error generating avatar video: {e}")
        return None, None

# Main conversation function
def converse(input_text, system_context, model_name, tone):
    global conversation
    conversation = MaxSystemContextConversation()
    llm = load_model(model_name)
    if not llm:
        return "Error loading language model.", gr.update(value=None)

    # Initialize conversation agent
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)
    agent.conversation.system_context = SystemMessage(content=f"{system_context}\nTone: {tone}")
    result = agent.exec(input_text)

    # Generate avatar video
    video_id, video_check_url = generate_avatar_video(result)
    if not video_id:
        return result, gr.update(value=None, label="Error generating video.")

    # Initial response with loading message
    loading_message = gr.update(value="Video is being generated, please wait...", visible=True)
    yield result, loading_message

    # Poll for video status every 5 seconds
    while True:
        time.sleep(5)
        headers = {"x-api-key": TAVUS_API_KEY}
        status_response = requests.get(video_check_url, headers=headers).json()
        print(status_response)
        
        if status_response.get("status") == "ready":
            download_url = status_response.get("download_url")
            mp4_download_url = download_url + ".mp4"  # Ensure .mp4 extension

            # Update the video component with the download URL
            yield result, gr.update(value=mp4_download_url, visible=True)
            return  # Exit once the video is ready and displayed

        print("Video generation in progress...")

# Define Gradio interface
with gr.Interface(
    fn=converse,
    inputs=[
        gr.Textbox(label="Your Input", placeholder="Type your message here..."),
        gr.Textbox(label="System Context", placeholder="Enter the system context..."),
        gr.Dropdown(label="Model Name", choices=allowed_models, value=allowed_models[0]),
        gr.Dropdown(label="Conversation Tone", choices=["Friendly", "Formal", "Casual", "Neutral", "Professional", "Empathetic", "Humorous", "Angry", "Romantic"], value="Neutral")
    ],
    outputs=[
        gr.Textbox(label="Chatbot Response"),
        gr.Video(label="Avatar Video", autoplay=True)
    ],
    title="System Context Conversation Bot with Speaking Avatar",
    description="Interact with the chatbot, and receive a lifelike video response."
) as demo:
    demo.launch(share=True)
