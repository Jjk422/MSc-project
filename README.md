# MSc-project
Msc project

## Required python libraries to run
### All scripts
- Python 3
- Jupyter notebook
- NLTK

## Individual scripts
### iteration_1_PDF data extractor.ipynb
- ...

### iteration_2_part_of_speech_grammar_parser.ipynb
- ...

### iteration_2_part_of_speech_grammar_parser_removed_old_code.ipynb
- dicttoxml

### iteration_3_stanford_dependency_parser.ipynb
- standfordnlp
- Unittest

## Script summary
### iteration_1_PDF data extractor.ipynb
- First try at concept and relationship extraction
- Extracts concepts, and calculates metrics for concept accuracy vs manual concepts extracted

### iteration_2_part_of_speech_grammar_parser.ipynb
- Old version of the second try at concept and relationship extraction

### iteration_2_part_of_speech_grammar_parser_removed_old_code.ipynb
- New version of the second try at concept and relationship extraction
- Works better then the first and automatically extracts concepts and relationships from text
- Also includes a link to the full pdfminer text extraction for the service operation book
- Includes a converter to xml so output can be easily viewed in chrome

### iteration_3_stanford_dependency_parser.ipynb
- This includes an example of the standford dependency parser that seems to work a bit better than NLTK
- Uses the text version of the glossary and definitions to gather concepts from the text
- Once concepts have been gathered, searches text for relations between the concepts
- Stores concepts and relations within simple knowledge base
- Includes question generator that uses templates to generate questions
- Can generate questions based on the definitions, the books where the concept is most talked about and the
relationships between concepts