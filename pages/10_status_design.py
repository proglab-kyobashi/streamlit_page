import streamlit as st
import time

st.title("ステータス表示関係のプログラム一覧")

st.write("進行状況や更新中を表現するときに利用する")

st.divider()

st.header("st.progress()",divider="gray")
st.subheader("ページ更新進み具合の表示")
st.write("0\~100のint型か、0.0\~1.0のfloat型で管理")

def update_data(): # コールバック関数
    global placeholder
    placeholder.progress(0, text="少々お待ちください...0%")
    for percent_complete in range(100):
        time.sleep(0.05)
        placeholder.progress(percent_complete + 1, text=f"少々お待ちください...{percent_complete + 1}%")
    time.sleep(0.01)
    placeholder.progress(100, text="完了!!")
    time.sleep(1)
    placeholder.empty()
    
st.button("クリックするとプログレスバーが出現", on_click=update_data)
placeholder = st.empty()

t = """
import time

def update_data(): # コールバック関数
    global placeholder
    placeholder.progress(0, text="少々お待ちください...0%")
    for percent_complete in range(100):
        time.sleep(0.05)
        placeholder.progress(percent_complete + 1, text=f"少々お待ちください...{percent_complete + 1}%")
    time.sleep(0.01)
    placeholder.progress(100, text="完了!!")
    time.sleep(1)
    placeholder.empty()
    
st.button("クリックするとプログレスバーが出現", on_click=update_data)
placeholder = st.empty()
"""
st.code(t)

st.divider()

st.header("st.spinner()",divider="gray")
st.subheader("待機中モーションの表示")

t = """
import time

if st.button("クリックすると3秒間待機状態になる"):
    with st.spinner('少々お待ちください'):
        time.sleep(3)
        #
        # ここに処理を作れば、それが終わるまでスピナーが表示される
        #
    st.success('完了!')
"""
st.code(t)

if st.button("クリックすると3秒間待機状態になる"):
    with st.spinner('少々お待ちください'):
        time.sleep(3)
    st.success('完了!')

st.divider()

st.header("st.status()",divider="gray")
st.subheader("処理中の内容を表示")

t = """
import time

if st.button("クリックすると処理を開始"):
    with st.status("Downloading data...", expanded=True) as status: # あとでupdate処理をしたい場合は「as 〇〇」で変数に格納しておく
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)
        status.update(label="Download complete!", state="complete", expanded=False)
        # 「status=」： "complete"(完了マーク), "running"(処理中マーク), "error"(エラーマーク)を表示できる
        # 「expanded=」： 折りたたみを開くか閉じるかを設定できる(True, False)
"""
st.code(t)

if st.button("クリックすると処理を開始"):
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)
        status.update(label="Download complete!", state="complete", expanded=False)

st.divider()

st.header("st.toast()",divider="gray")
st.subheader("画面右下に文字を一時的にポップアップ表示")

t = """
import time

if st.button('トーストの表示'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉') # アイコンの設定も可能
"""
st.code(t)

if st.button('トーストの表示'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

st.write("1つのポップアップで中身の表示だけ変更することも可能")

t = """
import time

def cook_breakfast():
    msg = st.toast('準備中...')
    time.sleep(1)
    msg.toast('調理開始...')
    time.sleep(1)
    msg.toast('完成しました!', icon = "🥞")

if st.button('朝ごはんの調理'):
    cook_breakfast()
"""
st.code(t)

def cook_breakfast():
    msg = st.toast('準備中...')
    time.sleep(1)
    msg.toast('調理開始...')
    time.sleep(1)
    msg.toast('完成しました!', icon = "🥞")

if st.button('朝ごはんの調理'):
    cook_breakfast()

st.divider()

st.header("st.balloons()",divider="gray")
st.subheader("画面に風船を飛ばす")

t = """
if st.button('風船出現'):
    st.balloons()
"""
st.code(t)

if st.button('風船出現'):
    st.balloons()

st.divider()

st.header("st.snow()",divider="gray")
st.subheader("画面に雪の結晶を降らす")

t = """
if st.button('雪の結晶出現'):
    st.snow()
"""
st.code(t)

if st.button('雪の結晶出現'):
    st.snow()

