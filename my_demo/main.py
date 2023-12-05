import streamlit as st
import demo_tool

st.set_page_config(
    page_title="ChatGLM3 Demo",
    page_icon=":robot:",
    layout='centered',
    initial_sidebar_state='expanded',
)

# 设置标题
st.title("ChatGLM3 Demo")

# 添加自定义文本
st.markdown("<sub>智谱AI 公开在线技术文档: https://lslfd0slxc.feishu.cn/wiki/WvQbwIJ9tiPAxGk8ywDck6yfnof </sub> \n\n <sub> 更多 ChatGLM3-6B 的使用方法请参考文档。</sub>", unsafe_allow_html=True)

with st.sidebar:
    top_p = st.slider(
        'top_p', 0.0, 1.0, 0.8, step=0.01
    )
    temperature = st.slider(
        'temperature', 0.0, 1.5, 0.95, step=0.01
    )
    repetition_penalty = st.slider(
        'repetition_penalty', 0.0, 2.0, 1.2, step=0.01
    )

    # 清空按钮
    if st.button("清空聊天"):
        st.session_state['chat_history'] = []
        st.session_state['tool_history'] = []

prompt_text = st.chat_input(
    'Interact with ChatGLM3!',
    key='chat_input',
)

# 初始化或获取聊天历史
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# 如果有新的输入，调用 Tool 功能
if prompt_text:
    demo_tool.main(top_p, temperature, prompt_text, repetition_penalty)
