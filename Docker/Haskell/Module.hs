module Module where

sumFiveEven :: Int -> Int
sumFiveEven a = sum $ takeWhile (<a+1) $ filter even . filter (\x -> x `mod` 5 == 0) $ [0..]
