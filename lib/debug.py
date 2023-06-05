#!/usr/bin/env python3

from customer import Customer, CONN, CURSOR
import ipdb


if __name__ == '__main__':
    Customer.get_all()
    ipdb.set_trace()
