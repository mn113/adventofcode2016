module Main where

-- constants:
--pyscs = [16,2,0,3,1,12,10]
discs = [2,2,5,4,5,11]
sizes = [17,7,19,5,3,13]
limit = 3*5*7*13*17*19  -- Entire disc system will repeat after this many steps
times = [14,33..limit]         -- The disc with 19 positions will only be 0 every 19 steps
goal = take 6 (repeat 0)  -- [0,0,0,0,0,0,0]

-- Recursive loop function:
incrementDiscs :: [Int] -> [Int] -> [Char]  -- put in two lists of integers, get out a string
incrementDiscs times discs
    -- test end conditions:
    | times == []    = "Out of times."
    | t > limit      = "Limit passed. " ++ show t ++ " seconds elapsed."
    | discs == goal  = "All zeros! " ++ show t ++ " seconds elapsed."
    -- call recursively, with chopped t and incremented, modulo'd discs:
    | otherwise      = incrementDiscs (tail times) [(d + t) `mod` m | d <- discs, m <- sizes]
  where t = head times

main = do
    putStrLn $ "limit " ++ show limit
    putStrLn $ "last time " ++ show (last times)
    putStrLn $ incrementDiscs times discs
    -- subtract 1 from given time to get button-pressing time
