import java.util.Scanner;
import java.awt.Color;
import java.io.File;
import java.io.FileNotFoundException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;
import java.awt.*;

public class Calculator extends JFrame {
    
    /** serial UID */
	private static final long serialVersionUID = 1L;

    /** Our JFrame and the title of the JFrame */
	private Frame frame = new Frame("Calculator");

    /** Our expression */
    private String expression;

    /** Our answer */
    private double answer;

    /** The Add JButton */
	private Button enter = new Button("Enter");

    /** One button */
    private Button one = new Button("1");

    /** Two button */
    private Button two = new Button("2");

    /** Three button */
    private Button three = new Button("3");

    /** Four button */
    private Button four = new Button("4");

    /** Five button */
    private Button five = new Button("5");

    /** Six button */
    private Button six = new Button("6");

    /** Seven button */
    private Button seven = new Button("7");

    /** Eight button */
    private Button eight = new Button("8");

    /** Nine button */
    private Button nine = new Button("9");

    /** One button */
    private Button zero = new Button("0");

    /** Decimal Button */
    private Button decimal = new Button(".");

    /** Left Parentheses */
    private Button left_paren = new Button("(");

    /** Right Parenteses */
    private Button right_paren = new Button(")");

    /** Addition */
    private Button add = new Button("+");

    /** Subtraction */
    private Button sub = new Button("-");

    /** Multiplication */
    private Button mul = new Button("*");

    /** Division */
    private Button div = new Button("/");

    /** Exponentiation */
    private Button exp = new Button("^");

    /** The Clear JButton */
	private Button clear = new Button("Clear");

    /** Exit calculator button */
    private Button exit = new Button("Exit");

    /** Our expression */
    private Label ourExp;

    /** Our answer */
    private Label ourAns;

    public Calculator() {
        initializeCalculator();
    }

    public Color getBackgroundColor() throws FileNotFoundException {
        Scanner scnr = new Scanner(new File("csc116/search_engine/color.txt"));
        String color = scnr.next();
        scnr.close();
        if (color.equals("red")) {
            return new Color(255, 0, 0);
        } else if (color.equals("green")) {
            return new Color(0, 255, 0);
        } else if (color.equals("blue")) {
            return new Color(0, 0, 255);
        } else if (color.equals("white")) {
            return new Color(255, 255, 255);
        } else if (color.equals("yellow")) {
            return new Color(255, 255, 0);
        } else if (color.equals("cyan")) {
            return new Color(0, 255, 255);
        } else {
            return new Color(255, 0, 255);
        }
    }

    public void addToExpression(char ch) {
        if (ch == '(' || ch == ')' || ch == '^') {
            expression += ch;
        } else if (ch == '.') {
            expression = expression.substring(0, expression.length() - 1) + ch;
        } else {
            expression += ch + " ";
        }
    }

    public void displayExpression() {
        frame.remove(ourExp);
        ourExp = new Label(expression);
        ourExp.setBounds(100, 100, 400, 50);
        frame.add(ourExp);
    }

    public void displayAnswer() {
        frame.remove(ourAns);
        ourAns = new Label(String.valueOf(answer));
        ourAns.setBounds(450, 100, 10, 10);
        frame.add(ourAns);
    }

    public void initializeCalculator() {

        // Initiate the expression and answer
        expression = "";
        ourExp = new Label(expression);
        ourExp.setBounds(100, 100, 400, 50);
        answer = 0;
        ourAns = new Label();
        ourAns.setBounds(450, 100, 10, 10);

        // Setup the panel
        try {
            frame.setBackground(getBackgroundColor());
        } catch (FileNotFoundException e) {
            JOptionPane.showMessageDialog(frame, "Error. Cannot load color");
        }
        frame.setVisible(true);
        frame.setLayout(null);

        // Set the sizes of our buttons
        zero.setBounds(50, 400, 50, 50);
        one.setBounds(125, 400, 50, 50);
        two.setBounds(200, 400, 50, 50);
        three.setBounds(275, 400, 50, 50);
        four.setBounds(125, 325, 50, 50);
        five.setBounds(200, 325, 50, 50);
        six.setBounds(275, 325, 50, 50);
        seven.setBounds(125, 250, 50, 50);
        eight.setBounds(200, 250, 50, 50);
        nine.setBounds(275, 250, 50, 50);
        left_paren.setBounds(350, 400, 50, 50);
        right_paren.setBounds(425, 400, 50, 50);
        decimal.setBounds(350, 325, 50, 50);
        add.setBounds(425, 325, 50, 50);
        sub.setBounds(350, 250, 50, 50);
        mul.setBounds(425, 250, 50, 50);
        div.setBounds(50, 325, 50, 50);
        exp.setBounds(50, 250, 50, 50);
        clear.setBounds(100, 175, 100, 50);
        enter.setBounds(300, 175, 100, 50);
        exit.setBounds(400, 50, 50, 20);

        // Add the action listeners
        exit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              System.exit(0);
            }
        });
        zero.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('0');
              displayExpression();
            }
        });
        one.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('1');
              displayExpression();
            }
        });
        two.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('2');
              displayExpression();
            }
        });
        three.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('3');
              displayExpression();
            }
        });
        four.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('4');
              displayExpression();
            }
        });
        five.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('5');
              displayExpression();
            }
        });
        six.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('6');
              displayExpression();
            }
        });
        seven.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('7');
              displayExpression();
            }
        });
        eight.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('8');
              displayExpression();
            }
        });
        nine.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('9');
              displayExpression();
            }
        });
        left_paren.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('(');
              displayExpression();
            }
        });
        right_paren.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression(')');
              displayExpression();
            }
        });
        add.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('+');
              displayExpression();
            }
        });
        sub.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('-');
              displayExpression();
            }
        });
        mul.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('*');
              displayExpression();
            }
        });
        div.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('/');
              displayExpression();
            }
        });
        decimal.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('.');
              displayExpression();
            }
        });
        exp.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              addToExpression('^');
              displayExpression();
            }
        });
        clear.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              expression = "";
              displayExpression();
            }
        });
        enter.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
              displayAnswer();
            }
        });


        // add our buttons to the frame
        frame.add(clear);
        frame.add(enter);
        frame.add(zero);
        frame.add(one);
        frame.add(two);
        frame.add(three);
        frame.add(four);
        frame.add(five);
        frame.add(six);
        frame.add(seven);
        frame.add(eight);
        frame.add(nine);
        frame.add(left_paren);
        frame.add(right_paren);
        frame.add(decimal);
        frame.add(add);
        frame.add(sub);
        frame.add(mul);
        frame.add(div);
        frame.add(exp);
        frame.add(exit);

        // Add our panel
        frame.setSize(500, 500);
        frame.show();
    }

    public static void main(String[] args) {
        @SuppressWarnings("unused")
        Calculator c = new Calculator();
    }
}
