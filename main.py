# Яблоко

import config
import stt
import tts
import random
import wave
import pyaudio
import subprocess


print(f"{config.VA_NAME} начало свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # Обращаются к ассистенту

        if len(voice.split(' ')) > 1:
            send_to_gpt(voice.removeprefix(voice.split(' ')[0]))
            return

        num = random.randint(1, 4)

        play(f'audios/mention_{num}.wav')



def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    return cmd


def send_to_gpt(text):

    # Отправка разпознанного с микрофона текста нейросети для генерации текста
    # Тут надо получить текст в ответ от нейросети (переменная 'response')

    # API GIGACHAT на моем компьютере для тестирования работы программы:
    # ------------------------------------------------------------------
    bash_command = f'bash /home/alex/Scripts/GigaChat.sh "{text}"'
    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    response = output.decode()
    # ------------------------------------------------------------------
    print(response)
    
    # Синтез речи из ответа нейросети (текст)
    tts.synthesize('audio', response)
    print('Запуск пригрывания аудио')
    play('audio.wav')



def play(audio):
    CHUNK = 1024

    with wave.open(audio, 'rb') as wf:
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        stream.close()

        p.terminate()


# Начать прослушивание команд
stt.va_listen(va_respond)