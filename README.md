# Startup Research Assistant Agent

## Overview

The Startup Research Assistant Agent is an AI-powered business research system designed to analyze companies/startups using external web research and generate structured business insights.

The agent accepts a company research query from the user, retrieves external information using a web search tool, processes the data using an LLM, and returns:

- Company summary
- Main products/services
- Target customers
- Industry focus
- Enterprise AI use cases
- Practical follow-up business action

This project was built as part of an AI Agent Hiring Task assignment.

---

# Objective

Build an AI agent capable of:

1. Understanding user research requests
2. Planning and retrieving company information
3. Using external tools/APIs
4. Producing structured business insights
5. Generating enterprise AI use cases
6. Suggesting actionable follow-up recommendations

---

# Architecture Overview

## Workflow

User Query
↓
AI Agent
↓
Tavily Search Tool
↓
External Web Research
↓
LLM Processing (Groq/OpenAI)
↓
Structured Business Insights
↓
Final Response

---

# Tech Stack

## Backend
- Python

## LLM
- Groq API (Llama3-70B)
  OR
- OpenAI GPT-4o-mini

## External Tool
- Tavily Search API

## Frontend
- Streamlit

## Environment Management
- python-dotenv

---

# Project Structure

```bash
startup-research-agent/

├── app.py
├── agent.py
├── tools.py
├── prompts.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# Agent Design

## 1. User Request Understanding

The agent:
- extracts company name
- understands research intent
- prepares retrieval workflow

Example:

```text
Research OpenAI and suggest 3 enterprise use cases
```

---

## 2. Tool Integration

The system uses Tavily Search API to:
- retrieve company information
- gather external business context
- improve factual grounding

---

## 3. Prompt Engineering

A structured system prompt is used to ensure:
- consistent formatting
- business-focused outputs
- enterprise use case generation
- actionable recommendations

---

## 4. Structured Output

The agent returns:

### Company Summary
- company overview
- products/services
- target customers
- industry focus

### Enterprise Use Cases
Three AI/business use cases based on company research.

### Follow-up Action
A practical business recommendation or next step.

---

# Installation Guide

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd startup-research-agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

OR

```env
OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

# Running the Project

## Terminal Version

```bash
python app.py
```

---

## Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# Example Query

```text
Research OpenAI and suggest 3 enterprise use cases
```

---

# Example Output

## Company Summary
- Company overview
- Products/services
- Customers
- Industry

## Enterprise Use Cases
1. AI customer support automation
2. Internal knowledge assistant
3. Enterprise workflow automation

## Follow-up Action
- Enterprise partnership outreach recommendation

---

# Error Handling

The project handles:
- missing API keys
- empty search results
- invalid company names
- tool/API failures

---

# Limitations

- depends on external API availability
- search quality depends on retrieved web data
- no persistent memory implementation
- no database storage

---

# Future Improvements

- multi-agent workflow
- memory support
- caching
- logging & tracing
- vector database integration
- advanced planning agents
- LangGraph orchestration

---

# Evaluation Criteria Coverage

## Agent Design
- modular architecture
- reasoning workflow
- task orchestration

## Tool Integration
- Tavily Search API integration
- external retrieval system

## Prompt Engineering
- structured prompts
- consistent outputs

## Code Quality
- readable modular code
- separation of concerns

## Edge Case Handling
- API failures
- missing results
- invalid queries

---

# Author

Om Singh