def solve(string):
    n = len(string)
    t = [[-1 for _ in range(n)] for _ in range(n)]

    for g in range(n):
        i = 0
        for j in range(g, n):
            if g == 0:
                t[i][j] = 1
            elif g == 1:
                if string[i] == string[j]:
                    t[i][j] = 3
                else:
                    t[i][j] = 2
            else:
                if string[i] == string[j]:
                    t[i][j] = (t[i][j - 1] + t[i + 1][j] + 1)%1000000007
                else:
                    t[i][j] = (t[i][j - 1] + t[i + 1][j] - t[i + 1][j - 1])%1000000007
            i = i + 1

    return t[0][n - 1]


if __name__ == '__main__':
    string = 'mbcgepnkdqemhmkuqosgeonbcrphobcmbhrgppkfpdqckigsomktpsurknsospighufulqijcupisnuqcqfpuckrndmqeeklqfcrfnemeghmnlunlpslncqllmbebnoudihgpigrfbrqbcurmqnfroheqltkbnpocousjepehgppmblodppsqrglprtekmsqlqekhjseotocgkfcrkssmmenhitupdcoujscnetbrrcdoctqdfssupfnuolrobckseuromqsuoctmnbudnthrctndtrnietrkqbropugptpuhclftohuendhhnpnhqqkmksigbcrtrtjtmhonnumnnupgtntdhefushmrshselrdfqnoddmqqhjrjtknmokrlgdrcomnbjdlcothrhgsljreflusnnnrkckstoluhduguicfomgjkorgmujoonekscbikeshbqfqfrbcmspqphujltqebostmbkunhhhqmdqdqmfsbekeonmsiqsbomhmrtnqtmutrbmrlthhieihqjebklckemustsufbqmbjcqdtkdjscmdsrkkqdfojplektrsinjfbhmfoumqirfehdhgdkejefupstmhqesqobcqftpgbrckqrjqdosfjschbhbuobhriguipdkeeggbtecsqheelrqiqfdokqhrdsdcifnkulloeckeghochpdfjpqesqmqsngcbpngjurdsbhtsilkoiglbgmofnjuojtgjqnpgobmfehjnqbfmternugrhbnrgqusloiuusqogtqsclesqsmhjghqdtqkgikghflotgfmkdngklcorqlegpdidptohlgnnnflhtcmpcehogooflhujpichtknfqicpkjmgjjdnmtsprcueeolruiqjpeldelnukfitfgqsdejupshdtebtqfrqbtuttkldbuupidurhimnrmpdfjtbuinfchjormhissgpdbisugtrqqdiqekpnicpej'
    print(solve(string))
