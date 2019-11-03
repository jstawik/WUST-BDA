-- For T2:
import Data.List as DL
-- For T3:
import  Data.Numbers.Primes as DNP

-- TASK 1
foldmap :: (a -> b) -> [a] -> [b]
foldmap f = foldr (\x xs->(f x):xs) []

-- TASK 2
sum_of_squares :: Num a => [a] -> a
sum_of_squares = DL.foldl' (\a x -> a + x^2) 0

-- TASK 3
-- count_prime :: Num a => [a] -> a
count_prime = DL.foldl' (\a _ -> a+1) 0 . filter DNP.isPrime

-- TASK 4
e_approx n = snd $ foldl (\(p, s) i -> (p*i, (s+(1/(p*i))))) (1, 1) [1..n]
