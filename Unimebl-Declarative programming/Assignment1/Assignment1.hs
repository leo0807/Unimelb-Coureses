--  File     : Assignment1.hs
--  Author   : Junxu Zhang
--  Purpose  : This is Assignment1
module Assignment1 (subst, interleave, unroll) where
subst :: Eq t => t -> t -> [t] -> [t]
subst a b [] = []
subst a b (x:xs)= 
    if a==x
    then 
      b:(subst a b xs)
    else
      x:(subst a b xs) 
interleave :: [t] -> [t] -> [t]
interleave [] [] = [] 
interleave (x:xs) [] = (x:xs)
interleave [] (y:ys) = (y:ys)
interleave (x:xs) (y:ys)=
    x:y:(interleave xs ys)
unroll :: Int -> [a] -> [a]
unroll 0 (x:xs) = xs
unroll n []     = []
unroll n (x:xs) = 
        take n (cycle (x:xs))