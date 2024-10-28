<p align="center">
   <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-neko-neko-company/refs/heads/main/docs/swarm-neko-neko-company.png" width="100%">
   <h1 align="center">🐱 neko neko company AI Agents 🐱</h1>
</p>

<p align="center">
  <a href="https://github.com/yourusername/swarm-neko-neko-company">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-neko--neko--company-blue?logo=github">
  </a>
  <a href="https://github.com/yourusername/swarm-neko-neko-company/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
  </a>
  <a href="https://github.com/yourusername/swarm-neko-neko-company/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/yourusername/swarm-neko-neko-company?style=social">
  </a>
</p>

<h2 align="center">
  ～ A wonderfully amazing AI-Powered Corporate Management System ～

<a href="https://github.com/Sunwood-ai-labs/swarm-neko-neko-company/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/Sunwood-ai-labs/swarm-neko-neko-company/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>

</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
</p>

## 🚀 Project Overview

neko neko company AI Agents is an innovative AI agent system utilizing the Swarm framework.  Cute cat-themed AI agents cooperate in their respective areas of expertise to support efficient corporate management. They're incredibly reliable allies!

## 🎥 Demo Video

https://github.com/user-attachments/assets/0f12fce0-214e-42a6-bdba-c19a7bfc3f07

## ✨ Main Features

1. **Intelligent Reception System**:
   - Accurate request routing by Mikeko AI
   - Smart inter-departmental collaboration

2. **Specialized Cat-Eared AI Agents**:
   - Management decision support (Nyantaro AI)
   - Project management (Mofusuke AI)
   - Design supervision (Purin AI)
   - Technology strategy (Tama AI)
   - System development (Gomachan AI)
   - Human resource management (Fuwari AI)

## 🏢 neko neko company AI Organizational Structure

```mermaid
%%{init: {'theme':'base'}}%%
graph LR
    A[CEO<br>Nyantaro] -->|transfer_to_director| B[Director<br>Mofusuke]
    A -->|transfer_to_designer| C[Design Director<br>Purin]
    A -->|transfer_to_tech_lead| D[Tech Director<br>Tama]
    A -->|transfer_to_hr| E[HR Director<br>Fuwari]
    A -->|transfer_to_engineer| F[Lead Engineer<br>Gomachan]
    G[Reception<br>Mikeko] -->|transfer_to_ceo| A
    G -->|transfer_to_director| B
    G -->|transfer_to_designer| C
    G -->|transfer_to_tech_lead| D
    G -->|transfer_to_hr| E
    G -->|transfer_to_engineer| F

    %% 各エージェントの実行関数と成果
    A -->|make_strategic_decision| S[Management Decisions]
    A -->|escalate_to_human| H[Escalation to Human]
    
    B -->|manage_project| P[Project Planning]
    B -->|coordinate_departments| CD[Departmental Coordination]
    
    C -->|review_design| RD[Design Review]
    C -->|create_design_guidelines| DG[Design Guidelines]
    
    D -->|review_code| RC[Code Review]
    D -->|solve_technical_issues| TI[Technical Issue Resolution]
    
    F -->|write_code| WC[Code]
    F -->|debug_code| DC[Bug Fixing]
    
    E -->|handle_reception| R[Recruitment]
    E -->|manage_employee_relations| ER[Employee Relations Management]

    %% 成果物のスタイル
    classDef result fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    class S,H,P,CD,RD,DG,RC,TI,WC,DC,R,ER result
```

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/swarm-neko-neko-company.git
cd swarm-neko-neko-company
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Set environment variables:
   - Copy `.env.example` and create `.env`
   - Set the necessary tokens

2. Start the system:
```bash
python main.py
```

3. Start the Streamlit UI:
```bash
streamlit run app.py
```

## 💼 Agent Details

### 🐱 Receptionist Mikeko
- Role: Request routing
- Characteristics: Smart and kind calico cat, excellent judgment
- Functions: Optimal transfer and coordination to each department

### 😺 CEO Nyantaro
- Role: Management strategy, important decisions
- Characteristics: Former IT company CTO, management specialist
- Catchphrase: "Important decision, nya!"
- Functions: Strategic decision-making, escalation to humans

### 😸 Director Mofusuke
- Role: Project management, department coordination
- Characteristics: Fluffy long-haired cat, project management expert
- Catchphrase: "Schedule management is perfect, nya!"
- Functions: Project management, inter-departmental coordination

### 😺 Design Director Purin
- Role: UI/UX design, branding
- Characteristics: Cute brown tabby cat, excellent sense
- Catchphrase: "Lovely design, nya~♪"
- Functions: Design review, guideline creation

### 🐱 Tech Director Tama
- Role: System architecture design, technology strategy
- Characteristics: Cool white cat, technology expert
- Catchphrase: "Architecture design, nya!"
- Functions: Technology strategy planning, quality control

### 😺 Lead Engineer Gomachan
- Role: System development, implementation
- Characteristics: Black cat, coding genius
- Catchphrase: "Fixing bugs, nya~!"
- Functions: Coding, debugging, unit test creation

### 😽 HR Director Fuwari
- Role: Recruitment, labor management
- Characteristics: Kind Persian cat, soothing
- Catchphrase: "Making everyone happy, nya♪"
- Functions: Recruitment management, employee relations management

## 🛠️ Tech Stack

- **Framework**: Swarm
- **Frontend**: Streamlit
- **Main Libraries**:
  - aira
  - sourcesage
  - openai
  - loguru
  - colorama
  - pyfiglet

## 📁 Project Structure

```plaintext
├─ configs/
│  ├─ agents.py    # The incredibly clever agents
│  ├─ tools.py     # Useful tools
├─ app.py          # Streamlit app
├─ main.py         # Main script
├─ README.md       # This file
└─ requirements.txt
```

## 🤝 Contributions

Contributions to the project are welcome! We look forward to contributions of all kinds, including bug reports, feature additions, and documentation improvements.  We eagerly await your wonderfully amazing ideas!

## 📄 License

This project is licensed under the MIT License.

---

🐱 Let's achieve more efficient and smart corporate management with neko neko company AI Agents! Nya♪
```