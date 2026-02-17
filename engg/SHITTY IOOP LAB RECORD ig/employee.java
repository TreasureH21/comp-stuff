import java.util.*;

class employee {
    class Department {
        String dep_name;
        String location;

        Department(String dep_name, String location) {
            this.dep_name = dep_name;
            this.location = location;
        }

        
        public void setDetails(String dep_name, String location) {
            this.dep_name = dep_name;
            this.location = location;
        }

        
        public void displayDepartment() {
            System.out.println("Department: " + dep_name + ", Location: " + location);
        }
    }

    
    String eName;
    double salary;
    Department[] depts;
    int deptCount;

    
    employee(String eName, double salary, int maxDepartments) {
        this.eName = eName;
        this.salary = salary;
        depts = new Department[maxDepartments];
        deptCount = 0;
    }

    
    public void addDepartment(String name, String location) {
        if (deptCount < depts.length) {
            depts[deptCount] = new Department(name, location);
            deptCount++;
        } else {
            System.out.println("Cannot add more departments.");
        }
    }

    
    public void displayEmployee() {
        System.out.println("Employee Name: " + eName);
        System.out.println("Salary: " + salary);
        System.out.println("Departments:");
        for (int i = 0; i < deptCount; i++) {
            depts[i].displayDepartment();
        }
    }

	public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter employee name:");
    String name = sc.nextLine();
    System.out.println("Enter salary:");
    double salary = sc.nextDouble();

    System.out.println("Enter number of departments:");
    int maxDepartments = sc.nextInt();
    sc.nextLine(); // consume newline

    employee emp = new employee(name, salary, maxDepartments);

    for (int i = 0; i < maxDepartments; i++) {
        System.out.println("Enter department name:");
        String deptName = sc.nextLine();
        System.out.println("Enter department location:");
        String location = sc.nextLine();
        emp.addDepartment(deptName, location);
    }

    emp.displayEmployee();
}
}
