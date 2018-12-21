
javaCode = """
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Auribises
{
	public static void main (String[] args) throws java.lang.Exception
	{
		System.out.println("Welcome to Java");
	}
}
    
"""

with open("/Users/ishantkumar/Downloads/Auribises.java","w") as file:
    file.write(javaCode)
    print(">> Java Code Written")
    file.close()

