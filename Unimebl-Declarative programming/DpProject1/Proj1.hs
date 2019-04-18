--  File     : proj1.hs
--  Author   : Junxu ZHANG <junxuz@student.unimelb.edu.au>
--  Origin   : Mon April 09 21:06:04 2019 (modified)
--  Purpose  : proj1 project assignment, to implement the following
--             fuctions, including "toPitch", "feedback", "initialGuess" and -
--             "nextGuess".

{-  The purpose of this programm is trying to use a minimum of steps to
    get the correct three pitches. Initially, the programm will previously 
    set up an initial guess. When a user input a target and run the programm,
    the programm will continously output a feedback of the guess result and 
    the number of guesses. The programm end up with getting the correct guess
    (target)and output the number of guesses. While the feedback contains 
    three parts, the first factor is the number of correct pitches, the second
    is the correct number of notes in remain pitches and the third elements 
    store the the number of remainning correct octaves.
-}
module Proj1 (Pitch, toPitch, feedback,
GameState, initialGuess, nextGuess) where
import Data.List
import qualified Data.Map as M
-- Defining such type can limit its scope.
-- Ord type is using to filter all posiible pitches to
-- GameState.
data Note =  A | B | C | D | E | F | G
             deriving (Show, Eq, Ord)
data Octave =  One | Two | Three
              deriving (Eq,Ord)
-- use one two three to limits the number of Octave
-- and also because 1,2,3 are integer, which cannot be constructors
instance Show Octave where
     show One = "1"
     show Two = "2"
     show Three = "3"

data Pitch = Pitch Note Octave
     deriving (Eq, Ord)

--Use instance to  enumerate all possible type of Pitches
instance Show Pitch where
    show (Pitch A One)   = "A1"
    show (Pitch A Two)   = "A2"
    show (Pitch A Three) = "A3"
    show (Pitch B One)   = "B1"
    show (Pitch B Two)   = "B2"
    show (Pitch B Three) = "B3"
    show (Pitch C One)   = "C1"
    show (Pitch C Two)   = "C2"
    show (Pitch C Three) = "C3"
    show (Pitch D One)   = "D1"
    show (Pitch D Two)   = "D2"
    show (Pitch D Three) = "D3"
    show (Pitch E One)   = "E1"
    show (Pitch E Two)   = "E2"
    show (Pitch E Three) = "E3"
    show (Pitch F One)   = "F1"
    show (Pitch F Two)   = "F2"
    show (Pitch F Three) = "F3"
    show (Pitch G One)   = "G1"
    show (Pitch G Two)   = "G2"
    show (Pitch G Three) = "G3"

-- As GameState will store all posiible pitches, GameState is just
-- a list of list of pitches.
type GameState = [[Pitch]]

-- According to the input, return the whether the input belongs to pitches
-- types. If the input is legal, return a "Just" type of corresponding 
-- pitches, otherwise return "Nothing".
toPitch :: String -> Maybe Pitch 
toPitch [] = error"Empty"
toPitch s
       |s == "A1" = Just $Pitch A One
       |s == "A2" = Just $Pitch A Two
       |s == "A3" = Just $Pitch A Three
       |s == "B1" = Just $Pitch B One
       |s == "B2" = Just $Pitch B Two
       |s == "B3" = Just $Pitch B Three
       |s == "C1" = Just $Pitch C One
       |s == "C2" = Just $Pitch C Two
       |s == "C3" = Just $Pitch C Three
       |s == "D1" = Just $Pitch D One
       |s == "D2" = Just $Pitch D Two
       |s == "D3" = Just $Pitch D Three
       |s == "E1" = Just $Pitch E One
       |s == "E2" = Just $Pitch E Two
       |s == "E3" = Just $Pitch E Three
       |s == "F1" = Just $Pitch F One
       |s == "F2" = Just $Pitch F Two
       |s == "F3" = Just $Pitch F Three
       |s == "G1" = Just $Pitch G One
       |s == "G2" = Just $Pitch G Two
       |s == "G3" = Just $Pitch G Three
       |otherwise = Nothing

-- Take Note and Octave from Pitch data type out, and then calculate their
-- numbers respectively
convertNote :: Pitch -> Note
convertNote (Pitch a b) = a
convertOctave :: Pitch -> Octave
convertOctave (Pitch a b) = b

-- This is used to remove common elements e.g. Picth
-- cause same number of Pitch will affect results.
-- removeCommon is a function from the third part called Sound.Tidal.Utils, i
-- found it in Hoogle as this package needs to be downloaded,
-- so i use its orginal fuction
removeCommon :: Eq a => [a] -> [a] -> ([a],[a])
removeCommon [] bs = ([],bs)
removeCommon as [] = (as,[])
removeCommon (a:as) bs | a `elem` bs = removeCommon as (delete a bs)
                       | otherwise = (a:as',bs')
                      where (as',bs') = removeCommon as bs

-- Use list comprehension to identify each data
-- nub is used to remove duplicate Note or Ocatve
-- e.g. target: A1 B1 C1 guess:E1 F1 G1, it should return (0,0,1) rather 
-- than (0,0,3), while dollar sign represents  parentheses to the end.
numPitch :: [Pitch] -> [Pitch] -> Int
numPitch a b = length $ filter (`elem`b) a

-- As removeCommon return the tuple type of results, so "fst" and "snd" are
-- needed to use to extract value.
numNote :: [Pitch] -> [Pitch] -> Int
numNote  a b = length $ Prelude.filter (`elem`(nub y)) $nub x
        where
           x  = [convertNote m | m <- fst $removeCommon a b]
           y  = [convertNote n | n <- snd $removeCommon a b]

-- To count the number of Octave is different with above two(Pitch an Note)
-- Operation "x\\y" will remove the elements in x wihch also contained in y
numOctave :: [Pitch] -> [Pitch] -> Int
numOctave  a b = length x - length(x\\y)
        where
           x  = [convertOctave m | m <- fst $ removeCommon a b]
           y  = [convertOctave n | n <- snd $ removeCommon a b]

-- After calculating the Pitch, Note and Octave, it only needs to put them
-- into feedback fuction
feedback :: [Pitch] -> [Pitch] -> (Int, Int, Int)
feedback  a b =  (numPitch a b, numNote a b, numOctave a b)

-- To combine a Note and an Ocatve to make up with a Pitch type,
-- which facilitate to filter all posiible pitches in the next fuction.
combine :: Note -> Octave -> Pitch
combine note octave = Pitch note octave

-- Use combine function to combine all pitches
combine_list ::[Pitch] 
combine_list = [combine n o | n <- [A,B,C,D,E,F,G], o <- [One,Two,Three]]

-- To filter all posiible guesses easily, use Ord to define data types;
-- therefore, pitches A1 is the smallest and G3 is the biggest.
allguesses :: [[Pitch]]
allguesses = [[a,b,c]|a <- combine_list,
                            b <-combine_list, c <- combine_list, a< b && b<c]

-- Set an initialguess and put possible pitches in gamestate in order to remove
-- pitches in foollowing steps
initialGuess :: ([Pitch], GameState)
initialGuess = ([Pitch A One, Pitch B One, Pitch C Two], allguesses)

--According to the previous guess, precdict the possible nextguess  
-- This method is foollowing "Hint 3" `s instruction. According to the feedback
-- of the initial guess, continously filter pitches stored in GameState, and
-- the last element in GameState is the target.
-- new_remain stores the filtered pitches and use its the first element as
-- the next initialguess. 
nextGuess :: ([Pitch], GameState) -> (Int, Int, Int) -> ([Pitch], GameState)
nextGuess (guess, remain) (a, b, c) = (head new_remain, new_remain)
   where 
          new_remain = [cand|cand <- remain,(a,b,c) == feedback guess cand]