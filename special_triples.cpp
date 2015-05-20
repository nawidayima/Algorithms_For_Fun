#include <iostream>
#include <cmath>
#include <map>
using namespace std;

class TRIPLES{
    private:
        struct S{
            int first;
            int second;
            S(){
                first = 0;
                second = 0;
            }
        };
        map<int, S> map;
    public:
        void load(int end){
           int send = sqrt(end);
            for (int i = 0; i <= send; i++){
                for(int j = i; j <= send; j++){
                    if (map.count(i*i+j*j)) continue;
                    map[i*i+j*j].first = i;
                    map[i*i+j*j].second = j;
                }
            }
        }
        void reset(){
            for (auto it = map.begin(); it != map.end(); ++it){
                map.erase(it);
            }
        }
        void find(int start, int end){
            reset();
            load(end);
            for (auto it = map.begin(); it != map.end(); it++){
                int num = it->first;
                if (num > start && num < end){
                    if (map.count(num-1) && map.count(num+1)){
                        cout<<"("<<num-1<<", "<<num<<", "<<num+1;
                        cout<<") (equal to "<<map[num-1].first<<"^2+";
                        cout<<map[num-1].second<<"^2, "<<map[num].first;
                        cout<<"^2+"<<map[num].second<<"^2, ";
                        cout<<map[num+1].first<<"^2+"<<map[num+1].second;
                        cout<<"^2) is a solution.\n";
                    }
                }
            }
            return;
        }
};

int main(){
    TRIPLES triples;
    triples.find(1,10000);
    return 0;
}

// for ( auto local_it = mymap.begin(i); local_it!= mymap.end(i); ++local_it )
//       std::cout << " " << local_it->first << ":" << local_it->second;
//           std::cout << std::endl;
//             }
