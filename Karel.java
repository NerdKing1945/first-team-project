function main()
{
   while(frontIsClear())
   {
      if(leftIsClear())
      {
        putBeeperLine();
        sideStep();
        goBack();
        turnAround();
      } else 
      {
        putBeeperLine();
      }
    }
}
//마지막에는 좀 운이 따라줬지만.. 
//while 구문 frontIsClear는 결국 길이 끝날때까지 작동하는 거지..
//leftIsClear는 마지막 줄에서 blocked로 바뀌는 순간 줄바뀜 없이 한 줄만 채우면서 종료된다. 


function putBeeperLine()
{
   putBeeper();
   while(frontIsClear()) 
   {
      move();
      putBeeper();
   }
}

function sideStep()
{
   while(frontIsBlocked()) 
   {
      turnLeft();
      move();
      turnLeft();
      
   }
}

function goBack()
{
   while(frontIsClear())
   {
      move();
   }
}   
   