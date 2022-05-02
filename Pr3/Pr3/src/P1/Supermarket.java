package P1;

/**
 * Created by yanixxx on 18.04.2022.
 */
public class Supermarket
{
    private String nameotdela;//название отдела
    private int productCode;//код товара
    private String name;//наименование товара
    private String country;//страна-производитель
    private double retailPrice;//розничная цена
    private String nameSource;//поставщик

    public Supermarket(String nameotdela, int productCode, String name, String country, double retailPrice)
    {
        this.nameotdela=nameotdela;
        this.productCode=productCode;
        this.name=name;
        this.country=country;
        this.retailPrice=retailPrice;
    }

    public void setNameotdela(String nameotdela)
    {
        this.nameotdela=nameotdela;
    }

    public String getNameotdela()
    {
        return nameotdela;
    }

    public void setProductCode(int productCode)
    {
        this.productCode=productCode;
    }

    public int getProductCode()
    {
        return productCode;
    }

    public void setName(String name)
    {
        this.name=name;
    }

    public String getName()
    {
        return name;
    }

    public void setCountry(String country)
    {
        this.country=country;
    }

    public String getCountry()
    {
        return country;
    }

    public void setRetailPrice(double retailPrice)
    {
        this.retailPrice=retailPrice;
    }

    public double getRetailPrice()
    {
        return retailPrice;
    }

    public void setNameSource(String nameSource)
    {
        this.nameSource=nameSource;
    }

    public String getNameSource()
    {
        return nameSource;
    }

    public String toString()
    {
        return "Название отдела: "+nameotdela+"\nКод товара: "+productCode+"\nНаименование товара: "+name+
                "\nСтрана-производитель: "+country+"\nРозничная цена: "+retailPrice+"\nПоставщик: "+nameSource;
    }
}
