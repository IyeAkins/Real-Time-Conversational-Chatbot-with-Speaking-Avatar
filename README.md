# Real-Time-Conversational-Chatbot-with-Speaking-Avatar

This documentation provides a comprehensive overview of the **Conversational AI System with a Speaking Avatar**, which enables real-time interaction with an AI-driven avatar that responds visually and verbally with synchronized gestures and expressions.

## Overview

The Conversational AI System creates an immersive, lifelike experience by combining a language model for real-time dialogue with an avatar capable of gestures and expressions. Through an intuitive Gradio interface, users engage in seamless conversations and receive visual feedback from a speaking avatar.

## Key Features

- **Real-time language processing**: Powered by GroqModel, facilitating natural conversation flow.
- **AI-generated avatar video responses**: Tavus API creates lifelike videos with gestures and facial expressions.
- **Customizable conversational tones**: Supports multiple tones like friendly, professional, and humorous.
- **Simple user interface**: Built with Gradio for streamlined accessibility and ease of use.
  
## System Components

### Model Framework: Swarmauri with GroqModel

The system employs **GroqModel**, a powerful language model accessed through the Swarmauri framework. GroqModel offers real-time processing, essential for maintaining fluid interaction. It was chosen because it balances flexibility and performance, handling tone adjustments and rapid response generation.

- **Dynamic tone control**: GroqModel supports nuanced tones, enriching the conversation experience.
- **Efficient real-time response handling**: The model is optimized for quick replies, minimizing delays and enhancing responsiveness.
- **Adaptability**: Various configurations are possible, making it suitable for diverse conversational needs.

### Avatar Framework: Tavus API

The **Tavus API** generates an AI avatar video that mirrors the conversational tone through gestures and expressions. Tavus was selected due to its advanced animation capabilities, producing videos with human-like facial expressions and body language in sync with the spoken content. 

- **Realistic responses**: Tavus avatars replicate human gestures and expressions, adding a visual component to the conversation.
- **Reliable video generation**: Tavus enables synchronous verbal and nonverbal feedback, providing a more immersive experience.
- **Flexible configurations**: Tavus supports a variety of avatar styles, broadening customization options.

### Interface Framework: Gradio

**Gradio** was used to create the user interface for this system. Gradio was chosen because it provides a seamless way to integrate complex AI models and avatar interactions into an accessible, user-friendly interface. Gradio offers:

- **Rapid prototyping**: Simplifies creating web-based interfaces, enabling quick deployment and testing.
- **User-friendly components**: Includes widgets like text boxes, dropdowns, and video players that streamline interactivity.
- **Flexible deployment**: Gradio provides a public URL for the application, making it accessible to users without requiring complex deployment setups.

Gradio’s flexible design allows for smooth integration of API responses and video playback, letting users experience text and video responses side-by-side without noticeable delay. Additionally, Gradio’s video component supports autoplay, which enhances the interactive experience with the avatar.

## Deployment

Gradio provides a **public URL** that enables the application to be accessed by anyone with an internet connection, without requiring additional deployment configurations. This public URL is especially valuable for quick sharing, allowing easy testing and user feedback collection.

Deployment with Gradio involves simply running the `.launch()` function in the code, which generates a temporary link that can be accessed directly or embedded into other sites. For larger deployments, Gradio interfaces can also be hosted on cloud services, further extending accessibility.

Here are the setup instructions for the Real-Time Conversational AI System with a Speaking Avatar:

---

### Setup Instructions

1. **Install Required Python Packages**
   - Make sure you have Python installed (preferably version 3.8 or above).
   - Install the following dependencies:
     ```bash
     pip install gradio requests python-dotenv
     pip install "swarmauri[full]==0.4.1"
     ```

2. **Obtain API Keys**
   - **GroqModel API Key**: Register on Swarmauri’s platform to get access to GroqModel and obtain your API key.
   - **Tavus API Key**: Sign up on Tavus API's website, navigate to your account settings, and create an API key.

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory of the project, and add your API keys:
     ```bash
     touch .env
     ```
   - Open the `.env` file and add the following lines:
     ```plaintext
     GROQ_API_KEY=<your_groqmodel_api_key>
     TAVUS_API_KEY=<your_tavus_api_key>
     ```
   - Replace `<your_groqmodel_api_key>` and `<your_tavus_api_key>` with your actual API keys.

4. **Run the Application**
   - Start the Gradio app by running the Python script:
     ```bash
     python <your_script_name>.py
     ```
   - Replace `<your_script_name>` with the name of your Python file containing the code.

5. **Access the Application**
   - Once the script runs, Gradio will launch a local interface, and you’ll see a public URL generated in the terminal.
   - Open the URL in a browser to access the application.
