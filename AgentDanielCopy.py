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
            if abs(percentDiffPictures(self, ImageChops.logical_or(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.logical_or(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += orIncr
            if abs(percentDiffPictures(self, ImageChops.logical_and(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.logical_and(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]]),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += andIncr

            # INVERTED XOR
            if abs(percentDiffPictures(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compList1[0]], matrixImages1[compList1[1]])),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += xorIncr

            return tot

        def compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                logicalThreshold, tot, xorIncr):
            if abs(percentDiffPictures(self, ImageChops.logical_or(matrixImages1[compList1[0]], matrixImages1[compList1[1]]),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.logical_or(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                    tot += orIncr
            if abs(percentDiffPictures(self, ImageChops.logical_and(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.logical_and(matrixImages1[compListAns[0]], answerImages1[ans]), matrixImages1[compListAns[1]])) < logicalThreshold:
                    tot += andIncr

            # INVERTED XOR
            if abs(percentDiffPictures(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compList1[0]], matrixImages1[compList1[1]])),
                                    matrixImages1[compList1[2]])) < logicalThreshold:
                if abs(percentDiffPictures(self, ImageChops.invert(ImageChops.logical_xor(matrixImages1[compListAns[0]], matrixImages1[compListAns[1]])),
                                        answerImages1[ans])) < logicalThreshold:
                    tot += xorIncr

            return tot

        def darkPixelTotal(imgA):
            'computes the total number of pixels in an image'
            #totalPixelsNum = 0
            # imgALoad = imgA.load()
            # for i in range(imgA.size[0]):
            #     for j in range(imgA.size[1]):
            #         if imgALoad[i, j] == 0:
            #             totalPixelsNum += 1
            # return totalPixelsNum
            return sum(imgA.histogram()[:-1])


        def percentDiffPictures(self, imgA, imgB):
            '''
            :param imgA: provided image
            :param imgB: provided image
            :return:
            Calculates the percentage difference between 2 images by 1st converting to pixel sums
            '''
            # calculate image statistics

            return (darkPixelTotal(imgB) - darkPixelTotal(imgB)) / ((darkPixelTotal(imgB) + darkPixelTotal(imgB))*.5)


        def percentDiff(self, imgA, imgB):
            '''
            :param imgA: pixel number
            :param imgB: pixel number
            :return:
            Calculates the percentage difference between 2 image pixel sums
            '''
            if imgB + imgA < 0.000001:
                return 0
            else:
                return (imgB - imgA) / ((imgB + imgA)*.05)

        def rowColAddition(imgA, imgB, imgC):
            return darkPixelTotal(imgB) + darkPixelTotal(imgA) + darkPixelTotal(imgC)

        def deletionDiff(self, imgA, imgB):
            '''
            Calculates the deletion pixel difference between 2 images
            '''
            # calculate image statistics

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

            similarIncr = 1
            deleteIncr = 10
            xorIncr = 10
            andIncr = 10
            orIncr = 15
            similarThreshold = 0.06
            logicalThreshold = 0.04

            print("\n" + problem.name + "\n")

            # Store figure variables in a list

            matrixList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            answerList = ['1', '2', '3', '4', '5', '6', '7', '8']

            matrixImages = {}
            answerImages = {}
            matrixImages1 = {}
            answerImages1 = {}

            # load visual representations for comparison operations
            for key in matrixList:
                matrixImages[key] = Image.open(problem.figures[key].visualFilename).convert("L")
            for key in answerList:
                answerImages[key] = Image.open(problem.figures[key].visualFilename).convert("L")
            # load visual representations for logical operations
            for key in matrixList:
                matrixImages1[key] = Image.open(problem.figures[key].visualFilename).convert("1")
            for key in answerList:
                answerImages1[key] = Image.open(problem.figures[key].visualFilename).convert("1")
            # for key in matrixList:
            #     matrixImages1[key] = Image.open(problem.figures[key].visualFilename)
            # for key in answerList:
            #     answerImages1[key] = Image.open(problem.figures[key].visualFilename)

            # Todo: Extend to vertical and diagonal comparisons

            # Calculate Column and Row differences without answers

            col1TotPixels = rowColAddition(matrixImages['A'],matrixImages['D'],matrixImages['G'])
            col2TotPixels = rowColAddition(matrixImages['B'],matrixImages['E'],matrixImages['H'])
            row1TotPixels = rowColAddition(matrixImages['A'],matrixImages['B'],matrixImages['C'])
            row2TotPixels = rowColAddition(matrixImages['D'],matrixImages['E'],matrixImages['F'])

            col21diff = col2TotPixels - col1TotPixels
            row21diff = row2TotPixels - row1TotPixels

            col3TotPixelsDict = {}
            row3TotPixelsDict = {}
            col32diffDict = {}
            row32diffDict = {}

            # calculate transformations with the answers

            for ans in answerList:
                tot = 0
                print('\n  Now comparing answer: ' + str(ans) + ' to ' + problem.name + ':\n')

                # comparing similarity

                percdiff = percentDiffPictures(self, matrixImages['A'], answerImages[ans])
                #Debug
                # percdiffXOR = percentDiffPictures(self, ImageChops.logical_or(matrixImages1['G'], matrixImages1['H']), answerImages1[ans])
                # print('Percentage diff XOR GHI for ans: ' + str(ans) + ' = ' + str(percdiffXOR))

                if abs(percdiff) < similarThreshold:
                    tot += similarIncr

                percdiff = percentDiffPictures(self, matrixImages['E'], answerImages[ans])
                if abs(percdiff) < similarThreshold:
                    tot += similarIncr

                if problem.name == 'Basic Problem D-07':

                    # Diagonal similar deletion comparisons eg. for D-07

                    additionDiffPic = ImageChops.add(matrixImages['A'], matrixImages['E'])

                    additionDiff = percentDiffPictures(self, additionDiffPic, answerImages[ans])
                    if abs(additionDiff) < similarThreshold:
                        tot += similarIncr

                    if ans == '1':

                        im1 = matrixImages1['A']
                        im2 = matrixImages1['E']
                        pasteImage = im1.paste(im2)
                        print(pasteImage)
                        additionDiffPic.show()

                # LOGICAL COMPARISONS:

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

                compList1 = ['D', 'G', 'A']
                compListAns = ['F', 'C']

                tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                               logicalThreshold, tot, xorIncr)

                compList1 = ['A', 'G', 'D']
                compListAns = ['C', 'F']

                tot = compLogicOperationsAns2nd(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                                               logicalThreshold, tot, xorIncr)

                # Diagonal Comparisons
                # compList1 = ['C', 'E', 'G']
                # compListAns = ['A', 'E']
                #
                # tot = compLogicOperations(self, andIncr, ans, answerImages, compList1, compListAns, matrixImages, orIncr,
                #                                logicalThreshold, tot, xorIncr)


                # Deletion difference for E-04 and E-12
                # answerImageSum = ImageStat.Stat(answerImages[ans])._getsum()
                answerImageSum = darkPixelTotal(answerImages[ans])
                print('answerImageSum for:' + str(ans) + ' = ' + str(answerImageSum))


                print ('deletionDiff HG = ' + str(abs(deletionDiff(self, matrixImages['H'], matrixImages['G']))))
                if abs(percentDiff(self, abs(deletionDiff(self, matrixImages['H'], matrixImages['G'])), answerImageSum)) < similarThreshold:
                    print('CORRECT Deletion Difference GHI!!')
                    tot += deleteIncr

                # Deletion difference for D-06

                if abs(percentDiff(self, (deletionDiff(self, matrixImages1['A'],matrixImages1['E'])), (deletionDiff(self, matrixImages1['E'],answerImages[ans])))) < similarThreshold:
                    tot += deleteIncr

                # Calculate Column and Row differences with answers
                
                col3TotPixels = rowColAddition(matrixImages['C'],matrixImages['F'],answerImages[ans])
                row3TotPixels = rowColAddition(matrixImages['B'],matrixImages['E'],matrixImages['H'])
                col32diff = col3TotPixels - col2TotPixels
                row32diff = row3TotPixels - row2TotPixels

                # Final return
                if tot > maxTot:
                    maxTot = tot
                    answer = ans

            return answer