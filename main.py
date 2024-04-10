import streamlit as st

st.title("メインページ")

st.write("ここではstraemlitの各パーツについて使い方の例と共に紹介")
st.write("各使い方についてはサイドバーから別ページに飛んで確認してください")
st.divider()
st.header("まずはpipでインストールする")
st.write("Windowsの場合")
st.code("pip install streamlit", language="shellSession")
st.write("Macの場合")
st.code("pip3 install streamlit", language="objectivec")
st.divider()
st.header("プログラム作成時は最初に以下を追加")
st.code("import streamlit as st")
st.divider()
st.header("実行するときは以下のコマンド")
st.caption("このとき、メインページのプログラムを指定")
st.code("streamlit run 〇〇.py")
st.divider()
st.header("複数ページを作りたい場合")
st.write("メインページと同じ階層に「pages」フォルダを作成して、その中に別ページを作成")
st.write("「pages」内のプログラム名の最初に「01_」「02_」...と付けることで順番を決められる")
st.write("ただしプログラム名がそのまま反映されるので、日本語表記にしたい場合などはサイドバーを作成するウィジェットを使う必要がある")
t = '''
streamlit_app       <- カレントディレクトリ名
 L __init__.py  
 L main.py          <- メインページのプログラム
 L pages            <- 複数ページ作成用
     L 01_page1.py
     L 02_page2.py
 L images           <- メディア管理用
     L hoge.png
     L video.mp4
 L requirements.txt <- pipインストール用          
'''
st.code(t, language="yaml")

st.divider()
st.header("サイトマップ")
st.page_link("main.py", label="メインページ")
st.page_link("pages/01_text.py", label="文字を表示する")
st.page_link("pages/02_dataFrame.py", label="DataFrame型の情報を表示する")
st.page_link("pages/03_dataFrame_sub.py", label="DataFrame型の表示系のオプション")
st.page_link("pages/04_chart.py", label="グラフを表示する")
st.page_link("pages/05_button.py", label="各種ボタンの設置")
st.page_link("pages/06_widget.py", label="各種ウィジェットの設置")
st.page_link("pages/07_file_and_media.py", label="ファイルのアップロードやwebカメラの設置と画像等を扱う")
st.page_link("pages/08_layout.py", label="デザインを整える")
st.page_link("pages/09_chat.py", label="チャット機能のテンプレートを設置")
st.page_link("pages/10_status_design.py", label="処理中、更新中時に表現するウィジェットの設置")
st.page_link("pages/11_data_cache.py", label="一時的な情報を記憶・利用する")
st.page_link("pages/80_third_party.py", label="サードパーティ製のプログラム")
st.page_link("pages/99_deploy.py", label="web上に公開する")