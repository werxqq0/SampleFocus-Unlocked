import os
import requests
import json
from bs4 import BeautifulSoup

download_folder = 'samplefocus_export'

print('SampleFocus Unlocked 1.0.1\nMade by werxqq0\nhttps://github.com/werxqq0/SampleFocus-Unlocked\n')

while True:
    music_link = input('Music Link: ')

    def download_music(link):
        if link.startswith('https://samplefocus.com/'):
            os.makedirs(download_folder, exist_ok=True)
            def download_system(url):
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    sample_waveform_div = soup.find('div', {'data-react-class': 'SampleWaveform'})

                    if sample_waveform_div:
                        data_react_props = sample_waveform_div.get('data-react-props')

                        props_json = json.loads(data_react_props)

                        music_url = props_json.get('sample').get('sample_mp3_url')

                        if music_url:
                            file_name = os.path.basename(f'{music_link}.mp3')
                            file_path = os.path.join(download_folder, file_name)

                            response = requests.get(music_url)
                            if response.status_code == 200:
                                with open(file_path, 'wb') as file:
                                    file.write(response.content)
                                print(f'File {file_name} downloaded successfully.')
                            else:
                                print(f'Cannot download file {file_name}!')
                        else:
                            print('Could not find a link to download music on the page!')
                    else:
                        print('The download element could not be found on the page!')
                else:
                    print('This audio does not exist!')

            download_system(music_link)
        else:
            print('This link is not a SampleFocus site!')
            return False

    download_music(music_link)
