{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-08 20:28:23.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.157 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.157 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.173 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.173 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.173 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.173 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.189 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-08 20:28:23.189 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import whisper\n",
    "import openai\n",
    "import os\n",
    "\n",
    "# Set your OpenAI API key here or use environment variable\n",
    "openai.api_key = os.getenv(\"OPENAI_API_KEY\")\n",
    "\n",
    "# Load Whisper model\n",
    "@st.cache_resource\n",
    "def load_model():\n",
    "    return whisper.load_model(\"base\")\n",
    "\n",
    "model = load_model()\n",
    "\n",
    "# UI\n",
    "st.title(\"🎙️ Grammar Scoring System for Spoken Audio\")\n",
    "st.write(\"Upload an audio file (WAV, MP3, M4A) to get a grammar score and feedback.\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload audio\", type=[\"wav\", \"mp3\", \"m4a\"])\n",
    "\n",
    "if uploaded_file:\n",
    "    st.audio(uploaded_file)\n",
    "\n",
    "    with st.spinner(\"Transcribing with Whisper...\"):\n",
    "        # Save file locally\n",
    "        with open(\"temp_audio\", \"wb\") as f:\n",
    "            f.write(uploaded_file.read())\n",
    "        # Transcribe\n",
    "        result = model.transcribe(\"temp_audio\")\n",
    "        transcription = result[\"text\"]\n",
    "\n",
    "    st.markdown(\"### 📝 Transcribed Text:\")\n",
    "    st.write(transcription)\n",
    "\n",
    "    with st.spinner(\"Evaluating grammar with GPT-4...\"):\n",
    "        prompt = f\"\"\"\n",
    "You are a grammar evaluator. A user has spoken the following text:\n",
    "\n",
    "\\\"{transcription}\\\"\n",
    "\n",
    "Your task:\n",
    "1. Score the grammar on a scale of 0 to 100.\n",
    "2. List grammatical errors with brief explanations.\n",
    "3. Suggest improvements.\n",
    "\n",
    "Respond in this format:\n",
    "Score: <score>/100\n",
    "\n",
    "Mistakes:\n",
    "- <mistake 1>\n",
    "- <mistake 2>\n",
    "\n",
    "Suggestions:\n",
    "- <suggestion 1>\n",
    "- <suggestion 2>\n",
    "\"\"\"\n",
    "\n",
    "        response = openai.ChatCompletion.create(\n",
    "            model=\"gpt-4\",\n",
    "            messages=[{\"role\": \"user\", \"content\": prompt}],\n",
    "            temperature=0.5\n",
    "        )\n",
    "\n",
    "        feedback = response.choices[0].message.content\n",
    "        st.markdown(\"### 📊 Grammar Feedback:\")\n",
    "        st.text(feedback)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
