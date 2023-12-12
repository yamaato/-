import streamlit as st

# アプリケーションのタイトル
st.title('旅行先の国を決めるアプリ')

# ユーザーに質問を表示し、選択肢を提供
country = st.selectbox('どんな国に行きたいですか？', ['日本', 'イタリア', 'フランス', 'アメリカ'])

# ユーザーの選択に基づいて情報を表示
if country == '日本':
    st.write('日本は文化が豊かで美しい国です。')
elif country == 'イタリア':
    st.write('イタリアは美食と歴史が豊かな国です。')
elif country == 'フランス':
    st.write('フランスは芸術と文化が息づく国です。')
else:
    st.write('アメリカは多様性に富んだ国です。')

# アプリケーションの実行
if __name__ == '__main__':
    st.write('アプリを実行するには、ターミナルで "streamlit run your_script.py" を実行してください。')