import java.util.*;

interface PaymentStrategy {
    void pay(double amount);
}

class CreditCardPayment implements PaymentStrategy {
    public void pay(double amount) {
        System.out.println("Оплата банковской картой: " + amount + " тг");
    }
}

class PayPalPayment implements PaymentStrategy {
    public void pay(double amount) {
        System.out.println("Оплата через PayPal: " + amount + " тг");
    }
}

class CryptoPayment implements PaymentStrategy {
    public void pay(double amount) {
        System.out.println("Оплата криптовалютой: " + amount + " тг");
    }
}

class PaymentContext {
    private PaymentStrategy strategy;
    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }
    public void executePayment(double amount) {
        if (strategy == null) {
            System.out.println("Способ оплаты не выбран!");
        } else {
            strategy.pay(amount);
        }
    }
}

interface Observer {
    void update(String currency, double rate);
}

interface Subject {
    void addObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}

class CurrencyExchange implements Subject {
    private Map<String, Double> rates = new HashMap<>();
    private List<Observer> observers = new ArrayList<>();
    public void addObserver(Observer o) {
        observers.add(o);
    }
    public void removeObserver(Observer o) {
        observers.remove(o);
    }
    public void notifyObservers() {
        for (Observer o : observers) {
            for (String currency : rates.keySet()) {
                o.update(currency, rates.get(currency));
            }
        }
    }
    public void setRate(String currency, double rate) {
        rates.put(currency, rate);
        System.out.println("\nНовый курс: " + currency + " = " + rate);
        notifyObservers();
    }
}

class BankDisplay implements Observer {
    public void update(String currency, double rate) {
        System.out.println("Банк получил обновление: " + currency + " = " + rate);
    }
}

class MobileAppDisplay implements Observer {
    public void update(String currency, double rate) {
        System.out.println("Мобильное приложение: " + currency + " = " + rate);
    }
}

class WebsiteDisplay implements Observer {
    public void update(String currency, double rate) {
        System.out.println("Сайт обновил курс: " + currency + " = " + rate);
    }
}

public class TravelAndStockSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("1 - Паттерн Стратегия (оплата)");
        System.out.println("2 - Паттерн Наблюдатель (валютные курсы)");
        System.out.print("Выберите: ");
        String choice = sc.nextLine();

        if (choice.equals("1")) {
            runStrategyDemo(sc);
        } else if (choice.equals("2")) {
            runObserverDemo();
        } else {
            System.out.println("Неверный выбор!");
        }
        sc.close();
    }

    private static void runStrategyDemo(Scanner sc) {
        PaymentContext context = new PaymentContext();
        System.out.println("\nВыберите способ оплаты:");
        System.out.println("1 - Банковская карта");
        System.out.println("2 - PayPal");
        System.out.println("3 - Криптовалюта");
        System.out.print("Ваш выбор: ");
        String option = sc.nextLine();

        switch (option) {
            case "1": context.setPaymentStrategy(new CreditCardPayment()); break;
            case "2": context.setPaymentStrategy(new PayPalPayment()); break;
            case "3": context.setPaymentStrategy(new CryptoPayment()); break;
            default:
                System.out.println("Неверный выбор!"); return;
        }

        System.out.print("Введите сумму оплаты: ");
        try {
            double amount = Double.parseDouble(sc.nextLine());
            context.executePayment(amount);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка: введите число!");
        }
    }

    private static void runObserverDemo() {
        CurrencyExchange exchange = new CurrencyExchange();
        Observer bank = new BankDisplay();
        Observer app = new MobileAppDisplay();
        Observer site = new WebsiteDisplay();
        exchange.addObserver(bank);
        exchange.addObserver(app);
        exchange.addObserver(site);
        exchange.setRate("USD", 475.50);
        exchange.setRate("EUR", 505.30);
        exchange.removeObserver(app);
        System.out.println("\nМобильное приложение отключено от уведомлений.");
        exchange.setRate("USD", 480.00);
    }
}
