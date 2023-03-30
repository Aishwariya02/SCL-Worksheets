#include<windows.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include<math.h>
#include <stdlib.h>
#include<vector>
#include<iostream>
using namespace std;


/* GLUT callback Handlers */

void init()
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0,640,0,480);
    glClearColor(0,0,0,0.5);
}

struct Point{
    int x;
    int y;
};

int iter = 0;
Point p[4];
vector<Point> pts;


static void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glClearColor(0,0,0,1);
    glFlush();
}


void Bezier()
{
    double xt=0.0,yt=0.0,t=0.1;
    vector<Point> pts;
    while(t < 1)
    {
        Point pt;
        xt=pow((1-t),3)*p[0].x + 3*(pow((1-t),2))*t*p[1].x+3*(1-t)*pow(t,2)*p[2].x+pow(t,3)*p[3].x;
        yt=pow((1-t),3)*p[0].y + 3*(pow((1-t),2))*t*p[1].y+3*(1-t)*pow(t,2)*p[2].y+pow(t,3)*p[3].y;
        pt.x=xt;
        pt.y=yt;
        pts.push_back(pt);
        t+=0.1;
    }
    glBegin(GL_LINE_STRIP);
    for(int i = 0; i < pts.size() ; i++)
    {
        glVertex2d(pts[i].x,pts[i].y);
    }
    glEnd();
    glFlush();

}

void mouse(int button,int state, int x,int y)
{
    if(button==GLUT_LEFT_BUTTON && state == GLUT_DOWN && iter < 4)
    {
        Point P1;
        P1.x = x;
        P1.y = 480-y;
        p[iter] = P1;
        cout<<P1.x<<","<<P1.y<<endl;
        glColor3d(1,1,1);
        glPointSize(2);
        glBegin(GL_POINTS);
            glVertex2f(P1.x,P1.y);
        glEnd();
        iter++;
    }
    else if(button== GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        Bezier();
        iter = 0;
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

    glutCreateWindow("Bezier Curve");
    init();
    glutMouseFunc(mouse);

    glutDisplayFunc(display);
    glClearColor(0,0,0,1);

    glutMainLoop();

    return EXIT_SUCCESS;
}
