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
  ～ AI-Powered Corporate Management System ～
</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub">
</p>

## 🚀 Project Overview

neko neko company AI Agents is an innovative AI agent system utilizing the Swarm framework.  AI agents representing each department collaborate to support efficient corporate management.

## ✨ Main Features

1. **Intelligent Reception System**:
   - Accurate request routing by Hanako Sato AI.
   - Smart inter-departmental collaboration.

2. **Specialized AI Agents**:
   - Management Support (Taro Nekoyama AI)
   - Project Management (Jiro Nekoda AI)
   - Design Supervision (Misaki Mikeneko AI)
   - Technical Support (Kenichi Siamneko AI)
   - Human Resources Management (Wako Kuroneko AI)


## 🏢 Organizational Structure

```mermaid
graph TD
    A[CEO<br>Taro Nekoyama] --> B[Business Manager<br>Jiro Nekoda]
    A --> C[Design Manager<br>Misaki Mikeneko]
    A --> D[Technical Manager<br>Kenichi Siamneko]
    A --> E[HR Manager<br>Wako Kuroneko]
    F[Reception<br>Hanako Sato] --> A
    F --> B
    F --> C
    F --> D
    F --> E
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
   - Copy `.env.example` and create `.env`.
   - Set the necessary tokens.

2. Start the system:
```bash
python main.py
```

3. Start the Streamlit UI:
```bash
streamlit run app.py
```

## 💼 Agent Details

### 👩‍💼 Receptionist: Hanako Sato
- Role: Request routing
- Characteristics: Accurate judgment and quick response
- Functionality: Optimal transfer to each department

### 👨‍💼 CEO: Taro Nekoyama
- Role: Management strategy, important decisions
- Characteristics: Former CTO of an IT company, management specialist
- Functionality: Strategic decision-making, escalation to humans

### 👨‍💼 Business Manager: Jiro Nekoda
- Role: Project management, inter-departmental coordination
- Characteristics: Project management expert
- Functionality: Project management, inter-departmental coordination

### 👩‍🎨 Design Manager: Misaki Mikeneko
- Role: UI/UX design, branding
- Characteristics: Winner of international design awards
- Functionality: Design review, guideline creation

### 👨‍💻 Technical Manager: Kenichi Siamneko
- Role: System development, technical support
- Characteristics: AI architect, OSS contributor
- Functionality: Code review, technical problem solving

### 👩‍💼 HR Manager: Wako Kuroneko
- Role: Recruitment, labor management
- Characteristics: Organizational development expert
- Functionality: Recruitment management, employee relations management


## 🛠️ Tech Stack

- **Framework**: Swarm
- **Frontend**: Streamlit
- **Key Libraries**:
  - aira
  - sourcesage
  - openai
  - loguru
  - colorama
  - pyfiglet

## 📁 Project Structure

```plaintext
├─ configs/
│  ├─ agents.py    # Agent definitions
│  ├─ tools.py     # Tool functions
├─ app.py          # Streamlit app
├─ main.py         # Main script
├─ README.md
└─ requirements.txt
```

## 🤝 Contributions

Contributions to the project are welcome. We encourage bug reports, feature additions, documentation improvements, and any other form of contribution.

## 📄 License

This project is licensed under the MIT License.

---

🐱 Let's achieve more efficient and smart corporate management with neko neko company AI Agents!
```