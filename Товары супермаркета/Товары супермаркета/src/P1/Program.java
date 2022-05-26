package P1;

public class Program
{
    public static void main(String[] args)
    {
        ListOfProducts listOfProducts=new ListOfProducts();
        listOfProducts.Add(new Toy("Отдел игрушек", "Конструктор", "Китай", 700.34, "Лего Логистикс лтд", AgeGroup.Middle, "Развивающая игрушка"));
        listOfProducts.Add(new Toy("Отдел игрушек", "Кукла", "Польша", 599.92, "ООО Ромашка", AgeGroup.Younger, "Развлекающая игрушка"));
        listOfProducts.Add(new Fruit("Продовольственный", "Яблоки", "Россия", 100.51, "ООО Василёк",72, 25));
        listOfProducts.Add(new DimensionalProduct("мебельный", "стол", "Россия", 5478.22, "ООО Мебельная фабрика", 0.9, 0.6, 1.8));

        System.out.println(listOfProducts);
    }
}
