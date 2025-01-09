import os
import sys
import time
import asyncio
import whisper #https://github.com/openai/whisper

async def process_files_on_demand():
    audio_dir = os.path.join(os.path.dirname(__file__), 'audios/')
    model = whisper.load_model("medium")
    tasks = []

    for audio_path in get_files_path(audio_dir):
        print(f'Audio => {audio_path}')

        tasks.append(process_file(audio_path, model))


    await asyncio.gather(*tasks)


def get_files_path(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        yield filepath


async def process_file(audio_path, model):
    print(f'Processing Audio => {audio_path}')
    result = model.transcribe(audio_path, language='pt', fp16=False)

    print('\n=============TEXTO=================\n')
    print(result['text'])
    print('\n=============TEXTO=================\n')


start_time = time.time()
asyncio.run(process_files_on_demand())
end_time = time.time()

print(f'\n============TEMPO {end_time - start_time} Segundos==================')