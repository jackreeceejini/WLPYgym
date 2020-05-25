from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

session = WolframLanguageSession()



if __name__ == '__main__':  
    session.evaluate(wlexpr('Table[x,{x,5}]'))
