from time import time, sleep


def get_text_list(the_text: str):
    result = []
    all_text_list = the_text.strip().split()
    i = 0

    if len(the_text.strip()) < 500 or len(all_text_list) < 90:
        print("")
        print("文本长度不足！")
        return []

    while len(result) != 5:
        unit_text_list = []
        while len(unit_text_list) < 15 or len(" ".join(unit_text_list)) < 80:
            unit_text_list.append(all_text_list[i])
            i += 1
        result.append(" ".join(unit_text_list))

    return result


long_text = """

The two pictures compare the layout of a school as it was in the year 2004 with a proposed site design for the year 2024.

It is clear that the main change for 2024 involves the addition of a new school building. The school will then be able to accommodate a considerably larger number of students.

In 2004, there were 600 pupils attending the school, and the two school buildings were separated by a path running from the main entrance to the sports field. By 2024, it is expected that there will be 1000 pupils, and a third building will have been constructed. Furthermore, the plan is to join the two original buildings together, creating a shorter path that links the buildings only.

As the third building and a second car park will be built on the site of the original sports field, a new, smaller sports field will need to be laid. A new road will also be built from the main entrance to the second car park. Finally, no changes will be made to the main entrance and original car park.

"""

text_list = get_text_list(long_text)

if not text_list:
    exit

time_list = []

print(f"测试即将开始，你有 10 秒钟准备时间")
sleep(10)


def get_errors(origin: str, yours: str):
    print("\n")

    o_list = origin.split()
    y_list = yours.split()

    if len(o_list) != len(y_list):
        print("单词数量不符！")
        return False

    for i in range(len(o_list)):
        o = o_list[i]
        y = y_list[i]

        if o == y:
            continue

        print(f"{y} 应该为 {o}")
    
    return True


for text in text_list:
    answer = ""
    duration = 0

    while answer != text:
        answer = answer.strip()

        if answer and answer != text:
            print("\n")
            print("输入错误！请重新输入！你有 5 秒钟准备时间")
            get_errors(text, answer)
            sleep(5)

        print("\n")
        print(f"请输入以下字符，并按回车：\n\n{text}\n")
        start_time = time()
        answer = input()
        end_time = time()
        duration = end_time - start_time
    
    time_list.append(len(text) / duration)

    if text != text_list[-1]:
        print("\n")
        print("你现在有 10 秒钟的休息时间，下一题出现后，请立刻继续输入！")
        sleep(10)

avg = sum(time_list) / len(time_list)
speed = (avg / 8) * 60

print("\n")
print(f"平均每秒钟击打字符：{int(avg)} 个")
print(f"预计每分钟击打字符：{int(avg * 60)} 个")
print(f"预计每分钟输入单词：{int(speed)} 个")
print("\n")
print(f"预计小作文时间：{150 / speed:.1f} 分钟")
print(f"预计大作文时间：{250 / speed:.1f} 分钟")
print("\n")
