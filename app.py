import streamlit as st
from configs.agents import *
from swarm import Swarm
import os
from datetime import datetime

# ページ設定
st.set_page_config(
    page_title="🐱 Neko Neko Company AI Chat 🐱",
    page_icon="🐱",
    layout="wide"
)

# Swarmクライアントの初期化
client = Swarm()

# セッション状態の初期化
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = os.getenv("OPENAI_API_KEY", "")
if 'context_variables' not in st.session_state:
    st.session_state['context_variables'] = {
        "company_context": """neko neko company 会社概要:
    
設立: 2024年
従業員数: 50名
事業内容: AIソリューション開発、システムインテグレーション

主要メンバー:
1. 代表取締役社長 猫山太郎
   - 元IT企業CTO
   - 経営戦略のスペシャリスト
   
2. 事業部長 猫田次郎
   - プロジェクトマネジメントの達人
   - 複数の大規模プロジェクト成功実績
   
3. デザイン部長 三毛猫美咲
   - 国際的なデザイン賞受賞
   - UI/UXデザインの第一人者
   
4. 技術部長 シャム猫健一
   - AIアーキテクト
   - オープンソースコミッティメンバー
   
5. 人事部長 黒猫和子
   - 組織開発のエキスパート
   - 従業員満足度向上のスペシャリスト
"""}

# サイドバーの設定
with st.sidebar:
    st.image("https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-neko-neko-company/refs/heads/main/docs/swarm-neko-neko-company.png", use_column_width=True)
    st.title("🐱 Neko Neko Company")
    
    # API Key設定セクション
    st.markdown("### ⚙️ API設定")
    api_key = st.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.success("✅ API Keyが設定されました！")
    
    st.markdown("---")
    st.markdown("""
    ### 社内AI支援システム
    
    各部署のAIエージェントが、あなたの質問やリクエストに応答します。
    
    #### 🌟 主なエージェント
    - 👋 受付 みけこ
    - 👔 社長 にゃんたろう
    - 📊 事業部長 もふすけ
    - 🎨 デザイン部長 ぷりん
    - 💻 技術部長 たま
    - 🔧 主任エンジニア ごまちゃん
    - 👥 人事部長 ふわり
    """)
    
    if st.button("チャットをクリア"):
        st.session_state['messages'] = []
        st.rerun()

# メインコンテンツ
st.title("🐱 Neko Neko Company AI Chat System")

# チャット履歴の表示
for message in st.session_state['messages']:
    with st.chat_message(message["role"], avatar=message.get("avatar")):
        st.write(f"**{message.get('name', 'User')}**: {message['content']}")

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください..."):
    # ユーザーメッセージの追加
    st.session_state['messages'].append({
        "role": "user",
        "content": prompt,
        "name": "User"
    })
    
    with st.chat_message("user"):
        st.write(f"**User**: {prompt}")

    try:
        # Swarmを使用してエージェントの応答を取得
        messages = [{"role": "user", "content": prompt}]
        
        # メッセージプレースホルダーの作成
        with st.chat_message("assistant", avatar="🐱"):
            message_placeholder = st.empty()
            message_placeholder.markdown("🤔 考え中...")
            
            # 非ストリーミングモードで実行
            response = client.run(
                agent=triage_agent,
                messages=messages,
                context_variables=st.session_state['context_variables'],
                stream=False
            )

            # レスポンスからメッセージを取得
            if response and response.messages:
                # 最後のメッセージを取得
                last_message = response.messages[-1]
                full_response = last_message["content"]
                current_agent_name = last_message.get("sender", triage_agent.name)
                message_placeholder.markdown(f"**{current_agent_name}**: {full_response} 🐱")
        
        # 全てのエージェントの応答を保存
        if response and response.messages:
            for msg in response.messages:
                if msg["role"] == "assistant":
                    st.session_state['messages'].append({
                        "role": "assistant",
                        "content": msg["content"],
                        "name": msg.get("sender", triage_agent.name),
                        "avatar": "🐱"
                    })

    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")

# フッター
st.markdown("---")
st.markdown("© 2024 Neko Neko Company. All rights reserved. 🐱")
