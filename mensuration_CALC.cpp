//calculating surface area and volume.
#include<iostream>
#include<math.h>
#include<conio.h>
#include<string>
#include<stdlib.h>
#include<windows.h>
using namespace std;
double pi=3.14159;

/* function definition for setting cursor position in the console window */
void gotoxy(int x, int y)
{
    COORD coord;
    coord.X=x;
    coord.Y=y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//3D shapes

class area_volume{
	public:
		//cube operations
		void area_vol(double l)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of cube : "<<6*l*l<<endl;
			cout<<"\t\t\t\tvolume of the cube : "<<l*l*l;
		}
		//cuboid operations
		void area_vol(double l, double b, double h)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of cuboid : "<<2*(l*b+b*h+h*l)<<endl;
			cout<<"\t\t\t\tvolume of the cuboid : "<<l*b*h;
		}
		//cylinder operations
		void area_vol(double r,double h)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of cylinder : "<<(2*pi*r*h)+(2*pi*r*r)<<endl;
			cout<<"\t\t\t\tvolume of the cylinder : "<<pi*r*r*h;
		}
		//frustum of a cone
		void area_vol(double r, double R, double h, double s)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface are of frustum of cone : "<<pi*s*(R+r)+pi*r*r+pi*R*R<<endl;
			cout<<"\t\t\t\tvolume of frustum of cone : "<<(pi/3)*(r*r+r*R+R*R)*h;
		}
		//In following method another name is used
		//cone operations
		void area_vol2(double r, double h)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of cone : "<<(pi*r*(sqrt(r*r+h*h)))+pi*r*r<<endl;
			cout<<"\t\t\t\tvolume of the cone : "<<(0.3333)*pi*r*r*h;
		}
		//sphere operations
		void area_vol2(double r)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of sphere : "<<4*pi*r*r<<endl;
			cout<<"\t\t\t\tvolume of the sphere : "<<(1.3333)*pi*r*r*r;
		}
		//In following method another name is used
		//Torus operations
		void area_vol3(double r, double R)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of Torus : "<<4*pi*pi*r*R<<endl;
			cout<<"\t\t\t\tvolume of the Torus : "<<2*pi*pi*r*r*R;
		}
		//Regular Tetrahedron
		void area_vol3(double s)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of the regular tetrahedron : "<<sqrt((3*s*s))<<endl;
			cout<<"\t\t\t\tvolume of the regular tetrahedron : "<<(0.0833)*sqrt((2*s*s));
		}
		//In following method another name is used
		//Square pyramid
		void area_vol4(double s, double h)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tsurface area of the  square pyramid : "<<s*(s+sqrt((s*s+4*h*h)))<<endl;
			cout<<"\t\t\t\tvolume of the square pyramid : "<<(0.3333)*s*s*h;
		}
		//In following method another name is used
		//pyramid
		void area_void5(double A, double h)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tvolume area of the pyramid : "<<(0.3333)*A*h;
		}
};

//2D shepes

class area_perimeter{
	public:
		//square
		void area_peri(double s)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the square : "<<s*s<<endl;
			cout<<"\t\t\t\tthe perimeter of the square : "<<4*s;
		}
		//rectangle
		void area_peri(double l, double w)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the rectangle : "<<l*w<<endl;
			cout<<"\t\t\t\tthe perimeter of the rectangle : "<<2*l+2*w;
		}
		//parallelogram
		void area_peri(double b, double h, double a)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the parallelogram : "<<b*h<<endl;
			cout<<"\t\t\t\tthe perimeter of the parallelogram : "<<2*a+2*b;
		}
		//trapezoid
		void area_peri(double a, double b, double h, double c, double d)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the trapezoid : "<<(0.5)*(a+b)*h<<endl;
			cout<<"\t\t\t\tthe perimeter of the trapezoid : "<<a+b+c+d;
		}
		//triangle
		void area_peri(double b, double h, double a, double c)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the triangle : "<<(0.5)*b*h<<endl;
			cout<<"\t\t\t\tthe perimeter of the triangle : "<<a+b+c;
		}
		//following method has another name
		//equilateral triangle
		void area_peri1(double s)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe height of the equilateral triangle : "<<(0.8660)*s<<endl;
			cout<<"\t\t\t\tthe area of the equilateral triangle : "<<(0.4330)*s*s<<endl;
			cout<<"\t\t\t\tthe perimeter of the equilateral traingle : "<<3*s;
		}
		//sector of circle
		void area_peri1(double r, double o)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe length of arc :"<<o*r<<endl;
			cout<<"\t\t\t\tthe area of the sector of circle : "<<(0.5)*o*r*r<<endl;
			cout<<"\t\t\t\tthe perimeter of the sector of cirle : "<<2*r+o*r;
		}
		//following method has another name
		//circle
		void area_peri2(double r)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe diameter of the cirlce : "<<2*r<<endl;
			cout<<"\t\t\t\tthe area of the circle : "<<pi*r*r<<endl;
			cout<<"\t\t\t\tthe circumference of  the circle : "<<2*pi*r;
		}
		//eclipse
		void area_peri2(double a, double b)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe area of the eclipse : "<<pi*a*b<<endl;
			cout<<"\t\t\t\tthe circumference of the eclipse : "<<pi*(3*(a+b)-sqrt(((a+3*b)*(b+3*a))));
		}
		//following method has another name
		//annulus
		void area_peri3(double r, double R)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tthe average radius of the annulus : "<<(0.5)*(r+R)<<endl;
			cout<<"\t\t\t\tthe width : "<<R-r<<endl;
			cout<<"\t\t\t\tthe area of the annulus : "<<pi*(R*R-r*r);
		}
		//following method has another name
		//regular polygun
		void area_peri4(double s, double n)
		{
		    cout<<"\t\t\t\t-------------------------------------";
			cout<<endl<<"\t\t\t\tarea of the polygun : "<<(0.25)*n*s*s*(1/tan(pi/n))<<endl;
			cout<<"\t\t\t\tperimetre of the polygun : "<<n*s;
		}
};
int main()
{
	char ch;
	int ch1,ch2;
	class area_volume send;
	class area_perimeter send1;
	double l,b,h,g,k;
	while(1)
    {
        system("cls");
        gotoxy(30,5);
	    cout<<"Choose the Shape"<<endl;
	    gotoxy(30,6);
	    cout<<"1 - 3D shapes"<<endl;
	    gotoxy(30,7);
	    cout<<"2 - 2D shapes"<<endl<<endl;
	    gotoxy(30,10);
	    cout<<"whats your choice : ";
	    ch=getch();
	    system("cls");
   	    switch (ch)
	    {
	 	      //if user select 3D shapes
        case('1'):
	          {
	              gotoxy(30,5);
	              cout<<"Enter number respectively for choosing the shape"<<endl;
	              gotoxy(30,6);
                  cout<<"1 - Cube";
                  gotoxy(30,7);
                  cout<<"2 - Cuboid";
                  gotoxy(30,8);
                  cout<<"3 - Cylinder";
                  gotoxy(30,9);
                  cout<<"4 - Sphere";
                  gotoxy(30,10);
                  cout<<"5 - Cone";
                  gotoxy(30,11);
                  cout<<"6 - Pyramid";
                  gotoxy(30,12);
	              cout<<"7 - Torus";
	              gotoxy(30,13);
	              cout<<"8 - regular tetrahedron";
	              gotoxy(30,14);
	              cout<<"9 - frustum of a cone";
	              gotoxy(30,15);
	              cout<<"10 - square pyramid";
	              gotoxy(30,18);
                  cout<<"whats your choice : ";
	              cin>>ch1;
	              system("cls");
	              switch (ch1)
	              {
                  //cube
                  case(1):
                      {
                          gotoxy(30,5);
                          cout<<"enter the side of the cube : ";
		                  cin>>l;
		                  send.area_vol(l);
		                  break;
                      }
		          //cuboid
                  case (2):
                      {
                          gotoxy(30,5);
                          cout<<"enter the length cuboid : ";
                          cin>>l;
                          gotoxy(30,6);
		                  cout<<"enter the width of cuboid : ";
		                  cin>>b;
		                  gotoxy(30,7);
                          cout<<"enter the height of cuboid : ";
		                  cin>>h;
		                  send.area_vol(l,b,h);
		                  break;
                      }

                  //cylinder
		          case (3):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the radius of the cylinder : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter height of the cylinder : ";
                          cin>>h;
		                  send.area_vol(l,h);
		                  break;
		              }

		         //sphere
		          case (4):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the radius of the sphere : ";
		                  cin>>l;
		                  send.area_vol2(l);
		                  break;
		               }

		         //cone
		          case (5):
		              {
		                  gotoxy(30,5);
		                  cout<<"enter the radius of the cone : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter the height of the cone : ";
		                  cin>>h;
		                  send.area_vol2(l,h);
                          break;
		              }

		         //pyramid
		          case (6):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the area of base of the pyramid : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter the height of the pyramid : ";
		                  cin>>b;
		                  send.area_void5(l,b);
                          break;
		              }

		          //torus
		          case (7):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the tube radius : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter the torus radius :";
		                  cin>>b;
		                  send.area_vol3(l,b);
		                  break;
		              }

		         //tetrahedron
		          case (8):
		              {
		                  gotoxy(30,5);
		                  cout<<"enter the side of tetrahedron : ";
		                  cin>>l;
		                  send.area_vol3(l);
		                  break;
		              }

		         //frustrun of cone
		          case (9):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the top radius of the frustrum of cone : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter the base radius of the frustrum of cone : ";
		                  cin>>b;
		                  gotoxy(30,7);
		                  cout<<"enter the height of the frustrum of cone : ";
		                  cin>>h;
		                  gotoxy(30,8);
		                  cout<<"enter the slant height of the frustrum of cone : ";
		                  cin>>g;
		                  send.area_vol(l,b,h,g);
		                  break;
		              }
                  //square pyramid
		          case (10):
		              {
		                  gotoxy(30,5);
                          cout<<"enter the side of the square pyramid : ";
		                  cin>>l;
		                  gotoxy(30,6);
		                  cout<<"enter the height of the square pyramid : ";
		                  cin>>b;
		                  send.area_vol4(l,b);
		                  break;
		              }

	    	      }//end of the switch 3D
	              break;
	          }
	         //if user select 2D sahpes
	    case('2'):
	        {
                  gotoxy(30,5);
                  cout<<"Enter number respectively for choosing the shape"<<endl;
                  gotoxy(30,6);
                  cout<<"1 - square";
                  gotoxy(30,7);
                  cout<<"2 - rectangle";
                  gotoxy(30,8);
                  cout<<"3 - triangle";
                  gotoxy(30,9);
                  cout<<"4 - equilateral triangle";
                  gotoxy(30,10);
                  cout<<"5 - circle";
                  gotoxy(30,11);
                  cout<<"6 - eclipse";
                  gotoxy(30,12);
                  cout<<"7 - parallelogram";
                  gotoxy(30,13);
                  cout<<"8 - trapezoid";
                  gotoxy(30,14);
                  cout<<"9 - sector of circle";
                  gotoxy(30,15);
                  cout<<"10 - annulus";
                  gotoxy(30,16);
                  cout<<"11 - regular polygun";
                  gotoxy(30,20);
	              cout<<"whats your choice : ";
	              cin>>ch2;
	              system("cls");
	              switch(ch2)
	              {
                   //square
	      	       case (1):
	      	           {
	      	               gotoxy(30,5);
	      	               cout<<"enter the side of the square : ";
	      	               cin>>l;
	      	               send1.area_peri(l);
                           break;
	      	           }
	      	        //rectangle
                   case (2):
                       {
                           gotoxy(30,5);
                           cout<<"enter the length of rectangle : ";
	      	               cin>>l;
	      	               gotoxy(30,6);
	      	               cout<<"enter the width of reectangle : ";
	      	               cin>>b;
	      	               send1.area_peri(l,b);
                           break;
                       }
	                //traingle
                  case (3):
                      {
                           valid:
                                   gotoxy(30,5);
	      	                       cout<<"enter base of triangle : ";
	      	                       cin>>l;
	      	                       gotoxy(30,6);
	      	                       cout<<"enter the height of traingle : ";
	      	                       cin>>b;
	      	                       gotoxy(30,7);
	      	                       cout<<"enter the side of triangle : ";
	      	                       cin>>h;
	      	                       gotoxy(30,8);
	      	                       cout<<"enter the other side of traingle : ";
	      	                       cin>>g;
	      	                       if(l+h>g && l+g>h && h+g>l)
	      	                               send1.area_peri(l,b,h,g);
	      	                       else
	      	                       {
	      	       	                     cout<<"the entered triangle is not valid please enter again "<<endl;
	      	     	                     goto valid;
                                   }
                           break;
                      }

	      	        //equilateral triangle
	      	        case (4):
	      	            {
	      	                gotoxy(30,5);
	      	                cout<<"enter the side of equilateral triangle : ";
	      	                cin>>l;
	      	                send1.area_peri1(l);
	      	                break;
	      	            }

	      	        //circle
                    case (5):
                        {
                            gotoxy(30,5);
                            cout<<"enter the radius of circle : ";
	      	                cin>>l;
	      	                send1.area_peri2(l);
                            break;
                        }
                    //eclipse
	      	        case (6):
	      	            {
	      	                gotoxy(30,5);
	      	                cout<<"enter the semimajor axis of eclipse : ";
	      	                cin>>l;
	      	                gotoxy(30,6);
	      	                cout<<"enter the semiminor axis of eclipse : ";
	      	                cin>>b;
	      	                send1.area_peri2(l,b);
	      	                break;
	      	            }
	                //parallelogram
	      	        case (7):
	      	            {
	      	                gotoxy(30,5);
	      	                cout<<"enter the base of parallelogram : ";
                            cin>>l;
                            gotoxy(30,7);
	      	                cout<<"enter the height of parellelogram : ";
	      	                cin>>b;
	      	                gotoxy(30,8);
	      	                cout<<"enter the side of parellelogram : ";
	      	                cin>>h;
	      	                send1.area_peri(l,b,h);
                            break;
	      	            }

	      	         //trapezoid
                    case (8):
                        {
                            gotoxy(30,5);
                            cout<<"enter the base of trapezoid : ";
	      	                cin>>l;
	      	                gotoxy(30,6);
	      	                cout<<"enter the other base of trapezoid : ";
                            cin>>b;
                            gotoxy(30,7);
	      	                cout<<"enter the height of the trapezoid : ";
	      	                cin>>h;
	      	                gotoxy(30,8);
	      	                cout<<"enter the side of the trapezoid : ";
	      	                cin>>g;
	      	                gotoxy(30,9);
	      	                cout<<"enter the other side of trapezoid : ";
                            cin>>k;
	      	                send1.area_peri(l,b,h,g,k);
	      	                break;
                        }
                     //circle
	      	        case (9):
	      	            {
	      	                gotoxy(30,5);
	      	                cout<<"enter the radius of sector of circle : ";
	      	                cin>>l;
	      	                gotoxy(30,6);
	      	                cout<<"enter the angle of radiuns : ";
	      	                cin>>b;
	      	                send1.area_peri1(l,b);
                            break;
	      	            }
                    //annulus
                    case (10):
                        {
                            gotoxy(30,5);
                            cout<<"enter the innner radius of the annulus : ";
	      	                cin>>l;
	      	                gotoxy(30,6);
	      	                cout<<"enter the outer radius of the annulus : ";
	      	                cin>>b;
	      	                send1.area_peri3(l,b);
                        }
                    //polygun
	      	        case (11):
	      	            {
	      	                gotoxy(30,5);
	      	                cout<<"enter the side of polygun : ";
                            cin>>l;
                            gotoxy(30,6);
	      	                cout<<"enter the number of sides : ";
	      	                cin>>b;
	      	                send1.area_peri4(l,b);
	      	                break;
	      	            }

                    }//switch for the 2D

		     }//second switch statement case 2
         }//first switch statement for (2d or 3d);
    gotoxy(30,15);
    cout<<"enter any key to continue calculating";
    getch();
    }//end of the while loop
}//end of the main function
