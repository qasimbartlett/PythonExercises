# Given a string of numbers flip the numbers divisible by 3
# 83459    7534567839 
# 89453    7594537863
class Flip:
    # Assumptions
    def __init__(self, in_str):
        print('in_str=%s' % in_str)
        in_list = list(map(int, in_str))
        left = 0
        right = len(in_list) - 1
        while left < right:
            if in_list[left] % 3 == 0:
                while right > left:
                    if in_list[right] % 3 == 0:
                        val_left = in_list[left]
                        val_right = in_list[right]
                        in_list[left] = val_right
                        in_list[right] = val_left
                        right = right - 1 
                        break             
                    right = right - 1
            left += 1
        print(in_list)


def main():
    Flip('7534567839')
    Flip('83459')
    Flip('1')
    Flip('369')
    Flip('')


if __name__ == "__main__":
    main()
