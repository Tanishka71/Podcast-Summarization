import streamlit as st
import glob
import json
from api_communication import save_transcript

st.title("Podcast Summaries")

json_files = glob.glob('*.json')

episode_id = st.sidebar.text_input("Episode ID")
button = st.sidebar.button("Download Episode summary", on_click=save_transcript, args=(episode_id,))


def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t


if button:
    filename = episode_id + '_chapters.json'
    print(filename)
    with open(filename, 'r') as f:
        data = json.load(f)

    chapters = data['chapters']
    episode_title = data['episode_title']
    episode_thumbnail = data['episode_thumbnail']
    podcast_title = data['podcast_title']
    # audio = data['audio_url']

    st.header(f"{podcast_title} - {episode_title}")
    st.image(episode_thumbnail, width=200)
    st.markdown(f'#### {episode_title}')

    for chp in chapters:
        with st.expander(chp['gist'] + ' - ' + get_clean_time(chp['start'])):
            chp['summary']


# from api_communication import *
# import streamlit as st
# import json

# st.title('Welcome to my application that creates podcast summaries')
# episode_id=st.sidebar.text_input('Please iput an episode id')
# button=st.sidebar.button('Get podcast summary!', on_click=save_transcript, args={episode_id,})

# if button:
#     filename=episode_id + '_chapters.json'
#     with open(filename,'r') as f:
#         data=json.load(f)

#         chapters=data['chapters']
#         podcast_title=data['podcast_title']
#         episode_title=data['episode_title']
#         episode_thumbnail=data['episode_thumbnail']

#     st.header(f'{podcast_title} - {episode_title}')
#     st.image(episode_thumbnail)
#     for chap in chapters:
#         with st.expander(chap['gist']):
#             chap['summary']
# save_transcript("71de733737a74d4994b0d4d58ebbeafe")