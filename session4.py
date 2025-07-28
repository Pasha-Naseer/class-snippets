# set
# unordered, changeable, no duplicates
singers = {"Pavarotti", "Bocelli", "Caruso", "Di Stefano"}
print(singers)

singers.pop()  # Do not relly on the order
print(singers)

singers2 = singers.copy()
print(singers)

singers2.clear()
print(singers2)

singers.remove("Bocelli")  # Returns an error if the element is absent
print(singers)

singers.update({"Corelli", "Tebaldi"})
print(singers)

singers.add("Gigli")
print(singers)

singers.discard("Tebaldi")  # Doesn't return an error when the element is absent
print(singers)

# Let's get mathematical
a = {1, 3, 6}
b = {2, 6, 4}

print(a.union(b))
print(b.union(a))  # both give us the same result

print(a.difference(b))
print(b.difference(a))  # they are different

print(a.intersection(b))
print(b.intersection(a))  # both give us the same result

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))  # both give us the same result

print(a.isdisjoint(b))  # happens when they have nothing in common

print(a.issuperset(b))

print(a.issubset(b))

a.difference_update(b)  # modifies the first set by deleting the item in common
print(a)

a.symmetric_difference_update(b)  # modifies the first set so that it contains all elements from a-b U b-a
print(a)

print("AAA")
print(b)
a.intersection_update(b)  # modifies the first set, so it only contains the elements in common with b
print(a)
