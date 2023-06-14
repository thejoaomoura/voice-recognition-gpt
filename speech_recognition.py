{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMWsIbxYBjbbGI3p4emt31J"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uAzUh5W8MHSX"
      },
      "outputs": [],
      "source": [
        "!pip install SpeechRecognition"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install openai"
      ],
      "metadata": {
        "id": "OHFqjc2EOSpC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import speech_recognition as sr\n",
        "import openai\n",
        "\n",
        "openai.api_key = \"CHAVE_API_OPENAI\" #substitua pela sua chave\n",
        "\n",
        "def speech_to_text(audio_file):\n",
        "    recognizer = sr.Recognizer()\n",
        "\n",
        "    with sr.AudioFile(audio_file) as source:\n",
        "        audio_data = recognizer.record(source)\n",
        "\n",
        "    try:\n",
        "        text = recognizer.recognize_google(audio_data, language=\"pt-BR\")\n",
        "        print(\"Texto reconhecido:\", text, end=\"\")\n",
        "        return text\n",
        "    except sr.UnknownValueError:\n",
        "        print(\"Google Speech Recognition não entendeu o áudio\")\n",
        "    except sr.RequestError as e:\n",
        "        print(f\"Não foi possível solicitar resultados do serviço Google Speech Recognition; {e}\")\n",
        "\n",
        "def text_to_gpt(text):\n",
        "    # Envia uma consulta ao chatgpt 3.5 e recebe uma resposta corrigida e pontuada\n",
        "    response = openai.ChatCompletion.create(\n",
        "        model=\"gpt-3.5-turbo-0613\",\n",
        "        messages=[\n",
        "            {\"role\": \"system\", \"content\": \"Você é um corretor de escrita formal de Português.\"},\n",
        "            {\"role\": \"user\", \"content\": f\"Corrija os erros de português e adicione pontuação ao texto a seguir:\\n\\n{text}\"},\n",
        "        ]\n",
        "    )\n",
        "    corrected_text = response[\"choices\"][0][\"message\"][\"content\"]\n",
        "    print(\"\\nTexto corrigido📝:\", corrected_text)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    audio_file = \"/content/sample_data/Audio-2.wav\" #substitua pelo diretório do seu arquivo de áudio em wav\n",
        "    text = speech_to_text(audio_file)\n",
        "    text_to_gpt(text)"
      ],
      "metadata": {
        "id": "Duu35XeuMjxj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "rOw3SEdLOeqk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}