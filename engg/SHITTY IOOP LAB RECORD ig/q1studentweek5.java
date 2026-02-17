import java.util.*;

class STUDENT {
    class Subject {
        String subjectName;
        int marks;

        Subject(String subjectName, int marks) {
            this.subjectName = subjectName;
            this.marks = marks;
        }

        public void assignMarks(int marks) {
            this.marks = marks;
        }

        public void displaySubject() {
            System.out.println("Subject: " + subjectName + ", Marks: " + marks);
        }

        public int getMarks() {
            return marks;
        }
    }

    Subject[] subjects;
    int subcount;

    STUDENT(int maxSubjects) {
        subjects = new Subject[maxSubjects];
        subcount = 0;
    }

    public void addSubject(String name, int marks) {
        if (subcount < subjects.length) {
            subjects[subcount] = new Subject(name, marks);
            subcount++;
        } else {
            System.out.println("Cannot add more subjects.");
        }
    }

    public void displaySubjects() {
        for (int i = 0; i < subcount; i++) {
            subjects[i].displaySubject();
        }
    }

    public int calculateTotal() {
        int total = 0;
        for (int i = 0; i < subcount; i++) {
            total += subjects[i].getMarks();
        }
        return total;
    }

    public double calculateAverage() {
        if (subcount == 0) return 0;
        return (double) calculateTotal() / subcount;
    }
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of subjects:");
        int maxSubjects = sc.nextInt();

        STUDENT student = new STUDENT(maxSubjects);

        for (int i = 0; i < maxSubjects; i++) {
            System.out.println("Enter the subject name:");
            String name = sc.next();
            System.out.println("Enter the marks:");
            int marks = sc.nextInt();
            student.addSubject(name, marks);
        }

        student.displaySubjects();
        System.out.println("Total Marks: " + student.calculateTotal());
        System.out.println("Average Marks: " + student.calculateAverage());
    }
}

