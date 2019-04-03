subst :: Eq t => t -> t -> [t] -> [t]
subst a b [] = []
subst a b (x:xs)= 
    if a==x
    then 
      b:(subst a b xs)
    else
      x:(subst a b xs)