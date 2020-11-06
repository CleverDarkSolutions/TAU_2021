package zad1;

public class NWD {
	public int a, b;
	public int NWD(int a,int b){
		a = Math.abs(a);
		b = Math.abs(b);
		
		if(a==0 && b==0)
			throw new IllegalArgumentException();
		
		if(a==0)
			return b;
		if(b==0)
			return a;
		
		while (a != b){
			if (a > b)
				a -= b;
			else
				b -= a;
		}
		return a;
	}

}
