package P1;

import java.io.*;

/**
 * Created by yanixxx on 18.04.2022.
 */
public class Program
{
    public static void main(String[] args)
    {
        Supermarket supermarket=new Supermarket("мебельный", 123987, "стол", "Россия", 5478.22);
        System.out.println(supermarket);
        System.out.println();
        supermarket.setNameSource("ООО Мебельная фабрика");
        System.out.println(supermarket);
    }
}
