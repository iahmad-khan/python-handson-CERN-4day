import sys
if len(sys.argv) > 2 and sys.argv[2] == 'psyco':
    # psyco is a dynamic to-native-binary compiler for Python, which
    # works on the Intel-like processors
    try:
        import psyco
    except ImportError:
        raise SystemExit, "Cannot find the psyco module"
    else:
        psyco.full()

# Memoizer implementation using a class.
class memoize:

    def __init__ (self, callable):
        self.cache = {}
        self.callable = callable

    def __call__ (self, *args):
        try: return self.cache[args]
        except KeyError:
            return self.cache.setdefault(args, self.callable(*args))

        # Without using setdefault the except block might look like this:
            #val = self.callable(*args)
            #self.cache[args] = val
            #return val

# Alternative implementation using a closure:
def clmemoize(callable):
    cache = {}
    def proxy(*args):
        try: return cache[args]
        except KeyError: return cache.setdefault(args, callable(*args))
    return proxy



if __name__ == '__main__':

    # Instead of defining a fib function here, I could say
    # from fibonacci import fibr as fib
    # But this would make the trick of giving the proxy the same name
    # as the original function, not work ... so I define fib again.
    def fib(n):
        if n < 3:
            return 1
        return fib(n-1) + fib(n-2)

    import time

    # Give usage instructions to user, if necessary.
    try:
        N = int(sys.argv[1])
    except (IndexError, ValueError):
        print "You must pass an integer as a command-line argument." 
        print "(I'd start with something below 30)"
        raise SystemExit

    # A utility which allows us to perform timings
    def time_report(message1, message2, callable, *args):
        start = time.time()
        result = callable(*args)
        stop = time.time()
        print message1, 'took %10.7f seconds: %d - %s' % (stop - start, result, message2)
        return result

    # Keep a handle on the unmemoized verison
    unmemoized_fib = fib

    # Collect a sequence of tests into a single function
    def tester(the_memoizer):
        global fib
        # The original function
        time_report("     fib(N)", "Always slow",                 fib, N)

        # Meomize it and call it twice with the same argument
        memfib = the_memoizer(fib)
        time_report("  memfib(N)", "Slow first time",             memfib, N)
        time_report("  memfib(N)", "Fast second time",            memfib, N)

        # Now let the proxy have the same name as the original function
        fib = the_memoizer(fib)
        time_report("     fib(N)", "Fast the first time",         fib, N)
        time_report("     fib(N)", "Even faster the second time", fib, N)

    print "Test the class-based version:"
    tester(memoize)

    
    print "Test the closure-based version:"
    # Retrieve the unmemoized version
    fib = unmemoized_fib
    tester(clmemoize)

