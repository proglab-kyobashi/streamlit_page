import streamlit as st
import datetime

st.title("入力ウィジェット系のプログラム一覧")

st.write("文字入力やスライダー等によるユーザーからのアクションを可能にする")
st.write("追加オプションに「key='〇〇'」を追加することで「st.session_state.〇〇」という形で情報を保持することができる")
st.write("各ウィジェットは「disabled=」「label_visibility=」「on_change=」「key=」「help=」のオプションも可能で「st.radio()」を参考")

st.divider()

st.header("st.radio()",divider="gray")
st.subheader("ラジオボタン")
st.write("変数には選択した項目情報が入る。「st.write()」と同様に文字の装飾も可能")

genre = st.radio(
    "好きな映画のジャンルは？",
    [":rainbow[コメディ]", "***ドラマ***", "ドキュメンタリー :movie_camera:"],
)

st.write("You selected:", genre)

t = """
genre = st.radio(
    "好きな映画のジャンルは？", # ラジオボタンの内容
    [":rainbow[コメディ]", "***ドラマ***", "ドキュメンタリー :movie_camera:"], # ラジオボタンの選択項目
)

st.write("You selected:", genre)
"""
st.code(t)
with st.expander("細かいオプションについて"):
    st.write("選択できないようにしたり横並びにすることも可能")

    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"

    st.radio(
        "ラベルの表示設定を下から選択 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=False,
        horizontal=True,
        captions = ["表示する", "隠す(隠した場所は残る)", "隠す(隠した場所ごと消す)"], # 各選択項目の補助内容
        help = '項目についての説明も可能' # 項目の説明
    )

    t = """
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"

    st.radio(
        "ラベルの表示設定を下から選択 👇", 
        ["visible", "hidden", "collapsed"], 
        key="visibility",
        label_visibility=st.session_state.visibility, # 説明文の表示、非表示の設定('visible', 'hidden', 'collapsed')
        disabled=False, # 選択肢の変更が可能かどうか(True, False)
        horizontal=True, # 横並びにするかどうか(True, False)
        captions = ["表示する", "隠す(隠した場所は残る)", "隠す(隠した場所ごと消す)"], # 各選択項目の補助内容
        help = '項目についての説明も可能' # 項目の説明
    )
    # 「on_change=」: コールバック関数の設定(「args=」「kwargs=」で引数の設定も可能)
    # 「index=」: 初期で選択状態になっている項目の設定。「None」の場合はどれも選択していない状態
    """
    st.code(t)

st.divider()

st.header("st.checkbox()",divider="gray")
st.subheader("チェックボックス")
st.write("変数にはbool値(True, False)が入る")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write('Ouch...')

t = """
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write('Ouch...')
"""
st.code(t)

st.divider()

st.header("st.toggle()",divider="gray")
st.subheader("トグル")
st.write("変数にはbool値(True, False)が入る")

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

t = """
on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')
"""
st.code(t)

st.divider()

st.header("st.selectbox()",divider="gray")
st.subheader("選択リスト")
st.write("変数には選択した項目情報が入る。")

option = st.selectbox(
    '好きな項目を選択してください',
    ('Email', 'Home phone', 'Mobile phone'),
    index=None,
    placeholder="1つ選択してください",
)
st.write('You selected:', option)

t = """
option = st.selectbox(
    '好きな項目を選択してください', # 選択肢についての説明など
    ('Email', 'Home phone', 'Mobile phone'), # 選択項目
    index=None, # 初期の選択肢
    placeholder="1つ選択してください", # 「index=None」の時の内容
    )
st.write('You selected:', option)
"""
st.code(t)


st.divider()

st.header("st.multiselect()",divider="gray")
st.subheader("複数選択リスト")
st.write("変数には選択した項目情報(リスト型)が入る。")

options = st.multiselect(
    '好きな色を選択してください',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'],
    placeholder="1つ以上選択してください",
    )

st.write('あなたが選択した色:', options)

t = """
options = st.multiselect(
    '好きな色を選択してください', # 選択肢についての説明など
    ['Green', 'Yellow', 'Red', 'Blue'], # 選択項目
    ['Yellow', 'Red'], # 初期選択肢(Noneも可能)
    placeholder="1つ以上選択してください", # 「index=None」の時の内容
    )

st.write('あなたが選択した色:', options)
# 「max_selections=」: 選択できる最大数
"""
st.code(t)

st.divider()

st.header("st.slider()",divider="gray")
st.subheader("スライダー")
st.write("数値の設定を直感的に調整可能")

age = st.slider('何歳ですか？', 0, 130, 25)
st.write("私は", age, '歳です')

t = """
age = st.slider('何歳ですか？', 0, 130, 25)
st.write("私は", age, '歳です')
"""
st.code(t)

with st.expander("細かいオプションについて"):
    st.write("最小値と最大値の2つを選択することも可能(タプル型管理)")
    values = st.slider(
        '数値の範囲を選択', # 説明や内容
        min_value = 0.0, # 最小値
        max_value = 100.0, # 最大値
        value = (25.0, 75.0), # 初期値(2つ選択も可能)
        step = 0.01, # 数値の細かさ
        help = '項目についての説明も可能' # 項目の説明
        ) 
    st.write('範囲:', values)
    st.write('最小値:', values[0], ', 最大値:', values[1])

    t = """
    values = st.slider(
        '数値の範囲を選択', # 説明や内容
        min_value = 0.0, # 最小値
        max_value = 100.0, # 最大値
        value = (25.0, 75.0), # 初期値(2つ選択も可能)
        step = 0.01, # 数値の細かさ
        help = '項目についての説明も可能' # 項目の説明
        ) 
    st.write('範囲:', values)
    st.write('最小値:', values[0], ', 最大値:', values[1])
    """
    st.code(t)

    st.write("datetime型のスライダーの作成も可能(import必須)")
    st.code("import datetime")

    start_time = st.slider(
        "When do you start?",
        value=datetime.datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm") # フォーマットの設定も可能(datetime型にも対応)
    st.write("Start time:", start_time)

    t = """
    start_time = st.slider(
        "When do you start?",
        value=datetime.datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm") # フォーマットの設定も可能(datetime型にも対応)
    st.write("Start time:", start_time)
    """
    st.code(t)

st.divider()

st.header("st.select_slider()",divider="gray")
st.subheader("選択式スライダー")
st.write("リスト内の選択肢を直感的に選択可能")

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

t = """
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)
"""
st.code(t)

st.divider()

st.header("st.text_input()",divider="gray")
st.subheader("文字入力")
st.write("変数には文字列型で入る")

title = st.text_input('何か入力すると下の文字列が変化', '初期に入力されてる文字')
st.write('入力した文字は', title)

t = """
title = st.text_input('何か入力すると下の文字列が変化', '初期に入力されてる文字')
st.write('入力した文字は', title)
"""
st.code(t)
with st.expander("細かいオプションについて"):
    title = st.text_input('何か入力すると下の文字列が変化(今回は最大文字数20文字まで)', 
                        value=None,
                        max_chars=20,
                        type="default",
                        help="詳細な説明文を書き込める",
                        autocomplete="default",
                        placeholder="何かいれてね",
                        )
    st.write('入力した文字は', title)

    t = """
    title = st.text_input('何か入力すると下の文字列が変化(今回は最大文字数20文字まで)', 
                        value=None, # 初期値
                        max_chars=20, # 最大文字数
                        type="default", # 入力文字を隠すかどうか("default", "password")
                        help="詳細な説明文を書き込める", # 項目の説明
                        autocomplete="default", # htmlの<input>と同じ入力規則の設定が可能(例:メールアドレスの場合は「email」)
                        placeholder="何かいれてね", # 入力がない時の文字
                        )
    st.write('入力した文字は', title)
    """
    st.code(t)

st.divider()

st.header("st.number_input()",divider="gray")
st.subheader("数値入力")
st.write("変数には数値型で入る")
st.write("「min_value=」「max_value=」「value=」「step=」のオプションも可能で「st.slider()」と同じ")

number = st.number_input('Insert a number')
st.write('The current number is ', number)

t = """
number = st.number_input('Insert a number')
st.write('The current number is ', number)
"""
st.code(t)

st.divider()

st.header("st.text_area()",divider="gray")
st.subheader("改行有りのテキスト入力")
st.write("変数には文字列型で入る")
st.write("「max_chars=」「placeholder=」のオプションも可能で「st.text_input()」と同じ")

txt = st.text_area(
    "Text to analyze", # 項目タイトル
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...) \nこんな感じで初期値の設定も可能",
    height=150,
    )

st.write(f'You wrote {len(txt)} characters.')

t = """
txt = st.text_area(
    "Text to analyze", # 項目タイトル
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...) \\nこんな感じで初期値の設定も可能", # 改行コード等にも対応
    height=150,
    )

st.write(f'You wrote {len(txt)} characters.')
"""
st.code(t)
st.write("改行も文字数にカウントされる点には注意")

st.divider()

st.header("st.date_input()",divider="gray")
st.subheader("日付情報の入力")
st.write("変数にはdatetime型で入る(import必須)")
st.code("import datetime")
st.write("「min_value=」「max_value=」のオプションも可能で「st.slider()」と同じ")

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

t = """
d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)
"""
st.code(t)
with st.expander("細かいオプションについて"):
    st.write("期間の指定も可能")

    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    d = st.date_input(
        "Select your vacation for next year",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="YYYY.MM.DD",
    )
    st.write("最初の日",d[0])
    st.write("最終の日",d[1])

    t = """
    d = st.date_input(
        "Select your vacation for next year", # 項目の説明
        (jan_1, datetime.date(next_year, 1, 7)), # 初期値
        jan_1, # 最小の日
        dec_31, # 最大の日
        format="YYYY.MM.DD", # フォーマット形式の指定
    )
    st.write("最初の日",d[0])
    st.write("最終の日",d[1])
    """
    st.code(t)

st.divider()

st.header("st.time_input()",divider="gray")
st.subheader("時間情報の入力")
st.write("変数にはdatetime型で入る(import必須)")
st.code("import datetime")
st.write("「step=」のオプションも可能。デフォルトは15分刻み")

t = st.time_input('Set an alarm for', value=None)
st.write('Alarm is set for', t)

t = """
t = st.time_input('Set an alarm for', value=None)
st.write('Alarm is set for', t)
"""
st.code(t)

st.divider()

st.header("st.color_picker()",divider="gray")
st.subheader("色情報の指定(HEXで設定)")

color = st.color_picker('色を指定', '#00f900')
st.write('選ばれた色は', color)

t = """
color = st.color_picker('色を指定', '#00f900')
st.write('選ばれた色は', color)
"""
st.code(t)