import streamlit as st

st.title("記憶保持関係のプログラム一覧")

st.write("キャッシュデータを利用して情報を保持することで画面の更新を維持できる")

st.divider()

st.header("st.session_state",divider="gray")
st.subheader("保持している情報の読み書きをする。保持した情報は他のページでも利用可能")

st.divider()

st.subheader("初期化方法")
t = """
# 辞書型のように扱う
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# enumのように扱う
if 'key' not in st.session_state:
    st.session_state.key = 'value'
"""
st.code(t)

st.divider()

st.subheader("中身の確認")

if 'key' not in st.session_state:
    st.session_state.key = 'value'

st.write("辞書型のように扱う")
st.write(st.session_state["key"])
st.write("enumのように扱う")
st.write(st.session_state.key)
t = """
st.write("辞書型の変数のように扱う")
st.write(st.session_state["key"])

st.write("enumのように扱う")
st.write(st.session_state.key)
"""
st.code(t)

st.divider()

st.subheader("更新")

st.session_state['key'] = 'value2'  # Dictionary like API
st.session_state.key = 'value2'     # Attribute API
st.write(st.session_state.key)

t = """
st.session_state['key'] = 'value2'  # 辞書型の変数のように扱う
st.session_state.key = 'value2'     # enumのように扱う

st.write(st.session_state.key)
"""
st.code(t)

st.divider()

st.subheader("中身を全て確認")
st.write(st.session_state)

st.code("st.write(st.session_state)")

st.divider()

st.subheader("削除")

t = """
# 一部を削除する場合
del st.session_state[key]

# 全て削除する場合
for key in st.session_state.keys():
    del st.session_state[key]
"""
st.code(t)

st.divider()

st.subheader("ウィジェットの更新による管理")
st.write("ボタンや各ウィジェットの更新に合わせて情報を保持する場合は「key=」オプションを追加すれば良い")

st.text_input("Your name", key="name")

# This exists now:
st.write(st.session_state)

t = """
# 他のウィジェットにもオプションに「key=」がある
st.text_input("Your name", key="name")

# 更新後の中身:
st.write(st.session_state)
"""
st.code(t)

st.divider()

st.subheader("コールバックを利用した更新")
st.write("ボタンや各ウィジェットの更新時に実行する「コールバック関数」を利用するには「on_click=」または「onchange=」を追加する")
st.write("このとき、引数を当てるときは可変超引数「args=」「kwargs=」を追加する")

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

t = """
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
"""
st.code(t)

st.divider()

st.header("st.query_params",divider="gray")
st.subheader("URLの後ろに付くクエリパラメーターを取得する")
st.write("クエリパラメーターは「URL?〇〇=△△」の「〇〇=△△」部分")

URL = """
<a href="/data_cache?key=hogehoge&name=Noname">クエリパラメーター付きURL</a>
"""
st.write(URL, unsafe_allow_html=True)

query_dict = st.query_params.to_dict()
st.write(query_dict)
if query_dict:
    st.write(query_dict["name"])

st.write(st.query_params.get("key"))
t = """
URL = '<a href="/data_cache?key=hogehoge&name=Noname">クエリパラメーター付きURL</a>'
st.write(URL, unsafe_allow_html=True)

query_dict = st.query_params.to_dict()
st.write(query_dict)
if query_dict:
    st.write(query_dict["name"])
    
st.write(st.query_params.get("key"))
"""
st.code(t)