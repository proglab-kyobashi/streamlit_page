import streamlit as st
import numpy as np

st.title("レイアウト関係のプログラム一覧")

st.write("ウィジェットを横並びにしたり、折りたたみ枠を作るなど、UIデザインを整えるのに必要")

st.divider()

st.header("st.columns()",divider="gray")
st.subheader("横並びにする")

col1, col2, col3 = st.columns(3, gap="small")

with col1:
   st.subheader("ID")
   st.write("01")

with col2:
   st.subheader("名前")
   st.write("Proglab")

with col3:
   st.subheader("概要")
   st.write("ロボットプログラミング教室")
   
t = """
col1, col2, col3 = st.columns(3, gap="small")

with col1:
   st.subheader("ID")
   st.write("01")

with col2:
   st.subheader("名前")
   st.write("Proglab")

with col3:
   st.subheader("概要")
   st.write("ロボットプログラミング教室")
"""
st.code(t)
with st.expander("細かいオプションについて"):
   st.write("全体のうち何%かで設定することも可能")

   col1, col2, col3 = st.columns([0.1, 0.3, 0.6], gap="medium")

   with col1:
      st.subheader("col1")
      st.write("10%")

   with col2:
      st.subheader("col2")
      st.write("30%")

   with col3:
      st.subheader("col3")
      st.write("60%")

   t = """
   col1, col2, col3 = st.columns([0.1, 0.3, 0.6], gap="medium")

   #
   # 各columnの中身は省略
   #
   """
   st.code(t)

   st.write("1つのcolを基準とした比率で設定することも可能")

   col1, col2, col3 = st.columns([1, 2, 3], gap="large")

   with col1:
      st.subheader("col1")
      st.write("これを基準として")

   with col2:
      st.subheader("col2")
      st.write("2倍")

   with col3:
      st.subheader("col3")
      st.write("3倍")

   t = """
   col1, col2, col3 = st.columns([1, 2, 3], gap="large")

   #
   # 各columnの中身は省略
   #
   """
   st.code(t)

st.divider()

st.header("st.container()",divider="gray")
st.subheader("コンテナ")

# 基本的には「with」で扱うと良い
with st.container(border=True): # 「border=True」で枠線をつけられる
   st.write("このテキストとグラフはコンテナ内")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("このテキストはコンテナ外")
   
t = """
# 基本的には「with」で扱うと良い
with st.container(border=True): # 「border=True」で枠線をつけられる
   st.write("このテキストとグラフはコンテナ内")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("このテキストはコンテナ外")
"""
st.code(t)
with st.expander("細かいオプションについて"):
   st.write("高さの設定も可能。中身が高さを超える場合はスクロールが機能する")
   long_text = "大量の文字 " * 1000

   with st.container(height=300):
      st.markdown(long_text)

   t = """
   long_text = "大量の文字 " * 1000

   with st.container(height=300):
      st.markdown(long_text)
   """
   st.code(t)

st.divider()

st.header("st.empty()",divider="gray")
st.subheader("切り替え用の空コンテナ")
st.write("時間経過や何かしらのアクションによって、あとで中身を変化させたい時に利用")
st.write("以下の方法を試してみると、「st.empty()」の中身が切り替わっていくだけで文字が増えるわけではないことが分かる")
t = """
import time

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} 秒経過")
        time.sleep(1)
    st.write("✔️ 10秒経ちました!")
"""
st.code(t)
st.write("ただし、この方法では処理が完了するまでそれ以下の処理が行われないので、基本的には次のような処理をすると良い")

import time

placeholder = st.empty()
def timeschedule():
    for seconds in range(10):
        placeholder.write(f"⏳ {seconds} 秒経過")
        time.sleep(1)
    placeholder.write("✔️ 10秒経ちました!")

t = """
import time

placeholder = st.empty()

def timeschedule():
    for seconds in range(10):
        placeholder.write(f"⏳ {seconds} 秒経過")
        time.sleep(1)
    placeholder.write("✔️ 10秒経ちました!")

#
# ここに他のプログラムを作る
#

# プログラムの最後に「time.sleep()」系の処理を持ってくる
timeschedule()
"""
st.code(t)
st.write("コンテナ内の内容を変化させたい時は、代入した変数に通常の「st.〇〇()」の「.〇〇()」部をくっ付ければ良い。(上記プログラムの場合：st.write('テスト') → placeholder.write('テスト'))")

st.divider()

st.header("st.expander()",divider="gray")
st.subheader("拡張コンテナ(折りたたみコンテナ)")
st.write("情報量が多くて必要な人だけが見たら良いようなものなどを折りたたんでおける")

# 基本的には「with」で扱うと良い
with st.expander("ここをクリックすると中身が表示される"):
    st.write("中身はなんでも入れられる")
    st.image('./download/flower.png', caption='花の画像', width= 100)
   
t = """
# 基本的には「with」で扱うと良い
with st.expander("ここをクリックすると中身が表示される"):
    st.write("中身はなんでも入れられる")
    st.image('./download/flower.png', caption='花の画像', width= 100)
"""
st.code(t)

st.divider()

st.header("st.popover()",divider="gray")
st.subheader("ポップアップコンテナ")
st.write("仕組みは「st.expander()」と同じだが、ポップアップとして、上に重なるように表示される")

# 基本的には「with」で扱うと良い
with st.popover("ここをクリックすると中身が表示される"):
    st.write("中身はなんでも入れられる")
    st.image('./download/flower.png', caption='花の画像', width= 100)
   
t = """
# 基本的には「with」で扱うと良い
with st.popover("ここをクリックすると中身が表示される"):
    st.write("中身はなんでも入れられる")
    st.image('./download/flower.png', caption='花の画像', width= 100)
"""
st.code(t)

st.divider()

st.header("st.sidebar",divider="gray")
st.subheader("サイドバー")
st.write("サイドバーに要素を作りたい場合に使用。ページ遷移の要素とは別管理で作れる。")
st.write("「()」は必要ない")
st.write("実際のデモはサイドバーで確認")
# オブジェクト管理の場合
# サイドバーへ追加する場合は通常の「st.〇〇()」の「.〇〇()」部をくっ付ければ良い。
# 例：st.write('テスト') → st.sidebar.write('テスト')
st.sidebar.write("サイドバーのデモ")
add_selectbox = st.sidebar.selectbox(
    "連絡手段は何ですか?",
    ("Email", "Home phone", "Mobile phone")
)

# 「with」管理の場合
with st.sidebar:
    add_radio = st.radio(
        "どのモードが良い?",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
   
t = """
# オブジェクト管理の場合
# サイドバーへ追加する場合は通常の「st.〇〇()」の「.〇〇()」部をくっ付ければ良い。
# 例：st.write('テスト') → st.sidebar.write('テスト')
st.sidebar.write("サイドバーのデモ")
add_selectbox = st.sidebar.selectbox(
    "連絡手段は何ですか?",
    ("Email", "Home phone", "Mobile phone")
)

# 「with」管理の場合
with st.sidebar:
    add_radio = st.radio(
        "どのモードが良い?",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
"""
st.code(t)

st.divider()

st.header("st.tabs()",divider="gray")
st.subheader("タブコンテナ")
st.write("仕組みは「st.columns()」に似ているが、タブで切り替えできる仕組みになっている。")

col1, col2, col3 = st.tabs(["ID", "名前", "概要"])

with col1:
   st.subheader("ID")
   st.write("01")

with col2:
   st.subheader("名前")
   st.write("Proglab")

with col3:
   st.subheader("概要")
   st.write("ロボットプログラミング教室")
   
t = """
col1, col2, col3 = st.tabs(["ID", "名前", "概要"])

with col1:
   st.subheader("ID")
   st.write("01")

with col2:
   st.subheader("名前")
   st.write("Proglab")

with col3:
   st.subheader("概要")
   st.write("ロボットプログラミング教室")
"""
st.code(t)









timeschedule()