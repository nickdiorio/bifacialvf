import os

def write_header(sunUpIndex, index, timeStepsPerYear, dataArray, fileName, headerGuard, variableName, roundData):

    roundedData = dataArray
    if roundData:
        roundedData = ['%.4f' % elem for elem in dataArray]

    if sunUpIndex == 0 and os.path.exists(fileName):
        os.remove(fileName)

    with open(fileName, 'a+') as writefile:
        if sunUpIndex == 0:
            writefile.write('#ifndef ' + headerGuard + ' \n')
            writefile.write('#define ' + headerGuard + ' \n')
            writefile.write('#include <vector>\n')
            writefile.write('static std::vector<std::vector<double>> ' + variableName + ' = {\n')

            lst = map(str, roundedData)
            line = "{" + ",".join(lst) + "},\n"
            writefile.write(line)
        # automatically cut out at 8 hours before the end of the year
        elif index == timeStepsPerYear - 8:
            writefile.write('};\n')
            writefile.write('#endif\n')
        else:
            lst = map(str, roundedData)
            line = "{" + ",".join(lst) + "},\n"
            writefile.write(line)

def write_text_file(sunUpIndex, index, timeStepsPerYear, dataArray, fileName, roundData):

    roundedData = dataArray
    if roundData:
        roundedData = ['%.4f' % elem for elem in dataArray]

    if sunUpIndex == 0 and os.path.exists(fileName):
        os.remove(fileName)

    with open(fileName, 'a+') as writefile:

        if sunUpIndex >= 0 and index <= timeStepsPerYear - 8:

            lst = map(str, roundedData)
            line = " ".join(lst) + "\n"
            writefile.write(line)

