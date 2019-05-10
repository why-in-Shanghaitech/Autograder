class Poople:
    def __init__(self, doc_path):
        self.id2name = {}
        self.inverted_index = {}
        raise NotImplementedError
    
    def tokenizer(self):
        raise NotImplementedError

    def build_index(self):
        raise NotImplementedError

    def Query(self, query, mode='AND'):
        raise NotImplementedError

    def Rank(self, query, mode='AND'):
        raise NotImplementedError
