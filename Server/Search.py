def search(onlinejudge, problem, index = 0):
    code = '''
	#include <cstdio>
	int main()
	{
		int a, b;
		while (~scanf("%d%d", &a, &b))
			printf("%d\\n", a + b);
		return 0;
	}
	'''
    return code