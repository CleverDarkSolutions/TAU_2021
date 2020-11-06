package zad1;

import static org.junit.Assert.*;

import org.junit.*;

public class NWDTest {
	private NWD nwd;
	
	@Before
	public void setUp(){
		nwd = new NWD();
		System.out.println("Before");
	}
	
	@After
	public void tearDown(){
		nwd = null;
		System.out.println("After");
	}
	
	@Test
	public void testNwd() {
		int result = nwd.NWD(4,2);
		assertEquals(2,result);
		System.out.println("Test1");
	}
	
	
	@Test
	public void testNwd2() {
		int result = nwd.NWD(40,20);
		assertEquals(20,result);
		System.out.println("Test2");
	}
}
