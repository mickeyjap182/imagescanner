from pprint import pprint

# 連結リストのサンプル
class LinkedList:

    class Cell:
        def __init__(self, data, link=None):
            self.data = data
            self.link = link

    def __init__(self, *args):
        self.top = LinkedList.Cell(None) # ヘッダセル
        for x in reversed(args) :
            self.insert(0, x)

    def __iter__(self):
        # イテレータの状態を作り出すため、iterator取得時に呼び出される(forなら初回のみ)
        self.index = self.top.link
        return self

    def __next__(self):
        # イテレータの繰り返し処理で呼び出される。
        pprint("next")
        if self.index is None:
            raise StopIteration()
        data = self.index.data
        self.index = self.index.link
        return data

    def at(self, n):
        cp = self._nth(n)
        return None if cp is None else cp.data

    def insert(self, n, x):
        # 一つ前のリストを取得
        cp = self._nth(n - 1)
        while cp is not None :
            # 一つ前のリストのリンク先に新しいオブジェクトを指定
            cp.link = LinkedList.Cell(x, cp.link)
            return x
        return None

    def delete(self, n):
        cp = self._nth(n - 1)
        while cp is not None :
            # 一つ前のリストのリンク先を一つ先のオブジェクトに変更
            cp.data = cp.link.data
            cp.link = cp.link.link
            return cp.data
        return None

        pass
    def isEmpty(self, n):
        # 一つ前のリストのリンク先の存在確認
        cp = self._nth(n - 1)
        return True if cp.link is None else False

    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n : return cp
            i += 1
            # リンク先を取得
            cp = cp.link
        return None

ll = LinkedList('a','b')
pprint(ll.insert(1,"a"))
pprint(ll.insert(2,"b"))
pprint(ll.insert(3,"c"))
pprint(ll.insert(4,"d"))
pprint('==中身==')
for ele in ll :
    pprint(ele)
pprint(ll.at(1))
pprint(ll.at(2))
pprint(ll.at(3))
pprint(ll.at(4))
pprint('==削除==')
pprint(ll.delete(1))
pprint('==削除結果==')
pprint(ll.at(1))
pprint(ll.at(2))
pprint(ll.at(3))
pprint(ll._nth(1))