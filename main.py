import uvicorn

if __name__ == '__main__':
    uvicorn.run('Text:app', host='0.0.0.0',
                port=1703, reload=True, debug=True)
