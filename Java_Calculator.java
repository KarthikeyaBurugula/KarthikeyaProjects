//This is Calculator Application using Java
//In this Application we will trye to build a calculator module.
//This will cover up from the basic arthematic operations to conversion of units related to various quantites.
//Let us Start.

//First we will import a Scanner odule as we have to take the user input.
import java.util.Scanner;

class Java_Calculator{
    static double add(float a,float b){
    float c=a+b;
    return c;
}
static double subtract(float a,float b){
    float c=a-b;
    return c;
}
static double multiply(float a,float b){
    float c=a*b;
    return c;
}
static double divide(float a,float b){
    float c=a/b;
    return c;
}
//Areas
//Here we are overloading a method called are with various Parameters.
//We are trying to implement Polymorphisim with method overloading.
//For a Single Parameter the method area will calculate Area of Square.
//For 2 Parameters it will calculate the area of Rectangle.
static double area(float a){
    float b=a*a;
    
    return b;
}

static double area(float a,float b){
    float c=2*(a+b);
    
    return c;
}

static double circle_area(float r){
    double c=3.14*r*r;
    return c;
}
static double Triangle_area(float b,float h){
    double c=(b*h)/2;
    return c;
}


    public static void main(String args[]){
        //Creating a Scanner Class for the User Input.
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter 1 for Arthematic Operations Enter 2 for Calculating Areas ");
        int choice=sc.nextInt();

        if(choice==1){
            System.out.println("Enter the numbers for Arthematic operations");
            //Taking the float numbers as User Input.
            float x=sc.nextFloat();
            float y=sc.nextFloat();
            System.out.println("Enter the Arthematic operation ");
            System.out.println('+'+" for addition"+'-'+" for Subtraction"+'*'+" for multiplication"+'/'+" for division");
        //Taking the Symbol input to Perform Operation according to that.
        char symbol=sc.next().charAt(0);
        switch(symbol){
            case '+':
                     System.out.println(add(x,y));
                     break;
            case '-':
                     System.out.println(subtract(x,y));
                     break;
            case '*':
                     System.out.println(multiply(x,y));
                     break;
            case '/':
                     System.out.println(divide(x,y));
                     break;

        }
        }else if(choice==2){
            System.out.println("For Calculating Square Area Type S for Rectangle type R and C for circle and T for Triangle");
        

            //Creating Switch Case module to Performe operation according to the choice.
            char sy=sc.next().charAt(0);
            switch(sy){
                case 'S':
                          System.out.println("Enter the side of Square");
                          float a=sc.nextFloat();
                          System.out.println("Square Area is");
                          System.out.println(area(a));
                          break;
                case 'R':
                             System.out.println("Enter the Length and breadth of Rectangle");
                             float b=sc.nextFloat();
                             float c=sc.nextFloat();

                             System.out.println("Rectangle Area is ");
                             System.out.println(area(b,c));
                case 'C':
                            System.out.println("Enter the Radious");
                            float r=sc.nextFloat();
                            System.out.println("Circle Area is ");
                            System.out.println(circle_area(r));
                case 'T':
                            System.out.println("Enter base and height");
                            float k=sc.nextFloat();
                            float l=sc.nextFloat();
                            System.out.println("Triangle area is ");
                            System.out.println(Triangle_area(k,l));

                
            }


        }
        
        
        
            
                             
                          
        }
    }

