import streamlit as st
import pandas as pd

st.title("データベース表示の細かい表現方法一覧")

st.divider()

st.header("使用前に",divider="gray")
st.write("この項目では「st.dataframe()」の「column_config」で扱える「st.column_config.〇〇」について書かれています")

st.divider()

st.header(".TextColumn()",divider="gray")
st.write("カラム内に文字を表示")

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            width="large",
            disabled= False,
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets", # 項目名
            width="large", # カラムの幅("small", "medium", "large")
            help="Streamlit **widget** commands 🎈", # カラムの説明
            disabled= False, # 値の変更が可能か設定(True, False)
            default="st.", # 新しく行を追加する際のデフォルト値
            max_chars=50, # 入力値の最大文字数
            validate="^st\.[a-z_]+$", # 入力規則の設定。正しくないと無効になる.

        )
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".NumberColumn()",divider="gray")
st.write("カラム内に数値を表示")
st.write("単位を設定できる部分がミソ")

data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            width="middle", # カラムの幅("small", "medium", "large")
            disabled= False, # 値の変更が可能か設定(True, False)
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD", # カラムの説明
            width="large", # カラムの幅("small", "medium", "large")
            disabled= False, # 値の変更が可能か設定(True, False)
            min_value=0, # 最小値
            max_value=1000, # 最大値
            step=1, # 数値の細かさの管理を設定可能
            format="$%d", # 単位の設定
        )
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".CheckboxColumn()",divider="gray")
st.write("カラム内チェックボックスを設定")

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "favorite": [True, False, False, True],
    }
)

st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?", # 項目名
            width="medium", # カラムの幅("small", "medium", "large")
            help="Select your **favorite** widgets", # カラムの説明
            disabled= False, # 値の変更が可能か設定(True, False)
            default=False, # 新しく行を追加する際のデフォルト値(True, False)
        )
    },
    disabled=["widgets"],
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "favorite": [True, False, False, True],
    }
)

st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?", # 項目名
            width="medium", # カラムの幅("small", "medium", "large")
            help="Select your **favorite** widgets", # カラムの説明
            disabled= False, # 値の変更が可能か設定(True, False)
            default=False, # 新しく行を追加する際のデフォルト値(True, False)
        )
    },
    disabled=["widgets"],
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".SelectboxColumn()",divider="gray")
st.write("カラム内を選択肢方式にする")

data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
            required=False,
            default="", # 新しく行を追加する際のデフォルト値
        )
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category", # 項目名
            help="The category of the app", # カラムの説明
            width="medium", # カラムの幅("small", "medium", "large")
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ], # 選択肢の設定
            required=False, # セルに必ず値が必要かどうか
            default="", # 新しく行を追加する際のデフォルト値
        )
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".DatatimeColumn()",divider="gray")
st.write("日時の表示。 表示の統一が可能")
st.write("「.DateColumn()」「.TimeColmun()」もあるが、ここでは割愛。")

from datetime import datetime

data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Appointment", # 項目名
            width="middle", # カラムの幅("small", "medium", "large")
            help="datetime", # カラムの説明
            disabled= False, # 値の変更が可能か設定(True, False)
            min_value=datetime(2023, 6, 1), # 設定できる最低日時
            max_value=datetime(2025, 1, 1), # 設定できる最大日時
            format="YYYY/MMM/D, h:mm a", # 日時の表示方法の設定
            step=60, # 数値の細かさの管理を設定可能
        ),
    },
    hide_index=True,
)

t = """
from datetime import datetime

data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Appointment", # 項目名
            width="middle", # カラムの幅("small", "medium", "large")
            help="datetime", # カラムの説明
            disabled= False, # 値の変更が可能か設定(True, False)
            min_value=datetime(2023, 6, 1), # 設定できる最低日時
            max_value=datetime(2025, 1, 1), # 設定できる最大日時
            format="YYYY/MMM/D, h:mm a", # 日時の表示方法の設定
            step=60, # 数値の細かさの管理を設定可能
        ),
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".ListColumn()",divider="gray")
st.write("カラム内に文字を表示")

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ListColumn(
            "Sales (last 6 months)", # 項目名
            help="The sales volume in the last 6 months", # カラムの説明
            width="medium", # カラムの幅("small", "medium", "large")
        ),
    },
    hide_index=True, # 行数の表示を隠すかどうか
)

t = """
data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ListColumn(
            "Sales (last 6 months)", # 項目名
            help="The sales volume in the last 6 months", # カラムの説明
            width="medium", # カラムの幅("small", "medium", "large")
        ),
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".LinkColumn()",divider="gray")
st.write("カラム内にリンクを設定")

data_df = pd.DataFrame(
    {
        "apps": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ],
        "creator": [
            "https://github.com/streamlit",
            "https://github.com/arnaudmiribel",
            "https://github.com/streamlit",
            "https://github.com/streamlit",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
            "Trending apps", # 項目名
            help="The top trending Streamlit apps", # カラムの説明
            validate="^https://[a-z]+\.streamlit\.app$", # 入力規則
            max_chars=100, # 入力値の最大文字数
            display_text="https://(.*?)\.streamlit\.app" # リンクを貼る文字の設定。 正規表現を使うことでリンクURLの一部を文字とすることができる。
        ),
        "creator": st.column_config.LinkColumn(
            "App Creator", display_text="Open profile" # リンクを貼る文字に正規表現を使わない場合は、すべて設定した文字列になる
        ),
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "apps": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ],
        "creator": [
            "https://github.com/streamlit",
            "https://github.com/arnaudmiribel",
            "https://github.com/streamlit",
            "https://github.com/streamlit",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
            "Trending apps", # 項目名
            help="The top trending Streamlit apps", # カラムの説明
            validate="^https://[a-z]+\.streamlit\.app$", # 入力規則
            max_chars=100, # 入力値の最大文字数
            display_text="https://(.*?)\.streamlit\.app" # リンクを貼る文字の設定。 正規表現を使うことでリンクURLの一部を文字とすることができる。
        ),
        "creator": st.column_config.LinkColumn(
            "App Creator", display_text="Open profile" # リンクを貼る文字に正規表現を使わない場合は、すべて設定した文字列になる
        ),
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".ImageColumn()",divider="gray")
st.write("カラム内に画像を表示")
st.write("ローカルのファイルも表示可能")

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", # 項目名
            width="medium", # カラムの幅("small", "medium", "large")
            help="Streamlit app preview screenshots", # カラムの説明
        )
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", # 項目名
            width="medium", # カラムの幅("small", "medium", "large")
            help="Streamlit app preview screenshots", # カラムの説明
        )
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".LineChartColumn()",divider="gray")
st.write("カラム内に線グラフを表示")
st.write("曲線になってる点には注意")

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            "Sales (last 6 months)", # 項目名
            width="medium",  # カラムの幅("small", "medium", "large")
            help="The sales volume in the last 6 months", # カラムの説明
            y_min=0, # 縦軸の最小値
            y_max=100, # 縦軸の最大値
         ),
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            "Sales (last 6 months)", # 項目名
            width="medium",  # カラムの幅("small", "medium", "large")
            help="The sales volume in the last 6 months", # カラムの説明
            y_min=0, # 縦軸の最小値
            y_max=100, # 縦軸の最大値
         ),
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".BarChartColumn()",divider="gray")
st.write("カラム内に棒グラフを表示")

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            "Sales (last 6 months)", # 項目名
            width="medium",  # カラムの幅("small", "medium", "large")
            help="The sales volume in the last 6 months", # カラムの説明
            y_min=0, # 縦軸の最小値
            y_max=100, # 縦軸の最大値
        ),
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            "Sales (last 6 months)", # 項目名
            width="medium",  # カラムの幅("small", "medium", "large")
            help="The sales volume in the last 6 months", # カラムの説明
            y_min=0, # 縦軸の最小値
            y_max=100, # 縦軸の最大値
        ),
    },
    hide_index=True,
)
"""

st.code(t)

st.divider()

st.header(".ProgressColumn()",divider="gray")
st.write("カラム内に数値が最大値の何%に当たるかを可視化する")

data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Sales volume", # 項目名
            help="The sales volume in USD", # カラムの説明
            format="$%f", # 単位の設定
            min_value=0, # 最小値
            max_value=1000, # 最大値
        ),
    },
    hide_index=True,
)

t = """
data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Sales volume", # 項目名
            help="The sales volume in USD", # カラムの説明
            format="$%f", # 単位の設定
            min_value=0, # 最小値
            max_value=1000, # 最大値
        ),
    },
    hide_index=True,
)
"""

st.code(t)