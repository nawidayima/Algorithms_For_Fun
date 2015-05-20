#include <iostream>
#include <map>
#include <cmath>
#include <thread>
using namespace std;

struct C{
            bool c1;
            bool c2;
            bool c3;
            bool c4;
            C(){
                c1 = false;
                c2 = false;
                c3 = false;
                c4 = false;
            }
};

map<int, C> dict;

void C1(int mex, int LIMIT){
    //Cond1
    for (int a = 1; a < mex; a++){
        for (int b = 1; b <= a; b++){
            int n = a*a + b*b;
            if (!dict.count(n)){
                if (n <= LIMIT) dict[n].c1 = true;
            }
        }
    }
} 

void C2(int mex, int bmex2, int LIMIT){
    //Cond2
    for (int a = 1; a < mex; a++){
        for (int b = 1; b < bmex2; b++){
            int n = a*a + 2*b*b;
            if (n <= LIMIT) dict[n].c2 = true;
        }
    }
}

void C3(int mex, int bmex3, int LIMIT){
    //Cond3
    for (int a = 1; a < mex; a++){
        for (int b = 1; b < bmex3; b++){
            int n = a*a + 3*b*b;
            if (n <= LIMIT) dict[n].c3 = true;
        }
    }
}

void C4(int mex, int bmex4, int LIMIT){
    //Cond4
    for (int a = 1; a < mex; a++){
        for (int b = 1; b < bmex4; b++){
            int n = a*a + 7*b*b;
            if (n <= LIMIT) dict[n].c4 = true;
        }
    }
}

class PE229{
    private:
    public:
            int solution(int LIMIT){
                int mex = sqrt(LIMIT);
                int bmex2 = sqrt(LIMIT/2);
                int bmex3 = sqrt(LIMIT/3);
                int bmex4 = sqrt(LIMIT/7);
 
                thread t1(C1, mex, LIMIT);
                t1.join();
                thread t2(C2, mex, bmex2, LIMIT);
                thread t3(C3, mex, bmex3, LIMIT);
                thread t4(C4, mex, bmex4, LIMIT);
                t2.join();
                t3.join();
                t4.join();
                
                //std::thread t1(std::bind(&Threaded_Class::init,this));

//                C1(mex, LIMIT);
//                C2(mex, bmex2, LIMIT);
//                C3(mex, bmex3, LIMIT);
//                C4(mex, bmex4, LIMIT);
                //Count instances
                int count = 0;
                for (auto it = dict.begin(); it != dict.end(); it++){
                    if (it->second.c1 && it->second.c2 && it->second.c3 && it->second.c4){
                        count++;
                    }
                }

                return count;
            }
};


int main(int argc, char** argv){
    if (argc != 2){
        cerr << "please give an argument for the maximum number\n";
        exit(1);
    }
    
    PE229 problem;

    cout << "There are " << problem.solution(atoi(argv[1])) << " such numbers that";
    cout << " do not exceed " << argv[1] << endl;
    return 0;
}
