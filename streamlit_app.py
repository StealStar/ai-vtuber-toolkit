
import streamlit as st
st.set_page_config(page_title="AI VTuber", layout="wide")

st.title("AI VTuber Toolkit")
st.write("이 페이지는 Streamlit 웹앱 테스트용입니다.")
st.write("✅ 다국어 UI, ✅ TTS, ✅ AI 응답, ✅ 외형 미리보기 기능 등 통합 가능합니다.")

name = st.text_input("이름을 입력하세요", "유키")
if st.button("인사하기"):
    st.success(f"{name}님, 안녕하세요!")
