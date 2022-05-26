package P1;

/**
 * Created by yanixxx.
 */
public class DimensionalProduct extends Supermarket
{
    private double height;
    private double width;
    private double length;

    public DimensionalProduct(String nameotdela, String name, String country, double retailPrice,String nameSource, double height, double width, double length)
    {
        super(nameotdela,name,country,retailPrice,nameSource);
        this.height=height;
        this.width=width;
        this.length=length;
    }

    public void setHeight(double height)
    {
        this.height=height;
    }

    public double getHeight()
    {
        return height;
    }

    public void setWidth(double width)
    {
        this.width=width;
    }

    public double getWidth()
    {
        return width;
    }

    public void setLength(double length)
    {
        this.length=length;
    }

    public double getLength()
    {
        return length;
    }

    public String toString()
    {
        return super.toString()+"\nВысота: "+height+" м\nШирина: "+width+ " м\nДлина: "+length+" м";
    }
}
