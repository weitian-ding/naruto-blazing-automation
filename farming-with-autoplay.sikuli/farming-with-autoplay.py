while 1: 
   
    wait("1501397710908.png", 20)
    
    doubleClick("1501397710908.png")
    wait(Pattern("1501397774299.png").similar(0.80), 120)
    click("1501397774299.png")
    
    wait(Pattern("1501397974355.png").similar(0.50), 900)
    doubleClick(Pattern("1501397974355.png").similar(0.50))
    wait(Pattern("1501398033620.png").similar(0.85), 20)
    doubleClick("1501398033620.png")
    
    
    # wait for another next in LB trials  
    wait(20)
    if exists(Pattern("1501398033620.png").similar(0.85)):
        doubleClick(Pattern("1501398033620.png").similar(0.85))
    wait("1501398061521.png", 20)
    click("1501398061521.png")
    wait("1501398090920.png", 20)
    doubleClick("1501398090920.png")

    
    # refill stamina if needed
    while exists(Pattern("1501399449365.png").targetOffset(60,80)):
        doubleClick(Pattern("1501399449365.png").targetOffset(60,80))
        wait(10)
        while exists("1501649717261.png"):
      
            doubleClick(Pattern("1501649717261.png").targetOffset(-9,-1))
            wait(10)

    
    # check for level up stamina refill
    wait(10)
    if exists("1501834764766.png"):
        doubleClick("1501834780905.png")
        doubleClick("1501834963337.png")
   
    
