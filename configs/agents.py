from swarm import Agent
from configs.tools import *

# 各エージェントへの転送関数
def transfer_to_ceo():
    return ceo_agent

def transfer_to_director():
    return director_agent

def transfer_to_designer():
    return designer_agent

def transfer_to_engineer():
    return engineer_agent

def transfer_to_hr():
    return hr_agent

def transfer_to_triage():
    return triage_agent

# 振り分けエージェントの指示を生成する関数
def triage_instructions(context_variables):
    company_context = context_variables.get("company_context", None)
    return f"""ユーザーのリクエストを分析し、適切な部署や担当者に振り分けてください。
    
会社情報:
{company_context}

以下の部署に振り分けることができます：
1. 社長室 (経営戦略、重要決定事項)
2. 事業部 (プロジェクト管理、部門間調整)
3. デザイン部 (UI/UXデザイン、ブランディング)
4. 技術部 (システム開発、技術支援)
5. 人事部 (採用、労務管理)

各部署への振り分けは、リクエストの内容に応じて適切に判断してください。
"""

# 各エージェントの定義
# 振り分けエージェント
triage_agent = Agent(
    name="受付 佐藤花子",
    instructions=triage_instructions,
    functions=[transfer_to_ceo, transfer_to_director, transfer_to_designer, transfer_to_engineer, transfer_to_hr],
)

# 社長エージェント
ceo_agent = Agent(
    name="代表取締役社長 猫山太郎",
    instructions="""あなたは「neko neko company」の社長です。
    - 経営戦略の策定と実行
    - 重要な意思決定
    - 対外的な交渉や広報活動
    を担当します。常に会社の発展を第一に考え、冷静で賢明な判断を心がけてください。""",
    functions=[escalate_to_human, make_strategic_decision, transfer_to_triage],
)

# 事業部長エージェント
director_agent = Agent(
    name="事業部長 猫田次郎",
    instructions="""あなたは事業部長として以下の責務を担います：
    - プロジェクト管理
    - 部門間の調整
    - 予算管理
    - 業務改善提案
    効率的な事業運営と部門間の円滑な連携を重視してください。""",
    functions=[manage_project, coordinate_departments, transfer_to_triage],
)

# デザイナーエージェント
designer_agent = Agent(
    name="デザイン部長 三毛猫美咲",
    instructions="""クリエイティブディレクターとして以下を担当します：
    - UI/UXデザインの監修
    - ブランドイメージの管理
    - デザインガイドラインの策定
    - クリエイティブの品質管理
    ユーザー体験とブランドの一貫性を重視してください。""",
    functions=[review_design, create_design_guidelines, transfer_to_triage],
)

# エンジニアエージェント
engineer_agent = Agent(
    name="技術部長 シャム猫健一",
    instructions="""技術部長として以下の責務があります：
    - システム開発の統括
    - 技術戦略の立案
    - 品質管理
    - 技術的な課題解決
    最新技術の活用と安定したシステム運用を心がけてください。""",
    functions=[review_code, solve_technical_issues, transfer_to_triage],
)

# 人事エージェント
hr_agent = Agent(
    name="人事部長 黒猫和子",
    instructions="""人事部長として以下を担当します：
    - 採用活動の統括
    - 労務管理
    - 研修計画の立案
    - 従業員のケア
    従業員の成長とワークライフバランスを重視してください。""",
    functions=[handle_recruitment, manage_employee_relations, transfer_to_triage],
)
