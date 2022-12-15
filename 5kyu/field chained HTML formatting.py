#https://www.codewars.com//kata/5e98a87ce8255200011ea60f
class Format:
    tag = frozenset(("div", "h1", "p", "span"))
    def __init__(self, tg=None):
        self.tags = tg if tg else []
    def __getattr__(self, attr):
        return Format(self.tags + [attr])
    def __call__(self, *args):
        res = ''.join(args)
        for tag in self.tags[::-1]:
            res = f'<{tag}>{res}</{tag}>'
        return res    
format = Format()
