// https://community.topcoder.com/stat?c=problem_statement&pm=11344
#include <algorithm>
using namespace std;
struct FractalPicture 
{
    double getLengthImpl(int mod, int x1, int y1, int x2, int y2)
    {
        // limit area to (-27,0) - (27,81) -> prevent overflow
        if (x1<-27) x1=-27;
        if (x2>27) x2=27;
        if (y1<0) y1=0;
        if (y2>81) y2=81;
        // segment (0,0) - (0,81)
        // maxarea (-27,0) - (27,81)
        if (x1<=-27 && x2>=27 && y1<=0 && y2>=81)
            return 54*mod + 81; //2/3L = 54
        if (x1>=27 || y2<=0 || y1>=81 || x2<=-27)
            return 0;
        double length = 0;
        if (mod > 0)
        {
            if (x1 <= 0 && x2 >= 0 && y1 <= 54 && y2>= 0)
                length += min(y2,54)-max(y1,0);
            x1 *= 3;y1 *= 3;x2 *= 3;y2 *= 3;
            int bias = 54*3;
            //left
            length += getLengthImpl(mod-1,y1-bias,-x2,y2-bias,-x1) / 3.0;
            //right
            length += getLengthImpl(mod-1,-y2+bias,x1,-y1+bias,x2) / 3.0;
            //up
            length += getLengthImpl(mod-1,x1,y1-bias,x2,y2-bias) / 3.0;
        }
        else
        {
            if (x1 <= 0 && x2 >= 0 && y1 <= 81 && y2>= 0)
                length += min(y2,81)-max(y1,0);
        }
        return length;
    }
    double getLength(int x1, int y1, int x2, int y2)
    {
        return getLengthImpl(499,x1,y1,x2,y2);
    }
};