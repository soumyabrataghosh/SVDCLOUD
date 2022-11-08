import streamlit as st

# #Generations page
# st.markdown('Generations')
# st.sidebar.markdown('Generations')

# #Evaluations Page
# st.markdown('Evaluations')
# st.sidebar.markdown('Evaluations')

# #Benchmarking Page
# st.markdown('Benchmarking')
# st.sidebar.markdown('Benchmarking')


def navbar_component():
    with open("assets/images/settings.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

    component = rf'''
            ....
    '''
    st.markdown(component, unsafe_allow_html=True)
    
    js = '''
    <script>
    ....
    </script>
    '''
    html(js)

st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")