#include<iostream>
#include<stack>
#include<memory.h>

using namespace std;
int graph[9][9];//define graph
int nodes = 8;//number of nodes

//深度优先搜索函数
void dfs(int root,int goal)
{
	stack<int>_stack;
	_stack.push(root);//push root node into stack
	while (!_stack.empty())
	{
		int cur = _stack.top();//pop nodes 
		_stack.pop();
		cout << cur << " ";
		if (cur == goal)break;//if the target, break
		for (int i = 1; i <= nodes; i++)//find neighbors push them
		{
			if (graph[cur][i] == 1)
				_stack.push(i);
		}
	}
}

//initialize the graph
void init_graph( int(&g)[9][9] )
{
	memset(graph, 0, sizeof(graph));
	graph[1][2] = 1;
	graph[1][6] = 1;
	graph[2][3] = 1;
	graph[6][7] = 1;
	graph[6][8] = 1;
	graph[3][4] = 1;
	graph[3][5] = 1;
}

int main()
{
	int root = 1;
	int goal;
	cin >> goal;
	init_graph(graph);
	dfs(root, goal);
	return 0;
}
