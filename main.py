from configs.agents import *
from swarm.repl import run_demo_loop

# コンテキスト変数の設定
context_variables = {
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

if __name__ == "__main__":
    # デモループの実行
    run_demo_loop(triage_agent, context_variables=context_variables, debug=True)
