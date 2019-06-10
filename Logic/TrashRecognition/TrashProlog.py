from pyswip import Prolog

def get_trash(day: str):
    prolog = Prolog()
    from os import sep # os invariant separator
    prolog.consult(f"Logic{sep}TrashRecognition{sep}TrashKnowledge.pl")
    print(list(prolog.query("collect_trash(X)")))

if __name__ == "__main__":
    get_trash("monday")