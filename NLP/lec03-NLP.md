# Lecture 3: Natural Language Processing

> 이 자료는 고려대 강필성 교수님의 [강의 자료](https://github.com/pilsung-kang/text-mining)를 공부하고 정리한 자료입니다.



## Introduction to NLP

### Classical categorization of NLP

- Phonology (음운론) - the study of linguistic sounds
- Morphology (형태론) - the study of meaningful components of words
- Syntax (구문론, 통사론) - the study of structural relationships between words
- Semantics (의미론) - the study of meaning
- Pragmatics (어용론) - the study of how language is used to accomplish goals
- Discourse (담화론) - the study of larger linguistic units



### Why is NLP hard?

- Ambiguity appears on every analysis level
- Complex and subtle relationship between concepts in texts
- Ambuiguity and context sensitivity



## Lexical Analysis (어휘 분석)

- Goals
  - 문자 sequence를 토큰 sequence로 변환하는 것
- Process of lexical analysis
  - Tokenizing
  - POS tagging
  - Additional analysis: NER, 명사구 인식, 문장 분리, 단위화 (chunking)



- 1) Sentence Split
- 2) Tokenization
- 3) Morphological Analysis
  - Stemming - 단어를 기본형으로 축소
    - 규칙 기반으로도 가능 (보통 접미사를 제거)
    - 영어의 표준 알고리즘: Porter stemmer
    - Advantages
      - 간편, 신속
    - Disadvantages
      - 규칙은 언어에 따라 달라짐
      - 없는 단어를 생성할 수도 있음 (computers → comput)
      - 다른 단어를 같은 stem으로 만들어버림 (army, arm → arm)
    - Information Retrieval (정보 검색)
  - Lemmatization - 단어를 lemma로 축소 (root)
    - Advantages
      - 실제 단어인 root form을 인식
      - stemming보다 적은 에러
    - Disadvantages
      - stemming보다 복잡, 느림
      - 추가적인 언어 정보 필요
    - Text Mining
- 4) Part-of-Speech (POS) Tagging
  - 문장 X가 주어졌을 때, POS sequence Y를 예측하는 것
    - Input: 토큰
    - Output: 정의와 문맥을 고려한 가장 적절한 태그
  - POS Tagging Algorithms
    - Pointwise prediction: 각 단어를 개별적으로 예측 (Maximum Entropy Model)
    - Probabilistic models: $\text{argmax}_Y P(Y\vert X)$
      - Generative sequence models: 가장 가능한 태크 sequence를 탐색 (HMM)
      - Discriminative sequence models: 전체 sequence를 예측 (CRF)
    - Neural network-based models
- 5) Named Entity Recognition (NER)
  - 텍스트에서 기학습된 카테고리를 찾고 분류
    - Dictonary/Rule-based
      - List lookup
        - 리스트에 저장된 것만 인식
      - Shallow Parsing Approach
        - 이름들은 내부 구조를 가짐. 이 구성들은 저장되거나 예측될 수 있음 (위치: 대문자)
    - Model-based
      - MITIE (by MIT NLP lab)
      - CRF++
      - CNN (I-of-M coding, Wodr2Vec, n-grams)



## Syntax Analysis

- Syntax Analysis
  - 문법 규칙을 따르도록 심볼들을 분석하는 과정
- Parser
  - 문법에 따라 input string의 구조를 계산하는 알고리즘
  - 모든 parser는 두가지의 기본 속성을 가짐
    - Directionality: 구조가 구축되는 sequence (top-down / bottom-up)
    - Search Strategy: 가능한 분석이 실행될 순서
  - Parsing Representation
    - Tree vs List