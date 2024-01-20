import re

from preprocessing.tokenizer_config import (
    token_pattern,
    same_chars_3,
    same_terms_15,
    affix_list_15,
    halfspace,
)


def tokenize_text(text):
    """Use regular expression to extract tokens"""
    tokens = re.findall(token_pattern, text)
    return tokens


def normalize_tokens(tokens):
    """normalize a set of ordered tokens, extracted from a text"""
    intermed_tokens = [token.lower() for token in tokens]
    intermed_tokens = [_uniteForms(itoken, same_chars_3) for itoken in intermed_tokens]
    intermed_tokens = [_uniteForms(itoken, same_terms_15) for itoken in intermed_tokens]
    # english numbers
    # remove fathe, kasre, marks and etc
    # remove frequents
    normalized_tokens = _merge_over_tokenized(intermed_tokens, affix_list_15)

    return normalized_tokens


"""utility functions for normalizing
"""


def _uniteForms(input: str, lower_alternatives: dict):
    for lower_form, other_forms in lower_alternatives.items():
        for other_form in other_forms:
            input = input.replace(other_form, lower_form)
    return input


def _merge_by_halfspace(t1, t2):
    return t1 + halfspace + t2


def _remove_token_by_index(tokens, i):
    new_tokens = tokens[:i] + tokens[i + 1 :]
    return new_tokens, len(new_tokens)


def _merge_over_tokenized(tokens: list, affix_list: dict):
    token_len, i = len(tokens), 0
    while i < token_len:
        for affix in affix_list["post"] + affix_list["pre"]:
            if affix == tokens[i]:
                # postfix processing
                if affix in affix_list["post"]:
                    # merge with prev token
                    tokens[i - 1] = _merge_by_halfspace(tokens[i - 1], tokens[i])
                    tokens, token_len = _remove_token_by_index(tokens, i)
                    i -= 1
                else:
                    # merge with next token
                    tokens[i] = _merge_by_halfspace(tokens[i], tokens[i + 1])
                    tokens, token_len = _remove_token_by_index(tokens, i + 1)
        i += 1
    return tokens
