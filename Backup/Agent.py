# Author: Daniel Rozen
# Project 2
# KBAI

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

        # Define figure variables

        p1 = problem.figures['1']
        p2 = problem.figures['2']
        p3 = problem.figures['3']
        p4 = problem.figures['4']
        p5 = problem.figures['5']
        p6 = problem.figures['6']

        a = problem.figures['A']
        b = problem.figures['B']
        c = problem.figures['C']

        maxTot = 0   # initiate a best answer score variable to 0
        answer = -1   # initialize best answer response to skip

        # Define increment variables (Adjustable)
        sameIncr = 1  # same general property increment value
        angleIncr = 20   # same angle rotation transform increment value
        reflectIncr = 15  # same reflection transform increment value
        fillIncr = 40  # increment for correct fill transformation
        shapeIncr = 100 # increment for correct shape transformation
        deleteIncr = 200 # increment for correct deletion of objects
        deleteCompIncr = 20 # increment for compensation for deleted/added objects having less matches
        alignIncr = 35 # increment for correct alignment transformation
        sizeIncr = 50

        # Setup matching objects dictionary:
        matchObjsDict = {} # dictionary to match objects
        # attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of']
        attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
        incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

        # Comparison Flags:


        if problem.name == 'Basic Problem B-02':
            print('Set Breakpoint here!')

        if problem.problemType == "2x2":
            #  loop through all objects and add to dictionary

            matchObjsDict = Agent.matchObjects(self, a, b, matchObjsDict, attributeList, incrList)
            matchObjsDict = Agent.matchObjects(self, a, c, matchObjsDict, attributeList, incrList)
            for x in range(1,7):
                ans = problem.figures[str(x)]
                matchObjsDict = Agent.matchObjects(self, b, ans, matchObjsDict, attributeList, incrList)
                matchObjsDict = Agent.matchObjects(self, c, ans, matchObjsDict, attributeList, incrList)

            print("\n" + problem.name + "\n")

            print('\nOBJECT MATCHING DICTIONARY!')
            for keys in sorted(matchObjsDict):
                print(str(keys) + ": " + str(matchObjsDict[keys]))

        # compare shapes and attributes across figures A,B,C:

            for x in range(1, 7):     # loop through each potential answer from 1 to 6:

                print('\n  Now comparing answer: ' + str(x) + ' to ' + problem.name + ':\n')

                tot = 0   # initialize total points system

                transformDict = {}  # create dictionary for transformations

                Agent.initialize_dicts(self, transformDict) # initialize empty keys in transformation dicts

                # compare deletion from AB to CD
                tot = Agent.abcd_delete_comp(self, a, b, c, 'ab', 'cd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

                # compare deletion from AC to BD

                tot = Agent.abcd_delete_comp(self, a, c, b,  'ac', 'bd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

                # compare A to B

                Agent.compareAtoObj(self, a, b, 'ab', 'cd', transformDict, matchObjsDict)

                # compare C to D

                tot = Agent.compareObjtoAns(self, c, problem, x, 'ab', 'cd', alignIncr, angleIncr, fillIncr,
                                             reflectIncr, shapeIncr, sizeIncr, tot,
                                           transformDict, matchObjsDict)
                # # compare A to C

                Agent.compareAtoObj(self, a, c, 'ac', 'bd', transformDict, matchObjsDict)
                # # compare B to D
                tot = Agent.compareObjtoAns(self, b, problem, x, 'ac', 'bd', alignIncr, angleIncr, fillIncr,
                                            reflectIncr, shapeIncr, sizeIncr, tot,
                                           transformDict, matchObjsDict)

                # dict1 = Agent.matchObjects(self, a, b, attributeList, incrList)
                # print('\nOBJECT MATCHING DICTIONARY!')
                # print(dict1)

                # compare remaining attributes to answer
                # attributeList = ['size', 'shape', 'fill', 'alignment', 'angle', 'above', 'inside']
                attributeList = ['size', 'shape']
                objCompareList = [b, c]
                tot = Agent.compEqAttributes(self, matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x)

                # if local answer > max answer:
                print("current answer " + str(x) + ' total = ' + str(tot) + ' MaxTotal = ' + str(maxTot))

                if tot > maxTot:
                    # max answer = local answer
                    print("previous maxTot = " + str(maxTot))
                    maxTot = tot
                    print("new maxTot = " + str(maxTot))
                    # answer = current answer
                    print("previous answer = " + str(answer))

                    answer = x

                    print("new answer = " + str(answer))

            print("final answer = " + str(answer))

            return answer

# -------------------------------------------------------------------------------------------------------
        # FOR 3X3 check if problem type is 3x3

        elif problem.problemType == "3x3":

            a = problem.figures['A']
            b = problem.figures['B']
            c = problem.figures['C']
            # define extra figure objects

            d = problem.figures['D']
            e = problem.figures['E']
            f = problem.figures['F']
            g = problem.figures['G']
            h = problem.figures['H']

            # Setup matching objects dictionary:
            matchObjsDict = {} # dictionary to match objects
            # attributeList = ['size', 'shape', 'fill'] # list of attributes used to match objects
            # incrList = [5, 10, 5] # corresponding attribute weights
            # attributeList = ['size', 'shape', 'fill', 'angle', 'alignment'] # list of attributes used to match objects
            attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
            incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

            # loop through all objects and add to dictionary

            #print('Now Matching problem: ' + problem.name)
            #print('Now Matching objects ' + a.name + ' and ' + c.name + ' for ' + problem.name )

            matchObjsDict = Agent.matchObjects(self, a, c, matchObjsDict, attributeList, incrList)

            #print('Now Matching objects ' + a.name + ' and ' + g.name + ' for ' + problem.name )

            matchObjsDict = Agent.matchObjects(self, a, g, matchObjsDict, attributeList, incrList)
            for x in range(1,9):
                ans = problem.figures[str(x)]
                #print('Now Matching objects ' + c.name + ' and ' + ans.name + ' for ' + problem.name )

                matchObjsDict = Agent.matchObjects(self, c, ans, matchObjsDict, attributeList, incrList)

                #print('Now Matching objects ' + g.name + ' and ' + ans.name + ' for ' + problem.name )

                matchObjsDict = Agent.matchObjects(self, g, ans, matchObjsDict, attributeList, incrList)

            print("\n" + problem.name + "\n")

            print('\nOBJECT MATCHING DICTIONARY!')
            for keys in sorted(matchObjsDict):
                print(str(keys) + ": " + str(matchObjsDict[keys]))

            for x in range(1, 9):     # loop through each potential answer from 1 to 8:

                print('\n  Now comparing answer: ' + str(x) + ' to ' + problem.name + ':\n')
                tot = 0   # initialize

                transformDict = {}  # create dictionary for transformations

                Agent.initialize_dicts(transformDict) # initialize empty keys in transformation dicts

                # compare deletion from AC to GAns

                tot = Agent.abcd_delete_comp(a, c, g, 'ab', 'cd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

                # compare deletion from AG to CAns
                tot = Agent.abcd_delete_comp(a, g, c, 'ac', 'bd', deleteIncr, deleteCompIncr, problem, tot, transformDict, x)

                # for ansObjName in Agent.sortDict(problem.figures[str(x)].objects):
                #     ansObj = problem.figures[str(x)].objects[ansObjName]

                # compare A to C

                Agent.compareAtoObj(a, c, 'ab', 'cd', transformDict, matchObjsDict)

                # compare G to Ans

                tot = Agent.compareObjtoAns(g, problem, x, 'ab', 'cd', alignIncr, angleIncr, fillIncr,
                                            reflectIncr, shapeIncr, sizeIncr, tot,
                                           transformDict, matchObjsDict)
                # # compare A to G

                Agent.compareAtoObj(a, g, 'ac', 'bd', transformDict, matchObjsDict)

                # # compare C to D
                tot = Agent.compareObjtoAns(c, problem, x, 'ac', 'bd', alignIncr, angleIncr, fillIncr,
                                            reflectIncr, shapeIncr, sizeIncr, tot,
                                           transformDict, matchObjsDict)

                # dict1 = Agent.matchObjects(self, a, c, attributeList, incrList)
                # print('\nOBJECT MATCHING DICTIONARY!')
                # print(dict1)

                # compare remaining attributes to answer
                objCompareList = [c, g]
                # attributeList = ['size', 'shape', 'fill', 'alignment', 'angle', 'above', 'inside']
                attributeList = ['size', 'shape', 'fill', 'angle', 'alignment', 'above', 'inside', 'left-of'] # list of attributes used to match objects
                incrList = [10, 15, 5, 5, 4, 4, 4, 4] # corresponding attribute weights

                tot = Agent.compEqAttributes(matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x)

                print('Current Total: ' + str(tot) + ' for Answer: ' + str(x) + ' maxTot = ' + str(maxTot))
                # if local answer > max answer:
                if tot is not None:
                    if tot > maxTot:
                        # max answer = local answer
                        print("previous maxTot = " + str(maxTot))
                        maxTot = tot
                        print("new maxTot = " + str(maxTot))
                        # answer = current answer
                        print("previous answer = " + str(answer))
                        answer = x
                        print("new answer = " + str(answer))

            print("final answer = " + str(answer))

            return answer

# Helpful Functions:

    def initialize_dicts(self, transformDict):
        # initialize empty keys for angle transformations
        transformDict['abAngleDiff'] = None
        transformDict['cdAngleDiff'] = None
        transformDict['acAngleDiff'] = None
        transformDict['bdAngleDiff'] = None
        # initialize empty keys for fill transformations
        transformDict['abFillDiff'] = None
        transformDict['cdFillDiff'] = None
        transformDict['acFillDiff'] = None
        transformDict['bdFillDiff'] = None
        # initialize empty keys for shape transformations
        transformDict['abShapeDiff'] = ''
        transformDict['cdShapeDiff'] = ''
        transformDict['acShapeDiff'] = ''
        transformDict['bdShapeDiff'] = ''
        # initialize empty keys for size transformations
        transformDict['abSizeDiff'] = 0
        transformDict['cdSizeDiff'] = 0
        transformDict['acSizeDiff'] = 0
        transformDict['bdSizeDiff'] = 0
        # initialize empty keys for alignment transformations
        transformDict['abAlignDiff'] = 'empty-'
        transformDict['cdAlignDiff'] = 'empty-'
        transformDict['acAlignDiff'] = 'empty-'
        transformDict['bdAlignDiff'] = 'empty-'

    # def acbd_delete_comp(self, a, c, deleteIncr, g, varNames, varNames1, problem, tot, transformDict, x):
    #     transformDict[varNames + 'DeleteDiff'] = len(a.objects) - len(g.objects)
    #     print(varNames + 'DeleteDiff: ' + str(transformDict[varNames + 'DeleteDiff']))
    #     transformDict[varNames1 + 'DeleteDiff'] = len(c.objects) - len(problem.figures[str(x)].objects)
    #     print(varNames1 + 'DeleteDiff: ' + str(transformDict[varNames1 + 'DeleteDiff']))
    #     if transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff']:
    #         tot += (deleteIncr * transformDict[varNames + 'DeleteDiff'])
    #         # tot += (deleteIncr)
    #         print('AC BD same deletion!')
    #
    #     return tot

    def abcd_delete_comp(self, a, b, c, varNames, varNames1, deleteIncr, deleteCompIncr, problem, tot, transformDict, x):

        if a is None:
            aLen = 0
        else:
            aLen = len(a.objects)
        if b is None:
            bLen = 0
        else:
            bLen = len(b.objects)
        if c is None:
            cLen = 0
        else:
            cLen = len(c.objects)

        if problem.figures[str(x)] is None:
            ansLen = 0
        else:
            ansLen = len(problem.figures[str(x)].objects)

        transformDict[varNames + 'DeleteDiff'] = aLen - bLen
        # print(varNames + 'DeleteDiff: ' + str(transformDict[varNames + 'DeleteDiff']))
        transformDict[varNames1 + 'DeleteDiff'] = cLen - ansLen
        # print(varNames1 + 'DeleteDiff: ' + str(transformDict[varNames1 + 'DeleteDiff']))
        if transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff'] and transformDict[varNames + 'DeleteDiff'] != 0:
            # total is increased by increments x # deletions
            tot += (deleteIncr * abs(transformDict[varNames + 'DeleteDiff']))
            # tot += (deleteIncr)
            print('AB CD same deletion!')
        elif transformDict[varNames + 'DeleteDiff'] == transformDict[varNames1 + 'DeleteDiff'] and transformDict[varNames + 'DeleteDiff'] == 0:
            tot += deleteIncr
            print('AB CD same NO deletion!')

        # TODO: Compensate for deletion
        if ansLen < min(aLen, bLen, cLen):
            tot += (min(aLen, bLen, cLen) - ansLen) * deleteCompIncr
            print('Object Deletion compensation of ' + str(min(aLen, bLen, cLen) - ansLen) + ' objects. Tot = ' + str(tot))
        elif ansLen > max(aLen, bLen, cLen):
            tot += (ansLen - max(aLen, bLen, cLen)) * deleteCompIncr
            print('Object Addition compensation of ' + str(min(aLen, bLen, cLen) - ansLen) + ' objects. Tot = ' + str(tot))
        return tot

    def compEqAttributes(self, matchObjsDict, attributeList, objCompareList, problem, sameIncr, tot, x):

        ansObj = problem.figures[str(x)]
        # todo: choose min of the 2

        for c in objCompareList:
            for n in range(len(matchObjsDict[str(c.name) + ', ' + str(x)])):
                cObjName, ansObjName = matchObjsDict[str(c.name) + ', ' +str(x)][n][0], matchObjsDict[str(c.name) + ', ' +str(x)][n][1]
                cObj, ansObj = c.objects[str(cObjName)], problem.figures[str(x)].objects[str(ansObjName)]

                for n in range(len(attributeList)):
                    attributeName = attributeList[n]
                    if attributeName in cObj.attributes and attributeName in ansObj.attributes:
                        if ansObj.attributes[attributeName] == cObj.attributes[attributeName]:
                            tot += sameIncr

                    # compare multiple attributes at the same time!
                    if n < len(attributeList)-1:
                        attributeName1 = attributeList[n+1]
                        if attributeName in cObj.attributes and attributeName in ansObj.attributes and attributeName1 in cObj.attributes and attributeName1 in ansObj.attributes:
                            if ansObj.attributes[attributeName] == cObj.attributes[attributeName] and ansObj.attributes[attributeName1] == cObj.attributes[attributeName1]:
                                tot += sameIncr * 10
                            # print('Figure' + str(fig.name) + ' attrib: ' + attributeName + ' compared to ' + str(
                            #     x) + ', current total = ' + str(tot))
        return tot

    def matchObjects(self, fig1, fig2, matchObjsDict, attributeList, incrList):

        # Todo: create deleted objects

        candidateObjsList = [] # candidate object of fig2 list, will be removed once matched

        matchObjsList = []

        if len(fig2.objects) >= len(fig1.objects):

            for obj2Name in sorted(fig2.objects):
                candidateObjsList.append(fig2.objects[obj2Name])

            for obj1Name in sorted(fig1.objects):
                obj1 = fig1.objects[obj1Name]
                maxObj = None
                maxTot = 0
                for obj2 in candidateObjsList:
                    tot = 0
                    # for attributeName, incr in zip(attributeList, incrList):
                    #         if attributeName in obj1.attributes and attributeName in obj2.attributes:
                    #             if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                    #                 tot += incr
                                    # print('OBJECT MATCH! attr: ' + attributeName + ' ' + str(incr) + ' pts  New total: ' + str(tot) )
                    for n in range(len(attributeList)):
                        attributeName = attributeList[n]
                        incr = incrList[n]
                        if attributeName in obj1.attributes and attributeName in obj2.attributes:
                                if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                                    tot += incr
                                    # print('Object attribute match ' + attributeName + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                        # compare multiple attributes at the same time!
                        if n < len(attributeList)-1:
                            attributeName1 = attributeList[n+1]
                            incr1 = incrList[n+1]
                            if attributeName in obj1.attributes and attributeName in obj2.attributes and attributeName1 in obj1.attributes and attributeName1 in obj2.attributes:
                                if obj2.attributes[attributeName] == obj1.attributes[attributeName] and obj2.attributes[attributeName1] == obj1.attributes[attributeName1]:
                                    tot += (incr + incr1) * 10
                                    # print('DOUBLE ATTR INCR ' + attributeName + ' and ' + attributeName1 + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                    #print ('Total for objects ' + obj1Name + ' and ' + obj2.name + ' = ' + str(tot))
                    if tot > maxTot:
                        maxTot = tot
                        maxObj = obj2
                        # print ('New Max Obj! ' + obj2.name + ' = ' + str(tot))

                if maxObj is not None:
                    matchObjsList.append((obj1.name, maxObj.name))
                    candidateObjsList.remove(maxObj)

        elif len(fig2.objects) < len(fig1.objects):

            for obj1Name in sorted(fig1.objects):
                candidateObjsList.append(fig1.objects[obj1Name])

            for obj2Name in sorted(fig2.objects):
                obj2 = fig2.objects[obj2Name]
                maxObj = None
                maxTot = 0
                for obj1 in candidateObjsList:
                    tot = 0
                    # for attributeName, incr in zip(attributeList, incrList):
                    #         if attributeName in obj1.attributes and attributeName in obj2.attributes:
                    #             if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                    #                 tot += incr
                    #                 #print('OBJECT MATCH! attr: ' + attributeName + ' ' + str(incr) + ' pts  New total: ' + str(tot) )

                    for n in range(len(attributeList)):
                        attributeName = attributeList[n]
                        incr = incrList[n]
                        if attributeName in obj1.attributes and attributeName in obj2.attributes:
                                if obj1.attributes[attributeName] == obj2.attributes[attributeName]:
                                    tot += incr
                                    # print('Object attribute match ' + attributeName + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                        # compare multiple attributes at the same time!
                        if n < len(attributeList)-1:
                            attributeName1 = attributeList[n+1]
                            incr1 = incrList[n+1]
                            if attributeName in obj1.attributes and attributeName in obj2.attributes and attributeName1 in obj1.attributes and attributeName1 in obj2.attributes:
                                if obj2.attributes[attributeName] == obj1.attributes[attributeName] and obj2.attributes[attributeName1] == obj1.attributes[attributeName1]:
                                    tot += (incr + incr1) * 5
                                    # print('DOUBLE ATTR INCR ' + attributeName + ' and ' + attributeName1 + ' for ' + obj1Name + ' and ' + obj2.name + ' Tot = ' + str(tot))

                    #print ('Total for objects ' + obj1Name + ' and ' + obj2.name + ' = ' + str(tot))
                    if tot > maxTot:
                        maxTot = tot
                        maxObj = obj1
                        # print ('New Max Obj! ' + obj1.name + ' = ' + str(tot))

                if maxObj is not None:
                    matchObjsList.append((maxObj.name, obj2.name))
                    candidateObjsList.remove(maxObj)

        matchObjsDict[str(fig1.name) + ', ' +str(fig2.name)] = matchObjsList

        return matchObjsDict

    def compareAtoObj(self, a, b, varNames, varNames1, transformDict, matchObjsDict):

        # TODO: add  above, and inside transformations

        # todo: choose min of the 2
        for n in range(len(matchObjsDict[str(a.name) + ', ' + str(b.name)])):
            aObjName, bObjName = matchObjsDict[str(a.name) + ', ' + str(b.name)][n][0], matchObjsDict[str(a.name) + ', ' +str(b.name)][n][1]
            aObj, bObj = a.objects[str(aObjName)], b.objects[str(bObjName)]

            #TODO: make special case of square having properties of height and width and compare to rectangle
            Agent.convertSquareToRectangle(self, aObj)
            Agent.convertSquareToRectangle(self, bObj)

            #TODO: compare to rectangle
            Agent.compHeightAndWidth(self, aObj, bObj, n, transformDict, varNames)
            
            # check for shape transform:
            #if aObj.attributes['shape'] != bObj.attributes['shape']:
            transformDict[str(n) + varNames + 'ShapeDiff'] = (aObj.attributes['shape'] + '-' + bObj.attributes['shape'])
            print('\nShape Transform for ' + str(n) + varNames + ' : ' + transformDict[str(n) + varNames + 'ShapeDiff'])

            # Weighted Size transformation

            # if aObj.attributes['size'] != bObj.attributes['size']:
            if 'size' in aObj.attributes and 'size' in bObj.attributes:
                transformDict[str(n) + varNames + 'SizeDiff'] = Agent.convertSize(self, aObj.attributes['size']) - Agent.convertSize(self, bObj.attributes['size'])
                print(str(n) + varNames + 'SizeDiff: ' + str(transformDict[str(n) + varNames + 'SizeDiff']))

            # make alignment transformation comparison
            if 'alignment' in aObj.attributes and 'alignment' in bObj.attributes:
                if aObj.attributes['alignment'] != bObj.attributes['alignment']:
                    transformDict[str(n) + varNames + 'AlignDiff'] = aObj.attributes['alignment'] + '-' + bObj.attributes['alignment']
                    # remove duplicate words
                    transformDict[str(n) + varNames + 'AlignDiff'] = Agent.removeDuplicates([str(n) + varNames + 'AlignDiff'])
                    print(str(n) + varNames + 'AlignDiff: ' + transformDict[str(n) + varNames + 'AlignDiff'])

            # make fill transform:  if same int = 0, if different, int = 1
            # calculate AB fill difference
            if aObj.attributes['fill'] == bObj.attributes['fill']:
                transformDict[str(n) + varNames + 'FillDiff'] = 0
            else:
                transformDict[str(n) + varNames + 'FillDiff'] = 1  # if the fill changed across the transformation assign a 1

            # make transformation comparisons for angles:

            # print("making angle transformation comparisons")
            if 'angle' in aObj.attributes and 'angle' in bObj.attributes:  # check that this object has angles
                # calculate AB angle difference
                transformDict[str(n) + varNames + 'AngleDiff'] = int(aObj.attributes['angle']) - int(bObj.attributes['angle'])
                print(str(n) + varNames + " AngleDiff = " + str(transformDict[str(n) + varNames + 'AngleDiff']))

    def compHeightAndWidth(self, aObj, bObj, n, transformDict, varNames):
        if 'height' in aObj.attributes and 'height' in bObj.attributes:
            transformDict[str(n) + varNames + 'HeightDiff'] = Agent.convertSize(self, aObj.attributes[
                'height']) - Agent.convertSize(self, bObj.attributes['height'])
            print(str(n) + varNames + 'HeightDiff: ' + str(transformDict[str(n) + varNames + 'HeightDiff']))
        if 'width' in aObj.attributes and 'width' in bObj.attributes:
            transformDict[str(n) + varNames + 'WidthDiff'] = Agent.convertSize(self, aObj.attributes[
                'width']) - Agent.convertSize(self, bObj.attributes['width'])
            print(str(n) + varNames + 'WidthDiff: ' + str(transformDict[str(n) + varNames + 'WidthDiff']))

    def compareObjtoAns(self, c, problem, x, varNames, varNames1, alignIncr, angleIncr, fillIncr, reflectIncr, shapeIncr, sizeIncr,
                        tot, transformDict, matchObjsDict):

        ansObjFigure = problem.figures[str(x)]
        # todo: choose min of the 2
        for n in range(len(matchObjsDict[str(c.name) + ', ' + str(x)])):
            cObjName, ansObjName = matchObjsDict[str(c.name) + ', ' + str(x)][n][0], matchObjsDict[str(c.name) + ', ' +str(x)][n][1]
            cObj, ansObj = c.objects[str(cObjName)], ansObjFigure.objects[ansObjName]

            #TODO: make special case of square having properties of height and width and compare to rectangle
            Agent.convertSquareToRectangle(self, cObj)
            Agent.convertSquareToRectangle(self, ansObj)
            
            #TODO: compare to rectangle
            Agent.compHeightAndWidth(self, cObj, ansObj, n, transformDict, varNames1)
            
            if str(n) + varNames + 'HeightDiff' in transformDict and str(n) + varNames1 + 'HeightDiff' in transformDict:
                if (transformDict[str(n) + varNames + 'HeightDiff']) == (transformDict[str(n) + varNames1 + 'HeightDiff']):
                    tot += sizeIncr
                    print("CORRECT HEIGHT TRANSFORM! FOR " + str(n) + varNames + varNames1)
                    
            if str(n) + varNames + 'WidthDiff' in transformDict and str(n) + varNames1 + 'WidthDiff' in transformDict:
                if (transformDict[str(n) + varNames + 'WidthDiff']) == (transformDict[str(n) + varNames1 + 'WidthDiff']):
                    tot += sizeIncr
                    print("CORRECT WIDTH TRANSFORM! FOR " + str(n) + varNames + varNames1)

            # check for shape transform:
            # if cObj.attributes['shape'] != ansObj.attributes['shape']:

            transformDict[str(n) + varNames1 + 'ShapeDiff'] = (cObj.attributes['shape'] + '-' + ansObj.attributes['shape'])
            print('\nShape Transform for ' + str(n) + varNames1 + ': ' + transformDict[str(n) + varNames1 + 'ShapeDiff'])
            # print('cObjName = ' + cObj.name + ' ansObjName = ' + ansObj.name)

            #if n == (len(matchObjsDict[str(c.name) + ', ' + str(x)]) - 1):
            if str(n) + varNames + 'ShapeDiff' in transformDict and str(n) + varNames1 + 'ShapeDiff' in transformDict:
                # the sorting corrects the issue of the same shapes appearing in different orders
                if (transformDict[str(n) + varNames + 'ShapeDiff']) == (transformDict[str(n) + varNames1 + 'ShapeDiff']):
                    tot += shapeIncr
                    print("CORRECT SHAPE TRANSFORM! FOR " + str(n) + varNames + varNames1)

            if 'size' in cObj.attributes and 'size' in ansObj.attributes:
                transformDict[str(n) + varNames1 + 'SizeDiff'] = Agent.convertSize(self, cObj.attributes['size']) - Agent.convertSize(self, ansObj.attributes['size'])
                print(str(n) + varNames1 + 'SizeDiff: ' + str(transformDict[str(n) + varNames1 + 'SizeDiff']))
                # if transformDict[str(n) + varNames + 'SizeDiff'] != '' and transformDict[str(n) + varNames1 + 'SizeDiff'] != '':
            # the sorting corrects the issue of the same sizes appearing in different orders
            if str(n) + varNames + 'SizeDiff' in transformDict and str(n) + varNames1 + 'SizeDiff' in transformDict:
                if (transformDict[str(n) + varNames + 'SizeDiff']) == (transformDict[str(n) + varNames1 + 'SizeDiff']):
                    tot += sizeIncr
                    print("CORRECT SIZE TRANSFORM! FOR " + str(n) + varNames + varNames1)

            # calculate CD fill difference
            ansValue = ansObj.attributes['fill']
            if cObj.attributes['fill'] == ansValue:
                transformDict[str(n) + varNames1 + 'FillDiff'] = 0
            else:
                transformDict[str(n) + varNames1 + 'FillDiff'] = 1
                # Make fill transformation comparison:
            if str(n) + varNames + 'FillDiff' in transformDict and str(n) + varNames1 + 'FillDiff' in transformDict:
                if transformDict[str(n) + varNames + 'FillDiff'] == transformDict[str(n) + varNames1 + 'FillDiff']:
                    tot += fillIncr
                    print("CORRECT ab = cd FILL transformations!")

            # check alignment transform
            if 'alignment' in cObj.attributes and 'alignment' in ansObj.attributes:
                if cObj.attributes['alignment'] != ansObj.attributes['alignment']:
                    transformDict[str(n) + varNames1 + 'AlignDiff'] = cObj.attributes['alignment'] + '-' + ansObj.attributes['alignment']
                    print(str(n) + varNames1 + 'AlignDiff: ' + transformDict[str(n) + varNames1 + 'AlignDiff'])
                    # remove duplicate words
                    transformDict[str(n) + varNames1 + 'AlignDiff'] = Agent.removeDuplicates(transformDict[str(n) + varNames1 + 'AlignDiff'])
                    print(str(n) + varNames1 + 'AlignDiff: ' + transformDict[str(n) + varNames1 + 'AlignDiff'])
            # calculate alignment transform differences
            # if sorted(transformDict[str(n) + varNames + 'AlignDiff']) == sorted(transformDict[str(n) + varNames1 + 'AlignDiff']) and transformDict[
            #     str(n) + varNames + 'AlignDiff'] != 'empty-' and transformDict[str(n) + varNames1 + 'AlignDiff'] != 'empty-':
                if (str(n) + varNames + 'AlignDiff') in transformDict and (str(n) + varNames1 + 'AlignDiff') in transformDict:
                    if (transformDict[str(n) + varNames + 'AlignDiff']) == (transformDict[str(n) + varNames1 + 'AlignDiff']) and transformDict[
                        str(n) + varNames + 'AlignDiff'] != 'empty-' and transformDict[str(n) + varNames1 + 'AlignDiff'] != 'empty-':
                        tot += alignIncr
                        print("CORRECT Align transformations! for " + str(n) + varNames + varNames1)

            # if angle transformation equal tot+=1

            if 'angle' in cObj.attributes and 'angle' in ansObj.attributes:  # check that this object has angles
                transformDict[str(n) + varNames1 + 'AngleDiff'] = int(cObj.attributes['angle']) - int(ansObj.attributes['angle'])
                makeAngTransCompCD = True
                print("cdAngleDiff= " + str(transformDict[str(n) + varNames1 + 'AngleDiff']))
            else:
                makeAngTransCompCD = False

             # check for angle transformation
            # TODO: troubleshoot angle transformation comparisons
            if str(n) + varNames + 'AngleDiff' in transformDict and str(n) + varNames1 + 'AngleDiff' in transformDict:
                if abs(transformDict[str(n) + varNames + 'AngleDiff'] + 180) % 360 == abs(transformDict[str(n) + varNames1 + 'AngleDiff']):
                    tot += reflectIncr
                    print("Same reflections for " + str(n) + varNames + varNames1)
                elif transformDict[str(n) + varNames + 'AngleDiff'] == transformDict[str(n) + varNames1 + 'AngleDiff']:
                    tot += angleIncr
                    print("Same angle transformations for " + str(n) + varNames + varNames1)

        return tot

    def convertSquareToRectangle(self, aObj):
        if aObj.attributes['shape'] == 'square':
            aObj.attributes['length'] = aObj.attributes['size']
            aObj.attributes['width'] = aObj.attributes['size']

    def convertSize(self, size):
        ' converts object size to integer'
        if size == 'very small':
            return 1
        elif size == 'small':
            return 2
        elif size == 'medium':
            return 3
        elif size == 'large':
            return 4
        elif size == 'very large':
            return 5
        elif size == 'huge':
            return 6

    def removeDuplicates(self, inputString):
        alignList = ''
        alignList = inputString.split('-')
        listString = ''
        removeWords = []
        for word in alignList:
            if word in listString:
                removeWords.append(word)
            else:
                listString += word
        for removeWord in removeWords:
            listString = listString.replace(removeWord, "")
        return listString

    def sortDict(self, dict):
        # return sorted(dict, key=dict.get)
        return dict

    # Visual Transformation Functions borrowed from Bradley Demmons Project 1:
    def reflectVert(img1):
        # reflect the image over the vertical axis
        return img1.transpose(Image.FLIP_LEFT_RIGHT)

    def reflectHoriz(img1):
        # reflect the image over the horizontal axis
        return img1.transpose(Image.FLIP_TOP_BOTTOM)

    def rotate315(img1):
        # rotate the image 315 degrees
        # paste onto white background to eliminate edge clipping
        bkg = Image.new('L', (img1.size[0],img1.size[1]), (255))
        img1 = img1.rotate(315)
        bkg.paste(img1,img1)
        return bkg

    def rotate270(img1):
        # rotate the image 270 degrees
        return img1.transpose(Image.ROTATE_270)

    def rotate180(img1):
        # rotate the image 180 degrees
        return img1.transpose(Image.ROTATE_180)

    def rotate90(img1):
        # rotate the image 90 degrees
        return img1.transpose(Image.ROTATE_90)

    def rotate45(img1):
        # rotate the image 45 degrees
        # paste onto white background to eliminate edge clipping
        bkg = Image.new('L', (img1.size[0],img1.size[1]), (255))
        img1 = img1.rotate(45)
        bkg.paste(img1,img1)
        return bkg

