#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def main():
    print(os.getenv("DATABASE_URL"))


if __name__ == '__main__':
    main()