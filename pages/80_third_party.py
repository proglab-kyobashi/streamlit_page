import streamlit as st

st.title("サードパーティ製のプログラム一覧")
st.write("公式が作ったstreamlitのプログラムではないが、公式でオススメされている拡張プログラム")
st.write("種類が多いので使いやすそうなものを抜粋")
st.markdown("その他のプログラムを見たい場合は[こちら](https://streamlit.io/components)")

st.divider()
st.header("手書き用キャンバスを設置",divider="gray")
st.subheader("streamllit-drawable-canvas")
st.code("pip install streamlit-drawable-canvas", language="shellSession")
st.markdown("[提供ページ](https://github.com/andfanilo/streamlit-drawable-canvas)")

st.image("./download/demo.gif")

st.divider()
st.header("foliumと連携した地図アプリを設置",divider="gray")
st.subheader("streamllit-folium")
st.write("マーカーの設置もできる点が良い")
st.code("pip install streamlit-folium", language="shellSession")
st.markdown("[提供ページ](https://github.com/randyzwitch/streamlit-folium?tab=readme-ov-file)")

st.image("./download/baseline.png")

st.divider()
st.header("画像をクリックしたときにその座標を返す",divider="gray")
st.subheader("streamllit-image-coordinates")
st.write("間違い探しゲームを作るとき等に使えそう？")
st.code("pip install streamllit-image-coordinates", language="shellSession")
st.markdown("[提供ページ](https://github.com/blackary/streamlit-image-coordinates)")

st.divider()
st.header("2つの画像をスライダーで見比べられる",divider="gray")
st.subheader("streamllit-image-comparison")
st.write("画像の加工前後の比較とかに使えそう？")
st.code("pip install streamlit-image-comparison", language="shellSession")
st.markdown("[提供ページ](https://github.com/fcakyon/streamlit-image-comparison)")

st.image("./download/mix.gif")

st.divider()
st.header("画像の切り抜きができる",divider="gray")
st.subheader("streamllit-cropper")
st.code("pip install streamlit-cropper", language="shellSession")
st.markdown("[提供ページ](https://github.com/turner-anderson/streamlit-cropper)")

st.image("./download/crop.gif", width=700)