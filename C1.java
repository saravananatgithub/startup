import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class C1 {

	public static void main(String[] args) {
		//sop
		System.out.println(" Inside C1");
		int age = 45;
		String name = "Saravanan";
		String address = "Scwhalbach";
		System.out.println("age is:" + age);
		System.out.println("name is:" + name);
		
		List myList = new ArrayList<String>();
		myList.add("A");
		myList.add("A");
		myList.add("C");
		System.out.println("myList is:" + myList);
		
		Set mySet = new HashSet<String>();
		mySet.add("A");
		mySet.add("A");
		mySet.add("C");
		System.out.println("mySet is:" + mySet);
		
		Map myMap = new HashMap<String, String>();
		myMap.put("name1", "Saravanan");
		myMap.put("name2", "Lovester");
		myMap.put("name1", "XXXXXXXX");
		System.out.println("myMap is:" + myMap);		
		
	}

}
