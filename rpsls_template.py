#coding:gbk
"""
С��Ŀ��RPSLS
���ߣ����
���ڣ�2022.5.13
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ�����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='ʯͷ':
        number=0
    elif name=='ʷ����':
        number=1
    elif name=='��':
        number=2
    elif name=='����':
        number=3
    elif name=='����':
        number=4
    else:
        number=5
    return number

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number == 0:
        name = 'ʯͷ'
    elif number == 1:
        name='ʷ����'
    elif number == 2:
        name = '��'
    elif number == 3:
        name = '����'
    elif number == 4:
        name = '����'
    else:
        name=''
    return name
def rpsls(player_choice):
    
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==5:
        print('Error:No Correct Name')
        return
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_number=random.randrange(5)
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    comp_name=number_to_name(comp_number)

    # ����Ļ����ʾ�����ѡ����������
    print("�������ѡ��Ϊ:", comp_name)
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ���жϣ�������Ļ����ʾ�жϽ��
    i=player_choice_number
    if comp_number in [i+1,i+2]:
        print('����Ӯ�ˣ�')
    elif comp_number==player_choice_number:
        print('���ͼ��������һ����')
    else:
        print('��Ӯ��')

print("--------")
# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
choice_name= input('����������ѡ��\n')
# print("----------------")
# print("����������ѡ��:")
# choice_name=input()
rpsls(choice_name)


