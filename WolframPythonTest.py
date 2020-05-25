from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

session = WolframLanguageSession()



if __name__ == '__main__':  
    session.eval(wlexpr('Table[x,{x,5}]'))
