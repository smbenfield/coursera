text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find("0")
numnum = float(text[numpos+1:numpos+6])
print numnum