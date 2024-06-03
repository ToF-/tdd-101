
Alice, Bertrand, Clara and Desmond often make group purchases. They keep the list of their purchases in a csv file like this one:

    orders.csv

    item              , unitp  , qty , amount , buyer
    pencils           ,   0.50 ,  20 ,  10.00 , Bertrand
    paper             ,   1.50 ,  25 ,  37.50 , Alice
    paper             ,   1.80 ,  50 ,  90.00 , Desmond
    laundry detergent ,   2.00 ,  10 ,  20.00 , Clara
    trash bags        ,   4.30 , 100 , 430.00 , Clara
    gift cards        ,   8.00 ,   1 ,   8.00 , Bertrand
    lightbulbs        ,   1.00 ,  10 ,  10.00 , Clara
    ~ shipping        ,  40.00 ,   1 ,  40.00 , ~ shipping
    ~ total           , 645.50 ,   1 , 645.50 , ~ total

Lines starting with a `~` aren't part of the buyers purchased items but instead indicate the shipping fee and the grad total.

The shipping fee is not split into equal parts between buyers; rather it is attributed to each member in proportion to their purchase amount. In the example above, the total without shipping is 605.50. Clara's purchases amount to 460.00, so her part of the shipping fee is 460.00 / 605.50 * 40.0 = 30.38, making her total part of the bill 460.00 + 30.38 = 490.38.

