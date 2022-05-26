package P1;

/**
 * Created by yanixxx.
 */
public class Fruit extends Supermarket
{
    private double maxStorageTime;
    private double storageTemperature;

    public Fruit(String nameotdela, String name, String country, double retailPrice,String nameSource, double maxStorageTime, double storageTemperature)
    {
        super(nameotdela,name,country,retailPrice,nameSource);
        this.maxStorageTime=maxStorageTime;
        this.storageTemperature=storageTemperature;
    }

    public void setMaxStorageTime(double maxStorageTime)
    {
        this.maxStorageTime=maxStorageTime;
    }

    public double getMaxStorageTime()
    {
        return  maxStorageTime;
    }

    public void setStorageTemperature(double storageTemperature)
    {
        this.storageTemperature=storageTemperature;
    }

    public double getStorageTemperature()
    {
        return storageTemperature;
    }

    public String toString()
    {
        return super.toString()+"\nМаксимальное время хранения: "+maxStorageTime+" ч\nтемпература хранения: "+storageTemperature+"C";
    }
}
