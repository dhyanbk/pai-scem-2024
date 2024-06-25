def main():
    set1 = set(input("Enter elements of set 1: ").split())

    set2 = set(input("Enter elements of set 2 : ").split())

    union_set = set1.union(set2)
    print(f"Union of set1 and set2: {union_set}")

    intersection_set = set1.intersection(set2)
    print(f"Intersection of set1 and set2: {intersection_set}")

if __name__ == "__main__":
    main()
