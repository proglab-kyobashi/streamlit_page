import streamlit as st
import numpy as np

st.title("ファイル関係とwebカメラ関係のプログラム一覧")

st.write("画像、動画、CSVなどのファイルを扱える。 自身のPCのデータやwebカメラを使ったサービスで便利")

st.divider()

st.header("st.file_uploader()",divider="gray")
st.subheader("ファイルのアップロード")
st.write("追加オプションに「key='〇〇'」を追加することで「st.session_state.〇〇」という形で情報を保持することができる")
st.write("「disabled=」「label_visibility=」「on_change=」「help=」のオプションも可能で「st.radio()」と同じ")

t = """
uploaded_files = st.file_uploader("ファイルを選んでください", accept_multiple_files=True)
# 「accept_multiple_files=」: 複数ファイルを扱えるようにするかの設定
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read() # アップロードしたデータの取得(ここから「media」で表示等をする)
    st.write("filename:", uploaded_file.name)
"""
st.code(t)

uploaded_files = st.file_uploader("ファイルを選んでください", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)

st.divider()

st.header("st.camera_input()",divider="gray")
st.subheader("webカメラの利用")
st.write("追加オプションに「key='〇〇'」を追加することで「st.session_state.〇〇」という形で情報を保持することができる")
st.write("「disabled=」「label_visibility=」「on_change=」「help=」のオプションも可能で「st.radio()」と同じ")
st.write("OpenCV, Pillow, TensorFlowなどの画像処理系のライブラリとの組み合わせも可能")

t = """
picture = st.camera_input("Take a picture") # webカメラの起動と撮影ボタンの準備

if picture:
    st.image(picture) # 「st.image()」については後述
"""
st.code(t)

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture) 
st.divider()
st.write("OpenCVとの組み合わせ(プログラム例はグレースケール化)")

t = """
import cv2

picture = st.camera_input("Take a picture")

if picture is not None:
    # To read image file buffer with OpenCV:
    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR) # 画像情報をcv2で扱えるようにデコード
    cv2_img = cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY) # グレースケール画像に変換
    st.image(cv2_img)
"""
st.code(t)

import cv2

if picture is not None:
    # To read image file buffer with OpenCV:
    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR) # 画像情報をcv2で扱えるようにデコード
    cv2_img = cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY) # グレースケール画像に変換
    st.image(cv2_img)

st.divider()
st.write("Pillowとの組み合わせ(プログラム例は倍率変更)")

t = """
from PIL import Image

picture = st.camera_input("Take a picture")

if picture is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(picture)
    fx, fy = 0.702, 0.702 # 倍率の設定
    size = (round(img.width * fx), round(img.height * fx)) # 元画像の大きさに合わせて指定pxを決定
    dst = img.resize(size) # リサイズ
    st.image(dst)
"""
st.code(t)

from PIL import Image

if picture is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(picture)
    fx, fy = 0.702, 0.702
    size = (round(img.width * fx), round(img.height * fx))
    dst = img.resize(size)
    st.image(dst)

st.divider()
st.write("TensorFlowとの組み合わせ(実行例は割愛。TensorFlowで扱うための変換処理を紹介)")

t = """
import tensorflow as tf

picture = st.camera_input("Take a picture")

if picture is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = picture.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)
"""
st.code(t)

st.divider()

st.header("st.image()",divider="gray")
st.subheader("画像表示")
st.write("「.jpg」「.png」は確認済み。他にwebカメラの画像や、Pillowなどの画像処理系のライブラリで作成した画像も表示可能")

st.image('./download/flower.png',
          caption='花の画像',
          width= 100,
        )

t = """
st.image('./download/flower.png', # 表示する画像の指定
          caption='花の画像', # 画像の名前
          width= 100, # 画像の横幅(縦幅はアスペクト比に合わせて自動調整)
        )
"""
st.code(t)

st.write("外部サイトの画像のURLを指定すれば表示可能")

st.image('https://secure.proglab.education/lp/images/mv/logo.png',
          caption='proglabのサイトに使われているロゴ画像',
        )

t = """
st.image('https://secure.proglab.education/lp/images/mv/logo.png', caption='proglabのサイトに使われているロゴ画像')
"""
st.code(t)

st.divider()

st.header("st.audio()",divider="gray")
st.subheader("音楽の再生バー表示")
st.write("「.mp3」「.ogg」「.wav」は確認済み。numpyで作成した単音を鳴らすことも可能")
st.write("音声ファイルの形式に応じて「format=」の設定が必要")
link = '<p>※ formatの指定については<a href="https://www.tagindex.com/html/basic/mimetype.html">ここ</a>のMIMEタイプを確認</p>'
st.markdown(link, unsafe_allow_html=True)

st.write("=事前に用意した音楽ファイルの再生(※音量注意)=")
st.audio("./download/Trick_style.mp3", format="audio/mp3")

t = """
st.audio("./download/Trick_style.mp3", format="audio/mp3")
"""
st.code(t)

st.write("=外部サイトの音楽ファイルの再生(※音量注意)=")
st.audio("https://soundeffect-lab.info/sound/anime/mp3/trumpet1.mp3", format="audio/mp3")

t = """
st.audio("https://soundeffect-lab.info/sound/anime/mp3/trumpet1.mp3", format="audio/mp3")
"""
st.code(t)

st.write("=単音の再生(※音量注意)=")
sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds

frequency_la = 440  # Our played note will be 440 Hz

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)

# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)
st.audio(note_la, sample_rate=sample_rate)

t = """
sample_rate = 44100  # サンプルレート(基本これで良い)
seconds = 2  # 再生時間(秒数)

frequency_la = 440  # ヘルツ

t = np.linspace(0, seconds, seconds * sample_rate, False) # 再生時間分の枠

# 指定したヘルツのサイン波を作成
note_la = np.sin(frequency_la * t * 2 * np.pi)
st.audio(note_la, sample_rate=sample_rate)
"""
st.code(t)

st.divider()

st.header("st.video()",divider="gray")
st.subheader("動画の表示")
st.write("「.mp4」は確認済み。youtubeの動画URLを入れることも可能")
st.write("音声ファイルの形式に応じて「format=」の設定が必要")
link = '<p>※ formatの指定については<a href="https://www.tagindex.com/html/basic/mimetype.html">ここ</a>のMIMEタイプを確認</p>'
st.markdown(link, unsafe_allow_html=True)

st.write("=動画の再生(※音量注意)=")
st.video("https://youtu.be/4nsTce1Oce8")

t = """
st.video("https://youtu.be/4nsTce1Oce8")
"""
st.code(t)