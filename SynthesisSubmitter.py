import requests

# returns the url that represents azure async task to transfer the text to audio
def submit_synthesis(audioContext, payloadContext):
    response = requests.post(audioContext.url,
                             payloadContext.getPayload(),
                             headers = audioContext.header,
                             files = payloadContext.getFiles())
    print(response.headers['Location'])

    return response.headers['Location']
