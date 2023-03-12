#include<windows.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include <iostream>
#include <stdlib.h>
#include<vector>
using namespace std;

vector<pair<int,int> > clippingWindow; //clipping window
vector<pair<int,int> > points; //polygon points
vector<pair<int,int> > clippedPoints; //left clipper points
vector<pair<int,int> > rightClippedPoints; //right clipper points
vector<pair<int,int> > bottomClippedPoints; //bottom clipper points
vector<pair<int,int> > topClippedPoints; //top clipper points


void init(void){
    glClearColor(1,1,1,0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0,640.0,0.0,480.0);
}

void drawPolygon(void){
    glColor3f(0.0,1.0,0.0);
    glLineWidth(3.0);
    glBegin(GL_LINES);
    for(int i=0;i<points.size()-1;i++){
        glVertex2i(points[i].first,points[i].second);
        glVertex2i(points[i+1].first,points[i+1].second);
    }
    glEnd();
    glFlush();
}


/*void drawPolygonFinal(void){
    glColor3f(0.0,1.0,0.0);
    glLineWidth(3.0);
    glBegin(GL_LINES);
    for(int i=0;i<points.size()-1;i++){
        glVertex2i(points[i].first,points[i].second);
        glVertex2i(points[i+1].first,points[i+1].second);
    }
    int temp = points.size()-1;
    glVertex2i(points[temp].first,points[temp].second);
    glVertex2i(points[0].first,points[0].second);
    glEnd();
    glFlush();
}*/


void drawClippingWindow(void){
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0,0.0,0.0);
    glLineWidth(4.0);
    glBegin(GL_LINES);
    glVertex2i(clippingWindow[0].first,clippingWindow[0].second);
    glVertex2i(clippingWindow[1].first,clippingWindow[0].second);
    glVertex2i(clippingWindow[1].first,clippingWindow[0].second);
    glVertex2i(clippingWindow[1].first,clippingWindow[1].second);
    glVertex2i(clippingWindow[1].first,clippingWindow[1].second);
    glVertex2i(clippingWindow[0].first,clippingWindow[1].second);
    glVertex2i(clippingWindow[0].first,clippingWindow[1].second);
    glVertex2i(clippingWindow[0].first,clippingWindow[0].second);
    glEnd();
    glFlush();
}

/*void drawPolygon(void){
    glColor3f(0.0,1.0,0.0);
    glBegin(GL_POLYGON);
    for(int i=0;i<points.size()-1;i++){
        glVertex2i(points[i].first,points[i].second);
        glVertex2i(points[i+1].first,points[i+1].second);
    }
    glEnd();
    glFlush();
}*/

void drawFinalPolygon(void){
    glColor3f(0.0,0.0,1.0);
    glBegin(GL_POLYGON);
    for(int i=0;i<topClippedPoints.size()-1;i++){
        glVertex2i(topClippedPoints[i].first,topClippedPoints[i].second);
        glVertex2i(topClippedPoints[i+1].first,topClippedPoints[i+1].second);
    }
    glEnd();
    glFlush();
}


void topClipper(void){
    for(int i=0;i<bottomClippedPoints.size()-1;i++){
        cout<<"\nIn top clipper: "<<endl;
        cout<<bottomClippedPoints[i].first<<" "<<bottomClippedPoints[i].second<<","<<bottomClippedPoints[i+1].first<<" "<<bottomClippedPoints[i+1].second;
        //in-in
        if(bottomClippedPoints[i].second < clippingWindow[1].second && bottomClippedPoints[i+1].second < clippingWindow[1].second){
            pair<int,int> temp;
            temp.first = bottomClippedPoints[i+1].first;
            temp.second = bottomClippedPoints[i+1].second;
            topClippedPoints.push_back(temp);
        }
        //in-out
        else if(bottomClippedPoints[i].second < clippingWindow[1].second && bottomClippedPoints[i+1].second > clippingWindow[1].second){
            float m = float(bottomClippedPoints[i+1].second - bottomClippedPoints[i].second)/float(bottomClippedPoints[i+1].first - bottomClippedPoints[i].first);
            float y = float(clippingWindow[1].second);
            int x = int(float(y-bottomClippedPoints[i].second)/m+bottomClippedPoints[i].second);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            topClippedPoints.push_back(temp);
        }
        //out-in
        else if(bottomClippedPoints[i].second > clippingWindow[1].second &&bottomClippedPoints[i+1].second < clippingWindow[1].second){
            float m = float(bottomClippedPoints[i+1].second - bottomClippedPoints[i].second)/float(bottomClippedPoints[i+1].first -bottomClippedPoints[i].first);
            float y = float(clippingWindow[1].second);
            int x = int(float(y-bottomClippedPoints[i].second)/m+bottomClippedPoints[i].second);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            topClippedPoints.push_back(temp);
            temp.first = bottomClippedPoints[i+1].first;
            temp.second =bottomClippedPoints[i+1].second;
            topClippedPoints.push_back(temp);
        }
    }
    int s =bottomClippedPoints.size()-1;
    cout<<"\nIn top clipper: "<<endl;
    cout<<bottomClippedPoints[s].first<<" "<<bottomClippedPoints[s].second<<","<<bottomClippedPoints[0].first<<" "<<bottomClippedPoints[0].second;
    //in-in
        if(bottomClippedPoints[s].second < clippingWindow[1].second && bottomClippedPoints[0].second < clippingWindow[1].second){
            pair<int,int> temp;
            temp.first = bottomClippedPoints[0].first;
            temp.second = bottomClippedPoints[0].second;
            topClippedPoints.push_back(temp);
        }
        //in-out
        else if(bottomClippedPoints[s].second < clippingWindow[1].second && bottomClippedPoints[0].second > clippingWindow[1].second){
            float m = float(bottomClippedPoints[0].second - bottomClippedPoints[s].second)/float(bottomClippedPoints[0].first - bottomClippedPoints[s].first);
            float y = float(clippingWindow[1].second);
            int x = int(float(y-bottomClippedPoints[s].second)/m+bottomClippedPoints[s].first);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            topClippedPoints.push_back(temp);
        }
        //out-in
        else if(bottomClippedPoints[s].second > clippingWindow[1].second &&bottomClippedPoints[0].second < clippingWindow[1].second){
            float m = float(bottomClippedPoints[0].second - bottomClippedPoints[s].second)/float(bottomClippedPoints[0].first - bottomClippedPoints[s].first);
            float y = float(clippingWindow[1].second);
            int x = int(float(y-bottomClippedPoints[s].second)/m+bottomClippedPoints[s].first);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            topClippedPoints.push_back(temp);
            temp.first = bottomClippedPoints[0].first;
            temp.second =bottomClippedPoints[0].second;
            topClippedPoints.push_back(temp);
        }
    cout<<"\nTop clipper: "<<endl;
    for(int i=0;i<topClippedPoints.size();i++){
        cout<<topClippedPoints[i].first<<" "<<topClippedPoints[i].second<<endl;
    }
}

void bottomClipper(void){
    for(int i=0;i<rightClippedPoints.size()-1;i++){
        cout<<"\nIn bottom clipper: "<<endl;
        cout<<rightClippedPoints[i].first<<" "<<rightClippedPoints[i].second<<","<<rightClippedPoints[i+1].first<<" "<<rightClippedPoints[i+1].second;
        //in-in
        if(rightClippedPoints[i].second > clippingWindow[0].second && rightClippedPoints[i+1].second > clippingWindow[0].second){
            pair<int,int> temp;
            temp.first = rightClippedPoints[i+1].first;
            temp.second = rightClippedPoints[i+1].second;
            bottomClippedPoints.push_back(temp);
        }
        //in-out
        else if(rightClippedPoints[i].second > clippingWindow[0].second && rightClippedPoints[i+1].second < clippingWindow[0].second){
            float m = float(rightClippedPoints[i+1].second - rightClippedPoints[i].second)/float(rightClippedPoints[i+1].first - rightClippedPoints[i].first);
            float y = float(clippingWindow[0].second);
            int x = int(float(y-rightClippedPoints[i].second)/m+rightClippedPoints[i].first);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            bottomClippedPoints.push_back(temp);
        }
        //out-in
        else if(rightClippedPoints[i].second < clippingWindow[0].second &&rightClippedPoints[i+1].second > clippingWindow[0].second){
            float m = float(rightClippedPoints[i+1].second - rightClippedPoints[i].second)/float(rightClippedPoints[i+1].first -rightClippedPoints[i].first);
            float y = float(clippingWindow[0].second);
            int x = int(float(y-rightClippedPoints[i].second)/m+rightClippedPoints[i].first);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            bottomClippedPoints.push_back(temp);
            temp.first = rightClippedPoints[i+1].first;
            temp.second =rightClippedPoints[i+1].second;
            bottomClippedPoints.push_back(temp);
        }
    }
    int s = rightClippedPoints.size()-1;
    cout<<"\nIn bottom clipper: "<<endl;
    cout<<rightClippedPoints[s].first<<" "<<rightClippedPoints[s].second<<","<<rightClippedPoints[0].first<<" "<<rightClippedPoints[0].second;
    //in-in
        if(rightClippedPoints[s].second > clippingWindow[0].second && rightClippedPoints[0].second > clippingWindow[0].second){
            pair<int,int> temp;
            temp.first = rightClippedPoints[0].first;
            temp.second = rightClippedPoints[0].second;
            bottomClippedPoints.push_back(temp);
        }
        //in-out
        else if(rightClippedPoints[s].second > clippingWindow[0].second && rightClippedPoints[0].second < clippingWindow[0].second){
            float m = float(rightClippedPoints[0].second - rightClippedPoints[s].second)/float(rightClippedPoints[0].first - rightClippedPoints[s].first);
            float y = float(clippingWindow[0].second);
            int x = int(float(y-rightClippedPoints[s].second)/m+rightClippedPoints[s].second);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            bottomClippedPoints.push_back(temp);
        }
        //out-in
        else if(rightClippedPoints[s].second < clippingWindow[0].second &&rightClippedPoints[0].second > clippingWindow[0].second){
            float m = float(rightClippedPoints[0].second - rightClippedPoints[s].second)/float(rightClippedPoints[0].first - rightClippedPoints[s].first);
            float y = float(clippingWindow[0].second);
            int x = int(float(y-rightClippedPoints[s].second)/m+rightClippedPoints[s].second);
            pair<int,int> temp;
            temp.first = x;
            temp.second = int(y);
            bottomClippedPoints.push_back(temp);
            temp.first = rightClippedPoints[0].first;
            temp.second =rightClippedPoints[0].second;
            bottomClippedPoints.push_back(temp);
        }
    cout<<"\nBottom clipper: "<<endl;
    for(int i=0;i<bottomClippedPoints.size();i++){
        cout<<bottomClippedPoints[i].first<<" "<<bottomClippedPoints[i].second<<endl;
    }
}

void rightClipper(void){
    for(int i=0;i<clippedPoints.size()-1;i++){
        cout<<"\nIn right clipper: "<<endl;
        cout<<clippedPoints[i].first<<" "<<clippedPoints[i].second<<","<<clippedPoints[i+1].first<<" "<<clippedPoints[i+1].second;
        //in-in
        if(clippedPoints[i].first < clippingWindow[1].first && clippedPoints[i+1].first < clippingWindow[1].first){
            pair<int,int> temp;
            temp.first = clippedPoints[i+1].first;
            temp.second = clippedPoints[i+1].second;
            rightClippedPoints.push_back(temp);
        }
        //in-out
        else if(clippedPoints[i].first < clippingWindow[1].first && clippedPoints[i+1].first > clippingWindow[1].first){
            float m = float(clippedPoints[i+1].second - clippedPoints[i].second)/float(clippedPoints[i+1].first - clippedPoints[i].first);
            float x = float(clippingWindow[1].first);
            int y = int(m*(x - float(clippedPoints[i].first))+float(clippedPoints[i].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            rightClippedPoints.push_back(temp);
        }
        //out-in
        else if(clippedPoints[i].first > clippingWindow[1].first &&clippedPoints[i+1].first < clippingWindow[1].first){
            float m = float(clippedPoints[i+1].second - clippedPoints[i].second)/float(clippedPoints[i+1].first - clippedPoints[i].first);
            float x = float(clippingWindow[1].first);
            int y = int(m*(x - float(clippedPoints[i].first))+float(clippedPoints[i].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            rightClippedPoints.push_back(temp);
            temp.first = clippedPoints[i+1].first;
            temp.second =clippedPoints[i+1].second;
            rightClippedPoints.push_back(temp);
        }
    }
    int s = clippedPoints.size()-1;
    cout<<"\nIn right clipper: "<<endl;
    cout<<clippedPoints[s].first<<" "<<clippedPoints[s].second<<","<<clippedPoints[0].first<<" "<<clippedPoints[0].second;
    //in-in
        if(clippedPoints[s].first < clippingWindow[1].first && clippedPoints[0].first < clippingWindow[1].first){
            pair<int,int> temp;
            temp.first = clippedPoints[0].first;
            temp.second = clippedPoints[0].second;
            rightClippedPoints.push_back(temp);
        }
        //in-out
        else if(clippedPoints[s].first < clippingWindow[1].first && clippedPoints[0].first > clippingWindow[1].first){
            float m = float(clippedPoints[0].second - clippedPoints[s].second)/float(clippedPoints[0].first - clippedPoints[s].first);
            float x = float(clippingWindow[1].first);
            int y = int(m*(x - float(clippedPoints[s].first))+float(clippedPoints[s].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            rightClippedPoints.push_back(temp);
        }
        //out-in
        else if(clippedPoints[s].first > clippingWindow[1].first &&clippedPoints[0].first < clippingWindow[1].first){
            float m = float(clippedPoints[0].second - clippedPoints[s].second)/float(clippedPoints[0].first - clippedPoints[s].first);
            float x = float(clippingWindow[1].first);
            int y = int(m*(x - float(clippedPoints[s].first))+float(clippedPoints[s].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            rightClippedPoints.push_back(temp);
            temp.first = clippedPoints[0].first;
            temp.second =clippedPoints[0].second;
            rightClippedPoints.push_back(temp);
        }
    cout<<"\nRight clipper: "<<endl;
    for(int i=0;i<rightClippedPoints.size();i++){
        cout<<rightClippedPoints[i].first<<" "<<rightClippedPoints[i].second<<endl;
    }
}

void leftClipper(void){
    for(int i=0;i<points.size()-1;i++){
        cout<<"\nIn left clipper: "<<endl;
        cout<<points[i].first<<" "<<points[i].second<<","<<points[i+1].first<<" "<<points[i+1].second;
        //in-in
        if(points[i].first > clippingWindow[0].first && points[i+1].first > clippingWindow[0].first){
            pair<int,int> temp;
            temp.first = points[i+1].first;
            temp.second = points[i+1].second;
            clippedPoints.push_back(temp);
        }
        //in-out
        else if(points[i].first > clippingWindow[0].first && points[i+1].first < clippingWindow[0].first){
            float m = float(points[i+1].second - points[i].second)/float(points[i+1].first - points[i].first);
            float x = float(clippingWindow[0].first);
            int y = int(m*(x - float(points[i].first))+float(points[i].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            clippedPoints.push_back(temp);
        }
        //out-in
        else if(points[i].first < clippingWindow[0].first && points[i+1].first > clippingWindow[0].first){
            float m = float(points[i+1].second - points[i].second)/float(points[i+1].first - points[i].first);
            float x = float(clippingWindow[0].first);
            int y = int(m*(x - float(points[i].first))+float(points[i].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            clippedPoints.push_back(temp);
            temp.first = points[i+1].first;
            temp.second = points[i+1].second;
            clippedPoints.push_back(temp);
        }
    }
    int s = points.size()-1;
    cout<<"\nIn left clipper: "<<endl;
    cout<<points[s].first<<" "<<points[s].second<<","<<points[0].first<<" "<<points[0].second;
    if(points[s].first > clippingWindow[0].first && points[0].first > clippingWindow[0].first){
            pair<int,int> temp;
            temp.first = points[0].first;
            temp.second = points[0].second;
            clippedPoints.push_back(temp);
        }
        else if(points[s].first > clippingWindow[0].first && points[0].first < clippingWindow[0].first){
            float m = float(points[0].second - points[s].second)/float(points[0].first - points[s].first);
            float x = float(clippingWindow[0].first);
            int y = int(m*(x - float(points[s].first))+float(points[s].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            clippedPoints.push_back(temp);
        }
        else if(points[s].first < clippingWindow[0].first && points[0].first > clippingWindow[0].first){
            float m = float(points[0].second - points[s].second)/float(points[0].first - points[s].first);
            float x = float(clippingWindow[0].first);
            int y = int(m*(x - float(points[s].first))+float(points[s].second));
            pair<int,int> temp;
            temp.first = int(x);
            temp.second = y;
            clippedPoints.push_back(temp);
            temp.first = points[0].first;
            temp.second = points[0].second;
            clippedPoints.push_back(temp);
        }
    cout<<"\nLeft clipper: "<<endl;
    for(int i=0;i<clippedPoints.size();i++){
        cout<<clippedPoints[i].first<<" "<<clippedPoints[i].second<<endl;
    }
}

void drawPoly(void){
    glColor3f(0.0,1.0,0.0);
    glBegin(GL_POLYGON);
    for(int i=0;i<points.size();i++){
        glVertex2i(points[i].first,points[i].second);
    }
    glEnd();
    glFlush();
}

void clipPolygon(void){
    cout<<"Points: "<<endl;
    for(int i=0;i<points.size();i++){
        cout<<points[i].first<<" "<<points[i].second<<endl;
    }
    leftClipper();
    rightClipper();
    bottomClipper();
    topClipper();
    glFlush();
}


void display(void){
    glClear(GL_COLOR_BUFFER_BIT);
}

static void key(unsigned char keyVal,int x,int y){
    if(keyVal == 'c'){
        drawClippingWindow();
        clipPolygon();
        drawFinalPolygon();
    }
    glFlush();
}

void mouse(int button,int state,int x,int y){
    int windowHeight = glutGet(GLUT_WINDOW_HEIGHT);
    int wx = x;
    int wy = windowHeight - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && clippingWindow.size()<2){
        pair<int,int> temp;
        temp.first = wx;
        temp.second = wy;
        clippingWindow.push_back(temp);
    }
    if(clippingWindow.size()==2){
        drawClippingWindow();
        clippingWindow.push_back({0,0});
    }
    else if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && clippingWindow.size()==3){
        pair<int,int> temp;
        temp.first = wx;
        temp.second = wy;
        points.push_back(temp);
        drawPolygon();
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN ){
        drawPoly();
    }
    glFlush();
}

/* Program entry point */

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(10,10);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

    glutCreateWindow("Polygon Clipping");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(mouse);
    glutKeyboardFunc(key);
    glutMainLoop();

    return EXIT_SUCCESS;
}
