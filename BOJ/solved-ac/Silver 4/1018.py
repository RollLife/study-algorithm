"""
Class 2

체스판 다시 칠하기

문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고,
나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.


입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""

example_input = "10 13"
example_board = """BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""
input_string = example_input
board_string = example_board

# input_string = input()
# board_string = input()


N = int(input_string.split(" ")[0])
M = int(input_string.split(" ")[1])

PIECE_SET = {"B": "W", "W": "B"}


# 각 인자가 다른지 구분
def check_equal(previous_arg, current_arg):
    if previous_arg != current_arg:
        return False
    return True


def main(text):
    result_cnt = 0
    # 이전 값
    previous_value = ""
    each_line_list = text.split("\n")

    for each_line in each_line_list:
        for _idx, char in enumerate(each_line):
            # 가장 초기에 이전 값이 존재하지 않기에 초기화 시켜줌
            if not previous_value:
                previous_value = char
                print(char, end ="")
                continue

            # 체스 말이 교차되지 않고 같은 말이 연속으로 나오는지 확인
            is_equal = check_equal(previous_value, char)
            # print(is_equal, end="")
            if is_equal:
                result_cnt += 1
                # 현재의 교차되지 않고 다시 색칠해야하는 값으로 변경
                correct_piece = PIECE_SET[char]
                previous_value = correct_piece
                # print(correct_piece, end="")
                continue
            # print(char, end="")
            previous_value = char
        # print()
        # previous_value = ""
    return result_cnt


print(main(example_board))

# 7/15 문제가 이해가 되지 않아 풀 수 없었음.