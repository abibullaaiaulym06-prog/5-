import java.util.*;

// =======================
// ПАТТЕРН СТРАТЕГИЯ (Strategy)
// =======================

// 1. Интерфейс стратегии оплаты
interface PaymentStrategy {
    void pay(double amount);
}

// 2. Конкретные стратегии
class CreditCardPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("💳 Оплата банковской картой на сумму " + amount + " USD выполнена успешно.");
    }
}

class PayPalPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("💻 Оплата через PayPal на сумму " + amount + " USD выполнена успешно.");
    }
}

class CryptoPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("🪙 Оплата криптовалютой на сумму " + amount + " USD выполнена успешно.");
    }
}

// 3. Контекст, использующий стратегию
class PaymentContext {
    private PaymentStrategy strategy;

    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void executePayment(double amount) {
        if (strategy == null) {
            System.out.println("⚠️ Стратегия оплаты не выбрана!");
        } else {
            strategy.pay(amount);
        }
    }
}


// =======================
// ПАТТЕРН НАБЛЮДАТЕЛЬ (Observer)
// =======================

// 1. Интерфейсы наблюдателя и субъекта
interface Observer {
    void update(String currency, double rate);
}

interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

// 2. Конкретный субъект (Курсы валют)
class CurrencyExchange implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private Map<String, Double> rates = new HashMap<>();

    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }

    public void setRate(String currency, double rate) {
        rates.put(currency, rate);
        notifyObservers();
    }

    @Override
    public void notifyObservers() {
        for (Observer obs : observers) {
            for (Map.Entry<String, Double> rate : rates.entrySet()) {
                obs.update(rate.getKey(), rate.getValue());
            }
        }
    }
}

// 3. Конкретные наблюдатели
class BankObserver implements Observer {
    @Override
    public void update(String currency, double rate) {
        System.out.println("🏦 [Банк] Новый курс " + currency + ": " + rate);
    }
}

class BrokerObserver implements Observer {
    @Override
    public void update(String currency, double rate) {
        System.out.println("💼 [Брокер] Получил обновление курса " + currency + ": " + rate);
    }
}

class MobileAppObserver implements Observer {
    @Override
    public void update(String currency, double rate) {
        System.out.println("📱 [Мобильное приложение] Новый курс " + currency + ": " + rate);
    }
}


// =======================
// КЛИЕНТСКИЙ КОД
// =======================

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== ПАТТЕРН СТРАТЕГИЯ ===\n");

        PaymentContext context = new PaymentContext();

        System.out.println("Выберите способ оплаты:");
        System.out.println("1 — Банковская карта");
        System.out.println("2 — PayPal");
        System.out.println("3 — Криптовалюта");
        System.out.print("Ваш выбор: ");
        String choice = sc.nextLine();

        switch (choice) {
            case "1":
                context.setPaymentStrategy(new CreditCardPayment());
                break;
            case "2":
                context.setPaymentStrategy(new PayPalPayment());
                break;
            case "3":
                context.setPaymentStrategy(new CryptoPayment());
                break;
            default:
                System.out.println("❌ Неверный выбор!");
                return;
        }

        context.executePayment(150.0);

        System.out.println("\n=== ПАТТЕРН НАБЛЮДАТЕЛЬ ===\n");

        CurrencyExchange exchange = new CurrencyExchange();

        Observer bank = new BankObserver();
        Observer broker = new BrokerObserver();
        Observer app = new MobileAppObserver();

        exchange.attach(bank);
        exchange.attach(broker);
        exchange.attach(app);

        exchange.setRate("USD", 470.5);
        exchange.setRate("EUR", 510.3);

        System.out.println("\n📤 Брокер отписался от обновлений.\n");
        exchange.detach(broker);

        exchange.setRate("USD", 472.8);

        sc.close();
    }
}

