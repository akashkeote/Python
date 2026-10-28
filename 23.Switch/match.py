num = 5;

match num:
    case 1:
        print("one");
    case 2:
        print("two");
    case 3:
        print("three");
    case _:
        print("other than 1,2,3");

num = 15;
match num % 3:
    case 0:
        print("divisible by 3");
    case 2:
        print("not divisible by 3");