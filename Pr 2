package P1;

import java.*;
import java.io.*;
import java.util.*;

public class Program
{
    public static void main(String[] args)
    {
        System.out.println("Задача 1");
        System.out.println("Исходный массив");
        Integer [] A1={15,135,23,-8,23,15,32,32,23,44,98};
        for (int i=0; i<A1.length;i++)
            System.out.print(A1[i]+" ");
        System.out.println();
        ArrayList<Integer> B1=problem1(A1);
        System.out.println("Массив без повторов");
        System.out.println(B1);
        System.out.println();


        System.out.println("Задача 2");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Введите число от 1 до 10");
        try
        {
            int x = Integer.parseInt(br.readLine());
            Integer[][] A2=problem2(x);
            for (int i=0; i<10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    System.out.print(A2[i][j]+" ");
                }
                System.out.println();
            }
        }
        catch (IOException ioExc)
        {
            System.out.println(ioExc);
        }
        System.out.println();


        System.out.println("Задача 3");
        System.out.println("Матрица случайных чисел");
        int A[][]=new int[5][5];
        for (int i=0; i<5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                A[i][j] = (int) (Math.random() * 20 - 10);
                System.out.print(A[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("Среднее арифметическое положительных чисел на параллели главной диагонали, расположенной выше над диагональю, равно ");
        System.out.println(problem3(A));
        System.out.println();


        System.out.println("Задача 4");
        System.out.println("Исходный массив");
        int[] b=new int[10];
        for (int i=0; i<b.length;i++)
        {
            b[i]=(int) (Math.random() * 20 - 10);
            System.out.print(b[i]+" ");
        }
        System.out.println();
        System.out.println("Новый массив");
        Integer[] C=problem4(b);
        for (int i=0; i<C.length;i++)
        {
            System.out.print(C[i]+" ");
        }
        System.out.println();
    }

    //возвращает массив, состоящий из неповторяющихся элементов массива A
    private static ArrayList<Integer> problem1(Integer[] A)
    {
        Arrays.sort(A);
        ArrayList<Integer> result=new ArrayList<Integer>();

        HashMap<Integer,Integer> hm=new HashMap<>();
        for (int i=0; i<A.length; i++)
        {
            if (hm.containsKey(A[i]))
            {
                int count=hm.get(A[i])+1;
                hm.put(A[i],count);
            }
            else
            {
                hm.put(A[i],1);
            }
        }

        Set<Integer> keys=hm.keySet();
        for(Integer x:keys)
        {
            if (hm.get(x)==1)
                result.add(x);
        }

        return  result;
    }

    //возвращает матрицу, заполненную случайными значениями, не равными заданному x
    private static Integer[][] problem2(int x)
    {
        Integer[][] A=new Integer[10][10];
        for (int i=0; i<10; i++)
            for (int j=0; j<10; j++)
            {
                int r=(int)(Math.random()*10+1);
                if (r==x)
                    r++;
                A[i][j]=r;
            }

        return A;
    }

    //возвращает среднее арифметическое положительных чисел на параллели главной диагонали, расположенной выше над диагональю
    private static double problem3(int A[][])
    {
        double average=0;
        int count=0;

        for (int i=0; i<A.length-1; i++)
        {
            if (A[i][i+1]>0)
            {
                average += A[i][i + 1];
                count++;
            }
        }

        average/=count;

        return average;
    }

    //извлекает из массива b отрицательные числа и возвращает массив С из этих чисел, отсортированный по возрастанию
    private static Integer[] problem4(int[] b)
    {
        int count=0;
        for (int i=0; i<b.length; i++)
        {
            if (b[i]<0)
                count++;
        }

        Integer[] C=new Integer[count];
        int j=0;
        for (int i=0;i<b.length;i++)
        {
            if(b[i]<0)
            {
                C[j] = b[i];
                j++;
            }
        }

        mySort(C);

        return C;
    }

    //сортировка методом выбора и перестановки
    private static <T extends Comparable<? super T>> void mySort(T[] array)
    {
        for (int i = 0; i < array.length - 1; ++i)
        {
            int minPos = i;
            for (int j = i + 1; j < array.length; ++j)
            {
                if (array[j].compareTo(array[minPos]) < 0)
                {
                    minPos = j;
                }
            }
            T saveValue = array[minPos];
            array[minPos] = array[i];
            array[i] = saveValue;
        }
    }
}
