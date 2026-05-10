import streamlit as st
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

st.set_page_config(page_title="English → Chinese Translator", page_icon="🌏")

st.title("🌏 English → Chinese Translator")
st.caption("智能翻译 + 关键短语解释")

english_text = st.text_area(
    "Paste English text here:",
    height=150,
    placeholder="e.g. The market for AI engineers is splitting in two directions..."
)

if st.button("Translate", type="primary"):
    if not english_text.strip():
        st.warning("请先输入英文")
    else:
        with st.spinner("翻译中..."):
            prompt = f"""You are a professional English-to-Chinese translator.

Given the English text below:
1. Translate it to natural, fluent Chinese
2. Identify 3-5 key phrases or idioms worth explaining
3. For each key phrase, give the original English, the Chinese translation, and a brief usage note

Format your response as:

## 翻译
[your translation here]

## 关键短语
- **English phrase**: 中文翻译 — usage note
- ...

English text:
{english_text}"""

            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            st.markdown(response.content[0].text)
            
            with st.expander("Token usage"):
                st.write(f"Input: {response.usage.input_tokens}, Output: {response.usage.output_tokens}")