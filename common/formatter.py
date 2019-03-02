
class Formatter :
    @staticmethod
    # def current(base:str, trim:str='1') ->str:
    def kwstr(**kwargs) ->str:
        # base = '' if kwargs['base'] is None else kwargs['base']
        # trim = '' if kwargs['trim'] is None else kwargs['trim']
        return base + trim

ret = Formatter.current(base="test", trim="aaaa")
print(ret)