from jose import jwt

SECRET = "87jpagyB399Q2D55BkjdTmBsa6GLoJi4"
ALGORYTHM="HS256"
def CreateToken (claims):
    return jwt.encode(claims=claims,key=SECRET,algorithm=ALGORYTHM)

def ParseToken(token):
    return jwt.decode(token=token,key=SECRET,algorithms=ALGORYTHM)

