import sys
input = sys.stdin.readline

site_pw = {}
n, m = map(int, input().split())
for i in range(n):
    site, pw = input().split()
    site_pw[site] = pw
for i in range(m):
    site = input().strip()
    print(site_pw[site])