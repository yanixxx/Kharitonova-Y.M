package P1;

import java.util.ArrayList;

/**
 * Created by yanixxx.
 */
public class ListOfProducts
{
    private ArrayList<Supermarket> products;

    public ListOfProducts()
    {
        products=new ArrayList<Supermarket>();
    }

    public void Add(Supermarket product)
    {
        products.add(product);
    }

    public String toString()
    {
        String str="";

        for (int i=0; i<products.size();i++)
        {
            //str+=products[i].toString();
            str+=products.get(i);
            str+="\n------------------------\n";
        }

        return str;
    }

}
