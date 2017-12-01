# Author: Daniel Rozen
# Project 3
# KBAI
# Agent was inspired by JWang.

# Your self for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
# PIL import Image
import random

from PIL import Image, ImageChops, ImageOps, ImageStat, ImageFilter

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your self starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().

    # . The constructor will be called at the beginning of the program, so you may
    #  use this method to initialize any information necessary before your agent begins
    #  solving problems.
    def __init__(self):
       pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your self's Solve() method will be called. At the
    # conclusion of Solve(), your self should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your self
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your self's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your self to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your self to learn from its incorrect
    # answers; however, your self cannot change the answer to a question it
    # has already answered.
    #
    # If your self calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your self's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    # If your agent wants to skip a question, it should return a negative number.
    def Solve(self, problem):

    # Helpful Functions:
    #
    #  For Project 3:

        def compLogicOperations(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                logicalThreshold, tot, xorIncr):
            print('OR PercDiff = ' + str(percentDiff(self, ImageChops.logical_or(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])))
            print('AND PercDiff = ' + str(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])))
            print('XOR PercDiff = ' + str(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])))

            if abs(percentDiff(self, ImageChops.logical_or(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.logical_or(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += orIncr
                    print('OR Incr! PercDiff = ' + str(percentDiff(self, ImageChops.logical_or(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])))

            if abs(percentDiff(self, ImageChops.logical_and(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += andIncr
                    print('AND Incr! PercDiff = ' + str(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])))

            # INVERTED XOR
            if abs(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compList1[0]], matrixImages1[compList1[1]])),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += xorIncr
                    print('XOR Incr! PercDiff = ' + str(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])))

            return tot

        def compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                logicalThreshold, tot, xorIncr):
            if abs(percentDiff(self, ImageChops.logical_or(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.logical_or(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                    tot += orIncr
                    print('OR Incr! PercDiff = ' + str(percentDiff(self, ImageChops.logical_or(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])))


            if abs(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                    tot += andIncr
                    print('AND Incr! PercDiff = ' + str(percentDiff(self, ImageChops.logical_and(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])))

            # INVERTED XOR
            if abs(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compList1[0]], matrixImages1[compList1[1]])),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += xorIncr
                    print('XOR Incr! PercDiff = ' + str(percentDiff(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])))
            return tot

        def darkPixelTotal(imgA):
            'computes the total number of pixels in an image'
            return sum(imgA.histogram()[:-1])
            # return (imgA.histogram()[0])


        # #x is an image, color is the color you don't want to count (255)
        # def darkPixelTotal(x):
        #     count = 0
        #     for i in x.getdata():
        #         if i != 255: # don't want white pixels
        #             count += 1
        #     return count

        def percentDiff(self, imgA, imgB):
            '''
            :param imgA: provided image
            :param imgB: provided image
            :return:
            Calculates the percentage difference between 2 images by 1st converting to pixel sums
            '''
            # calculate image statistics

            if type(imgA) is int or type(imgB) is int or type(imgA) is float or type(imgB) is float:
                if abs(imgB + imgA) < 0.000001:
                    print('0 value in percentDiff')
                    return 0
                else:
                    return float((imgB - imgA) / ((imgB + imgA)*.05))
            else:
                return float((darkPixelTotal(imgB) - darkPixelTotal(imgA)) / ((darkPixelTotal(imgB) + darkPixelTotal(imgA))*.5))


        # def percentDiff(self, imgA, imgB):
        #     '''
        #     :param imgA: pixel number
        #     :param imgB: pixel number
        #     :return:
        #     Calculates the percentage difference between 2 image pixel sums
        #     '''
        #     if imgB + imgA < 0.000001:
        #         return 0
        #     else:
        #         return (imgB - imgA) / ((imgB + imgA)*.05)

        def rowColAddition(imgA, imgB, imgC):
            return  darkPixelTotal(imgA) + darkPixelTotal(imgB) + darkPixelTotal(imgC)

        def deletionDiff(self, imgA, imgB):
            '''
            Calculates the deletion pixel difference between 2 images
            '''
            return darkPixelTotal(imgB) - darkPixelTotal(imgA)

        # # Define figure variables
        #
        # p1 = problem.figures['1']
        # p2 = problem.figures['2']
        # p3 = problem.figures['3']
        # p4 = problem.figures['4']
        # p5 = problem.figures['5']
        # p6 = problem.figures['6']
        #
        # a = problem.figures['A']
        # b = problem.figures['B']
        # c = problem.figures['C']

        maxTot = 0   # initiate a best answer score variable to 0
        answer = -1   # initialize best answer response to skip

               #------------2x2 problem or 3x3 C--------------
        if problem.problemType == "2x2" or (problem.problemType == "3x3" and 'Basic Problem C-' in problem.name):
            from Project2Agent import Project2Solve
            return Project2Solve(self, problem)
#-------------------------------------------------------------------------------------------------------------

#PROJECT 3 CODE BEGINS HERE
# Todo: PROJECT 3

        elif problem.problemType == "3x3":

            # transformation weights
            similarIncr = 5 # similar figure
            subtractIncr = 31 # similar change of pixels from figure to figure
            xorIncr = 15 # similar XOR transformation
            andIncr = 15 # similar AND transformation
            orIncr = 16 # similar OR transformation
            sameRowIncr = 15 # similar row/column pixel change

            # similarity thresholds
            similarThreshold = 0.1
            subtractThreshold = 0.16
            logicalThreshold = 0.02 # for logical transformation comparisons
            rowEqualSimilarThreshold = 0.04 # for row/column pixel difference comparisons
            singleRowEqualThreshold = 0.05 # for single figure pixel difference comparisons across row/columns
            diagonalRoughThreshold = .5 # diagonal difference threshold

            print("\n" + problem.name + "\n")

            # load visual representations for comparison operations
            # Store figure variables in a list

            matrixList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            answerList = ['1', '2', '3', '4', '5', '6', '7', '8']

            matrixImages = {}
            answerImages = {}
            matrixImagesL = {}
            answerImagesL = {}
            matrixImages1 = {}
            answerImages1 = {}

             # load visual representations for stats
            for key in matrixList:
                matrixImages[key] = Image.open(problem.figures[key].visualFilename)
            for key in answerList:
                answerImages[key] = Image.open(problem.figures[key].visualFilename)

            for key in matrixList:
                matrixImagesL[key] = Image.open(problem.figures[key].visualFilename).convert("1")
                print('Total Pixels for L image ' + key + ' = ' + str(darkPixelTotal(matrixImagesL[key])))
                # print(matrixImagesL[key].histogram())
            for key in answerList:
                answerImagesL[key] = Image.open(problem.figures[key].visualFilename).convert("1")
                print('Total Pixels for L image ' + key + ' = ' + str(darkPixelTotal(answerImagesL[key])))
                # print(answerImagesL[key].histogram())

            # load visual representations for logical operations
            for key in matrixList:
                matrixImages1[key] = Image.open(problem.figures[key].visualFilename).convert("1")
            for key in answerList:
                answerImages1[key] = Image.open(problem.figures[key].visualFilename).convert("1")

                 # # Define figure variables
            a = matrixImages1['A']
            b = matrixImages1['B']
            c = matrixImages1['C']
            d = matrixImages1['D']
            e = matrixImages1['E']
            f = matrixImages1['F']
            g = matrixImages1['G']
            h = matrixImages1['H']

            # Todo: Extend to vertical and diagonal comparisons

            # Calculate Column and Row differences without answers

            col1TotPixels = rowColAddition(matrixImagesL['A'],matrixImagesL['D'],matrixImagesL['G'])
            col2TotPixels = rowColAddition(matrixImagesL['B'],matrixImagesL['E'],matrixImagesL['H'])
            row1TotPixels = rowColAddition(matrixImagesL['A'],matrixImagesL['B'],matrixImagesL['C'])
            row2TotPixels = rowColAddition(matrixImagesL['D'],matrixImagesL['E'],matrixImagesL['F'])

            col21diff = col2TotPixels - col1TotPixels
            row21diff = row2TotPixels - row1TotPixels

            # Individual row column transformations
            colExactCheck = False
            rowExactCheck = False
            colCheck = False
            rowCheck = False

            if (darkPixelTotal(c) - darkPixelTotal(b)) == (darkPixelTotal(f) - darkPixelTotal(e)):
                colExactCheck = True
                print('colExactCheck True!')
            if (darkPixelTotal(g) - darkPixelTotal(d)) == (darkPixelTotal(h) - darkPixelTotal(e)):
                rowExactCheck = True
                print('rowExactCheck True!')

            print('single col check  = ')
            print(percentDiff(self, (darkPixelTotal(c) - darkPixelTotal(b)),(darkPixelTotal(f) - darkPixelTotal(e))))
            if abs(percentDiff(self, (darkPixelTotal(c) - darkPixelTotal(b)),(darkPixelTotal(f) - darkPixelTotal(e)))) < singleRowEqualThreshold:
                colCheck = True
                print('col Check True!')

            print('single row check  = ')
            print(str(percentDiff(self, (darkPixelTotal(g) - darkPixelTotal(d)),(darkPixelTotal(h) - darkPixelTotal(e)))))
            if abs(percentDiff(self, (darkPixelTotal(g) - darkPixelTotal(d)),(darkPixelTotal(h) - darkPixelTotal(e)))) < singleRowEqualThreshold:
                rowCheck = True
                print('row Check True!')

            # calculate transformations with the answers

            for ans in answerList:
                tot = 0
                print('\n  Now comparing answer: ' + str(ans) + ' to ' + problem.name + ':\n')

                ansImage = answerImages1[ans]

                # comparing similarity

                if 'Basic Problem D-' in problem.name:

                    # comparing diagonal similarity - Only for D
                    percdiff = percentDiff(self, matrixImages1['A'], matrixImages1['E'])

                    if abs(percdiff) < similarThreshold:
                        percdiff = percentDiff(self, matrixImages1['A'], answerImages1[ans])
                        if abs(percdiff) < similarThreshold:
                            tot += similarIncr
                            print('A similar to Ans. PercentDiff = ' + str(percdiff))

                        percdiff = percentDiff(self, matrixImages1['E'], answerImages1[ans])
                        if abs(percdiff) < similarThreshold:
                            tot += similarIncr
                            print('E similar to Ans PercentDiff = ' + str(percdiff))


                # DEBUGGING
                # if problem.name == 'Basic Problem D-07':
                #
                #     # Diagonal similar deletion comparisons eg. for D-07
                #
                #     additionDiffPic = ImageChops.add(matrixImagesL['A'], matrixImagesL['E'])
                #
                #     additionDiff = percentDiff(self, additionDiffPic, answerImagesL[ans])
                #     if abs(additionDiff) < similarThreshold:
                #         tot += similarIncr
                #
                #     if ans == '1':
                #
                #         im1 = matrixImages1['A']
                #         im2 = matrixImages1['E']
                #         pasteImage = im1.paste(im2)
                #         print(pasteImage)
                #         additionDiffPic.show()

                # LOGICAL COMPARISONS:
                # Do only for E problems
                if 'Basic Problem E-' in problem.name:

                    # Horizontal Comparisons
                    compList1 = ['A', 'B', 'C']
                    compListAns = ['G', 'H']

                    tot = compLogicOperations(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                                   logicalThreshold, tot, xorIncr)

                    compList1 = ['B', 'C', 'A']
                    compListAns = ['G', 'H']

                    tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                                   logicalThreshold, tot, xorIncr)

                    compList1 = ['A', 'C', 'B']
                    compListAns = ['H', 'G']

                    tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                                   logicalThreshold, tot, xorIncr)

                       # Debugging
                    # if problem.name == 'Basic Problem E-08':
                        # if ans == '1' or ans == '2':
                        #     matrixImages1[compListAns[0]].show()
                        #     matrixImages1[compListAns[1]].show()
                        #     ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])).show()
                        #     answerImages1[ans].show()

                    # Vertical Comparisons
                    compList1 = ['A', 'D', 'G']
                    compListAns = ['C', 'F']

                    tot = compLogicOperations(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                                   logicalThreshold, tot, xorIncr)

                    # compList1 = ['D', 'G', 'A']
                    # compListAns = ['F', 'C']
                    #
                    # tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                    #                                logicalThreshold, tot, xorIncr)
                    #
                    # compList1 = ['A', 'G', 'D']
                    # compListAns = ['C', 'F']
                    #
                    # tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                    #                                logicalThreshold, tot, xorIncr)

                    # Diagonal Comparisons
                    # compList1 = ['C', 'E', 'G']
                    # compListAns = ['A', 'E']
                    #
                    # tot = compLogicOperations(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                    #                                logicalThreshold, tot, xorIncr)


                    # Subtraction difference for E-04 and E-12
                    # answerImageSum = ImageStat.Stat(answerImagesL[ans])._getsum()
                    answerImageSum = darkPixelTotal(answerImagesL[ans])

                    #print('deletionDiff HG = ' + str(abs(deletionDiff(self, matrixImagesL['H'], matrixImagesL['G']))))
                    print('Subtraction Difference GHI: '+ str(percentDiff(self, abs(deletionDiff(self, matrixImagesL['H'], matrixImagesL['G'])), answerImageSum)))
                    if abs(percentDiff(self, abs(deletionDiff(self, matrixImagesL['H'], matrixImagesL['G'])), answerImageSum)) < subtractThreshold:
                        print('CORRECT Subtraction Difference GHI!!')
                        tot += subtractIncr

                # Do only for  problems
                if 'Basic Problem D-' in problem.name:

                    # Subtraction difference for problems like D-06


                    print('diagonal difference similarity of: ' + str(percentDiff(self, (deletionDiff(self, matrixImagesL['A'],matrixImagesL['E'])), (deletionDiff(self, matrixImagesL['E'],answerImagesL[ans])))))

                    if abs(percentDiff(self, (deletionDiff(self, matrixImagesL['A'],matrixImagesL['E'])), (deletionDiff(self, matrixImagesL['E'],answerImagesL[ans])))) <  diagonalRoughThreshold:

                        tot += subtractIncr
                    # Calclculate INDIVIDIDUAL Column and Row differences with answers

                    if colExactCheck == True:
                        if (darkPixelTotal(ansImage) - darkPixelTotal(h)) == (darkPixelTotal(f) - darkPixelTotal(e)):
                            tot += sameRowIncr * 5
                            print('SAME EXACT Individual col increase!')
                    if rowExactCheck == True:
                        if (darkPixelTotal(ansImage) - darkPixelTotal(f)) == (darkPixelTotal(h) - darkPixelTotal(e)):
                            tot += sameRowIncr * 5
                            print('SAME EXACT Individual row increase!')
                    if colCheck == True:
                        if abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(h)),(darkPixelTotal(f) - darkPixelTotal(e)))) < singleRowEqualThreshold and abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(h)),(darkPixelTotal(f) - darkPixelTotal(e)))) != 0:
                        # if abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(h)),(darkPixelTotal(f) - darkPixelTotal(e)))) < singleRowEqualThreshold:
                            tot += sameRowIncr
                            print('SAME Individual col increase!! percentDiff = ' + str(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(h)),(darkPixelTotal(f) - darkPixelTotal(e)))))

                    if rowCheck == True:
                         if abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(f)),(darkPixelTotal(h) - darkPixelTotal(e)))) < singleRowEqualThreshold and abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(f)),(darkPixelTotal(h) - darkPixelTotal(e)))) != 0:
                        # if abs(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(f)),(darkPixelTotal(h) - darkPixelTotal(e)))) < singleRowEqualThreshold:
                            tot += sameRowIncr
                            print('SAME Individual row increase!! percentDiff = '+ str(percentDiff(self, (darkPixelTotal(ansImage) - darkPixelTotal(f)),(darkPixelTotal(h) - darkPixelTotal(e)))))

                    # Row differences only for D
                    # Calculate TOTAL Column and Row differences with answers

                    col3TotPixels = rowColAddition(matrixImages1['C'],matrixImages1['F'],answerImages1[ans])
                    row3TotPixels = rowColAddition(matrixImages1['G'],matrixImages1['H'],answerImages1[ans])
                    col32diff = col3TotPixels - col2TotPixels
                    row32diff = row3TotPixels - row2TotPixels

                    if col32diff == col21diff:
                        tot += sameRowIncr*5
                        print('Same EXACT col Diff!')

                    if row32diff == row21diff:
                        tot += sameRowIncr*5
                        print('Same EXACT row Diff!')

                     # Row comparisons only for D Problems
                    # if 'Basic Problem D-' in problem.name:
                    if abs(percentDiff(self, col32diff, col21diff)) < rowEqualSimilarThreshold and abs(percentDiff(self, col32diff, col21diff)) != 0:
                    # if abs(percentDiff(self, col32diff, col21diff)) < rowEqualSimilarThreshold :
                    #     tot += sameRowIncr
                        print('Same col Diff! percent diff : ')
                        print(percentDiff(self, col32diff, col21diff))

                    if abs(percentDiff(self, row32diff, row21diff)) < rowEqualSimilarThreshold and abs(percentDiff(self, row32diff, row21diff)) != 0:
                    # if abs(percentDiff(self, row32diff, row21diff)) < rowEqualSimilarThreshold:
                        tot += sameRowIncr
                        print('Same row Diff! percent diff : ' + str(percentDiff(self, row32diff, row21diff)))

                # Final return
                if tot > maxTot and tot != 0:
                    # max answer = local answer
                    print("previous maxTot = " + str(maxTot))
                    maxTot = tot
                    print("new maxTot = " + str(maxTot))

                    print("previous answer = " + str(answer))
                    answer = ans
                    print("new answer = " + str(answer))
                elif tot == maxTot and tot != 0: #random tie breaker
                    randint = random.randint(0,1)
                    if randint == 1:
                        maxTot = tot
                        print("TIED new maxTot = " + str(maxTot))
                        # answer = current answer
                        print("TIED previous answer = " + str(answer))
                        answer = ans
                        print("TIED new answer = " + str(answer))

            return answer