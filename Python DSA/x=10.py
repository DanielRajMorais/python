# def my_func(**kwargs):
#   total = 0
#   len_str = len(s)

#   for x, y in z:
#     print(x,y)
#     if x == 0:
#       total += y
#       print("inside x loop", total)
#     else:
#       total -= y
#       print("inside y loop", total)
#   print(f"before final loop: total={total} , length= {len_str}")
#   total = total % len_str
#   print("outside loop" , total)
#   print(s[total:] + s[:total])


# s = 'cutshort'
# z = [[0, 3], [1, 11], [2,4]]

# if __name__ == "__main__":
#   my_func(s='cutshort', z= [[0, 3], [1, 11], [2,4]])



new = {i:i*2 for i in range(0,20) }
print(new)