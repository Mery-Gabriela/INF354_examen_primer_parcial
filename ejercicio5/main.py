from kanren import Relation, facts, var, lall, run

def main():
    padres = Relation()
    facts(padres, ("Jose", "Ada"),
                ("Mery", "Ada"),
                ("Marco", "Luciana"),
               ("Florentino", "Mery"),
               ("Manuel",  "Jose"))
    abuelos = Relation()
    facts(abuelos, ("Manuel", "Ada"),
                    ("Manuel", "Luciana"),
                    ("Florentino", "Ada"))
    tios = Relation()
    facts(tios, ("Limber", "Ada"),
                ("Jose", "Luciana"),
                ("Marco", "Ada"),
                ("Jorge", "Ada"))
    primos = Relation()
    facts(primos, ("Ada", "Luciana"))
    hijos = Relation()
    facts(hijos, ("Jose", "Manuel"),
                ("Marco", "Manuel"),
                ("Mery", "Florentino"),
                ("Limber", "Florentino"),
                ("Ada", "Jose"),
                ("Ada", "Mery"),
                ("Luciana", "Marco")
        )
    x = var()
    print("Ada es hija de...")
    print(run(0, x, hijos("Ada", x )))
    print("Ada es prima de...")
    print(run(0, x, primos("Ada", x )))
    print("Ada es sobrina de...")
    print(run(0, x, tios(x, "Ada" )))
    print("Ada es nieta de...")
    print(run(0, x, abuelos(x, "Ada" )))

if __name__ == "__main__":
    main()
