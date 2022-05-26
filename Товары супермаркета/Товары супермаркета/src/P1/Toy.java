package P1;

/**
 * Created by yanixxx.
 */
enum AgeGroup
{
    Younger, Middle, Senior
}

public class Toy extends Supermarket
{
    private AgeGroup ageGroup;
    private  String type;

    public Toy(String nameotdela, String name, String country, double retailPrice,String nameSource, AgeGroup ageGroup, String type)
    {
        super(nameotdela,name,country,retailPrice,nameSource);
        this.ageGroup=ageGroup;
        this.type=type;
    }

    public void setAgeGroup(AgeGroup ageGroup)
    {
        this.ageGroup=ageGroup;
    }

    public AgeGroup getAgeGroup()
    {
        return ageGroup;
    }

    public  void setType(String type)
    {
        this.type=type;
    }

    public String getType()
    {
        return type;
    }

    public String toString()
    {
        return super.toString()+"\nВозрастная группа: "+ageGroup+"\nТип: "+type;
    }
}
