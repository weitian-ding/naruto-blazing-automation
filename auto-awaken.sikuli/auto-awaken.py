scroll3_purple = "1501835086589.png"
ramen3_puerple = "1501835103461.png"
repeat = 1
i = 0


# click after time sec
def delayedClick(img, time):
    wait(img, time)
    doubleClick(img)

while i < repeat:
    delayedClick(scroll3_purple, 20)
    delayedClick("1501835155858.png", 20)
    delayedClick("1501835232185.png", 20)
    wait(15)   # wait for awaken to finish
    delayedClick("1501835277673.png", 20)
    i = i + 1







