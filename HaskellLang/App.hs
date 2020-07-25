-- so you need to complete this functions
-- it has to return the sum of even numbers that are 
-- multiples of 5 from 0 to n (inclusive)
--sumFiveEven :: Int -> Int -- it should be called sumFiveEven n and return the correct value  
--sumFiveEven = -- You can write the solution here, or use a more space, just mantain the signature.

module App where

sumFiveEven :: Int -> Int
sumFiveEven a = sum $ takeWhile (<a+1) $ filter even . filter (\x -> x `mod` 5 == 0) $ [0..]