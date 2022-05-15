def q_S (x):
    
    if len(x)> 1:
        R=x.pop()
        B_spisok, An_spisok, M_spisok = [], [R], []
        
        for i in x:
            
            if i < R:
                M_spisok.append(i)
            elif i == R:
                An_spisok.append(i) 
            else:
                B_spisok.append(i)
                
        return (q_S(M_spisok) + An_spisok + q_S(B_spisok))
        
    else:
        return x
