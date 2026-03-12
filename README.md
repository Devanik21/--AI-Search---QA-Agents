# AI Search + QA Agents

**Author:** Devanik

**GitHub:** [https://github.com/Devanik21](https://github.com/Devanik21)

## Overview

AI Search + QA Agents is a unified retrieval‑augmented reasoning system that enables semantic querying across heterogeneous information sources including documents, websites, and GitHub repositories.

The system integrates large language models with structured information retrieval pipelines to produce context‑aware answers. The architecture follows a simplified Retrieval Augmented Generation (RAG) paradigm:

1. Data ingestion
2. Context extraction
3. Prompt construction
4. Generative inference

This repository demonstrates a lightweight yet extensible implementation using **Streamlit + Gemini API**.

---

# System Architecture

The application is organized into three primary intelligent agents:

• Multi‑Document QA Agent
• Website QA Agent
• GitHub Repository Assistant

Each module implements a variant of a context retrieval pipeline.

Let

D = {d1, d2, ... dn}

represent a corpus of documents.

A query q is processed through a function

A(q) = M(q, R(D))

where

R(D) = retrieval function extracting relevant textual context

M = generative model mapping context to an answer.

---

# Retrieval Augmented Generation Formulation

The answer generation process follows

P(a | q, C) = LM(q ⊕ C)

where

q = user query
C = contextual text extracted from sources
LM = large language model

The concatenation operator ⊕ merges query and context.

---

# Agent 1 — Multi‑Document QA Bot

This module enables question answering across multiple uploaded documents.

Supported formats include:

PDF
TXT
DOCX
CSV
JSON
Markdown
PPTX
XLSX
HTML
EPUB

## Document Processing Pipeline

Each document type requires a specialized parser.

For example:

PDF extraction uses PyMuPDF
DOCX uses docx2txt
CSV/XLSX uses pandas
HTML uses BeautifulSoup
EPUB uses ebooklib

The system converts each document into a unified text representation

T = Σ Ti

where Ti represents text extracted from document i.

This combined representation is used as contextual input for the LLM.

---

# Agent 2 — Website QA Agent

The Website Agent performs dynamic retrieval from a provided URL.

Pipeline:

1. HTTP request to fetch page
2. HTML parsing using BeautifulSoup
3. Removal of markup
4. Extraction of semantic text

Let

W = webpage content

Then

C = clean(W)

The generative model receives

LM(q ⊕ C)

---

# Agent 3 — GitHub Repository Assistant

The GitHub assistant clones repositories and performs semantic code inspection.

Pipeline:

1. Repository cloning
2. Recursive file traversal
3. Code aggregation

Let

S = set of source files

S = {s1, s2, ... sn}

The system constructs

C = Σ text(si)

Limited to the first 20000 characters to maintain inference efficiency.

The resulting context is used to generate explanations of the codebase.

---

# Mathematical Interpretation of Context Fusion

Let

Ci be contextual segments extracted from each source.

The aggregated context becomes

C_total = ⋃ Ci

The LLM performs inference

argmax_a P(a | q, C_total)

where a is the generated answer.

---

# Implementation Details

Language: Python
Framework: Streamlit
Model: Gemini 2.0 Flash

Core Libraries

streamlit
PyMuPDF
pandas
docx2txt
BeautifulSoup
ebooklib
python-pptx
openpyxl
GitPython

---

# Performance Considerations

The system limits context length to reduce computational overhead.

Let

L_max = model context window

Then

|C| ≤ L_max

This constraint ensures stable inference latency.

---

# Future Extensions

Potential improvements include:

Vector embeddings
Semantic chunking
Approximate nearest neighbor retrieval
Hybrid search architectures
Knowledge graph integration

---



# License

This project is released without copyright restrictions.

Created March 2026 by Devanik.
