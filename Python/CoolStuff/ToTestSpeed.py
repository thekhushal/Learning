import speedtest

test = speedtest.speedtest()

downSpeed = test.download()
upSpeed = test.upload()

print("downSpeed", downSpeed)
print("upSpeed", upSpeed)