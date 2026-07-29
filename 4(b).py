import java.util.Scanner;

interface Calculator {
    void add(double num1, double num2);
    void subtract(double num1, double num2);
    void multiply(double num1, double num2);
    void divide(double num1, double num2);
}

class SimpleCalculator implements Calculator {

    public void add(double num1, double num2) {
        System.out.println("Addition = " + (num1 + num2));
    }

    public void subtract(double num1, double num2) {
        System.out.println("Subtraction = " + (num1 - num2));
    }

    public void multiply(double num1, double num2) {
        System.out.println("Multiplication = " + (num1 * num2));
    }

    public void divide(double num1, double num2) {
        if (num2 != 0)
            System.out.println("Division = " + (num1 / num2));
        else
            System.out.println("Division by zero is not possible.");
    }
}

public class InterfaceCalculator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter First Number: ");
        double num1 = sc.nextDouble();

        System.out.print("Enter Second Number: ");
        double num2 = sc.nextDouble();

        Calculator c = new SimpleCalculator();

        c.add(num1, num2);
        c.subtract(num1, num2);
        c.multiply(num1, num2);
        c.divide(num1, num2);

        sc.close();
    }
}
