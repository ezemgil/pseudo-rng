from LinearCongruentialMethod import LinearCongruentialMethod
from MultiplicativeCongruentialMethod import MultiplicativeCongruentialMethod

def main():
    lcm = LinearCongruentialMethod(seed=0, a=0, m=0, c=0)
    lcm.execute()

    print("\n" + "="*50 + "\n")

    mcm = MultiplicativeCongruentialMethod(seed=0, a=0, m=0)
    mcm.execute()

if __name__ == '__main__':
    main()