"""
https://www.acmicpc.net/problem/1181
단어 정렬

문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로


입력
첫째 줄에 단어의 개수 N이 주어진다.
 (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
  주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.
 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
"""
import string

ALPHABET_LIST = list(string.ascii_lowercase)
NUMBER_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 예제 입력
input_string = """13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours"""

# input_string = input()

result = {}


def check_duplicate(word):
    if word in result:
        return True
    return False


def diff_by_dictionary(first_word, second_word):
    for first_word_chr in list(first_word):
        for second_word_chr in list(second_word):
            if first_word_chr == second_word_chr:
                continue
            # if first_word_chr in NUMBER_LIST:
            #     first_word_chr = int(first_word_chr)
            # if second_word_chr in NUMBER_LIST:
            #     second_word_chr = int(second_word_chr)
            # if isinstance(first_word_chr, int) and isinstance(second_word_chr, str):
            #     return "first_number"
            # if isinstance(first_word_chr, str) and isinstance(second_word_chr, int):
            #     return "second_number"
            # first word get priority
            if not (first_word_chr > second_word_chr):
                return "first"
            # second word get priority
            else:
                return "second"


def diff_length(first_word, second_word):

    pass


def diff_each(first_word, second_word):
    pass


def sort(text):
    original_list = input_string.split("\n")
    print(original_list)


# sort(input_string)

print(diff_by_dictionary("12312", "123"))
