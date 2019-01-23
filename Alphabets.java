import java.lang.*;
import java.util.*;
import java.math.*;

class Alphabets
{
	public String process(String str)
	{
		char[] ch= str.toCharArray();
		char[] ch1= new char[100];
		int k=0,diff;
		int s,s1;
System.out.println(ch.length);
		for(int i=0;i<ch.length-1;i++)
		{
			ch1[k]=ch[i];
			s=(int) ch[i];
			s1=(int) ch[i+1];
			diff=Math.abs(s-s1);
			k=k+1;
			int add=96+diff;
			ch1[k]=(char)add;
			k=k+1;
		}

		String str1=ch1.toString();
		return str1;
	}


	public static void main(String args[])
	{
		Scanner obj= new Scanner(System.in);
		String str=obj.nextLine();
		Alphabets ob = new Alphabets();
		String str1 = ob.process(str);
		System.out.println(str1);
		//System.out.println(A);
	}
}