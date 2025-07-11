import asyncio
import streamlit as st
from streamlit_ace import st_ace
from helpers.sidebar import show as show_sidebar
import helpers.util
from services import prompts, llm

st.set_page_config(
    page_title="Generate Code Page",
    page_icon="🖥️",
    layout="wide"
)
st.title('Generate Code Page')

show_sidebar()

# Constants
INITIAL_CODE = ''

language = ''

if "user_code" not in st.session_state:
    st.session_state.user_code = INITIAL_CODE


# Code Editor
code: str = st_ace(value=INITIAL_CODE,
                  language='',
                  placeholder='This is placeholder text when no code is present',
                  theme='solarized_light',
                  keybinding='vscode',
                  font_size=14,
                  tab_size=4,
                  wrap=False,
                  show_gutter=True,
                  show_print_margin=True,
                  auto_update=False,
                  readonly=False,
                  key='editor-basic')
st.markdown("<br>", unsafe_allow_html=True)


# Explicitly cache buttons
review_button = st.sidebar.button("Review Code")
debug_button = st.sidebar.button("Debug Code")
error_string = st.sidebar.text_input("Optional Error String", key="error_string")
modify_button = st.sidebar.button("Modify Code")
modification_instructions = st.sidebar.text_input("Modification Instructions", key="modification_instructions")
placeholder = st.empty()

review = review_button
debug = debug_button
modify = modify_button

user_code = code
modification_history = []
# Initialize modification_history in session state if it doesn't exist
if "modification_history" not in st.session_state:
    st.session_state.modification_history = []

# Use st.session_state.modification_history instead of modification_history
if review or debug or modify:
    advice = st.markdown("### Ducky Assisting...")
    learning_prompt = ''
    if review:
        learning_prompt = prompts.review_prompt(user_code, language )
    elif debug:
        # Include optional error string for debugging
        learning_prompt = prompts.debug_prompt(user_code, language, error_string)
    elif modify:
        # Update code with previous modifications
        modified_code = user_code
        for modification in st.session_state.modification_history:
            modified_code = prompts.modify_code_prompt(modified_code, language, modification)
        # Add current modification instructions
        modification_instructions = modification_instructions.strip()  # Remove leading/trailing whitespace
        st.session_state.modification_history.append(modification_instructions)
        learning_prompt = prompts.modify_code_prompt(modified_code, language, modification_instructions)

    messages = llm.create_conversation_starter('')
    messages.append({"role": "user", "content": learning_prompt})
    modified_code = asyncio.run(helpers.util.run_conversation(messages, advice))
    user_code = modified_code  # Update user code with the latest modification

# Reset Feature
reset_button = st.button('Reset Page')
if reset_button:
    st.session_state.code = INITIAL_CODE
    st.session_state.modification_history = []  # Clear modification history
    st.experimental_rerun()
