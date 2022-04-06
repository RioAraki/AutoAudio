import requests
import SynthesisSubmitter
import AudioContext
def get_voices():
    region = 'eastus'
    key = '040924bc281a43f2959cc8d3d246a636'
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/voices'.format(region)
    header = {
        'Ocp-Apim-Subscription-Key': key
    }

    response = requests.get(url, headers=header)
    print(response.text)

def submit_synthesis():
    audioContext = AudioContext.AudioContext()
    payloadContext = AudioContext.PayloadContext('译者前言.txt', './钢铁是怎样炼成的', AudioContext.VoiceContext())
    return SynthesisSubmitter.submit_synthesis(audioContext, payloadContext)


def get_synthesis():
    url = 'https://eastus.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/fea84560-ed1a-45f2-960c-20c8038a65f2'
    key = '040924bc281a43f2959cc8d3d246a636'
    header = {
        'Ocp-Apim-Subscription-Key': key
    }
    response = requests.get(url, headers=header)
    print(response.text)


def get_files():
    id = 'fea84560-ed1a-45f2-960c-20c8038a65f2'
    region = 'eastus'
    key = '040924bc281a43f2959cc8d3d246a636'
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/{}/files'.format(region, id)
    header = {
        'Ocp-Apim-Subscription-Key': key
    }

    response = requests.get(url, headers=header)
    print('response.status_code: %d' % response.status_code)
    print(response.text)


# get_voices()
print(submit_synthesis())
# get_synthesis()
# # get_files()