import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("データベース表示のプログラム一覧")

st.divider()

st.header("使用前に",divider="gray")
st.write("この項目では「Pandas」によるDataFrame型の変数を扱います")
st.write("そのため「Pandas」を事前にpipでダウンロードして")
st.code("pip install pandas", language="objectivec")
st.write("プログラムの最初に以下を追加しましょう")
text = '''
import pandas as pd
import numpy as np
'''
st.code(text)

st.divider()

st.header("st.dataframe()",divider="gray")
st.write("データベースの表示(編集不可)")
st.write("エクセルやデータベースから読み込んだデータフレーム型のものであればなんでもOK")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)
t = '''
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)
'''
st.code(t)

with st.expander("細かいオプションについて"):
    st.write("オプションの処理もいろいろ可能(例はcol(列)ごとに一番大きい値にハイライト)")
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
    t = '''
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))
    '''
    st.code(t)

    st.write("\n")
    st.write("「column_config」を追加することで、各項目ごとにどのような表現をさせるか決められる。")

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )

    st.write("このとき、グラフやリンクを生成する関数を入れることで複雑な表現が可能となる。「st.column_config.〇〇」")
    link = '<p>※ 詳細については<a href="https://docs.streamlit.io/library/api-reference/data/st.column_config">ここから</a>確認</p>'
    st.markdown(link, unsafe_allow_html=True)

st.divider()

st.header("st.data_editor()",divider="gray")
st.write("データベースの表示(編集可能)")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

t = '''
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

# 「rating」の一番高い「command」を表示する方法
# 「rating」の数値を変更すると結果も変わる
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
'''
st.code(t)

st.divider()

st.header("st.table()",divider="gray")
st.write("静的なテーブルの表示")
st.write("シンプルにテーブルを表示するだけ")

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.table(df)

t = '''
df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.table(df)
'''
st.code(t)

st.divider()

st.header("st.metric()",divider="gray")
st.write("気温や湿度、株価などの数値で表現する項目をおしゃれに統一感を出して表示できる")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

t = '''
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
'''
st.code(t)
with st.expander("細かいオプションについて"):
    st.write("正の値は緑色の上矢印、負の値は赤色の下矢印となる")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    t = '''
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    '''
    st.code(t)

    st.write('色効果を逆にしたい場合は「delta_color="inverse"」、色効果を消したい場合は「delta_color="off"」')

    st.metric(label="Gas price", value=4, delta=-0.5,
        delta_color="inverse")

    st.metric(label="Active developers", value=123, delta=123,
        delta_color="off")

    t = '''
    st.code(t)

    st.metric(label="Gas price", value=4, delta=-0.5,
        delta_color="inverse")

    st.metric(label="Active developers", value=123, delta=123,
        delta_color="off")
    '''
    st.code(t)

st.divider()

st.header("st.json()",divider="gray")
st.write("json形式のデータを表示でき折りたたみ表示も可能になる")

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

t = '''
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
'''
st.code(t)