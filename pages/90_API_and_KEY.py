import streamlit as st

st.title("APIキーを扱う時の注意点と扱い方")
t = """
googlemapやChatGPT等のWebAPIやwebサーバーを扱う場合、APIキー(シークレットキー)という他の人に絶対にバレてはいけない情報がある。  
APIキーは「環境変数」で管理することになるが、:red[GitHubに絶対公開してはいけない]ので、GitHubにはaddせずにStreamlit Cloud側で設定する必要がある。  
  
このページでは環境変数の設定とGitHubにaddされない方法を紹介
"""
st.write(t)
st.divider()

st.header("1. ローカルでの環境変数の設定",divider="gray")

st.write("ローカルで扱う環境変数を設定するファイルの作成")

t = '''
streamlit_app
 L __init__.py         
 L main.py          
 L pages            
     L 01_page1.py
     L 02_page2.py
 L images           
     L hoge.png
     L video.mp4
 L requirements.txt 
 L  .streamlit         <- 「.streamlit」ディレクトリを作成して
     L secrets.toml    <- その中に「secrets.toml」を作成
'''
st.code(t, language="yaml")

st.write("「secrets.toml」内に環境変数を書き込む")
t = """
# 環境変数の設定
db_username = "Jane"
db_password = "mypassword"

# [〇〇]の場合は、より細かい環境変数名を指定できる
[my_other_secrets]
language = "toml"
"""
st.code(t, language="toml")

st.header("2. 環境変数の扱い方",divider="gray")
st.subheader("st.secrets")
# 辞書型の変数のように扱う
st.write("ユーザー名:", st.secrets["db_username"])
st.write("パスワード:", st.secrets["db_password"])
st.write("使用言語:", st.secrets["my_other_secrets"]["language"])

# enumのように扱う
st.write("ユーザー名:", st.secrets.db_username)
st.write("パスワード:", st.secrets.db_password)
st.write("使用言語:", st.secrets.my_other_secrets.language)
t = """
# 辞書型の変数のように扱う
st.write("ユーザー名:", st.secrets["db_username"])
st.write("パスワード:", st.secrets["db_password"])
st.write("使用言語:", st.secrets["my_other_secrets"]["language"])

# enumのように扱う
st.write("ユーザー名:", st.secrets.db_username)
st.write("パスワード:", st.secrets.db_password")
st.write("使用言語:", st.secrets.my_other_secrets.language)
"""
st.code(t)

st.header("3. 環境変数をGitHubに公開しない設定",divider="gray")

st.write("作成したファイルをGitHubにaddされないようにする")
st.write("「.gitignore」を作成")

t = '''
streamlit_app
 L __init__.py         
 L main.py          
 L pages            
     L 01_page1.py
     L 02_page2.py
 L images           
     L hoge.png
     L video.mp4
 L requirements.txt 
 L  .streamlit         
     L secrets.toml    
 L  .gitignore         <- 直下に「.gitignore」を作成
'''
st.code(t, language="yaml")

st.write("「.gitignore」内に除外対象のファイル名またはディレクトリ名を指定")
st.caption("設定方法の詳細は[ここで確認](https://zenn.dev/purigen/articles/67bb8de047e1bb)")
t = '''
/.streamlit/
'''
st.code(t, language="yaml")

st.write("あとはいつも通り[デプロイ方法](/deploy)でGitHubへ公開")
st.warning("一度公開したファイルは非公開処理されないので、別に処理処理が必要")

st.header("4. Streamlit Cloudでの環境変数の設定", divider="gray")

st.write("streamlit Cloudにログインして公開済みアプリの3点リーダーをクリック")
st.image("./download/apikey1.png")

st.write("「settings」をクリック")
st.image("./download/apikey2.png")

st.write("「Secrets」に「secrets.toml」と同じ内容をコピー&ペーストして「Save」をクリックして完了!")
st.image("./download/apikey3.png")

st.subheader("これで環境変数を非公開にしてWebAPIを利用した")
st.subheader("Webアプリの公開が可能になる！！")