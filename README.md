# News Intelligence with NLP  

**An NLP-powered dashboard for news classification, entity extraction, and event insights**  

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)  
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=flat-square&logo=streamlit)  
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green?style=flat-square&logo=openai)  
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)  

---

## Overview  
This project applies **Natural Language Processing (NLP)** to analyze the **BBC News Full Text Dataset**.  
It goes beyond simple classification by:  
- Breaking down articles into **fine-grained subcategories**  
- Extracting **named entities** (people, roles, media figures)  
- Summarizing **events in April** across multiple domains  

Everything is packaged into an **interactive Streamlit app** where you can explore the results in real time.  

---

## File Structure

```
News_intelligence_with_NLP/
├── data/                               # Raw + processed datasets  
├── outputs/                            # Generated CSV results  
├── streamlit_app.py                    # Interactive Streamlit dashboard  
├── News_Intelligence_with_NLP.ipynb    # Jupyter/Colab notebook with pipeline steps  
├── README.md                           # Project documentation (this file)  
└── LICENSE                             # MIT license
```

---

## What the project does  

- **Subcategorization**  
  - Classifies the 5 main BBC categories (Business, Politics, Sports, Entertainment, Tech) into detailed subcategories  
  - Uses **GPT-3.5 with dictionary logic** for consistent outputs  

- **Named Entity Recognition (NER)**  
  - Extracts names of people mentioned in articles  
  - Tags their **roles** (e.g., politician, athlete, journalist, CEO)  
  - Filters a dedicated list of **media personalities**  

- **Event Summarization**  
  - Captures and summarizes all **April events** (political summits, sports fixtures, cultural activities)  

- **Streamlit App**  
  - Upload datasets and explore interactively  
  - Search by category, subcategory, role, or event  
  - View clean CSV outputs directly in the app  

---

## Dataset & Outputs  

- Dataset: **BBC News Full Text** (2,225 articles across 5 categories)  
- Processed outputs include:  
  - `bbc_combined_subcategories.csv` → fine-grained classifications  
  - `NER_named_entities.csv` → full list of names + roles  
  - `NER_media_personalities.csv` → curated list of media figures  
  - `April_events_summary.csv` → April-only event dataset  
  - `bbc_full_combined.csv` → integrated dataset  

---

## Workflow  

1. **Data Processing** → Clean and prepare text files  
2. **Subcategorization** → Classify into detailed sub-topics  
3. **NER + Role Classification** → Extract people and occupations  
4. **Media Personality Filter** → Isolate broadcasters, journalists, entertainers  
5. **Event Extraction** → Summarize April-specific events  
6. **Streamlit App** → Deploy results interactively  

---

## Results  

- **Subcategories**  
  Identified 25+ meaningful groupings within BBC’s 5 main categories.  

- **Named Entity Recognition (NER)**  
  Extracted over 1,000 unique names and tagged them with their professional roles.  

- **Media Personalities**  
  Built a focused dataset highlighting journalists, broadcasters, and other public-facing figures.  

- **April Events**  
  Summarized key April events across business, politics, sports, and culture.  

---

## Bias & Limitations  

- **Misclassification Bias**  
  Some subcategories were mislabeled, even with dictionary support. Manually reviewed 50 random outputs to validate results.  

- **Role Ambiguity**  
  Titles like *minister* or *host* were sometimes interpreted differently depending on context.  

- **Mitigation**  
  Applied dictionary-enforced logic and human validation to improve consistency.  

---


## Future Improvements  

- Fine-tune model for more accurate subcategorization.  
- Extend temporal event extraction beyond April to cover events across the full year.  
- Integrate **visual analytics** (charts, timelines, trend graphs) into the Streamlit dashboard.  
- Add user-friendly **search and filtering** within the app for faster exploration.  



👤 Author

Udodirim Nwosu:
udynwosu@gmail.com


