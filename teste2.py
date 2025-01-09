import os
import sys
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor
import whisper #https://github.com/openai/whisper

async def process_files_on_demand():
    audio_dir = os.path.join(os.path.dirname(__file__), 'audios/')

    with ProcessPoolExecutor(max_workers=4) as executor:
        tasks = []
        model = whisper.load_model("medium")
        loop = asyncio.get_running_loop()

        for audio_path in get_files_path(audio_dir):
            print(f'Audio => {audio_path}')

            tasks.append(loop.run_in_executor(executor, process_file, audio_path, model))

        await asyncio.gather(*tasks) #spread loop executor func



def get_files_path(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        yield filepath



def process_file(audio_path, model):
    print(f'Processing Audio => {audio_path}')

    result = model.transcribe(audio_path, language='pt', fp16=False)

    print('\n=============TEXTO=================\n')
    print(result['text'])
    print('\n=============TEXTO=================\n')



if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(process_files_on_demand())
    end_time = time.time()

    print(f'\n============TEMPO {end_time - start_time} Segundos==================')