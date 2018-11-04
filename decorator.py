import time, random

def timer( function):
    print(function.__name__)
    def wrapper_timer( *args, **kwargs):
        print(args, kwargs, function.__name__)
        start_ts = time.time()
        result = function( *args, **kwargs)
        end_ts = time.time()
        print("time of blabla '{}' is {} ms."\
              .format(function.__name__, (end_ts-start_ts)* 1000))
        return result
    return wrapper_timer

def sleeper_(function):
    print('hello')
    def sleeper(from_, to_):
        print(function.__name__, 'hello2')
        def wrapper_sleeper(*args, **kwargs):
            print('sleeper', args, kwargs)
            print(function.__name__)
            time.sleep(random.randint( from_, to_))
            result = function(*args, **kwargs)
            print('a')
            return result
        return wrapper_sleeper
    return sleeper(1, 3)

@sleeper_
@timer
def foo(a, b):
    print('Call')
    return a + b

if __name__ == "__main__":
    print( foo(b=10, a=5))
