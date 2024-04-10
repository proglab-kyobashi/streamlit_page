import streamlit as st
import numpy as np

st.title("チャット関係のプログラム一覧")

st.write("チャットの仕組みを作れる")
st.write("あくまで枠組みだけなので、「st.session_state」等で情報を保持する仕組みが必要")

st.divider()

st.header("st.chat_input()",divider="gray")
st.subheader("チャット用の文字入力")
st.write("基本的には入力ウィジェット系の「st.text_input()」と同じ")
st.write("※必ずページの一番下に重なって表示される")

t = """
prompt = st.chat_input("何か書き込む")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
else:
    st.write("内容はここに表示される")
"""
st.code(t)

prompt = st.chat_input("何か書き込む")
if prompt:
    st.write(f"入力内容: {prompt}")
else:
    st.write("入力内容: 内容はここに表示される")

st.divider()
st.write("「st.container()」を使えば、その中で入力ウィジェットを作成できる(ただし、上に入力ウィジェットができる)")

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.container(height=300)
prompt = messages.chat_input("ここに書き込むと下に追加されていく",key="message")
if prompt:
    st.session_state.messages.append(prompt)
for i in st.session_state.messages:
    messages.chat_message("user").write(i)

t = """
if "messages" not in st.session_state: # もし記憶用のkeyが存在しなければ初期化する
    st.session_state.messages = []

messages = st.container(height=300)
prompt = messages.chat_input("ここに書き込むと下に追加されていく",key="message") # 複数作る場合は「key=」の設定が必要

if prompt:
    st.session_state.messages.append(prompt)

for i in st.session_state.messages: # 記憶したリストを表示する
    messages.chat_message("user").write(i) # 「.chat_message()」を挟むとアイコンを表示できる(詳細は下記)
"""
st.code(t)

st.divider()

st.header("st.chat_message()",divider="gray")
st.subheader("チャットへの表示")
st.write("指定アイコンと一緒に文字や図などを表示するためのウィジェット")
st.write('「"user"」「"human"」「"assistant"」「"ai"」で規定アイコンを表示(全2種)。それ以外の文字列は最初の1文字が表示される')

t = """
with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("user", avatar="🧑‍💻"): # 「avatar=」には絵文字と画像を指定可能
    st.write("文字以外の表示もOK")
    st.line_chart(np.random.randn(30, 3))

with st.chat_message("user", avatar="./download/flower.png"):
    st.write("指定した画像での設定も可能")
"""
st.code(t)

with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("user", avatar="🧑‍💻"):
    st.write("文字以外の表示もOK")
    st.line_chart(np.random.randn(30, 3))

with st.chat_message("user", avatar="./download/flower.png"):
    st.write("指定した画像での設定も可能")

st.write("オブジェクト管理の場合。「st.chat_input()」の内容を「st.container()」で反映する場合はこの方法の方が良い")

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))

t = """
message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
"""
st.code(t)