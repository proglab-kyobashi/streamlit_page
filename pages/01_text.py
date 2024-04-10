import streamlit as st

st.title("文字表示のプログラム一覧")

st.divider()
st.header("st.write()",divider="gray")
st.write("文字を表示(文字列型以外の表示も可能)")
with st.expander("使用方法"):
    st.write("よく使う文字を表示プログラム")
    st.code('st.write("よく使う文字を表示プログラム")')
    st.write("pythonのprintに近い使い方が可能。", "複数の文章を入れられる")
    st.code('st.write("pythonのprintに近い使い方が可能。", "複数の文章を入れられる")')
    st.write("<h5>html文として処理することも可能</h5>", unsafe_allow_html=True)
    st.code('st.write("<h5>html文として処理することも可能</h5>", unsafe_allow_html=True)')
    st.write("画像やデータフレーム、マークアップ言語などを入れても自動で処理してくれる")

st.header("st.title()",divider="gray")
st.write("文字を表示(1番大きい文字)")
with st.expander("使用方法"):
    st.title("一番大きい文字")
    st.code('st.title("一番大きい文字")')
    st.title("_斜め文字_")
    st.code('st.title("_斜め文字_")')
    st.title(":rainbow[色を付ける]")
    st.code('st.title(":rainbow[色を付ける]")')
    st.write("対応する色はblue, green, orange, red, violet, gray/grey, rainbow")
    st.title("絵文字 :sunglasses:")
    st.code('st.title("絵文字 :sunglasses:")')
    link = '<p>※ その他の絵文字については<a href="https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/">ここから</a>確認</p>'
    st.markdown(link, unsafe_allow_html=True)

st.header("st.header()",divider="gray")
st.write("文字を表示(2番目に大きい文字)")
with st.expander("使用方法"):
    st.header("ヘッダー(2番目に大きい文字)", divider="rainbow")
    st.code('st.header("ヘッダー(2番目に大きい文字)", divider="rainbow")')
    st.write("基本的にはtitleと同じ")
    st.write("下線を追加することが可能(対応色は上記と同じ)")


st.header("st.subheader()",divider="gray")
st.write("文字を表示(3番目に大きい文字)")
with st.expander("使用方法"):
    st.subheader("サブヘッダー(3番目に大きい文字)", divider="rainbow")
    st.code('st.subheader("サブヘッダー(3番目に大きい文字)", divider="rainbow")')
    st.write("基本的にはtitleと同じ")
    st.write("下線を追加することが可能(対応色は上記と同じ)")


st.header("st.caption()",divider="gray")
st.write("文字を表示(ちょっと薄い文字)")
with st.expander("使用方法"):
    st.caption("キャプション(ちょっと薄い文字)")
    st.code('st.caption("キャプション")')
    st.write("基本的にはtitleと同じ")
    st.caption("<h1>html文として処理することも可能</h1>", unsafe_allow_html=True)
    st.code('st.caption("<h1>html文として処理することも可能</h1>", unsafe_allow_html=True)')

st.header("st.code()",divider="gray")
st.write("プログラムの表示")
with st.expander("使用方法"):
    #st.write("文字を特定のプログラミング言語の表記で表示する")
    st.code("print('Hello World!!')", language="python")
    t = f"""st.code("print('Hello World!!')", language="python")"""
    st.write("上の表示をする場合のプログラム")
    st.code(t)
    link = '<p>※ その他の言語については<a href="https://github.com/react-syntax-highlighter/react-syntax-highlighter/blob/master/AVAILABLE_LANGUAGES_PRISM.MD">ここから</a>確認</p>'
    st.markdown(link, unsafe_allow_html=True)

st.divider()

st.header("st.error()",divider="gray")
st.write("エラー文を表示")
st.error('This is an error', icon="🚨")
st.code("""st.error('This is an error', icon="🚨")""")

st.header("st.warning()",divider="gray")
st.write("警告文を表示")
st.warning('This is a warning', icon="⚠️")
st.code("""st.warning('This is a warning', icon="⚠️")""")

st.header("st.info()",divider="gray")
st.write("強調したい情報を表示")
st.info('This is a purely informational message', icon="ℹ️")
st.code("""st.info('This is a purely informational message', icon="ℹ️")""")

st.header("st.success()",divider="gray")
st.write("成功文を表示")
st.success('This is a success message!', icon="✅")
st.code("""st.success('This is a success message!', icon="✅")""")

st.header("st.exception()",divider="gray")
st.write("エラー文を表示")
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
t = """
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
"""
st.code(t)


st.divider()

st.header("st.divider()",divider="gray")
st.write("区切り線を引く。","この項目の上下に引かれている薄い区切り線もこれを利用している")
st.code("st.divider()")

st.divider()

st.header("st.text()",divider="gray")
st.write("文字を表示(文字列型のみ表示)")
with st.expander("使用方法"):
    st.text("ただの文字列の表示")
    st.code('st.text("ただの文字列の表示")')
    st.text("基本的には「st.write()」を使えば良い")

st.header("st.write_stream()",divider="gray")
st.write("文字やデータが流れるように表示される")
with st.expander("使用方法"):
    #st.write("文字やデータが流れるように表示される")
    import time
    text = '''
    Streamlitは、Pythonで実装されたオープンソースの
    Webアプリケーションのフレームワークであり、機械学
    習やデータサイエンス向けのグラフィカルなWebアプリ
    を簡単に作成して全世界に公開（クラウドサービスにデ
    プロイ）できます。
    '''
    def streamData():
        for word in text:
            yield word
            time.sleep(0.01)

    t = """
    import time

    text = '''
    Streamlitは、Pythonで実装されたオープンソースの
    Webアプリケーションのフレームワークであり、機械学
    習やデータサイエンス向けのグラフィカルなWebアプリ
    を簡単に作成して全世界に公開（クラウドサービスにデ
    プロイ）できます。
    '''

    def streamData():
        for word in text:
            yield word
            time.sleep(0.01)

    if st.button("クリックで表示"):
        st.write_stream(streamData)
    """

    st.code(t)

    if st.button("クリックで表示"):
        st.write_stream(streamData)

st.header("st.markdown()",divider="gray")
st.write("文字を表示(マークダウン記法による表示)")
with st.expander("使用方法"):
    st.markdown("*Streamlit* は **とても** ***便利***.")
    st.markdown('''
        :red[Streamlit] :orange[は] :green[いろんな色] :blue[で] :violet[文字]
        :gray[が] :rainbow[書ける].''')
    st.markdown("絵文字の表示も可能 &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''
    # title
    ## h1
    ### h2
    #### h3
    [他のマークダウン記法はこちらを参照](https://qiita.com/kamorits/items/6f342da395ad57468ae3)
    '''
    st.markdown(multi)
    t = """
    st.markdown("*Streamlit* は **とても** ***便利***.")
    st.markdown('''
        :red[Streamlit] :orange[は] :green[いろんな色] :blue[で] :violet[文字]
        :gray[が] :rainbow[書ける].''')
    st.markdown("絵文字の表示も可能 -;
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''
    # title
    ## h1
    ### h2
    #### h3
    [他のマークダウン記法はこちらを参照](https://qiita.com/kamorits/items/6f342da395ad57468ae3)
    '''
    st.markdown(multi)
    """
    st.code(t)
    st.text("基本的には「st.write()」を使えば良い")


st.header("st.latex()",divider="gray")
st.write("LaTeX表示に利用(論文作成時によく利用される難しい計算式を表示するツール)")
t = """
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
"""
st.code(t)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')