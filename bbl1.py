with open('new.bbl', 'r') as input_file:
    lines = input_file.readlines()
     
with open("new1.bbl", "w") as output_file:
    for line in lines:
        if line.strip().startswith('{'):
            output_file.write(line)

# import re 
# name = "021.wav"
# name = re.sub("wav","")
# print(name)

# import re

# # Your input string
# text = r'{\it Accessibility.}'

# # Regex pattern
# pattern = r'\\it\s(.*)'

# # Find the pattern after \it
# match = re.search(pattern, text)

# # Print the result
# if match:
#     print(match.group(1))
# import audioread

# def get_mp3_duration(file_path):
#     with audioread.audio_open(file_path) as f:
#         duration = f.duration
#         return duration


# file_path = "audio_file.mp3"
# print(get_mp3_duration(file_path))



# import requests
# import audioread

# def download_audio_from_url(url, save_path):
#     url = f'http://115.241.55.85/call_record/recordings/{url}.wav'
#     response = requests.get(url)
#     with open(save_path, 'wb') as f:
#         f.write(response.content)

# def get_mp3_duration_from_url(url):
#         save_path = 'downloaded_audio.mp3'
#         download_audio_from_url(url, save_path)
#         with audioread.audio_open(save_path) as f:
#             duration = f.duration
#             return duration
# url = '1709645983.5292'
# # print(get_mp3_duration_from_url(url))

# def find_duration(url):
#     # url = '1709645983.5292'
#     get_mp3_duration_from_url(url)
#     if duration>20:
#         print('manish')
#     else:
#         print("anish")
# url = '1709645983.5292'   
# print(find_duration(url))    
    

# a = " "

# b = f"sonu {a}"

# print(b)

