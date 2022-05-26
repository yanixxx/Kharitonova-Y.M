package P1;

public class Supermarket
{
    private String nameotdela;//название отдела
    private String name;//наименование товара
    private String country;//страна-производитель
    private double retailPrice;//розничная цена
    private String nameSource;//поставщик

    public Supermarket(String nameotdela, String name, String country, double retailPrice, String nameSource)
    {
        this.nameotdela=nameotdela;
        this.name=name;
        this.country=country;
        this.retailPrice=retailPrice;
        this.nameSource=nameSource;
    }

    public void setNameotdela(String nameotdela)
    {
        this.nameotdela=nameotdela;
    }

    public String getNameotdela()
    {
        return nameotdela;
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
        return "Название отдела: "+nameotdela+"\nНаименование товара: "+name+
                "\nСтрана-производитель: "+country+"\nРозничная цена: "+retailPrice+"\nПоставщик: "+nameSource;
    }
}
