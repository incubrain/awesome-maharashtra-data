#!/usr/bin/env python3
"""
02_marathi_nlp_quickstart.py — Starter script for Marathi NLP tasks.

Demonstrates loading key Marathi language datasets from HuggingFace:
1. L3Cube-MahaCorpus for language model pretraining
2. L3Cube-MahaSent for sentiment analysis
3. AI4Bharat Samanantar for English-Marathi translation

Run with: python 02_marathi_nlp_quickstart.py

Requirements: pip install datasets transformers torch
"""

import sys


def demo_mahacorpus():
    """Demonstrate loading L3Cube-MahaCorpus."""
    print("=" * 60)
    print("1. L3Cube-MahaCorpus — Marathi Pretraining Corpus")
    print("=" * 60)
    print("""
    Source: https://github.com/l3cube-pune/MarathiNLP
    License: CC-BY-NC-SA-4.0
    Size: 24.8M sentences, 289M tokens

    Load from HuggingFace:
    ```python
    from datasets import load_dataset

    # L3Cube MahaCorpus
    ds = load_dataset("l3cube-pune/marathi-corpus")
    print(f"Training samples: {len(ds['train'])}")
    print(f"Sample: {ds['train'][0]['text'][:200]}")
    ```

    Use cases:
    - Marathi language model pretraining
    - Domain adaptation fine-tuning
    - Text generation
    """)


def demo_mahasent():
    """Demonstrate Marathi sentiment analysis."""
    print("=" * 60)
    print("2. L3Cube-MahaSent — Sentiment Analysis")
    print("=" * 60)
    print("""
    Source: https://github.com/l3cube-pune/MarathiNLP
    License: CC-BY-NC-SA-4.0
    Size: 16,000 tweets (3 classes: positive, negative, neutral)

    Quick sentiment analysis with MahaBERT:
    ```python
    from transformers import pipeline

    # Load pre-trained Marathi sentiment model
    sentiment = pipeline(
        "text-classification",
        model="l3cube-pune/marathi-sentiment-md"
    )

    texts = [
        "हा चित्रपट खूपच छान आहे",    # This movie is very good
        "आज हवामान खराब आहे",          # The weather is bad today
        "मला हे पुस्तक आवडले नाही",     # I did not like this book
    ]

    for text in texts:
        result = sentiment(text)
        print(f"  '{text}' -> {result[0]['label']} ({result[0]['score']:.2f})")
    ```
    """)


def demo_samanantar():
    """Demonstrate English-Marathi translation dataset."""
    print("=" * 60)
    print("3. AI4Bharat Samanantar — EN-MR Translation")
    print("=" * 60)
    print("""
    Source: https://huggingface.co/datasets/ai4bharat/samanantar
    License: CC0-1.0
    Size: 3.32M English-Marathi sentence pairs

    Load and explore:
    ```python
    from datasets import load_dataset

    ds = load_dataset("ai4bharat/samanantar", "mr")
    print(f"Parallel pairs: {len(ds['train'])}")

    # Sample pairs
    for i in range(3):
        sample = ds['train'][i]
        print(f"  EN: {sample['src']}")
        print(f"  MR: {sample['tgt']}")
        print()
    ```

    For translation, use AI4Bharat IndicTrans2:
    ```python
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

    model_name = "ai4bharat/indictrans2-en-indic-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    ```
    """)


def demo_tools():
    """Show available Marathi NLP tools."""
    print("=" * 60)
    print("4. Marathi NLP Tools Ecosystem")
    print("=" * 60)
    print("""
    Pre-trained Models:
    - MahaBERT: l3cube-pune/marathi-bert-v2 (HuggingFace)
    - MahaRoBERTa: l3cube-pune/marathi-roberta
    - IndicBERT: ai4bharat/indic-bert
    - IndicTrans2: ai4bharat/indictrans2-en-indic-1B

    Libraries:
    - iNLTK: pip install inltk (text generation, embeddings)
    - Indic NLP Library: pip install indic-nlp-library (tokenization, normalization)
    - Stanza: pip install stanza (POS tagging, NER)

    Quick tokenization example:
    ```python
    from indicnlp.tokenize import indic_tokenize

    text = "महाराष्ट्रातील शेतकऱ्यांना मदत करणे आवश्यक आहे."
    tokens = indic_tokenize.trivial_tokenize(text, 'mr')
    print(tokens)
    # ['महाराष्ट्रातील', 'शेतकऱ्यांना', 'मदत', 'करणे', 'आवश्यक', 'आहे', '.']
    ```
    """)


def main():
    print("Awesome Marathi Datasets — Marathi NLP Quickstart")
    print("=" * 60)
    print()

    demo_mahacorpus()
    print()
    demo_mahasent()
    print()
    demo_samanantar()
    print()
    demo_tools()

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("""
    1. Fine-tune MahaBERT on your domain (agriculture, legal, health)
    2. Build a Marathi chatbot using MahaSQuAD for QA
    3. Create a bilingual search engine with Samanantar embeddings
    4. Train a Marathi NER model using L3Cube-MahaNER

    Full dataset catalog: ../categories/01-language-nlp.md
    Benchmarks & tools: ../categories/15-benchmarks-fairness-dialects-tools.md
    """)


if __name__ == "__main__":
    main()
