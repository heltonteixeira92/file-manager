from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello world!'}


@app.post('/files')
def create_file(file: Annotated[bytes, File()]):
    return {'file_size': len(file)}


@app.post('/upload-files')
def create_upload_file(file: UploadFile):
    return {'filename': file.filename}
