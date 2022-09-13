from botok import WordTokenizer

from pathlib import Path


def get_tokens(wt):
    tokens = wt.tokenize(choechuk_text, split_affixes=False)
    return tokens


if __name__ == "__main__":
    wt = WordTokenizer()
    choechuk_tokenized_string = ""
    choechuk_text = Path('./Input/bo_test.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt)
    for token in tokens:
        choechuk_tokenized_string += token.text + "\t"
    Path('./Output/tokenized_text.txt').write_text(choechuk_tokenized_string, encoding='utf-8')
