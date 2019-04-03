unroll :: Int -> [a] -> [a]
unroll 0 (x:xs) = xs
unroll n []     = []
unroll n (x:xs) = 
        take n (cycle (x:xs))