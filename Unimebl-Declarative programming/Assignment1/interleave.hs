interleave :: [t] -> [t] -> [t]
interleave [] [] = [] 
interleave (x:xs) [] = (x:xs)
interleave [] (y:ys) = (y:ys)
interleave (x:xs) (y:ys)=
    x:y:(interleave xs ys)