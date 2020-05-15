#include<iostream>
#include<vector>
#include<algorithm>
using std::pair;
using std::vector;
using std::string;
using std::cout;

#define ROW 4
#define COULMN 4

// 1 if locked or visited 0 else
bool IsLocked(int grid[ROW][COULMN], int X_point, int Y_point)
{
    return grid[X_point][Y_point] == 1 | grid[X_point][Y_point] == -1;
}
// check if point is valid or not 
bool IsValid(int x_point, int Y_point)
{
    return x_point >= 0 && x_point < COULMN&& Y_point >= 0 && Y_point < ROW;
}
// cal Gvalue it's a cost form start point to current point
int GvalueCal(pair<int, int> startpoint, pair<int, int> currntpoint)
{
    return abs(startpoint.first - currntpoint.first) +
        abs(startpoint.second - currntpoint.second);
}
// heuristic function it's give me estimated value cost for current point to target point
// heuristic by manhattan distance method
int M_HeuristicValue(pair<int, int> currntpoint, pair<int, int> targentpoint)
{
    return abs(targentpoint.first - currntpoint.first) +
        abs(targentpoint.second - currntpoint.second);
}
int EvaluationFunction(int GVAlue, pair<int, int> startpoint, pair<int, int> currntpoint, pair<int, int> targentpoint)
{
    return /*GvalueCal(startpoint, currntpoint)*/ GVAlue +
        M_HeuristicValue(currntpoint, targentpoint);
}
bool IsTarget(pair<int, int> current, pair<int, int> target)
{
    return current.first == target.first && current.second == target.second;
}
// vector<pair<int,int>>
vector<pair<int, int>> a_StarAlgoritm(int grid[ROW][COULMN], pair<int, int> Source, pair<int, int> distantion)
{
    int Gvalue = 0;
    vector<pair<int, int>> FinalPath;
    if (!IsValid(Source.first, Source.second))
        return FinalPath;
    if (!IsValid(distantion.first, distantion.second))
        return FinalPath;
    if (IsLocked(grid, Source.first, Source.second))
        return FinalPath;
    if (IsLocked(grid, distantion.first, distantion.second))
        return FinalPath;
    // each successor by manhatten distance for 4 directions
                            /*
                                    |
                           <---   Point   --->
                                    |
                                    v
                            */

    FinalPath.push_back(Source);
    auto currentpoint = Source;

    while (currentpoint != distantion)
    {
        vector<pair<string, pair<int, int>>> temp;
        // pair<int,int>max_point=std::make_pair(-1,-1);
        // above 
        if (IsValid(currentpoint.first - 1, currentpoint.second) && !IsLocked(grid, currentpoint.first - 1, currentpoint.second))
        {
            temp.push_back(std::make_pair("above", std::make_pair(currentpoint.first - 1, currentpoint.second)));
        }
        // down
        if (IsValid(currentpoint.first + 1, currentpoint.second) && !IsLocked(grid, currentpoint.first + 1, currentpoint.second))
        {
            temp.push_back(std::make_pair("down", std::make_pair(currentpoint.first + 1, currentpoint.second)));
        }
        // left 
        if (IsValid(currentpoint.first, currentpoint.second - 1) && !IsLocked(grid, currentpoint.first, currentpoint.second - 1))
        {
            temp.push_back(std::make_pair("left", std::make_pair(currentpoint.first, currentpoint.second - 1)));
        }
        // right
        if (IsValid(currentpoint.first, currentpoint.second + 1) && !IsLocked(grid, currentpoint.first, currentpoint.second + 1))
        {
            temp.push_back(std::make_pair("right", std::make_pair(currentpoint.first, currentpoint.second + 1)));
        }
        // auto max = std::max(temp.begin(),temp.end(),[Source,distantion](pair<string,pair<int,int>> x,pair<string,pair<int,int>> y)
        // {
        //     return  EvaluationFunction(Source,x.second,distantion) > EvaluationFunction(Source,y.second,distantion); 
        // });
        // auto mx = std::max(temp.begin(),temp.end());
        pair<string, pair<int, int>> max = *std::max_element(temp.begin(), temp.end(), [Gvalue, Source, distantion](pair<string, pair<int, int>> x, pair<string, pair<int, int>> y)
            {
                return  EvaluationFunction(Gvalue + 1, Source, x.second, distantion) > EvaluationFunction(Gvalue + 1, Source, y.second, distantion);
            });
        cout << max.first << " ";
        Gvalue++;
        FinalPath.push_back(max.second);
        grid[currentpoint.first][currentpoint.second] = -1; // visited 
        currentpoint = max.second;
        if (IsTarget(currentpoint, distantion))
            FinalPath.push_back(currentpoint);
    }
    return FinalPath;
}

struct printvec
{
    template<class T>
    friend std::ostream& operator<<(std::ostream& out, vector<T> v)
    {
        for (auto a : v)
            out << a << " ";
        return out;
    }
};

static std::ostream& operator<<(std::ostream& out, pair<int, int> val)
{
    out << "(" << val.first << "," << val.second << ")";
    return out;
}
int main()
{
    pair<int, int> startpoint = std::make_pair(2,2);
    pair<int, int> target = std::make_pair(3, 3);

    int grid[ROW][COULMN] = {
        {0,1,0,0},
        {0,1,0,0},
        {0,0,0,0},
        {0,1,0,0},
    };
    auto path = a_StarAlgoritm(grid, startpoint, target);
    cout << "\n";
    for (auto p : path)
        cout << "->" << p;
}