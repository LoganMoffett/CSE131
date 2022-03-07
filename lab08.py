# 1. Name:
#      Logan
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This will sort alphabetically (or smallest to largest) a list given from the user
# 4. What was the hardest part? Be as specific as possible.
#      Honestly, this assignemnet was not hard at all. I used the design that we created 
#      in the prvious assignments and implemented it into code.
# 5. How long did it take for you to complete the assignment?
#      45 min

class sub_sort:

    def __init__(self):
        pass

    def run(self):
        array = self.get_array()
        sorted_array = self.sort(array)
        print(sorted_array)
    
    def get_array(self):
        user_input = "q"
        array = []
        while user_input != "":
            user_input = input("Enter the item you would like to add to the list that needs sorted, or enter nothing to end stop adding: ")
            if user_input != "":
                array.append(int(user_input))
        return array
    
    def sort(self, array):
        size = len(array)
        src = array
        des = [None] * len(array)
        num = 2
        while num > 1:
            num = 0
            begin1 = 0

            while begin1 < size:
                end1 = begin1 + 1
                while end1 < size and src[end1 - 1] <= src[end1]:
                    end1 += 1
                
                begin2 = end1
                if begin2 < size:
                    end2 = begin2 + 1
                else:
                    end2 = begin2
                while end2 < size and src[end2 - 1] <= src[end2]:
                    end2 += 1
                
                num += 1
                self.combine(src, des, begin1, begin2, end2)
                begin1 = end2
            for x in range(0, len(src)):
                src[x], des[x] = des[x], src[x]
        return src
    def combine(self, src, des, begin1, begin2, end2):
        end1 = begin2

        for i in range(begin1, end2):
            if (begin1 < end1) and (begin2 == end2 or src[begin1] < src[begin2]):
                des[i] = src[begin1]
                begin1 += 1
            else:
                des[i] = src[begin2]
                begin2 += 1
        return des

        

list = sub_sort()
list.run()
list.run()
list.run()
print(list.sort([6, 3]))
print(list.sort([3, 12, 26, 38, 49, 59, 64]))
print(list.sort([64, 59, 49, 38, 26, 12, 3]))
print(list.sort([3, 12, 26, 38, 49, 59, 64, 79]))
print(list.sort([79, 64, 59, 49, 38, 26, 12, 3]))
print(list.sort([31, 55, 99, 21, 49, 49]))