# 🦆 Ducky: AI-Powered Coding Assistant

**Ducky** is an AI-driven coding assistant designed to help software developers and learners streamline their workflow. It combines large language models (LLMs), prompt engineering, and blueprint-driven code generation into an interactive web application.

This project was developed as part of a course exploring applied AI in software development.

---

## ✨ Features

- 💬 **Quick Chat**
  - Get instant answers to coding questions.
- 📝 **Learning Mode**
  - Interactive explanations of development concepts.
- 🧠 **Code Review**
  - AI-assisted review of submitted code snippets.
- 🐞 **Debugging**
  - Guidance on fixing errors based on code and error messages.
- 🔄 **Code Modification**
  - Natural language instructions to refactor or improve code.
- 📄 **Blueprint Generation**
  - Generate project scaffolds using agent-based blueprints.
- 🗂️ **Dynamic Prompt Management**
  - Fetch prompts from an external server without redeployment.
- 🎨 **Customizable Interface**
  - Modern frontend with theming, icons, and navigation.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **LLM Integration:** OpenAI GPT-4 Turbo
- **Prompt Management:** CodePromptu server
- **Agent Framework:** aitools-autogen
- **Other Libraries:** httpx, markdownify, and supporting dependencies

---

## 🗂️ Project Overview

The project was developed in multiple phases:

- **Requirements Engineering**
  - Generated business and vision statements, RACI matrices, and ecosystem maps.
- **Prompt Engineering**
  - Created reusable prompts for coding assistance.
- **Application Development**
  - Built a Streamlit application supporting quick chat, learning, review, debug, and code modification.
- **External Prompt Integration**
  - Connected to the CodePromptu server to dynamically retrieve prompt text.
- **Blueprint Development**
  - Designed and implemented custom blueprints to automate code generation workflows.
- **Agent-Based Code Generation**
  - Added capabilities to run multi-agent blueprints for generating project files.

---

## 📁 Repository Structure (Selected)


---

## 🧩 Blueprint Capabilities

The application supports blueprint-driven code generation. A custom blueprint generates multiple code files to help developers solve problems beyond simple API scaffolds.

---

## 🌐 Prompt Management

Prompts for chat, learning, review, debug, and modify tasks are retrieved dynamically via the CodePromptu server using secure API calls.

---

## ⚠️ Important Notes

- **OpenAI API Connection**
  - The OpenAI credentials and API connection originally used for this project have expired and are no longer active.
  - The project is effectively **offline** and will not function fully without new credentials.
  - If you wish to reuse this project, you must supply your own valid OpenAI API key and configure the environment variables.

- **CodePromptu Integration**
  - CodePromptu credentials are also not included in this repository.
  - You will need to configure your own account and update `.env` with your credentials.

- **Setup**
  - This project was developed and graded as part of a university course.
  - Detailed build instructions, credentials, and configuration steps are intentionally omitted.

If you are reviewing this project and would like more information, please contact the repository owner.

---

## 🙌 Acknowledgments

- **OpenAI GPT-4 Turbo** for LLM capabilities
- **Streamlit** for the user interface
- **aitools-autogen** for blueprint agent support
- **CodePromptu** for external prompt storage
- **The Pragmatic Programmer** as a learning reference

---

## 📝 License

This project was completed for academic purposes. Reuse or distribution should be coordinated with the author.
