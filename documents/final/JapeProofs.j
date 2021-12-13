CONJECTUREPANEL Quiz
PROOF "(P1∧P2∧P3)→C, P1, P2, P3 ⊢ C"
INFER (P1∧P2∧P3)→C,
     P1,
     P2,
     P3 
     ⊢ C 
FORMULAE
0 C,
1 P1∧P2∧P3,
2 P1∧P2∧P3→C,
3 P3,
4 P1∧P2,
5 P2,
6 P1,
7 (P1∧P2∧P3)→C 
IS
SEQ (cut[B,C\4,0]) ("∧ intro"[A,B\6,5]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "(P∧C1), ¬C2, ¬C3 ⊢ (P∧¬C2)∧(P∧¬C3)"
INFER (P∧C1),
     ¬C2,
     ¬C3 
     ⊢ (P∧¬C2)∧(P∧¬C3)
FORMULAE
0 P∧¬C3,
1 P∧¬C2,
2 (P∧¬C2)∧(P∧¬C3),
3 ¬C2,
4 P,
5 ¬C3,
6 P∧C1,
7 C1 
IS
SEQ (cut[B,C\4,2]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\4,7]) (hyp[A\6])) (cut[B,C\0,2]) ("∧ intro"[A,B\4,5]) (hyp[A\4]) (hyp[A\5]) (cut[B,C\1,2]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\1,2]) (hyp[A\1]) (cut[B,C\0,2]) (hyp[A\0]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "¬¬P ⊢ P"
INFER ¬¬P 
     ⊢ P 
FORMULAE
0 ⊥,
1 ¬¬P,
2 ¬P,
3 P 
IS
SEQ ("contra (classical)"[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q ⊢ ¬Q→¬P"
INFER P→Q 
     ⊢ ¬Q→¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q,
5 ¬P 
IS
SEQ ("→ intro"[A,B\1,5]) ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Quiz
PROOF "(T∨P)→¬Q, S→(T∨P) ⊢ S→¬Q"
INFER (T∨P)→¬Q,
     S→(T∨P)
     ⊢ S→¬Q 
FORMULAE
0 ¬Q,
1 T∨P,
2 T∨P→¬Q,
3 S,
4 S→T∨P,
5 S→(T∨P),
6 (T∨P)→¬Q 
IS
SEQ ("→ intro"[A,B\3,0]) (cut[B,C\1,0]) ("→ elim"[A,B\3,1]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\1,0]) (hyp[A\1]) (cut[B,C\0,0]) ("→ elim"[A,B\1,0]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q, ¬Q ⊢ ¬P"
INFER P→Q,
     ¬Q 
     ⊢ ¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q 
IS
SEQ ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P∨¬P"
INFER P∨¬P 
FORMULAE
0 ⊥,
1 ¬(P∨¬P),
2 P∨¬P,
3 P,
4 ¬P,
5 ¬(P∨¬P)
IS
SEQ ("contra (classical)"[A\2]) (cut[B,C\3,0]) ("contra (classical)"[A\3]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\3,4]) (hyp[A\4])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\4,3]) (hyp[A\3])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P ⊢ ¬¬P"
INFER P 
     ⊢ ¬¬P 
FORMULAE
0 ⊥,
1 ¬P,
2 P 
IS
SEQ ("¬ intro"[A\1]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
