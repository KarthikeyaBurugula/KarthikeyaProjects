//Developing a Rock Paper Scissors game using the random modul to generate the computer input 
import java.util.Random;
//Taking the Scanner module to take the user input in order to get going into the game.
import java.util.Scanner;

//Rules
//The 3 main objects of this game are Rock Paper Scissors 
//The Symbols are Rock is 1, Paper is 2, Scissor is 3. 
//In Which Rock Dominate Scissors, Scissors dominate Paper and Paper Dominate Rock.
//Satisfying the above conditions Players will get points.

class Rock_Papers_Scissors{
    public static void main(String args[]){
        //Creating class object for Random class
        Random rand=new Random();
        //Creating Scanner class for user Input
        Scanner sc=new Scanner(System.in);
        //Prompting for selection
        System.out.println(1+" For Rock");
        System.out.println(2+" For Paper");
        System.out.println(3+" For Scissors");
        //Initializing the scores of User and Computer to Zero
        int user_Score=0;
        int com_Score=0;
        //Taking input for number of points to play
        System.out.println("Enter for how many points do you want to play");
        int points=sc.nextInt();
        //Iterating for number of time as a count of points
        for(int i=0;i<points;i++){
            //Taking user Input
            System.out.println("Dear user enter a number between 1 and 3");
            int u=sc.nextInt();
            //Taking Computer Input
            System.out.println("Computer giving its input between 1 and 3");
            int com=rand.nextInt(1,4);
            System.out.println(com);
            //Validating if both inputs are of range 1 to 3.
            boolean cond1=u>=1 && u<=3;
            boolean cond2=com>=1 && com<=3;
            
            if(cond1 && cond2 ){
                System.out.println("Proceeding to the game");
                //Checking the inputs and giving the points
                if((u==1 && com==3) || (u==2 && com==1) || (u==3 && com==2)){
                    user_Score=user_Score+1;
                }else if(u==com){
                    System.out.println("The Inputs are Same no points for anyone");
                    user_Score=user_Score;
                    com_Score=com_Score;
                    continue;
                }else{
                    com_Score=com_Score+1;
                }

            }else{
                //Warning if any of inputs are violating
                System.out.println("The entered inputs are wrong ");
            }

        }
        //Displaying the Scores
        System.out.println("Your Score is "+user_Score);
        System.out.println("Computer Score is "+com_Score);
        //Declaring the Winner
        if(user_Score > com_Score){
            System.out.println("Dear user you have won the game");
        }else if(user_Score <com_Score){
            System.out.println("You lose better luck next time");
        }else{
            System.out.println("Its a draw");
        }
       
    }
}