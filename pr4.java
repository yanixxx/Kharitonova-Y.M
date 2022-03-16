public class pr4 {
        public static void main(String N[])
        {
            if(N.length==2)
            { int i = Integer.parseInt(N[0]);
                int i2 = Integer.parseInt(N[1]); System.out.println(N[0]+" + "+N[1]+" = "+(i+i2));
            }
            else
            {
                System.out.println("Неверное количество параметров");
            }
        }
    }

