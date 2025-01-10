## Speech Recognition

This is a POC (Proof of Concept) for turning speech into text, validate accuracy and text precision and how much time is spent doing it.

## Python Virtual Env

To generate a virtual env run `python -m venv venv`.

To activate run `source venv/bin/activate`

## Install requirements

Run `pip install -r requirements.txt`


## Test scenarios

1 - Running `python teste.py` the process will be single threaded and blocking. It means that Python will perform speech recognition one by one because Whisper transcribe is a slow process due to its CPU intensive nature.

2 - Running `python teste2.py` the process will make Multi Processing and non-blocking. It means that Python will perform speech recognition of all files in parallel due to the process of dividing between CPU cores, making each process independent.


The process will be try to handled in asynchronous way due to *asyncio* is used to deal with concurrent code using the async/await syntax.

<br/>

## Related Links
- [https://numpy.org/](https://numpy.org/)
- [https://github.com/openai/whisper](https://github.com/openai/whisper)
- [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)
- [https://docs.python.org/3/library/concurrent.futures.html](https://docs.python.org/3/library/concurrent.futures.html)
