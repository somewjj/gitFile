#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

def calcu(salary):
	salary_rate = calcu_salary_rate(salary)
	print(salary_rate)

	if salary_rate < 1500:
		return salary_rate * 0.03 - 0
	elif salary_rate < 4500:
		return salary_rate * 0.1 - 105
	elif salary_rate < 9000:
		return salary_rate * 0.2 - 555
	elif salary_rate < 35000:
		return salary_rate * 0.25 - 1005
	elif salary_rate < 55000:
		return salary_rate * 0.3 - 2755
	elif salary_rate < 80000:
		return salary_rate * 0.35 - 5505
	else:
		return salary_rate * 0.45 - 13505

def calcu_salary_rate(salary):
	return salary *(1 - (0.08 + 0.02 + 0.005 + 0.06)) -3500
	
def dump_data():
	salary_dict = {}

	if len(sys.argv) < 2:
		print("Parameter Error")
	else:
		try:
			source_salary = sys.argv[1:]
		except:
			print("Parameter Error")

	for index, item in enumerate(source_salary):
		if len(item.split(":")) != 2:
			print("number {0} is wrong.".format(index))
			continue
		else:
			key,value = item.split(":")
			salary_dict[key] = value
	print(salary_dict)
	return salary_dict

if __name__ == "__main__":
	salary_dict = dump_data()
	if salary_dict is not None:
		for number, salary in salary_dict.items():
			rate = calcu(float(salary))
			print("{0} : {1}".format(number, rate))
	else:
		print("Parameter Error")
	
