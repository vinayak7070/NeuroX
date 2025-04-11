import streamlit as st
import base64

# Function to encode local image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

# Set background image
img_path = "/content/growtika-nGoCBxiaRO0-unsplash.jpg"
encoded_bg = get_base64_of_image(img_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-container {{
        padding-top: 4vh;
        padding-bottom: 4vh;
        padding-left: 5vw;
        padding-right: 5vw;
        background-color: rgba(0, 0, 0, 0.55);
        border-radius: 1rem;
        max-width: 800px;
        margin: auto;
    }}
    h1, h2, h3, p, label, div, span {{
        color: white !important;
    }}
    input, textarea, .stTextInput > div > div > input {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border-radius: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- APP UI ----
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # ✅ NEURO X Branding
    st.markdown(
        '<h1 style="color:white; font-weight:900; text-align:center; margin-bottom: 2rem;">NEURO X</h1>',
        unsafe_allow_html=True
    )

    st.title("🧠 REVEAL.AI")
    st.markdown("## **Multi-Modal Fake News Detection System**")
    st.markdown(
        "Powered by **AI**, this tool verifies if a news claim or image is **REAL or FAKE** "
        "using similarity-based intelligence."
    )

    # --- Text Input ---
    st.markdown("### 📝 Enter News Claim")
    news_text = st.text_area("Type your news here...", placeholder="e.g. NASA finds aliens under Arctic ice.")

    # --- Image Upload ---
    st.markdown("### 📸 Upload News Image")
    uploaded_image = st.file_uploader("Image formats: jpg, jpeg, png", type=["jpg", "jpeg", "png"])

    # --- Submit Button ---
    st.markdown("### ")
    if st.button("🔍 Analyze Now"):
        if news_text or uploaded_image:
            st.success("Analyzing... Please wait.")
        else:
            st.error("Please provide a news claim or an image.")

    st.markdown("</div>", unsafe_allow_html=True)
