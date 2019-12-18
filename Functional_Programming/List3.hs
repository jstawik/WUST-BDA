data Tree a = Leaf a | Node (Tree a) a (Tree a) deriving (Show, Read, Eq)

foldrT f acc (Leaf x) = f acc x
foldrT f acc (Node l x r) = foldrT f (f (foldrT f acc r) x) l

countT :: Tree a -> (Int, Int)
countT (Leaf a) = (0, 1)
countT (Node l _ r) = (1 + fst cl + fst cr, 0 + snd cl + snd cr) 
  where 
    cl = countT l 
    cr = countT r

checkT :: (Eq a) => Tree a -> a -> Bool
checkT (Leaf a) b = a == b
checkT (Node l x r) b = x == b || (checkT l b) || (checkT r b)

heigthT :: Tree a -> Int
heigthT (Leaf a) = 1
heigthT (Node l _ r) = maximum([(heigthT l + 1), (heigthT r + 1)])



-- Testing 
test_tree = Node (Leaf 1) 2 (Node (Leaf 3) 4 (Leaf 5))
-- foldrT (+) 0 test_tree 
-- foldrT countT (0,0) test_tree
-- checkT test_tree 3
-- checkT test_tree 6
-- heigthT test_tree
