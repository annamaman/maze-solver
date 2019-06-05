# 正方形型のテキストを分析
class SquareTextAnalyzer(object):
    def __init__(self, filename):
        self.filename = filename

    # 正方形の一辺のサイズ    
    def get_text_size(self):
        text_size = 0
        with open(self.filename, encoding='utf-8') as f:
            content = f.read()
        for ch in content:
            if ch == "\n":
                break
            text_size = text_size + 1
        return text_size
    
    # 正方形を維持したままリスト型へ
    def text_to_list(self):
        text_size = self.get_text_size()
        text_list = [[0 for i in range(text_size)] for j in range(text_size)]
        i = 0
        j = 0
        for ch in self.__iter_chars():
            if j == text_size:
                j = 0
                i = i + 1
            text_list[i][j] = ch
            j = j + 1
        return text_list
    
    # テキストを一文字ずつ分解してイテレーション
    def __iter_chars(self):
        with open(self.filename, encoding='utf-8') as f:
            content = f.read()
        for ch in content:
            if ch == "\n":
                continue
            yield ch