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


def diff_by_dictionary(first_word, second_word):
    """
    두 단어를 사전순으로 비교

    사전순으로 나중에 온것이 더 큰값을 받는다.
    :param first_word:
    :param second_word:
    :return:
    """
    for first_word_chr in list(first_word):
        for second_word_chr in list(second_word):
            if first_word_chr == second_word_chr:
                continue
            # first word get priority
            if not (first_word_chr > second_word_chr):
                return "first"
            # second word get priority
            else:
                return "second"


def diff_length(first_word, second_word):
    """
    문자 길이를 서로 확인
    문자가 더 긴것이 나중에 온다.
    :param first_word:
    :param second_word:
    :return:
    """
    if len(first_word) == len(second_word):
        return False
    if not (len(first_word) < len(second_word)):
        return "first"
    return "second"


def check_number(word):
    """
    숫자가 포함되어있는지 확인
    :param word:
    :return:
    """
    for number in NUMBER_LIST:
        if number in word:
            return True
    return False


def check_duplicate(word):
    """
    중복된 단어가 있는지 확인
    :param word:
    :return:
    """
    if word in result:
        return True
    return False


def diff_each(first_word, second_word):
    df_length_value = diff_length(first_word, second_word)
    if df_length_value:
        return df_length_value

    df_dict_value = diff_by_dictionary(first_word, second_word)
    return df_dict_value


def sort(text):
    original_list = text.split("\n")

    cnt = 0
    # 선별작업, 숫자와 중복된 단어 포함되어 있는지 확인
    for original_word in original_list:
        if check_number(original_word):
            continue
        if check_duplicate(original_word):
            continue
        result[original_word] = cnt
        cnt += 1

    # TODO:서로 비교하는 로직 구현하기
    for key, value in result.items():
        diff_each((key, value))

    print(result)


sort(input_string)

# print(diff_by_dictionary("12312", "123"))
