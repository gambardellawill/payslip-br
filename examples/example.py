#  -*- coding:utf-8 -*- 

import sys
import re

from payslip_br import payslip

# sys.path.insert(0, '../src/payslip_br/')
# import payslip


if __name__ == "__main__":
    # 846100000005659900641005011014371105921088409773
    typeable_string = input("Linha digitável: ")
    print(payslip.decode(re.sub(r"[^0-9]",'',typeable_string)))