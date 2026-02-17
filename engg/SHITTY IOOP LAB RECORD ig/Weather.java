import java.util.Scanner;

class Weather {
     double temperature;
     double humidity;
    public Weather(double temperature, double humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
    }
    static class Forecast {
        Weather weather;
        public Forecast(Weather weather) {
            this.weather = weather;
        }
        public String predictCondition() {
            double temp = weather.temperature;
            double hum = weather.humidity;
            if (temp > 30 && hum < 50) {
                return "Sunny";
            } else if (hum > 70) {
                return "Rainy";
            } else {
                return "Cloudy";
            }
        }

        public void displayForecast(String city) {
            System.out.println("City: " + city);
            System.out.println("Temperature: " + weather.temperature + "°C");
            System.out.println("Humidity: " + weather.humidity + "%");
            System.out.println("Predicted Weather: " + predictCondition());
            System.out.println("-----------------------------");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
      
        for (int i = 1; i <= 3; i++) {
            System.out.println("Enter city name:");
            String city = sc.nextLine();

            System.out.println("Enter temperature for " + city + ":");
            double temp = sc.nextDouble();

            System.out.println("Enter humidity for " + city + ":");
            double hum = sc.nextDouble();
            sc.nextLine(); // consume newline

            Weather w = new Weather(temp, hum);
            Forecast f = new Forecast(w);
            f.displayForecast(city);
        }

        sc.close();
    }
}
