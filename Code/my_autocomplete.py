import timeit


def get_words():
    return open('/usr/share/dict/words').read().splitlines()


def print_nested_dict(dictionary, tabs=0):
    for key, val in dictionary.items():
        print("|  "*tabs, key)
        if isinstance(val, dict):
            print_nested_dict(val, tabs+1)


class AutoCompleter(dict):
    def __init__(self, words=[]):
        super().__init__()
        for word in words:
            ref = self
            for char in word:
                if char not in ref:
                    ref[char] = dict()
                ref = ref[char]

    def __call__(self, prefix):
        options = [prefix]
        sub = self
        for char in prefix:
            sub = sub[char]

        def traverse(t):
            for char, children in t.items():
                options[-1] += char
                if len(children):
                    traverse(children)
                else:
                    options.append(prefix)

        traverse(sub)
        return options[:-1]


def build_retrieval_tree(words):
    base = dict()
    for word in words:
        ref = base
        for char in word:
            if char not in ref:
                ref[char] = dict()
            ref = ref[char]
    return base


def auto_completer(words):
    tree = build_retrieval_tree(words)

    def auto_complete(prefix):
        options = [""]
        sub = tree
        for char in prefix:
            sub = sub[char]

        def traverse(t):
            for char, children in t.items():
                options[-1] += char
                if len(children):
                    traverse(children)
                else:
                    options.append("")

        traverse(sub)
        return options[:-1]

    return auto_complete


if __name__ == '__main__':

    # print('getting words...')
    # words = get_words()
    # print('building lookup tree...')
    auto_complete = AutoCompleter([
        'ikey',
        'ikeyy',
        'hello',
        'pasta',
        'paster'
    ])

    print("finding words that start with 'hel' ...")
    print_nested_dict(auto_complete)
