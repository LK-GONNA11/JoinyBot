import os as O, time as T, selenium.webdriver as W
from selenium.webdriver.common.by import By as B
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.chrome.service import Service as S
from selenium.webdriver.firefox.service import Service as F
from selenium.webdriver.chrome.options import Options as C
from selenium.webdriver.firefox.options import Options as G

def C0(): O.system("cls" if O.name == "nt" else "clear")
def S0(): print("\n" + "="*50 + "\n")
C0()
S0()
z = input("Choose browser (1=Chrome, 2=Firefox): ")
if z == '1':
 r = C(); r.add_argument("--start-maximized")
 p, D = "chromedriver", W.Chrome(service=S(p), options=r)
elif z == '2':
 r = G(); r.add_argument("--start-maximized")
 p, D = "geckodriver", W.Firefox(service=F(p), options=r)
else: exit()
S0()
D.get("https://discord.com/login")
input("Login, then Enter...")
S0()
D.get("https://disboard.org/servers")
k = input("Keyword: ")
D.find_element(B.NAME, "q").send_keys(k + K.RETURN)
T.sleep(5)
b = D.find_elements(B.CLASS_NAME, "btn-join")
print(f"{len(b)} servers found. Joining 3...\n")
for x in b[:3]:
 try: x.click(); T.sleep(3)
 except: pass
S0()
m = input("Message: ")
c = int(input("How many times?: "))
d = float(input("Delay (s): "))
S0()
print("Spamming...\n")
for i in range(c):
 try:
  t = D.find_element(B.TAG_NAME, "textarea")
  t.send_keys(m + K.RETURN)
  print(f"[{i+1}/{c}] Sent.")
  T.sleep(d)
 except: break
S0()
print("Done.")
