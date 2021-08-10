from fastapi import FastAPI
#import time
import asyncio
import socket
app = FastAPI()

def func_1():
    #print('func_1 start...')
    #await asyncio.sleep(10)
    #print('func_1 end...')
    return 'func_1'

def func_2():
    #print('func_2 start...')
    #await asyncio.sleep(15)
    #print('func_2 end...')
    return 'func_2'

@app.get('/')
async def root_dir():
    #start = time.time()
    #a, b = await asyncio.gather(func_1(), func_2())
    a = func_1()
    b = func_2()
    #end = time.time()
    #print('time consumed : {}'.format(round(end-start)))
    return {
        'a':a,
        'b':b,
        'hostname':socket.gethostname()
    }
