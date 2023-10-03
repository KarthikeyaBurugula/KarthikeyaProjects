/*Today we are going to implement one of the Machine learning Concept to Predict the whether of tomorrow based on the previous table data*/
/*First of all we are going to create a database*/
create database Projects;
show databases;
/*We are going to use the databasse that is created*/
use Projects;
/*Creating the whether with Day number as Primary key*/
create table whether(day int primary key ,outlook varchar(10),Temprature varchar(10),Humidity varchar(10),wind varchar(10),Play_Cricket varchar(3));
/*Inserting the values into our table*/
insert into whether values(1,'sunny','hot','high','weak','No');
insert into whether values(2,'sunny','hot','high','strong','No');
insert into whether values(3,'overcast','hot','high','weak','Yes');
insert into whether values(4,'rain','mild','high','weak','Yes');
insert into whether values(5,'rain','cool','normal','weak','Yes');
insert into whether values(6,'rain','cool','normal','strong','No');
insert into whether values(7,'overcast','cool','normal','strong','Yes');
insert into whether values(8,'sunny','mild','high','weak','No');
insert into whether values(9,'sunny','cool','normal','weak','Yes');
insert into whether values(10,'rain','mild','normal','weak','Yes');
insert into whether values(11,'sunny','mild','normal','strong','Yes');
insert into whether values(12,'overcast','mild','high','strong','Yes');
insert into whether values(13,'overcast','hot','normal','weak','Yes');
insert into whether values(14,'rain','mild','high','strong','No');
/*Now we got all our values inserted lets have a breif look at our table*/
Select * from whether;
/*Now Play_Cricket is Our Target Variable*/
/*We have to predict the Target variable Play_cricket value to be Yes or no based on some parameters the parameters are
outlook=sunny, tmprature=cool, humidity=high, wind=strong, for these values we have to predict Yes or No*/

/*Step 1 is to Calculate Prior Propabilities Propability(Yes) and Propability(No)*/
/*Let us Calculate the Propability of Yes*/
Select count(*) from whether where Play_Cricket='Yes';/*No of Yes is 9*/

Select round((Select count(*) from whether where Play_Cricket='Yes')/Cast((Select count(*) from whether) AS Float),4) Yes from whether limit 1;

/*Let us Calculate the Propability of No*/
Select count(*) from whether where Play_Cricket='No';/*No of Yes is 5*/
Select round((Select count(*) from whether where Play_Cricket='No')/Cast((Select count(*) from whether) AS Float),4) No from whether limit 1;
Select * from whether;
/*It is Step 2 now we have to calculate the conditional Probabilities for each attributes*/
/*First for Outlook Attribute In the outlook we have Sunny Overcast Rain Conditions Lets calculate the conditional Propability*/
/*Total number of Sunny days are*/
Select count(*) from whether where outlook='sunny';/*Total 5 Sunny*/
/*Total no of sunny given Yes*/
Select count(*) from whether where outlook='sunny' and Play_Cricket='Yes';
Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) sunny_yes from whether limit 1;
/*Total no of sunny given No*/
Select count(*) from whether where outlook='sunny' and Play_Cricket='No';
Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) sunny_no from whether limit 1;

/*Next Condition is Overcast*/
/*Total no of overcast given Yes*/
Select count(*) from whether where outlook='overcast';
Select count(*) from whether where outlook='overcast' and Play_Cricket='Yes';
Select round((Select count(*) from whether where outlook='overcast' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) overcast_yes from whether limit 1;
/*Total no of overcast given no*/
Select count(*) from whether where outlook='overcast' and Play_Cricket='No';
Select round((Select count(*) from whether where outlook='overcast' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) overcast_no from whether limit 1;

/*Next Condition is Rain*/
/*Total no of Rain given Yes*/
Select count(*) from whether where outlook='rain';
Select count(*) from whether where outlook='rain' and Play_Cricket='Yes';
Select round((Select count(*) from whether where outlook='rain' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) rain_yes from whether limit 1;
/*Total no of overcast given no*/
Select count(*) from whether where outlook='rain' and Play_Cricket='No';
Select round((Select count(*) from whether where outlook='rain' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) rain_no from whether limit 1;

/*Our Next Feature is Tempreature*/
/*We have 3 Conditions Hot Mild and Cold*/
/*Lets calculate Conditionals of Hot*/
Select count(*) from whether where temprature='hot';
Select round((Select count(*) from whether where temprature='hot' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) hot_yes from whether limit 1;
Select round((Select count(*) from whether where temprature='hot' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) hot_no from whether limit 1;
/*Lets calculate Conditionals of mild*/
Select count(*) from whether where temprature='mild';
Select round((Select count(*) from whether where temprature='mild' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) mild_yes from whether limit 1;
Select round((Select count(*) from whether where temprature='mild' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) mild_no from whether limit 1;
/*Lets calculate Conditionals of cool*/
Select count(*) from whether where temprature='cool';
Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) cool_yes from whether limit 1;
Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) cool_no from whether limit 1;

/*Lets Move on to the next Feature Humidity*/
/*Humidity has 2 Conditions High normal*/
/*Lets Calculate condition high*/
Select count(*) from whether where humidity='high';
Select round((Select count(*) from whether where humidity='high' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) high_yes from whether limit 1;
Select round((Select count(*) from whether where humidity='high' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) high_no from whether limit 1;
/*Lets Calculate condition normal*/
Select count(*) from whether where humidity='normal';
Select round((Select count(*) from whether where humidity='normal' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) normal_yes from whether limit 1;
Select round((Select count(*) from whether where humidity='normal' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) normal_no from whether limit 1;

/*Lets move to next Feature Wind*/
/*We have 2 conditions strong weak*/
/*Lets calculate for strong*/
Select count(*) from whether where wind='strong'; 
Select round((Select count(*) from whether where wind='strong' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) strong_yes from whether limit 1;
Select round((Select count(*) from whether where wind='strong' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) strong_no from whether limit 1;
/*Lets calculate for strong*/
Select count(*) from whether where wind='weak'; 
Select round((Select count(*) from whether where wind='weak' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) weak_yes from whether limit 1;
Select round((Select count(*) from whether where wind='weak' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) weak_no from whether limit 1;

/*Upto this point we have calculated all the conditional propabilities of respective Features given for Target Variables Yes/No*/
/*We are Give upto 14 days of data and asked to predict the output for day 15*/
/*The Parameters and values of day 15 are 
outlook=sunny, temprature=cool, humidity=high, wind=strong, for both Yes and no*/

/*First we calculate propability of Yes for this given features*/
Select round((Select round((Select count(*) from whether where Play_Cricket='Yes')/Cast((Select count(*) from whether) AS Float),4) Yes from whether limit 1)*
(Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) sunny_yes from whether limit 1)*
(Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) cool_yes from whether limit 1)*
(Select round((Select count(*) from whether where humidity='high' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) high_yes from whether limit 1)*
(Select round((Select count(*) from whether where wind='strong' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) strong_yes from whether limit 1),4) Ultimate_Yes
from whether limit 1;/*The Value is 0.0053*/

/*Next we calculate propability of No for this given features*/
Select round((Select round((Select count(*) from whether where Play_Cricket='No')/Cast((Select count(*) from whether) AS Float),4) Yes from whether limit 1)*
(Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) sunny_no from whether limit 1)*
(Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) cool_no from whether limit 1)*
(Select round((Select count(*) from whether where humidity='high' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) high_no from whether limit 1)*
(Select round((Select count(*) from whether where wind='strong' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) strong_no from whether limit 1),4) Ultimate_No
from whether limit 1;/*The Value is 0.0206*/


/*Finally Deciding whether we can Play the cricket or not based on the prpabilities using If Condition*/
SELECT IF((Select round((Select round((Select count(*) from whether where Play_Cricket='Yes')/Cast((Select count(*) from whether) AS Float),4) Yes from whether limit 1)*
(Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) sunny_yes from whether limit 1)*
(Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) cool_yes from whether limit 1)*
(Select round((Select count(*) from whether where humidity='high' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) high_yes from whether limit 1)*
(Select round((Select count(*) from whether where wind='strong' and Play_Cricket='Yes' )/Cast((Select count(*) from whether where Play_Cricket='Yes') AS Float),4) strong_yes from whether limit 1),4) Ultimate_Yes
from whether limit 1/*The Value is 0.0053*/)>(Select round((Select round((Select count(*) from whether where Play_Cricket='No')/Cast((Select count(*) from whether) AS Float),4) Yes from whether limit 1)*
(Select round((Select count(*) from whether where outlook='sunny' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) sunny_no from whether limit 1)*
(Select round((Select count(*) from whether where temprature='cool' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) cool_no from whether limit 1)*
(Select round((Select count(*) from whether where humidity='high' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) high_no from whether limit 1)*
(Select round((Select count(*) from whether where wind='strong' and Play_Cricket='No' )/Cast((Select count(*) from whether where Play_Cricket='No') AS Float),4) strong_no from whether limit 1),4) Ultimate_Yes
from whether limit 1/*The Value is 0.0206*/), "Yes you can Play Cricket", "No You cant Play Cricket") Result;






