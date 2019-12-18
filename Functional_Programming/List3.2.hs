data Tree a = Leaf a | Node a [Tree a] deriving (Show, Read, Eq)
instance Functor Tree where
  fmap f (Leaf a) = (Leaf (f a))
  fmap f (Node a xs) = (Node (f a) (map (fmap f) xs))

foldrT :: (t -> t1 -> t) -> t -> Tree t1 -> t
foldrT f acc (Leaf x) = f acc x
foldrT f acc (Node a (x:xs)) = f (foldr (\i ac1 -> foldrT f ac1 i) (foldrT f acc x) xs) a
    
--foldrT f acc (Node a xs) = foldr (map ()  
--foldrT f acc (Node l x r) = foldrT f (f (foldrT f acc r) x) l

countT :: Tree a -> (Int, Int)
countT (Leaf a) = (0, 1)
countT (Node _ xs) = (1 + fst fl, 0 + snd fl) 
  where 
    fl = foldl (\acc a -> (fst acc + fst (countT a), snd acc + snd (countT a))) (0, 0) xs

checkT :: (Eq a) => a -> Tree a -> Bool
checkT b (Leaf a) = a == b
checkT b (Node a xs) = a == b || any (\i -> i) (map (checkT b) xs)

heigthT :: Tree a -> Int
heigthT (Leaf a) = 1
heigthT (Node _ xs) = 1 + maximum (map (heigthT) xs)



-- Testing 
test_tree = Node 2 [(Leaf 1),  (Node 4 [(Leaf 3),  (Leaf 5), Leaf(6)])]
-- fmap (+1) test_tree
-- foldrT (+) 0 test_tree
-- countT test_tree
-- checkT 2 test_tree
-- checkT 12 test_tree
-- heigthT test_tree
