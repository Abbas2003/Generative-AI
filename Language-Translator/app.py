import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load the model and tokenizer once at the start
@st.cache_resource
def load_model_and_tokenizer():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()

# Streamlit UI
st.title("English to Multiple Language Translator")
st.write("Translate English text into different languages using AI.")

# Sidebar for settings
st.sidebar.title("Settings")

# Dark mode toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

# Custom CSS for dark and light mode
if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #2e2e2e;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput>div>input {
            background-color: #4b4b4b;
            color: white;
            border: 1px solid #ccc;
        }
        .stSidebar {
            background-color: #383838;
        }
        .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar .markdown-text-container {
            color: #FFFFFF;
        }
        .stSidebar a {
            color: #1f77b4;
        }
        .stSidebar .stCheckbox div {
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #000000;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
        }
        .stTextInput>div>input {
            background-color: #FFFFFF;
            color: black;
            border: 1px solid #ccc;
        }
        .stSidebar {
            background-color: #f0f2f6;
        }
        .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar .markdown-text-container {
            color: #000000;
        }
        .stSidebar a {
            color: #1f77b4;
        }
        .stSidebar .stCheckbox div {
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Input text
input_text = st.text_area("Enter English text:", value="")

# Sidebar for language selection
st.sidebar.subheader("Select Target Language")

language_options = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh",
    "Arabic": "ar",
    "Hindi": "hi",
    "Japanese": "ja",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Urdu": "ur"  # Added Urdu language
}

selected_language = st.sidebar.selectbox("Target Language", list(language_options.keys()))

if st.button("Translate"):
    if input_text:
        # Interactive loading state
        with st.spinner('Translating... Please wait...'):
            # Set target language
            target_language = language_options[selected_language]
            tokenizer.src_lang = "en"
            encoded_input = tokenizer(input_text, return_tensors="pt")

            # Generate translation
            generated_tokens = model.generate(**encoded_input, forced_bos_token_id=tokenizer.get_lang_id(target_language))
            translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

        # Display translated text
        st.write(f"**Translated text ({selected_language}):**")
        st.write(translated_text)
    else:
        st.write("Please enter text to translate.")

# Contact information
st.sidebar.subheader("Contact Developer")
st.sidebar.write("Developer: [M.Abbas](https://www.linkedin.com/in/mohammad-abbas-dev/)")
st.sidebar.write("Gmail: Abbas.mohammad805@gmail.com")

# WhatsApp bot contact
whatsapp_link = "https://wa.me/+923108295635?text=Hi, What query you have about our English to Multiple Language Translator AI app."

st.sidebar.markdown(f"""
    <a href="{whatsapp_link}" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" style="width:50px;height:50px;">
    </a>
""", unsafe_allow_html=True)
