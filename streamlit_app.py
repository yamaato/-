import streamlit as st

# アプリケーションのタイトル
st.title('マッチングアプリ')
#　名前を入力させる
user_input = st.text_input('あなたの名前を入力しください')

# ユーザーに質問を表示し、選択肢を提供
gender = st.radio("性別を選択してください", ["男性", "女性"])

# ユーザーの選択に基づいて情報を表示
if sex == '男子':
    
    st.write('お勧めの異性はさんです')
elif sex  == '女子':
    st.write('お勧めの異性は大和さんです')


# アプリケーションの実行
if __name__ == '__main__':
    st.write('アプリを実行するには、ターミナルで "streamlit run your_script.py" を実行してください。')