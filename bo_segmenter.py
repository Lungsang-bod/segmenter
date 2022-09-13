from botok import sentence_tokenizer

from pathlib import Path


def get_sentence(wt):
    tokens = wt.tokenize(input_file, split_affixes=False)
    return tokens


input_file = Path('./Input/bo_test.txt').read_text(encoding='utf-8')

if __name__ == "__main__":
    wt = sentence_tokenizer(input_file)
    segmented_string = ""
    tokens = get_sentence(wt)
    for token in tokens:
        segmented_string += token.text + "\t" + token.lemma + "\t" + token.pos + "\t" + "NONE" + "\n"
    Path('./segmented.txt').write_text(segmented_string, encoding='utf-8')
