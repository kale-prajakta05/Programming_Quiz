from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry('600x500')
root.title("welcome to Test")

l=Label(root, text="Welcome to the Programming Quiz",justify=LEFT,font="lucia 19 bold").pack()
x=Label(root, text="Choose Type of Questions",justify=LEFT,font="lucia 19 bold").pack()

i=IntVar()



   


def cquestions():
    s1=Toplevel()
    s1.geometry("700x500")
   
      
  # check ans of 1 st que
    def check1():
     s2=Toplevel()
     s2.geometry("600x400")
     if (i.get()==1):
         Label(s2, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
         Label(s2, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()
         

  #1st question

    a=Label(s1, text="1. Who is Father  of C language ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
    r1=Radiobutton(s1, text="Dennis ritchie",value=1,variable=i).pack(anchor="w")
    r2=Radiobutton(s1, text="James A.Gosling  ",value=2,variable=i).pack(anchor="w")
    r2=Radiobutton(s1, text="bjarne stroustrup ",value=3,variable=i).pack(anchor="w")
   

    btn1=Button(s1,text="check ur ans" , command=check1,fg="black",font=20  ,bg="skyblue").pack(anchor="w")


  # check 2 nd que
     
  
    def check2():
     s3=Toplevel()
     s3.geometry("600x400")
     s3.title("check answer ")
    # to check answer
     if (i.get()==2):
         m=Label(s3, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s3, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

         




  #sec question

    def cq2():
       a=Label(s1, text="2. Which of the following is non linear data structure ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s1, text="queue",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s1, text="graph",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s1, text="stack",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s1, text="linked list",value=4,variable=i).pack(anchor="w")


       btn1=Button(s1,text="check ur ans" , command=check2,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s1,text="next ",command=cq3,fg="black",font=20  ,bg="skyblue").pack()
      

    btn2=Button(s1,text="next ",command=cq2,fg="black",font=20  ,bg="skyblue" ).pack()
    



    
  # check 3 nd que
     
  
    def check3():
     s4=Toplevel()
     s4.geometry("600x400")
     s4.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s4, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s4, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         




  # 3 question

    def cq3():
       a=Label(s1, text="3. Arrey is ...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
      
       r2=Radiobutton(s1, text="cannot  be of integer data type",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s1, text="collection of elemens of similar data types occupying contigious memory location",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s1, text="hetrogenous data structure",value=4,variable=i).pack(anchor="w")


       btn1=Button(s1,text="check ur ans" , command=check3,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s1,text="next ",command=cq4,fg="black",font=20  ,bg="skyblue").pack()
      

  
    


  
    
  # check 4 nd que
     
  
    def check4():
     s5=Toplevel()
     s5.geometry("600x400")
     s5.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s5, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s5, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         




  # 4 question

    def cq4():
       a=Label(s1, text="4. Arrey index starts with",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s1, text="1",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s1, text="-1",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s1, text="0",value=3,variable=i).pack(anchor="w")
       


       btn1=Button(s1,text="check ur ans" , command=check4,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s1,text="next ",command=cq5,fg="black",font=20  ,bg="skyblue").pack()       



  


    # check 4 nd que
     
  
    def check5():
     s6=Toplevel()
     s6.geometry("600x400")
     s6.title("check answer ")
    # to check answer
     if (i.get()==4):
         m=Label(s6, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s6, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         
    def thnq():
      thnx=Toplevel()
      thnx.geometry("200x200")
      m=Label(thnx,text="Thank you...",justify=LEFT,font="lucia 19 bold").pack()
      thnx.mainloop()



  # 5 question

    def cq5():
       a=Label(s1, text="5. What is correct value to return to os upon the successful compilation of program",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s1, text="1",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s1, text="-1",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s1, text="nothoing",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s1, text="0",value=4,variable=i).pack(anchor="w")


       btn1=Button(s1,text="check ur ans" , command=check4  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s1,text="Submit" , command=thnq ,bg="skyblue").pack()    
def cppque():
    
    s11=Toplevel()
    s11.geometry('500x500')
    s11.title("welcome to c++ questions")
  
      
  # check ans of 1 st que
    def check11():
     s22=Toplevel()
     s22.geometry("600x400")
   
     if (i.get()==3):
         Label(s22, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
         Label(s22, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()
         

  #1st question

    a=Label(s11, text="1. C++ inheritance relationship is a ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
    r1=Radiobutton(s11, text="has a",value=1,variable=i).pack(anchor="w")
    r2=Radiobutton(s11, text="association  ",value=2,variable=i).pack(anchor="w")
    r2=Radiobutton(s11, text="is a ",value=3,variable=i).pack(anchor="w")
  

    
    btn1=Button(s11,text="check ur ans" , command=check11,fg="black",font=20  ,bg="skyblue").pack(anchor="w")


    
  # check 2 nd que
     
  
    def check2():
     s33=Toplevel()
     s33.geometry("600x400")
     s33.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s33, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s33, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()


         




  #sec question

    def cq22():
       a=Label(s11, text="2. Friend function is...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="member function of class",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="not a member function of class",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="not a member function of class but can access privrte members of class",value=3,variable=i).pack(anchor="w")
       


       btn1=Button(s11,text="check ur ans" , command=check2,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq33,fg="black",font=20  ,bg="skyblue").pack()
      

    btn2=Button(s11,text="next ",command=cq22,fg="black",font=20  ,bg="skyblue" ).pack()

      
    def check33():
     s44=Toplevel()
     s44.title("check answer ")
     s44.geometry("600x400")
    # to check answer
     if (i.get()==2):
         m=Label(s44, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s44, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         




  # 3 question

    def cq33():
       a=Label(s11, text="3. Wraping of data and its related functionality is known as...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r2=Radiobutton(s11, text="ecapsulation",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="inheritance",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s11, text="polymorphism",value=4,variable=i).pack(anchor="w")


       btn1=Button(s11,text="check ur ans" , command=check33,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq44,fg="black",font=20  ,bg="skyblue").pack()



    
    def check44():
     s55=Toplevel()
     s55.geometry("600x400")
     s55.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s55, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s55, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         




  # 4 question

    def cq44():
       a=Label(s11, text="4. An operation A.X  in cpp means...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="A is member of object B",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="Product of A and B",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="B is a member of object A",value=3,variable=i).pack(anchor="w")
      


       btn1=Button(s11,text="check ur ans" , command=check44,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq55,fg="black",font=20  ,bg="skyblue").pack()
    

    
    def check55():
     s66=Toplevel()
     s66.geometry("600x400")
     s66.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s66, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s66, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
    def thnq():
      thnx=Toplevel()
      thnx.geometry("200x200")
      m=Label(thnx,text="Thank you...",justify=LEFT,font="lucia 19 bold").pack()
      thnx.mainloop()





  # 5 question

    def cq55():
       a=Label(s11, text="5. Reusablity in code is achived through ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="polymorphism",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="cresting object of class",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="inheritance",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s11, text="encapsulation",value=4,variable=i).pack(anchor="w")


       btn1=Button(s11,text="check ur ans" , command=check55  ,bg="skyblue").pack(anchor="w")
       btn1=Button(s11,text="Submit" , command=thnq ,bg="skyblue").pack()



    s11.mainloop()



def javaque():
    
    s11=Toplevel()
    s11.geometry('500x500')
    s11.title("welcome to c++ questions")
  
      
  # check ans of 1 st que
    def check11():
     s22=Toplevel()
     s22.geometry("600x400")
    
     if (i.get()==2):
         Label(s22, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
         Label(s22, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()
         

  #1st question

    a=Label(s11, text="1. which provides runtime environment for java byte codeto be executed ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
    r1=Radiobutton(s11, text="JDK",value=1,variable=i).pack(anchor="w")
    r2=Radiobutton(s11, text="JVM ",value=2,variable=i).pack(anchor="w")
    r2=Radiobutton(s11, text="JAVAC",value=3,variable=i).pack(anchor="w")

    
    btn1=Button(s11,text="check ur ans" , command=check11,fg="black",font=20  ,bg="skyblue").pack(anchor="w")


    
  # check 2 nd que
     
  
    def check2():
     s33=Toplevel()
     s33.geometry("600x400")
     s33.title("check answer ")
    # to check answer
     if (i.get()==3):
         m=Label(s33, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s33, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

         




  #sec question

    def cq22():
       a=Label(s11, text="2. What feature of oop has super class sub class concept ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="single inheritance",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="multilevel inheritance",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="Hierarchical inheritance",value=3,variable=i).pack(anchor="w")
      


       btn1=Button(s11,text="check ur ans" , command=check2,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq33,fg="black",font=20  ,bg="skyblue").pack()
      

    btn2=Button(s11,text="next ",command=cq22,fg="black",font=20  ,bg="skyblue" ).pack()

      
    def check33():
     s44=Toplevel()
     s44.title("check answer ")
    # to check answer
     if (i.get()==1):
         m=Label(s44, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s44, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
         




  # 3 question

    def cq33():
       a=Label(s11, text="3. Java language was initially  known as...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       
       r2=Radiobutton(s11, text="oak",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="pine",value=3,variable=i).pack(anchor="w")
       r4=Radiobutton(s11, text="java 1.0",value=4,variable=i).pack(anchor="w")


       btn1=Button(s11,text="check ur ans" , command=check33,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq44,fg="black",font=20  ,bg="skyblue").pack()



    
    def check44():
     s55=Toplevel()
     s55.geometry("600x400")
     s55.title("check answer ")
    # to check answer
     if (i.get()==1):
         m=Label(s55, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s55, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()
        

   
         




  # 4 question

    def cq44():
       a=Label(s11, text="4.  By default access specifier in Java is...",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="default(pakage level)",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="Private",value=2,variable=i).pack(anchor="w")
       r3=Radiobutton(s11, text="public",value=3,variable=i).pack(anchor="w")
       


       btn1=Button(s11,text="check ur ans" , command=check44,fg="black",font=20  ,bg="skyblue").pack(anchor="w")
       btn2=Button(s11,text="next ",command=cq55,fg="black",font=20  ,bg="skyblue").pack()
    

    
    def check55():
     s66=Toplevel()
     s66.geometry("600x400")
     s66.title("check answer ")
    # to check answer
     if (i.get()==2):
         m=Label(s66, text=" congrats !!!  your ans is right ",justify=LEFT,font="lucia 10 bold").pack()
     else:
        n= Label(s66, text="ohhh nooo your ans is wrong , dont worry try again",justify=LEFT,font="lucia 10 bold").pack()

   
    def thnq():
      thnx=Toplevel()
      thnx.geometry("200x200")
      m=Label(thnx,text="Thank you...",justify=LEFT,font="lucia 19 bold").pack()
      thnx.mainloop()





  # 5 question

    def cq55():
       a=Label(s11, text="5. Interface has condtructor  ?",justify=LEFT,font="lucia 13 bold").pack(anchor="w")
       r1=Radiobutton(s11, text="YES",value=1,variable=i).pack(anchor="w")
       r2=Radiobutton(s11, text="NO",value=2,variable=i).pack(anchor="w")
       
      


       btn1=Button(s11,text="check ur ans" , command=check55  ,bg="skyblue").pack(anchor="w")
       btn1=Button(s11,text="Submit" , command=thnq ,bg="skyblue").pack()



    s11.mainloop()  

btn1=Button(root,text="     c       " , command=cquestions,fg="black",font=20,bg="pink").pack(anchor="c")
btn2=Button(root,text="     c++     " , command=cppque,fg="black",font=25,bg="pink").pack(anchor="c")
btn3=Button(root,text="    Java     " , command=javaque,fg="black",font=25,bg="pink").pack(anchor="c")



root.mainloop()