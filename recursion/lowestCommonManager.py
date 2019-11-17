class Tree:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def add_children(self, children):
        self.directReports.extend(children)

def getLowestCommonManager(topManager, reportOne, reportTwo):

    if (topManager.name == reportOne.name) or (topManager.name == reportTwo.name):
        number_of_reports = 1
    else:
        number_of_reports = 0

    if topManager.directReports == []:
        return number_of_reports

    for child in topManager.directReports:
        child_reports = getLowestCommonManager(child, reportOne, reportTwo)
        if not isinstance(child_reports, int):
            return child_reports
        number_of_reports += child_reports

    if number_of_reports == 2:
        return topManager

    return number_of_reports


if __name__ == "__main__":
    a = Tree("a")

    aa = Tree("aa")
    ab = Tree("ab")
    ac = Tree("ac")

    aaa = Tree("aaa")
    aab = Tree("aab")
    aac = Tree("aac")

    aba = Tree("aba")
    abb = Tree("abb")
    abc = Tree("abc")

    aca = Tree("aca")
    acb = Tree("acb")
    acc = Tree("acc")

    aaaa = Tree("aaaa")
    aaab = Tree("aaab")
    aaac = Tree("aaac")

    aaa.add_children([aaaa, aaab, aaac])
    aa.add_children([aaa, aab, aac])
    a.add_children([aa, ab, ac])

    ans = getLowestCommonManager(a, aaaa, aab)
    print(ans.name)
