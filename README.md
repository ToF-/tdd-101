
# TDD 101

## Problem #1

An account number is a nine digits string. It is said to be valid if its checksum is a multiple of 11. The checksum is calculated as follows:


    (D1×9 + D2×8 + D3×7 + D4×6 + D5×5 + D6×4 + D7×3 + D8 × 2 + D9)

Here are examples of valid account numbers:

    000000000 // 0 mod 11 = 0
    130000000 // 1×9 + 3×8 = 33, 33 mod 11 = 0
    000000051 // 5×2 + 1×1 = 11, 11 mod 11 = 0
    123456789
    490867715
    999999990

Write a program that given an input file containing account numbers, outputs the same file with _invalid_ account numbers marked with a `*`.

### Input example

    902542346
    505687420
    761694102
    034384618
    550081068
    188630350
    941325075
    362359628
    469431482
    992449121
    435736663
    267603738
    909215197
    176150170
    545527430
    063240745
    742228185
    197586201
    568361326
    531799301
    171943058
    187969213
    393347786
    425903206
    989552321

### Output example

    902542346
    505687420*
    761694102
    034384618
    550081068*
    188630350*
    941325075
    362359628
    469431482
    992449121*
    435736663
    267603738
    909215197
    176150170*
    545527430
    063240745*
    742228185
    197586201
    568361326
    531799301
    171943058
    187969213
    393347786*
    425903206
    989552321*
