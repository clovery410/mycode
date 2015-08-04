#define IDENT(x) PRAGMA(ident #x)
#define PRAGMA(x) _Pragma(#x)



IDENT(foo)
PRAGMA(ident "foo")
_Pragma("ident \"foo\"")
#pragma ident "foo"
