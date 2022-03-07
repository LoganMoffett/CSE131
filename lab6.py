


def get_list():
    user_list = input("What is the list that you would like to sort? ")
    list = user_list.split(",")
    return list

def sort_list(unsorted_list):
    sorted_list = [None] * len(unsorted_list)
    print(sorted_list)
def main():
    list = get_list()
    sorted_list = sort_list(list)

main()

