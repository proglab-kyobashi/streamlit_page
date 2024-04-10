import streamlit as st

st.title("ボタンのプログラム一覧")

st.write("ボタンによるユーザーからのアクションを可能にする")

st.divider()

st.header("st.button()",divider="gray")
st.subheader("ボタン")

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

t = """
st.button("Reset", type="primary") # デザインを強調できる
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
"""
st.code(t)

st.write("コールバック関数を作成してボタンを押す時の細かい処理を作成可能")

if 'num_of_data' not in st.session_state: # streamlitによる更新をしても情報を保持したい場合は「st.session_state」を使う
    st.session_state['num_of_data'] = 0 # 初期値の設定。ブラウザでの更新をするとリセットされる

def update_num_of_data(num_of_add): # コールバック関数
    st.session_state['num_of_data'] += num_of_add

st.button("関数を動かす",
          on_click=update_num_of_data, # コールバック関数の設定
          args=[1], # 可変長引数の設定(「kwargs=」も可能)
          help="押す度に数値が増える", # ボタンの説明
          use_container_width=True # 全体の横幅に合わせてボタンの幅が変わる(True, False)
          ) 
st.write(st.session_state['num_of_data'])

t = """
if 'num_of_data' not in st.session_state: # streamlitによる更新をしても情報を保持したい場合は「st.session_state」を使う
    st.session_state['num_of_data'] = 0 # 初期値の設定。ブラウザでの更新をするとリセットされる

def update_num_of_data(num_of_add): # コールバック関数
    st.session_state['num_of_data'] += num_of_add

st.button("関数を動かす",
          on_click=update_num_of_data, # コールバック関数の設定
          args=[1], # 可変長引数の設定(「kwargs=」も可能)
          help="押す度に数値が増える", # ボタンの説明
          use_container_width=True # 全体の横幅に合わせてボタンの幅が変わる(True, False)
          ) 
st.write(st.session_state['num_of_data'])
"""
st.code(t)

st.divider()

st.header("st.download_button()",divider="gray")
st.subheader("ダウンロード用ボタン")
st.write("基本的には「st.button()」のオプションと同じものが使える")

text_contents = '''This is some text'''
st.download_button('テキストファイルをダウンロード', text_contents)

t = """
text_contents = '''This is some text'''
st.download_button('テキストファイルをダウンロード', text_contents)
"""
st.code(t)

st.write("画像データ等もダウンロードできる")

with open("./download/flower.png", "rb") as file:
    btn = st.download_button(
            label="画像をダウンロード",
            data=file,
            file_name="flower.png",
            mime="image/png"
          )

t = """
with open("./download/flower.png", "rb") as file:
    btn = st.download_button(
            label="画像をダウンロード", # ボタンの文字
            data=file, # ダウンロードデータ
            file_name="flower.png", # ダウンロード時のファイル名(拡張子も忘れずに)
            mime="image/png" # データのMIMEタイプ
          )
"""
st.code(t)
link = '<p>※ MIMEタイプについては<a href="https://www.tagindex.com/html/basic/mimetype.html">ここから</a>確認</p>'
st.markdown(link, unsafe_allow_html=True)

st.divider()

st.header("st.link_button()",divider="gray")
st.subheader("外部リンク先へ飛ぶボタン")
st.write("基本的には「st.button()」のオプションと同じものが使える")

st.link_button("youtubeへ飛ぶ", "https://www.youtube.com/", type="primary")

t = """
st.link_button("youtubeへ飛ぶ", "https://www.youtube.com/", type="primary")
"""
st.code(t)

st.divider()

st.header("st.page_link()",divider="gray")
st.subheader("リンク先へ飛ぶボタン")
st.write("内部リンクへの設定も可能。その場合はページ遷移となり、外部リンクの場合は別タブが開く")
st.write("基本的には「st.button()」のオプションと同じものが使える")

st.page_link("main.py", label="Home", icon="🏠")
st.page_link("pages/01_text.py", label="テキスト系")
st.page_link("pages/02_dataFrame.py", label="データを扱う系", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

t = """
st.page_link("main.py", label="Home", icon="🏠") # アイコン設定可能
st.page_link("pages/01_text.py", label="テキスト系")
st.page_link("pages/02_dataFrame.py", label="データを扱う系", disabled=True) # 選択できないようにすることも可能
st.page_link("http://www.google.com", label="Google", icon="🌎") # 外部リンクも可能
"""
st.code(t)

st.divider()

st.header("st.switch_page()",divider="gray")
st.subheader("リンク先へ飛ぶ(ボタンではなくプログラム)")
st.write("内部リンクへ飛ぶがこれ自体にボタンの要素はないので、「st.button()」と組み合わせたり、強制的なページ移動に利用する")

if st.button("Home"):
    st.switch_page("main.py")
if st.button("テキスト系"):
    st.switch_page("pages/01_text.py")
if st.button("データを扱う系"):
    st.switch_page("pages/02_dataFrame.py")

t = """
if st.button("Home"):
    st.switch_page("main.py")
if st.button("テキスト系"):
    st.switch_page("pages/01_text.py")
if st.button("データを扱う系"):
    st.switch_page("pages/02_dataFrame.py")
"""
st.code(t)