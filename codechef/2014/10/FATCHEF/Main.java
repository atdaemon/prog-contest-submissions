/**
 * http://www.codechef.com/OCT14/problems/FATCHEF
*/
import java.io.*;
import java.util.*;
public class Main
{
	static InputStream in;
	static PrintWriter out;
	static String INPUT = "";
	static void solve()
	{
		int T = readInt();
		int N,M,y;
		char x,old_color,new_color;
		int arr[];
		int[][] heap;
		int old_place,new_place ;
		long ans = 0,mult;
		for(int i = 0 ; i< T ; i++)
		{
			arr=readNumArray(2);
			N = arr[0];
			M = arr[1];
			heap = new int[M][2];
			for(int j = 0 ; j < M ; j++)
			{
				x = readChar();
				y = readInt();
				//System.out.println("X="+x+" ,y="+y);
				heap[j] = new int[]{y,x};
			}
			old_place = heap[0][0];
			old_color = (char) heap[0][1];
			ans = 1;
			for(int k = 0 ; k < M ; k++)
			{
				new_place = heap[k][0];
				new_color = (char) heap[k][1];
				if(old_color!=new_color)
				{
					mult = new_place - old_place;
					ans = (ans*mult)%(1000000009);
				}
				old_place = new_place;
				old_color=new_color;
			}
			out.println(ans);
		}
	}

	public static void main(String[] args) throws Exception
	{
		//long S = System.currentTimeMillis();
		in = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		solve();
		out.flush();
		//long G = System.currentTimeMillis();
		//tr(G-S+"ms");
	}
	private static boolean eof()
	{
		if(lenbuf == -1)return true;
		int lptr = ptrbuf;
		while(lptr < lenbuf)if(!isSpaceChar(inbuf[lptr++]))return false;
		try {
			in.mark(1000);
			while(true){
				int b = in.read();
				if(b == -1){
					in.reset();
					return true;
				}else if(!isSpaceChar(b)){
					in.reset();
					return false;
				}
			}
		} catch (IOException e) {
			return true;
		}
	}
	private static byte[] inbuf = new byte[1024];
	static int lenbuf = 0, ptrbuf = 0;
	private static int read()
	{
		if(lenbuf == -1)throw new InputMismatchException();
		if(ptrbuf >= lenbuf){
			ptrbuf = 0;
			try { lenbuf = in.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
			if(lenbuf <= 0)return -1;
		}
		return inbuf[ptrbuf++];
	}
	private static boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
	private static int skip() { int b; while((b = read()) != -1 && isSpaceChar(b)); return b; }
	private static double readDouble() { return Double.parseDouble(readString()); }
	private static char readChar() { return (char)skip(); }
	private static String readString()
	{
		int b = skip();
		StringBuilder sb = new StringBuilder();
		while(!(isSpaceChar(b))){ // when nextLine, (isSpaceChar(b) && b != ' ')
			sb.appendCodePoint(b);
			b = read();
		}
		return sb.toString();
	}
	private static char[] readString(int n)
	{
		char[] buf = new char[n];
		int b = skip(), p = 0;
		while(p < n && !(isSpaceChar(b))){
			buf[p++] = (char)b;
			b = read();
		}
		return n == p ? buf : Arrays.copyOf(buf, p);
	}
	private static char[][] nm(int n, int m)
	{
		char[][] map = new char[n][];
		for(int i = 0;i < n;i++)map[i] = readString(m);
		return map;
	}
	private static int[] readNumArray(int n)
	{
		int[] a = new int[n];
		for(int i = 0;i < n;i++)a[i] = readInt();
		return a;
	}
	private static int readInt()
	{
		int num = 0, b;
		boolean minus = false;
		while((b = read()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = read();
		}
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = read();
		}
	}
	private static long readLong()
	{
		long num = 0;
		int b;
		boolean minus = false;
		while((b = read()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
		if(b == '-'){
			minus = true;
			b = read();
		}
		while(true){
			if(b >= '0' && b <= '9'){
				num = num * 10 + (b - '0');
			}else{
				return minus ? -num : num;
			}
			b = read();
		}
	}
	private static void tr(Object... o) { if(INPUT.length() != 0)System.out.println(Arrays.deepToString(o)); }
}

