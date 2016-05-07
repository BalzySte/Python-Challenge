from string import ascii_lowercase

crypt_string = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq"
                " ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw"
                " rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkcl"
                "bcb. lmu ynnjw ml rfc spj.") 

intable = ascii_lowercase
outtable = ascii_lowercase[2:] + ascii_lowercase[ : 2]

print(crypt_string.translate(str.maketrans(intable, outtable)))

# Challenge suggests to translate the url
print("Translating the URL:")
in_string = "map.html"
print(in_string.translate(str.maketrans(intable,outtable)))

# next challenge is at .../ocr.html
