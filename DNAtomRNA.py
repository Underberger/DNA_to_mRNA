import pyperclip # needed module to copy mRNA sequence to clipboard
# User input DNA sequence
try:
    DNA_sequence = input("Please enter the DNA sequence below: \n")
except:
    print("Invalid, please enter a valid DNA sequence.")
# DNA sequence to uppercases
DNA = DNA_sequence.upper()
# check nucleotides for thymine (-> uracil)
mRNA = ""
for nuc in DNA:
    if nuc == "T":
        mRNA = mRNA + "U" # replace T with U
    else:
        mRNA = mRNA + nuc # do nothing

print("Success! mRNA sequence copied to clipboard and shown below:\n" + mRNA) # give back the mRNA sequence
pyperclip.copy(mRNA) # copy mRNA sequence to the clipboard