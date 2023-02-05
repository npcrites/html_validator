#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    html = _extract_tags(html)
    stack = []
    for symbol in html:
        if symbol[0:2] != '</':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            if symbol[2:-1] == stack[-1][1:-1]:
                stack.pop()
    return len(stack) == 0

# HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from
    # class will be that you will have to keep track of not just
    # the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used
    directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.



>>> _extract_tags('Python <strong>rocks</strong>!')
['<strong>', '</strong>']
    '''
    result = []
    while ('<' in html):
        start_index = html.find('<')
        # finding the start tag index
        space_index = html.find(' ', start_index)
        # addressing the space-tag edge case
        end_tag_index = html.find('>')
        if space_index != -1 and space_index < end_tag_index:
            result.append(html[start_index: space_index] + ">")
            # appending text from start index to space index
        elif end_tag_index == -1:
            # addressing '<' edge case
            result.append("<fail>")
            break
        else:
            result.append(html[start_index: end_tag_index + 1])
            # appending parsed tag from input string
        html = html[end_tag_index + 1:]
        # redefining 'html' for next iteration
    return result
