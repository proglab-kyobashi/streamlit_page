import streamlit as st
import pandas as pd
import numpy as np

st.title("グラフ表示のプログラム一覧")

st.write("作成されるグラフは表示後もマウス操作である程度動かすことが可能")
st.write("オプション機能を「面グラフ」にて紹介しているが、他のグラフも同様なので割愛")

st.divider()

st.header("st.area_chart()",divider="gray")
st.subheader("面グラフ")

st.write("グラフ全体の大きさを指定可能(widthは何故か変わらない)")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data,width=100,height=500)

t = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data,width=100,height=500)
'''
st.code(t)

with st.expander("細かいオプションについて"):
    st.write("データの各列毎にx軸,y軸,ラベルの割り当てを指定")

    chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
    )

    st.area_chart(chart_data, x="col1", y="col2", color="col3")

    t = '''
    chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
    )

    st.area_chart(chart_data, x="col1", y="col2", color="col3")
    '''
    st.code(t)

    st.write("各データの表示色の指定")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

    st.area_chart(
    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )

    t = '''
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

    st.area_chart(
    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )
    '''
    st.code(t)

st.divider()

st.header("st.bar_chart()",divider="gray")
st.subheader("棒グラフ")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

t = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
'''
st.code(t)

st.divider()

st.header("st.line_chart()",divider="gray")
st.subheader("折れ線グラフ")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

t = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
'''
st.code(t)

st.divider()

st.header("st.scatter_chart()",divider="gray")
st.subheader("散布図")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)

t = '''
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)
'''
st.code(t)

with st.expander("細かいオプションについて"):
    st.write("各点の大きさを可変にしてデータを当てることで3つの要素の表現も可能")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A','B','C'], 20)

    st.scatter_chart(
        chart_data,
        x='col1',
        y='col2',
        color='col4',
        size='col3',
    )

    t = '''
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A','B','C'], 20)

    st.scatter_chart(
        chart_data,
        x='col1',
        y='col2',
        color='col4',
        size='col3',
    )
    '''
    st.code(t)

st.divider()

st.header("st.pyplot()",divider="gray")
st.subheader("matplotlibのグラフを表示")
st.write("matplotlibの「plt.show()」の代わりのようなものなので、グラフのデザイン等も反映されるのがポイント")
st.write("事前にpipでインストールが必要")
st.code("pip install matplotlib", language="shellSession")

import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

t = '''
import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100) # 正規分布に従って乱数を生成
fig, ax = plt.subplots() # グラフを描画する土台の用意
ax.hist(arr, bins=20) # ヒストグラムを配置(他のグラフでもok)

st.pyplot(fig)
'''
st.code(t)
st.write("※ 他にもグラフを表示する外部ライブラリと連動可能になるライブラリがあるが割愛")

st.divider()

st.header("st.map()",divider="gray")
st.subheader("地図を表示(mapbox使用)")
#34.69713074889092, 135.53408376136866
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [34.69, 135.53],
    columns=['lat', 'lon'])

st.map(df)

t = '''
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [34.69, 135.53],
    columns=['lat', 'lon'])

st.map(df)
'''
st.code(t)

st.divider()

st.title("グラフ追加オプション関係")

st.header(".add_rows()",divider="gray")
st.subheader("データの追加")

t = '''
bt = st.button("押すと追加")
df1 = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

col1, col2 = st.columns(2)

with col1:
    my_table = st.table(df1)
with col2:
    my_chart = st.line_chart(df1)

if bt:
    df2 = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

    my_table.add_rows(df2) # DataFrame型を利用しているどのグラフに対しても有効
    my_chart.add_rows(df2) 
'''
st.code(t)

bt = st.button("押すと追加")
df1 = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

col1, col2 = st.columns(2)

with col1:
    my_table = st.table(df1)
with col2:
    my_chart = st.line_chart(df1)

if bt:
    df2 = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

    my_table.add_rows(df2) # DataFrame型を利用しているどのグラフに対しても有効
    my_chart.add_rows(df2) 