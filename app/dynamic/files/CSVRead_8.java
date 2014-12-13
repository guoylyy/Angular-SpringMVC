package csv;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;

import au.com.bytecode.opencsv.CSVReader;
import au.com.bytecode.opencsv.CSVWriter;

public class CSVRead {

	public static List<String> getX(String path) {
		List<String> x = new ArrayList<String>(); 
		try {
			CSVReader reader = new CSVReader(new FileReader(
					path));
			String[] line = null;
			//reader.readNext();
			while ((line = reader.readNext()) != null) {
				for (String cell : line) {
					x.add(cell);
				}
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return x;
	}

}
