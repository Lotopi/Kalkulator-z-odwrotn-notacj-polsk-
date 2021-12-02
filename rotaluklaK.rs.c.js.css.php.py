print("Witaj świecie !")

f = open("rotaluklaK.rs.c.js.css.php.py", "a")
f.write(" 2")
f.close()

f = open("rotaluklaK.rs.c.js.css.php.py", "r")
lines=f.readlines()
print(lines[-1][1:])
#