import json


class AudioContext:
    def __init__(self, region='eastus', key='040924bc281a43f2959cc8d3d246a636'):
        self.region = region
        self.key = key
        self.header = {'Ocp-Apim-Subscription-Key': self.key}
        self.url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis'.format(region)


class PayloadContext:
    def __init__(self, filename, filepath, voiceContext, outputformat='riff-16khz-16bit-mono-pcm', concatenateResult=True):
        self.displayName = filename
        self.description = filename
        self.filepath = filepath
        self.voiceContext = voiceContext
        self.outputFormat = outputformat
        self.concatenateResult = concatenateResult
        self.inputPath = filepath
        self.outputPath = filepath+"Audio"

    def getPayload(self):
        return {
            'displayname': self.displayName,
            'description': self.description,
            'locale': self.voiceContext.locale,
            'voices': json.dumps([{'voicename': self.voiceContext.voiceName}]),
            'outputformat': self.outputFormat,
            'concatenateresult': self.concatenateResult
        }

    def getFiles(self):
        return {
            'script': (self.displayName, open(self.inputPath+"/"+self.displayName, 'rb'), 'text/plain')
        }

class VoiceContext:
    def __init__(self, voiceName='zh-CN-YunxiNeural', locale='zh-CN'):
        self.locale = locale
        self.voiceName = voiceName




