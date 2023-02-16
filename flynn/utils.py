# coding: utf-8

import sys

def from_bytes(val, length, endianess):
	return int.from_bytes(val, length, endianess)

def to_bytes(val, length, endianess):
	return val.to_bytes(length, endianess)

