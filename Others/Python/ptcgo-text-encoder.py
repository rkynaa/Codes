def ptcgo_code(file_txt):
    text_file = open(file_txt, "w")
    cont = 0
    while (cont != 110):
        question = "Enter code #%i: " % (cont + 1)
        code = str(input(question))
        code = code[:3] + '-' + code[3:7] + '-' + code[7:10] + '-' + code[10:13]
        text_file.write("%s\n" % code)
        cont += 1
    text_file.close()

ptcgo_code("output-ptcgo.txt")