import streamlit as st

st.title("web上へ公開する方法")

st.write("ここではstreamlitの公式サイトとGitHubとの連携によって無料で公開する仕組みを紹介")
st.write("ただし、無料枠内ではいくつか制約があるので注意")
st.error("GitHubでは公開情報となるので、APIKEYなどの公開してはいけない情報がある場合はしっかりと対策をすること！！")

st.divider()

st.header("requirements.txtの作成",divider="gray")
st.write("pipで追加した外部ライブラリを外部サーバーで扱えるようにする")
st.write("カレントディレクトリの直下に「requirements.txt」を作成して、その中に以下の例のように追加する")
st.error("opencvについては「opencv-python」の代わりに「opencv-python-headless」を入れないといけない点に注意！")
t = """
pandas==2.2.1
numpy==1.26.2
matplotlib==3.8.3
opencv-python-headless==4.6.0.66
Pillow==9.5.0
"""
st.code(t, language="textile")

st.write("pipで追加している外部ライブラリとバージョンが分からない場合はコマンドプロンプト(ターミナル)で以下を実行する")
st.write("Windowsの場合")
st.code("pip freeze", language="shellSession")
st.write("Macの場合")
st.code("pip3 freeze", language="objectivec")

st.divider()

st.header("GitHubでアカウント登録",divider="gray")
st.write("GitHubでアカウントを作成していない人は以下のリンクから新規で作成")
st.link_button("GitHubへ", "https://github.co.jp/", type="primary")
st.image("./download/github_main.png")

st.header("Gitの設定",divider="gray")
st.write("1. gitの詳細とインストール方法については次の動画を参考")
st.caption("※9:09-11:36辺りでインストールの説明あり")
st.video("https://youtu.be/6SLMB7BPG9E")
st.write("2. インストールが完了したら、PC内のGitの初期設定を行なう")
t = """
git config --global user.name "〇〇"
git config --global user.email "〇〇@△△.△△"
"""
st.code(t, language="objectivec")
st.caption("※「〇〇」には半角英数でユーザー名を入れる")
st.caption("※「〇〇@△△.△△」にはGitHubで登録したメールアドレスを入れる")
st.write("3. 正しく設定できているか確認")
st.code("git config --global --list", language="objectivec")

st.write("4. GitHubで新しいレポジトリを作成する")
st.caption("メインのダッシュボードページにある「New」を選択")
st.image("./download/create_repository.png")
st.caption("レポジトリ名を設定して作成ボタンをクリック")
st.image("./download/set_name.png")
st.write("作成が完了すると以下のページが表示される")
st.image("./download/repository.png")

st.write("5.「streamlit run 〇〇.py」をするときに居るカレントディレクトリ上で以下のコマンドを入力")
st.code("git init", language="objectivec")

st.write("6. PCのgitを先ほど作成したGitHub内のレポジトリに反映させる")
t = """
git add -A
git commit -m "first commit"
git remote add origin git@github.com:◻︎◻︎◻︎/▽▽▽▽▽.git
git push -u origin main
"""
st.code(t, language="textile")
st.text("「git@github.com:◻︎◻︎◻︎/▽▽▽▽▽.git」部分は上記画像の「← この部分を覚えておく」を入れれば良い")
st.caption("「◻︎◻︎◻︎」はGitHubで登録したユーザー名")
st.caption("「▽▽▽▽▽」はGitHubで登録したレポジトリ名")

st.write("7. 以後、追加や変更がある場合は以下を行なえばOK")
t = """
git add -A
git commit -m "変更内容などのコメントを入力"
git push -u origin main
"""
st.code(t, language="textile")

st.divider()

st.header("Streamlit Cloudでアカウント登録",divider="gray")
st.write("Streamlit Cloudでアカウントを作成する")
st.write("新規登録する時は、「Continue with GitHub」を選択すること")
st.link_button("Streamlit Cloudへ", "https://share.streamlit.io/signup", type="primary")
st.image("./download/streamlit_login.png")

st.write("「New app」をクリック")
st.image("./download/create_app.png")

st.write("必要事項を設定して「Deploy!」をクリック")
st.image("./download/deploy_app.png")

st.subheader("ホームページが表示されたら完了！ブラウザのURLバーにあるURLを共有すれば誰でも閲覧可能")