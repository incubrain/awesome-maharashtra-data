#!/usr/bin/env python3
"""
03_gov_rag_quickstart.py — Starter script for Government Scheme RAG.

Demonstrates building a RAG (Retrieval-Augmented Generation) pipeline
over Maharashtra Government Resolutions and scheme documents:
1. Loading mahGRs (Maharashtra Government Resolutions) corpus
2. Chunking and embedding documents
3. Simple retrieval pipeline

Run with: python 03_gov_rag_quickstart.py

Requirements: pip install requests
Optional: pip install sentence-transformers chromadb langchain
"""

import sys


def demo_mahgrs_corpus():
    """Demonstrate the mahGRs corpus for RAG."""
    print("=" * 60)
    print("1. Maharashtra Government Resolutions (mahGRs)")
    print("=" * 60)
    print("""
    Source: https://github.com/orgpedia/mahGRs
    License: CC-BY-4.0
    Size: ~47,000 Government Resolutions from 33 departments
    Languages: Marathi + English (bilingual)

    Clone the corpus:
    ```bash
    git clone https://github.com/orgpedia/mahGRs.git
    ls mahGRs/
    # Contains .pdf and extracted text of GRs by department
    ```

    Departments covered:
    - Agriculture, Revenue, Education, Health
    - Urban Development, Rural Development
    - Water Resources, Finance, Home
    - And 24 more...

    Each GR contains:
    - Department name, GR number, date
    - Subject line (often bilingual)
    - Full text of the resolution
    - Referenced schemes and budgets
    """)


def demo_rag_pipeline():
    """Show a RAG pipeline architecture."""
    print("=" * 60)
    print("2. Building a RAG Pipeline")
    print("=" * 60)
    print("""
    Architecture:
    ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
    │ GR Documents │ --> │ Chunk + Embed│ --> │ Vector Store│
    │ (mahGRs)     │     │ (sentence-   │     │ (ChromaDB)  │
    │              │     │  transformers│     │             │
    └─────────────┘     └──────────────┘     └──────┬──────┘
                                                     │
    ┌─────────────┐     ┌──────────────┐            │
    │ User Query  │ --> │ Retrieve Top-K│ <----------┘
    │ (Marathi/EN)│     │ + Generate   │
    └─────────────┘     └──────────────┘

    Step 1: Load and chunk documents
    ```python
    import os
    from pathlib import Path

    gr_dir = Path("mahGRs/extracted_text/")
    documents = []
    for txt_file in gr_dir.glob("**/*.txt"):
        text = txt_file.read_text(encoding="utf-8")
        # Chunk into ~500 token segments with overlap
        chunks = chunk_text(text, chunk_size=500, overlap=50)
        for chunk in chunks:
            documents.append({
                "text": chunk,
                "source": txt_file.name,
                "department": txt_file.parent.name
            })
    print(f"Created {len(documents)} chunks from GR corpus")
    ```

    Step 2: Create embeddings
    ```python
    from sentence_transformers import SentenceTransformer

    # Use multilingual model that supports Marathi
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    embeddings = model.encode([d["text"] for d in documents])
    ```

    Step 3: Store in vector database
    ```python
    import chromadb

    client = chromadb.Client()
    collection = client.create_collection("mahgrs")
    collection.add(
        embeddings=embeddings.tolist(),
        documents=[d["text"] for d in documents],
        metadatas=[{"source": d["source"], "dept": d["department"]} for d in documents],
        ids=[f"doc_{i}" for i in range(len(documents))]
    )
    ```

    Step 4: Query
    ```python
    query = "शेतकऱ्यांसाठी पीक विमा योजना"  # Crop insurance scheme for farmers
    results = collection.query(query_texts=[query], n_results=5)
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(f"[{meta['dept']}] {doc[:200]}...")
    ```
    """)


def demo_additional_sources():
    """List additional RAG-ready sources."""
    print("=" * 60)
    print("3. Additional RAG-Ready Sources")
    print("=" * 60)
    print("""
    Government Scheme Documents:
    - PM-KISAN: https://pmkisan.gov.in/ (farmer income support)
    - PMFBY: https://pmfby.gov.in/ (crop insurance)
    - MGNREGA: https://nrega.nic.in/ (rural employment)
    - PM Awas Yojana: https://pmaymis.gov.in/ (housing)

    Legal Documents:
    - IndiaCode Maharashtra: https://www.indiacode.nic.in/
    - Bombay HC Judgments: https://indiankanoon.org/browse/bombay/
    - Maharashtra Acts & Rules

    Question-Answering Datasets:
    - AI4Bharat IndicQA (Marathi): HuggingFace ai4bharat/IndicQA
    - L3Cube-MahaSQuAD: 142K Marathi QA samples
    - Marathi Alpaca: 52K instruction-following pairs

    Multilingual Embedding Models:
    - paraphrase-multilingual-MiniLM-L12-v2 (384-dim, fast)
    - multilingual-e5-large (1024-dim, high quality)
    - ai4bharat/indic-sentence-bert (Indic-optimized)
    """)


def main():
    print("Awesome Marathi Datasets — Government Scheme RAG Quickstart")
    print("=" * 60)
    print()

    demo_mahgrs_corpus()
    print()
    demo_rag_pipeline()
    print()
    demo_additional_sources()

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("""
    1. Clone mahGRs corpus and extract text from PDFs
    2. Set up ChromaDB or FAISS vector store
    3. Build a Streamlit/Gradio interface for scheme queries
    4. Add Marathi-English cross-lingual retrieval
    5. Deploy as a citizen service chatbot

    Related catalogs:
    - ../categories/11-governance-census-demographics-legal.md
    - ../categories/14-agentic-instruction-rag.md
    """)


if __name__ == "__main__":
    main()
