# Spring Boot — Lesson 1: Why Spring Exists

Before writing a single Spring annotation, we need to understand **the problem Spring is solving**.

You already know Java OOP. That is exactly where we start.

---

## 1. Imagine a normal Java application

Suppose we are building a banking application.

We have:

```java
class AccountRepository {
    public Account findAccount(int id) {
        // database work
        return null;
    }
}
```

Then a service:

```java
class AccountService {

    private AccountRepository repository = new AccountRepository();

    public Account getAccount(int id) {
        return repository.findAccount(id);
    }
}
```

And a controller:

```java
class AccountController {

    private AccountService service = new AccountService();

    public Account getAccount(int id) {
        return service.getAccount(id);
    }
}
```

At first glance, this is perfectly reasonable.

The problem is this:

```text
AccountController
       ↓ creates
AccountService
       ↓ creates
AccountRepository
```

The classes are **tightly coupled**.

`AccountController` is not merely saying:

> "I need an AccountService."

It is saying:

> "I know exactly how to construct an AccountService."

And the service is doing the same thing with the repository.

---

# 2. Why is that a problem?

Imagine your repository eventually needs a database connection.

You change:

```java
private AccountRepository repository = new AccountRepository();
```

into something like:

```java
private AccountRepository repository =
        new AccountRepository(databaseConnection);
```

Now the service needs to know about the database connection.

Then perhaps the repository needs configuration.

Then the service needs a logger.

Then the logger needs configuration.

You start getting:

```text
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
   ↓
Configuration
```

with objects constructing other objects everywhere.

A large application can become difficult to manage.

---

# 3. What if objects were given their dependencies?

Instead of:

```java
class AccountService {

    private AccountRepository repository = new AccountRepository();

}
```

we could say:

```java
class AccountService {

    private AccountRepository repository;

    public AccountService(AccountRepository repository) {
        this.repository = repository;
    }
}
```

Now `AccountService` does **not create** the repository.

It simply says:

> "I need an AccountRepository."

Someone else provides it.

This is **Dependency Injection**.

---

# 4. You have actually already seen this idea

Consider:

```java
class Car {

    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

`Car` depends on `Engine`.

So:

```java
Engine engine = new Engine();
Car car = new Car(engine);
```

The `Engine` is injected into `Car`.

That is dependency injection.

There is nothing inherently magical about it.

**Spring's major job is to manage this process for you in a large application.**

---

# 5. Spring's basic idea

Instead of you doing:

```java
AccountRepository repository = new AccountRepository();

AccountService service =
        new AccountService(repository);

AccountController controller =
        new AccountController(service);
```

Spring can manage those objects.

Conceptually:

```text
                Spring
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
   Repository   Service  Controller
        │         │         │
        └─────────┴─────────┘
          dependencies
          connected
```

Spring creates and manages these objects and connects their dependencies.

These managed objects are called **beans**.

---

# 6. This gives us our first three terms

You will hear these constantly in Spring projects.

### Dependency

An object/class that another class needs.

```java
class AccountService {

    private AccountRepository repository;

}
```

`AccountService` has a dependency on `AccountRepository`.

### Dependency Injection

Providing that dependency from outside:

```java
AccountService(AccountRepository repository)
```

### Bean

An object that Spring creates and manages.

---

# 7. IoC — the bigger concept

You will also hear:

**IoC — Inversion of Control**

Normally, your code controls object creation:

```java
AccountService service = new AccountService(...);
```

With Spring, control over creating and managing these objects is moved to the Spring framework.

So instead of:

```text
Your code → creates objects
```

we have:

```text
Spring → creates/manages objects
Your code → uses them
```

That reversal of control is **Inversion of Control**.

Dependency Injection is one way of achieving IoC.

Think of the relationship as:

```text
IoC
 │
 └── Dependency Injection
```

---

# 8. One important distinction

Do not memorize:

> "Spring = dependency injection."

That is too narrow.

Spring is a large ecosystem/framework that provides many things:

```text
Spring
├── Dependency Injection / IoC
├── Web development
├── REST APIs
├── Database integration
├── Transactions
├── Security
├── Testing support
└── much more
```

But **IoC/Dependency Injection is one of the foundational ideas you need to understand first.**

---

# Prediction problem

Before we touch Spring annotations, answer this:

Suppose we have:

```java
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }
}
```

and:

```java
class PaymentRepository {
}
```

### Question 1

Is `PaymentRepository` a dependency of `PaymentService`?

### Question 2

Is this dependency injection?

### Question 3

Who is creating `PaymentRepository` in this code?

### Question 4

If we later use Spring, what do you think Spring's role will be?

Answer these four, and then we will move into **Beans, ApplicationContext, and our first actual Spring Boot application**.


# Spring Lesson 2 — What is a Bean?

Now that you understand **dependency injection**, we can introduce the first Spring term that actually matters.

And we will keep it simple.

---

## 1. Start with something you already know

Suppose we have:

```java
class PaymentService {

    public void makePayment() {
        System.out.println("Payment made");
    }
}
```

Nothing special here. It is just a Java class.

If we want an object:

```java
PaymentService service = new PaymentService();
```

Now `service` is an **object of `PaymentService`**.

You already know this.

---

# 2. What does Spring add?

Suppose we tell Spring:

> "Spring, I want you to create and manage a `PaymentService` object for me."

We can do that with:

```java
@Service
class PaymentService {

    public void makePayment() {
        System.out.println("Payment made");
    }
}
```

Now Spring sees `@Service` and essentially thinks:

> "Okay, `PaymentService` is something I should manage."

Spring creates an object of that class.

That object is called a **Bean**.

So:

```text id="p0m4ad"
PaymentService
      ↓
   class

Spring creates an object
      ↓
PaymentService object
      ↓
     Bean
```

That is the basic meaning.

---

# 3. Bean does NOT mean a special kind of Java object

This is important.

A Bean is not some completely different thing.

It is still an ordinary Java object.

For example:

```java
PaymentService service = new PaymentService();
```

That is an ordinary Java object.

If Spring creates and manages the object:

```text id="1ftrm3"
PaymentService object
        ↓
managed by Spring
        ↓
       Bean
```

So when you hear:

> "Spring Bean"

translate it in your head to:

> **"An object that Spring is managing."**

That is enough for now.

---

# 4. Why does Spring need to manage objects?

Remember our previous example.

We had:

```text id="f4k3b1"
Controller
    ↓
Service
    ↓
Repository
```

Suppose:

```java
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }
}
```

Somebody needs to create this:

```java
PaymentRepository repository = new PaymentRepository();

PaymentService service =
        new PaymentService(repository);
```

If Spring manages both objects, Spring can do this for us.

Conceptually:

```text id="f7r3nq"
                Spring
                  │
          ┌───────┴───────┐
          ↓               ↓
 PaymentRepository   PaymentService
                         ↑
                         │
                   needs repository
                         │
                         └──── Spring gives it
```

So now we have two important ideas:

**Bean**

> An object that Spring manages.

**Dependency Injection**

> Spring gives one Bean the other Bean it needs.

---

# 5. How does Spring know which classes to manage?

There are several ways.

You will commonly see:

```java
@Component
```

```java
@Service
```

```java
@Repository
```

and:

```java
@Controller
```

For now, do not worry about their differences.

Notice something interesting:

```java
@Service
class PaymentService
```

and:

```java
@Repository
class PaymentRepository
```

Both tell Spring:

> "Create and manage an object of this class."

The different annotations mainly communicate **what role that class has in the application**.

We will learn those roles properly later.

---

# 6. One more piece: the Application Context

You are going to see this term everywhere, so let us make it simple.

If Spring is managing hundreds of objects, it needs somewhere to keep track of them.

That system is called the **Application Context**.

Think of it like Spring's collection of managed objects:

```text id="qz6l6y"
Application Context
│
├── PaymentService object
├── PaymentRepository object
├── UserService object
├── UserRepository object
├── OrderService object
└── ...
```

So:

> **Application Context = the place/system where Spring keeps and manages its Beans.**

You do not need to worry about its implementation right now.

---

# 7. Put everything together

We now have:

```text id="h4crf2"
Java Class
    ↓
Spring sees @Service / @Repository / etc.
    ↓
Spring creates an object
    ↓
That object is a Bean
    ↓
Bean lives in the Application Context
    ↓
Spring can give that Bean to another Bean
    ↓
Dependency Injection
```

That is already enough to understand the foundation of Spring.

---

## PP — Prediction Problem

Consider:

```java
@Repository
class PaymentRepository {

}
```

and:

```java
@Service
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }
}
```

Answer these **without worrying about exact Spring syntax yet**:

**Q1.** How many Beans will Spring potentially create here?

**Q2.** What are those Beans?

**Q3.** Does `PaymentService` create the `PaymentRepository` object itself?

**Q4.** If Spring is managing both objects, who can provide the `PaymentRepository` to `PaymentService`?

**Q5.** In your own words, what is a Spring Bean?

After this, we will make our **first actual Spring Boot application** and see these ideas happen in code.


# Spring Lesson 3 — Your First Dependency Injection

Now we are going to make the thing we have been discussing actually happen.

We will start with **constructor injection**, because it is the clearest form and it matches the Java you already understand.

---

## 1. Our two classes

Imagine:

```java
class PaymentRepository {

    public void savePayment() {
        System.out.println("Payment saved");
    }
}
```

And:

```java
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }

    public void makePayment() {
        repository.savePayment();
    }
}
```

Forget Spring for a second.

If we wanted to use this ourselves:

```java
PaymentRepository repository = new PaymentRepository();

PaymentService service =
        new PaymentService(repository);

service.makePayment();
```

We understand exactly what is happening.

```text
we create Repository
        ↓
we create Service
        ↓
we give Repository to Service
        ↓
Service uses Repository
```

That is plain Java.

---

# 2. Now let Spring do it

We tell Spring:

```java
@Repository
class PaymentRepository {

    public void savePayment() {
        System.out.println("Payment saved");
    }
}
```

And:

```java
@Service
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }

    public void makePayment() {
        repository.savePayment();
    }
}
```

Now Spring sees:

```java
@Repository
```

and:

```java
@Service
```

and says, essentially:

> "I need to create objects for both of these classes."

So Spring creates:

```text
PaymentRepository object
        ↓
      Bean

PaymentService object
        ↓
      Bean
```

---

# 3. But there is still a question

How does Spring know that:

```java
PaymentService
```

needs:

```java
PaymentRepository
```

Look at the constructor:

```java
public PaymentService(PaymentRepository repository)
```

Spring sees that and understands:

> "To create a `PaymentService`, I need to give its constructor a `PaymentRepository`."

And Spring already has one:

```text
PaymentRepository Bean
```

So Spring essentially does the equivalent of:

```java
PaymentRepository repository =
        new PaymentRepository();

PaymentService service =
        new PaymentService(repository);
```

**You did not write those `new` statements.**

Spring did it.

That is the magic we were building toward.

---

# 4. This is Dependency Injection

Spring takes:

```text
PaymentRepository Bean
```

and puts it into:

```text
PaymentService Bean
```

So:

```text
PaymentRepository
        ↓
     provided to
        ↓
PaymentService
```

That is **Dependency Injection**.

And because we are doing it through the constructor, this particular form is called:

> **Constructor Injection**

---

# 5. What happens when the application starts?

Very roughly, Spring does something like:

```text
Application starts
       ↓
Spring starts
       ↓
Spring looks for classes it should manage
       ↓
Finds @Repository
       ↓
Creates PaymentRepository
       ↓
Finds @Service
       ↓
Sees PaymentService needs PaymentRepository
       ↓
Gives PaymentRepository to PaymentService
       ↓
PaymentService is created
       ↓
Application is ready
```

You do not manually create these objects.

---

# 6. And this is where Spring becomes genuinely useful

Imagine your service needed **three things**:

```java
@Service
class PaymentService {

    private PaymentRepository repository;
    private EmailService emailService;
    private NotificationService notificationService;

    public PaymentService(
            PaymentRepository repository,
            EmailService emailService,
            NotificationService notificationService) {

        this.repository = repository;
        this.emailService = emailService;
        this.notificationService = notificationService;
    }
}
```

Without Spring, somewhere you would need:

```java
PaymentRepository repository = new PaymentRepository();
EmailService emailService = new EmailService();
NotificationService notificationService =
        new NotificationService();

PaymentService service =
        new PaymentService(
                repository,
                emailService,
                notificationService
        );
```

And imagine doing this across a real application with **hundreds of classes**.

Spring takes responsibility for managing that object creation and connection.

That is one of the biggest reasons Spring exists.

---

# 7. One thing I want you to notice

Look at `PaymentService`:

```java
@Service
class PaymentService {

    private PaymentRepository repository;

    public PaymentService(PaymentRepository repository) {
        this.repository = repository;
    }
}
```

The class itself does **not care where the repository came from**.

It just says:

> "Give me a `PaymentRepository`."

That is a very powerful design principle.

The service does not need to know:

* who created it
* when it was created
* where it was created
* how it was configured

It just gets the object it needs.

---

# PP — Let's see if this actually clicked

Suppose we have:

```java
@Repository
class UserRepository {

    public void save() {
        System.out.println("User saved");
    }
}
```

```java
@Service
class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public void createUser() {
        repository.save();
    }
}
```

Now imagine we add:

```java
@Service
class EmailService {

    public void sendEmail() {
        System.out.println("Email sent");
    }
}
```

And change `UserService`:

```java
@Service
class UserService {

    private UserRepository repository;
    private EmailService emailService;

    public UserService(
            UserRepository repository,
            EmailService emailService) {

        this.repository = repository;
        this.emailService = emailService;
    }

    public void createUser() {
        repository.save();
        emailService.sendEmail();
    }
}
```

### Your prediction:

When Spring starts:

**Q1.** How many Beans will Spring create?

**Q2.** Which objects will be Beans?

**Q3.** What two things does `UserService` need?

**Q4.** Who creates those two objects?

**Q5.** Who gives those objects to `UserService`?

And one slightly deeper question:

**Q6.** If I remove `@Repository` from `UserRepository`, what do you predict will happen when Spring tries to create `UserService`?

Don't worry about being 100% certain on Q6. That one is designed to make you think.


# Spring Boot Lesson 4 — Our First Real Application

Now we are going to stop talking about Spring abstractly and **build one**.

The goal of this lesson is not to build anything impressive. It is to understand what happens when a Spring Boot application starts.

---

## 1. First, what are we building?

Very simple:

```text
User
  ↑
  │
UserRepository
  ↑
  │
UserService
  ↑
  │
UserController
```

Eventually, someone will send a request to our application:

```text
GET /users/1
```

and it will travel:

```text
Browser/Postman
      ↓
UserController
      ↓
UserService
      ↓
UserRepository
```

But **we are not worrying about HTTP yet**.

First, we want Spring to create these objects and connect them.

---

# 2. Create the Spring Boot project

Since you are using Maven, the project will have roughly this structure:

```text
my-spring-app/
│
├── pom.xml
│
└── src/
    └── main/
        └── java/
            └── com/example/demo/
                │
                ├── DemoApplication.java
                ├── UserController.java
                ├── UserService.java
                └── UserRepository.java
```

Do not worry about every folder yet.

The important thing is that we have a Maven project and some Java classes.

---

# 3. The main class

Spring Boot gives us something like:

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

You already understand:

```java
public static void main(String[] args)
```

That is where our Java application starts.

The unfamiliar part is:

```java
SpringApplication.run(...)
```

For now, think:

> **Start the Spring application.**

When this runs, Spring starts doing all the work we have been discussing.

---

# 4. Our Repository

Create:

```java
package com.example.demo;

import org.springframework.stereotype.Repository;

@Repository
public class UserRepository {

    public void saveUser() {
        System.out.println("User saved");
    }
}
```

The important part is:

```java
@Repository
```

We are telling Spring:

> "Create and manage an object of this class."

So when Spring starts, we get:

```text
UserRepository class
        ↓
Spring creates object
        ↓
UserRepository Bean
```

---

# 5. Our Service

Now:

```java
package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public void createUser() {
        repository.saveUser();
    }
}
```

Look at the constructor:

```java
public UserService(UserRepository repository)
```

We already understand this from our previous lessons.

`UserService` says:

> "I need a `UserRepository`."

Spring sees:

```java
@Repository
public class UserRepository
```

and knows:

> "I have a `UserRepository` Bean."

So Spring effectively does:

```java
UserRepository repository =
        new UserRepository();

UserService service =
        new UserService(repository);
```

You did not write those `new` statements.

**Spring handles it.**

---

# 6. Now let's actually prove it

For the moment, we will make our application print something.

Modify `UserService`:

```java
@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;

        System.out.println("UserService created");
    }

    public void createUser() {
        repository.saveUser();
    }
}
```

And:

```java
@Repository
public class UserRepository {

    public UserRepository() {
        System.out.println("UserRepository created");
    }

    public void saveUser() {
        System.out.println("User saved");
    }
}
```

Now run the application.

You should see something along the lines of:

```text
UserRepository created
UserService created
```

That is Spring creating our objects.

---

# 7. But we have not created UserService anywhere

Look at our `main()`:

```java
public static void main(String[] args) {
    SpringApplication.run(DemoApplication.class, args);
}
```

Where did we write:

```java
new UserRepository();
```

Nowhere.

Where did we write:

```java
new UserService(...);
```

Nowhere.

Yet the objects were created.

**That is Spring doing its job.**

---

# 8. And now we add the Controller

Create:

```java
package com.example.demo;

import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    private UserService service;

    public UserController(UserService service) {
        this.service = service;
    }
}
```

Now we have:

```text
UserController
      ↓ needs
UserService
      ↓ needs
UserRepository
```

And we tell Spring:

```text
@RestController → manage UserController
@Service        → manage UserService
@Repository     → manage UserRepository
```

Spring can therefore build the whole chain:

```text
UserRepository
      ↓
UserService
      ↓
UserController
```

Conceptually:

```text
Spring
  │
  ├── creates UserRepository
  │
  ├── creates UserService
  │       └── gives it UserRepository
  │
  └── creates UserController
          └── gives it UserService
```

**This is the first real Spring architecture you need to understand.**

---

# 9. One thing we have NOT done yet

Our controller currently does absolutely nothing.

That is intentional.

We have only established:

> **Spring can create our objects and connect them together.**

Next, we will give the controller an actual job:

```text
GET /users
```

Then you will finally see why we have:

* Controller
* Service
* Repository

and what actually happens when a request enters a Spring application.

---

## Your turn

Before we move forward, I want you to actually create this tiny project on your machine.

Do **not** worry about understanding every line of the generated Maven/Spring Boot project yet.

Once you have it running, tell me what output you get from:

```text
UserRepository created
UserService created
```

and then we will build our **first actual REST endpoint**.

# Spring Boot Lesson 5 — What Does a Controller Actually Do?

Now we get into the part that makes Spring Boot feel like **backend development**.

So far, we have:

```text
UserController
      ↓
UserService
      ↓
UserRepository
```

But you asked earlier: **"What actually is a controller?"**

Let us answer that properly.

---

## 1. Forget Spring for a moment

Imagine you have a website or mobile app.

A user clicks:

> "Show me user #15"

The frontend needs to communicate with your backend.

It might send an HTTP request:

```text
GET /users/15
```

Your Java application receives that request.

But which Java class should handle it?

That is one of the jobs of a **Controller**.

Think of a controller as the **entry point for requests coming into your backend**.

```text
Frontend
   ↓
HTTP request
   ↓
Controller
```

---

# 2. Our controller

We can write:

```java
@RestController
public class UserController {

    @GetMapping("/users")
    public String getUsers() {
        return "Here are the users";
    }
}
```

Now Spring understands:

> When someone sends `GET /users`, call `getUsers()`.

That is what this means:

```java
@GetMapping("/users")
```

You can read it as:

> **"When a GET request comes to `/users`, run this method."**

---

# 3. Let's actually call it

Start your Spring Boot application.

Then open a browser and go to:

```text
http://localhost:8080/users
```

Your browser sends:

```text
GET /users
```

Spring sees:

```java
@GetMapping("/users")
```

and calls:

```java
getUsers()
```

which returns:

```text
Here are the users
```

So the flow is:

```text
Browser
   │
   │ GET /users
   ↓
Spring
   ↓
UserController
   ↓
getUsers()
   ↓
"Here are the users"
   ↓
Browser
```

That is a REST endpoint.

---

# 4. But our controller should not do all the work

This is where the **Service** comes back in.

Suppose we want to actually retrieve users.

We could technically write:

```java
@RestController
public class UserController {

    @GetMapping("/users")
    public String getUsers() {

        // database code
        // business logic
        // calculations
        // validation
        // etc.

        return "...";
    }
}
```

But that becomes a mess.

The Controller's job is primarily:

> **Receive the request and hand the work to the appropriate part of the application.**

So we do:

```java
@RestController
public class UserController {

    private UserService service;

    public UserController(UserService service) {
        this.service = service;
    }

    @GetMapping("/users")
    public String getUsers() {
        return service.getUsers();
    }
}
```

Now:

```text
Request
   ↓
Controller
   ↓
Service
```

---

# 5. What does the Service do?

Now we can put the actual application logic here:

```java
@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public String getUsers() {

        // application/business logic

        return repository.getUsers();
    }
}
```

And the Repository handles the data:

```java
@Repository
public class UserRepository {

    public String getUsers() {

        // eventually:
        // query the database

        return "Users from database";
    }
}
```

Now the whole request travels through our application:

```text
              GET /users
                   ↓
             ┌───────────┐
             │ Controller│
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │  Service  │
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │ Repository│
             └─────┬─────┘
                   ↓
               Database
```

And the response comes back up:

```text
Database
   ↓
Repository
   ↓
Service
   ↓
Controller
   ↓
HTTP response
   ↓
Frontend
```

---

# 6. This is the architecture you will constantly see

When you open a real Spring Boot project at your company, you may see folders such as:

```text
controller/
service/
repository/
entity/
dto/
config/
exception/
```

Now you have a basic mental model for the first three:

### Controller

**Receives requests.**

### Service

**Does the application's/business logic.**

### Repository

**Deals with getting/storing data.**

These are not special Java things.

They are simply **different classes with different responsibilities**, and Spring helps manage them.

---

# 7. One important thing about `@RestController`

Earlier we had:

```java
@RestController
public class UserController
```

What does this actually tell Spring?

It tells Spring:

> "This class is a controller, and its methods can handle HTTP requests and return data as HTTP responses."

So:

```java
@GetMapping("/users")
public String getUsers() {
    return "Hello";
}
```

means:

```text
GET /users
   ↓
getUsers()
   ↓
"Hello"
```

We will later replace `"Hello"` with actual Java objects.

For example:

```java
@GetMapping("/users")
public User getUser() {
    return userService.getUser();
}
```

Spring can turn that Java object into JSON for the HTTP response.

That is where Spring Boot starts becoming extremely useful.

---

# PP — Let's test your understanding

Imagine we have:

```java
@RestController
public class UserController {

    private UserService service;

    public UserController(UserService service) {
        this.service = service;
    }

    @GetMapping("/users")
    public String getUsers() {
        return service.getUsers();
    }
}
```

and:

```java
@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public String getUsers() {
        return repository.getUsers();
    }
}
```

and:

```java
@Repository
public class UserRepository {

    public String getUsers() {
        return "Khushal, Rahul, Amit";
    }
}
```

### Predict what happens when someone visits:

```text
GET /users
```

Answer these:

**Q1.** Which method gets called first?

**Q2.** Which method does the Controller call?

**Q3.** Which method does the Service call?

**Q4.** What does the Repository return?

**Q5.** What ultimately gets sent back to the person who made the request?

**Q6.** Why did we not simply put `repository.getUsers()` directly inside the Controller?

# Spring Lesson 6 — Java Objects → JSON

Now we make our API behave more like a real backend.

So far, we returned:

```java
return "Khushal, Rahul, Amit";
```

But real APIs usually return **structured data**, usually JSON.

---

## 1. First, create a `User`

You already know how to create a Java class:

```java
public class User {

    private int id;
    private String name;

    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
```

Nothing Spring-specific here.

It's just a Java class.

We can create an object:

```java
User user = new User(1, "Khushal");
```

---

## 2. What if our Controller returns this?

```java
@GetMapping("/users")
public User getUser() {
    return new User(1, "Khushal");
}
```

Notice something strange.

Our Java method says:

```java
public User
```

It returns a **Java object**.

But HTTP doesn't send Java objects over the internet.

It sends data.

Spring therefore converts the object into JSON.

Conceptually:

```text
Java object
    ↓
Spring
    ↓
JSON
```

So the person calling:

```text
GET /users
```

would receive something like:

```json
{
    "id": 1,
    "name": "Khushal"
}
```

You don't have to manually construct that JSON string.

Spring handles the conversion.

---

# 3. Let's return multiple users

A real `/users` endpoint would probably return multiple users.

We can use a `List`, which you already know:

```java
@GetMapping("/users")
public List<User> getUsers() {

    List<User> users = new ArrayList<>();

    users.add(new User(1, "Khushal"));
    users.add(new User(2, "Rahul"));
    users.add(new User(3, "Amit"));

    return users;
}
```

Our Java code produces:

```text
List<User>
```

Spring converts it to JSON:

```json
[
    {
        "id": 1,
        "name": "Khushal"
    },
    {
        "id": 2,
        "name": "Rahul"
    },
    {
        "id": 3,
        "name": "Amit"
    }
]
```

This is a **very important thing to understand**:

> Your Spring Controller can return normal Java objects, and Spring handles turning them into JSON for the HTTP response.

---

# 4. But remember our architecture

We don't want the Controller creating all the users.

We want:

```text
Controller
    ↓
Service
    ↓
Repository
```

So let's move the code.

### Repository

```java
@Repository
public class UserRepository {

    public List<User> getUsers() {

        List<User> users = new ArrayList<>();

        users.add(new User(1, "Khushal"));
        users.add(new User(2, "Rahul"));
        users.add(new User(3, "Amit"));

        return users;
    }
}
```

The repository is currently pretending that these users came from a database.

Later, it really will get them from MySQL.

---

### Service

```java
@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public List<User> getUsers() {
        return repository.getUsers();
    }
}
```

The Service asks the Repository for the users.

---

### Controller

```java
@RestController
public class UserController {

    private UserService service;

    public UserController(UserService service) {
        this.service = service;
    }

    @GetMapping("/users")
    public List<User> getUsers() {
        return service.getUsers();
    }
}
```

Now our complete flow is:

```text
GET /users
     ↓
UserController
     ↓
UserService
     ↓
UserRepository
     ↓
List<User>
     ↓
Spring converts it to JSON
     ↓
HTTP response
```

---

# 5. Something important happened here

Look at the Controller:

```java
public List<User> getUsers() {
    return service.getUsers();
}
```

The Controller doesn't know:

* where the users came from
* whether they're in MySQL
* whether they're in a file
* how they're stored
* how they're retrieved

It just asks the Service:

> "Give me the users."

The Service doesn't need to know how the Controller received the request.

It asks the Repository:

> "Give me the users."

And the Repository handles getting the data.

That's the separation we were talking about earlier.

---

# 6. One thing to notice about JSON

Our Java class is:

```java
public class User {

    private int id;
    private String name;
}
```

Spring can turn:

```java
User(1, "Khushal")
```

into:

```json
{
    "id": 1,
    "name": "Khushal"
}
```

This process is called **serialization**.

You don't need to memorize that word yet. Just recognize it when you see it.

The reverse process is also possible:

```text
JSON
  ↓
Java object
```

That's called **deserialization**.

We'll use that when we start accepting data through `POST` requests.

---

# PP

Imagine our Controller contains:

```java
@GetMapping("/users")
public List<User> getUsers() {
    return service.getUsers();
}
```

The Service:

```java
public List<User> getUsers() {
    return repository.getUsers();
}
```

And the Repository returns:

```java
return List.of(
    new User(1, "Khushal"),
    new User(2, "Rahul")
);
```

### Q1.

What does the Repository return to the Service?

### Q2.

What does the Service return to the Controller?

### Q3.

Does the Controller receive JSON from the Service?

### Q4.

Who converts the `List<User>` into JSON?

### Q5.

What would the person calling `GET /users` actually receive?

### Q6.

Why is returning `List<User>` better than manually returning a string like `"Khushal, Rahul"`?

After this, we'll move to **POST requests**, where you'll see JSON coming *into* your Java application rather than just going out.


# Spring Lesson 7 — POST: JSON → Java Object

This is the other half of what we just learned.

Earlier:

```text
Java object
    ↓
Spring
    ↓
JSON
    ↓
Client
```

Now we're going in the opposite direction:

```text
Client
   ↓
JSON
   ↓
Spring
   ↓
Java object
```

This is how a frontend can **send data to your backend**.

---

## 1. Imagine creating a user

Suppose the frontend has a form:

```text
Name: Khushal
Age: 22
```

When the user clicks **Create User**, the frontend could send:

```json
{
    "name": "Khushal",
    "age": 22
}
```

to:

```text
POST /users
```

So the request looks conceptually like:

```text
Frontend
   ↓
POST /users

{
    "name": "Khushal",
    "age": 22
}
```

---

# 2. How does our Controller receive this?

We can write:

```java
@PostMapping("/users")
public String createUser(@RequestBody User user) {
    return "User received: " + user.getName();
}
```

There are two new things here:

```java
@PostMapping("/users")
```

and:

```java
@RequestBody User user
```

Let's understand them separately.

---

## 3. `@PostMapping`

Previously we had:

```java
@GetMapping("/users")
```

which means:

> When a **GET** request comes to `/users`, call this method.

Now:

```java
@PostMapping("/users")
```

means:

> When a **POST** request comes to `/users`, call this method.

So:

```text
GET /users
```

and:

```text
POST /users
```

can have completely different purposes.

For example:

```text
GET  /users → give me users
POST /users → create a user
```

Same URL.

Different HTTP method.

---

# 4. What is `@RequestBody`?

This is the important part.

The client sends:

```json
{
    "name": "Khushal",
    "age": 22
}
```

We want Spring to turn that JSON into:

```java
User user
```

So we write:

```java
@RequestBody User user
```

You can mentally read that as:

> **"Take the data in the request body and give me a `User` object."**

Spring handles the conversion.

So:

```text
JSON
 ↓
Spring
 ↓
User object
```

---

# 5. What does Spring actually give us?

Suppose the client sends:

```json
{
    "name": "Khushal",
    "age": 22
}
```

Inside our method:

```java
@PostMapping("/users")
public String createUser(@RequestBody User user) {

    System.out.println(user.getName());
    System.out.println(user.getAge());

    return "User received";
}
```

`user` is now an ordinary Java object.

Conceptually:

```java
User user = new User("Khushal", 22);
```

You didn't manually write that conversion.

Spring did it.

---

# 6. Notice the symmetry

We now have both directions.

### GET

```text id="vymx0j"
Database
   ↓
Repository
   ↓
Service
   ↓
Controller
   ↓
Java objects
   ↓
Spring
   ↓
JSON
   ↓
Client
```

### POST

```text id="l3nh2c"
Client
   ↓
JSON
   ↓
Spring
   ↓
Java object
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
```

This is the basic shape of a huge number of Spring Boot applications.

---

# 7. Let's put Service back into the picture

We don't want the Controller doing everything.

So:

```java
@RestController
public class UserController {

    private UserService service;

    public UserController(UserService service) {
        this.service = service;
    }

    @PostMapping("/users")
    public String createUser(@RequestBody User user) {
        return service.createUser(user);
    }
}
```

Then:

```java
@Service
public class UserService {

    private UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public String createUser(User user) {
        repository.saveUser(user);

        return "User created";
    }
}
```

And:

```java
@Repository
public class UserRepository {

    public void saveUser(User user) {
        System.out.println(
            "Saving " + user.getName()
        );
    }
}
```

So the request travels:

```text
POST /users
      ↓
Controller
      ↓
Service
      ↓
Repository
```

---

# 8. Where is the database?

We don't have one yet.

Our Repository is currently pretending:

```java
public void saveUser(User user) {
    System.out.println("Saving " + user.getName());
}
```

Later, this could actually do something like:

```text
INSERT INTO users (...)
```

and save the user into MySQL.

That's why we separated Repository from Service in the first place.

---

# 9. One thing I want you to notice

The Controller doesn't need to know **how** the user gets saved.

It simply says:

```java
service.createUser(user);
```

The Service doesn't need to know **how the database works**.

It says:

```java
repository.saveUser(user);
```

And eventually the Repository handles the database.

Each class has a relatively simple job.

---

# PP

The frontend sends:

```json
{
    "name": "Rahul",
    "age": 25
}
```

to:

```text
POST /users
```

Our Controller has:

```java
@PostMapping("/users")
public String createUser(@RequestBody User user) {
    return service.createUser(user);
}
```

### Q1.

Which Controller method gets called?

### Q2.

What does `@RequestBody` tell Spring to do?

### Q3.

Inside `createUser()`, what is the type of `user`?

### Q4.

Does the Controller receive a JSON string or a Java `User` object?

### Q5.

After receiving the `User`, which method does the Controller call?

### Q6.

Why don't we put the database-saving code directly inside the Controller?

### Q7 — important

For:

```text
GET /users
```

we were **getting data**.

For:

```text
POST /users
```

we are **sending data to the backend**.

Why do you think we use **two different HTTP methods** instead of just using `GET` for both?


# Spring Lesson 8 — Getting Data From the URL

We now know two ways a request can carry information into our backend:

```text
POST /users
       ↓
    Request Body
       ↓
     User object
```

But sometimes the information is already in the URL.

There are two very common ways:

1. **Path variable**
2. **Query parameter**

These are extremely common in real Spring projects.

---

# 1. Path Variable

Suppose we want to get a specific user:

```text
GET /users/25
```

Here, `25` is part of the URL.

We can write:

```java
@GetMapping("/users/{id}")
public String getUser(@PathVariable int id) {
    return "User id: " + id;
}
```

The important parts are:

```java
"/users/{id}"
```

and:

```java
@PathVariable int id
```

The `{id}` says:

> "There will be some value here."

So if someone requests:

```text
GET /users/25
```

Spring takes:

```text
25
```

and puts it into:

```java
int id
```

So inside the method:

```java
System.out.println(id);
```

would print:

```text
25
```

---

# 2. Why is this useful?

Because we can use that ID to find a particular user.

For example:

```java
@GetMapping("/users/{id}")
public User getUser(@PathVariable int id) {
    return service.getUser(id);
}
```

Now:

```text
GET /users/25
       ↓
id = 25
       ↓
service.getUser(25)
```

Then:

```text
Service
   ↓
Repository
   ↓
Find user with ID 25
```

This is probably one of the most common patterns you'll see.

---

# 3. Query Parameters

Now imagine we don't want one particular user.

Maybe we want to search users by name.

We could have:

```text
GET /users?name=Khushal
```

Here:

```text
name=Khushal
```

is a **query parameter**.

In Spring:

```java
@GetMapping("/users")
public String searchUsers(@RequestParam String name) {
    return "Searching for: " + name;
}
```

So:

```text
GET /users?name=Khushal
```

results in:

```java
name = "Khushal"
```

---

# 4. Path Variable vs Query Parameter

This distinction is worth understanding.

### Path variable

```text
/users/25
```

Think:

> **"I want resource number 25."**

```java
@PathVariable int id
```

### Query parameter

```text
/users?name=Khushal
```

Think:

> **"I want users, with this additional condition/filter."**

```java
@RequestParam String name
```

---

# 5. Multiple query parameters

You can have several:

```text
GET /users?name=Khushal&age=22
```

and:

```java
@GetMapping("/users")
public String searchUsers(
        @RequestParam String name,
        @RequestParam int age) {

    return name + " " + age;
}
```

Spring gives:

```text
name → "Khushal"
age  → 22
```

---

# 6. Putting the three methods together

You now have three different ways of getting information into your Java code.

### Request body

```text
POST /users
```

with:

```json
{
    "name": "Khushal",
    "age": 22
}
```

Spring:

```java
@RequestBody User user
```

---

### Path variable

```text
GET /users/25
```

Spring:

```java
@PathVariable int id
```

---

### Query parameter

```text
GET /users?name=Khushal
```

Spring:

```java
@RequestParam String name
```

So mentally:

```text
                 HTTP Request
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
      Request       Path        Query
       Body        Variable     Parameter
          ↓           ↓           ↓
      @RequestBody @PathVariable @RequestParam
```

---

# PP

Suppose we have:

```java
@GetMapping("/users/{id}")
public User getUser(@PathVariable int id) {
    return service.getUser(id);
}
```

### Q1

Someone sends:

```text
GET /users/42
```

What value will `id` contain?

### Q2

What does `{id}` in:

```java
"/users/{id}"
```

mean?

### Q3

What's the difference between:

```text
/users/42
```

and:

```text
/users?id=42
```

### Q4

Which annotation would you use for `/users/42`?

### Q5

Which annotation would you use for `/users?id=42`?

### Q6

If we have:

```java
@GetMapping("/users")
public List<User> getUsers(@RequestParam String name) {
    return service.searchUsers(name);
}
```

and someone sends:

```text
GET /users?name=Khushal
```

what will `name` contain?

Once you've got these, we'll move into **HTTP status codes and `ResponseEntity`**, which will make your APIs start looking much more like the ones you'll encounter professionally.


# Spring Lesson 9 — HTTP Status Codes & `ResponseEntity`

So far, we've focused on **what data goes into and out of our backend**.

Now we need to understand something else an API sends back:

> **What happened to the request?**

That's where HTTP status codes come in.

---

## 1. A response isn't just data

Suppose you request:

```text
GET /products/123
```

and the product exists.

The backend might respond:

```text
200 OK
```

with:

```json
{
    "id": 123,
    "name": "T-shirt"
}
```

But suppose product `123` doesn't exist.

The backend might respond:

```text
404 Not Found
```

with:

```json
{
    "message": "Product not found"
}
```

So an HTTP response contains more than just the JSON.

Think:

```text
HTTP Response
├── Status code
├── Headers
└── Body
```

We're mainly interested in the first and third for now.

---

# 2. The status codes you should know

Don't memorize every HTTP status code. These are the important ones for backend development:

| Code    | Meaning               | Typical use                                    |
| ------- | --------------------- | ---------------------------------------------- |
| **200** | OK                    | Successful GET                                 |
| **201** | Created               | Successful POST                                |
| **204** | No Content            | Successful DELETE/update with no response body |
| **400** | Bad Request           | Client sent invalid data                       |
| **401** | Unauthorized          | Authentication required/failed                 |
| **403** | Forbidden             | Authenticated but not allowed                  |
| **404** | Not Found             | Resource doesn't exist                         |
| **409** | Conflict              | Request conflicts with current state           |
| **500** | Internal Server Error | Something went wrong on server                 |

You don't need to memorize the exact wording right now. Understand **when they're used**.

---

# 3. What happens with our current Controller?

We've previously written:

```java
@GetMapping("/users")
public List<User> getUsers() {
    return service.getUsers();
}
```

If everything works, Spring automatically sends:

```text
200 OK
```

along with the list.

So:

```text
Controller returns List<User>
        ↓
Spring
        ↓
HTTP 200
        ↓
JSON
```

Pretty convenient.

---

# 4. But what if we want to control the status code?

This is where `ResponseEntity` comes in.

Instead of:

```java
@GetMapping("/users")
public List<User> getUsers() {
    return service.getUsers();
}
```

we can write:

```java
@GetMapping("/users")
public ResponseEntity<List<User>> getUsers() {

    List<User> users = service.getUsers();

    return ResponseEntity.ok(users);
}
```

Now we're explicitly saying:

> Return this data with HTTP status **200 OK**.

---

# 5. Returning 404

Imagine:

```java
@GetMapping("/users/{id}")
public ResponseEntity<User> getUser(@PathVariable int id) {

    User user = service.getUser(id);

    if (user == null) {
        return ResponseEntity.notFound().build();
    }

    return ResponseEntity.ok(user);
}
```

If the user exists:

```text
GET /users/25
       ↓
User found
       ↓
200 OK
       ↓
User JSON
```

If the user doesn't exist:

```text
GET /users/999
       ↓
User doesn't exist
       ↓
404 Not Found
```

This is much better than always returning `200 OK`.

---

# 6. Returning 201 for POST

Suppose we create a user:

```java
@PostMapping("/users")
public ResponseEntity<User> createUser(
        @RequestBody User user) {

    User createdUser = service.createUser(user);

    return ResponseEntity
            .status(201)
            .body(createdUser);
}
```

If successful:

```text
POST /users
       ↓
User created
       ↓
201 Created
       ↓
Created User JSON
```

You will often see the more readable version:

```java
return ResponseEntity.status(HttpStatus.CREATED)
        .body(createdUser);
```

---

# 7. Why does this matter?

Imagine you're building the frontend.

The frontend sends:

```text
POST /users
```

If it receives:

```text
201
```

it knows:

> User was successfully created.

If it receives:

```text
400
```

it knows:

> Something was wrong with what I sent.

If it receives:

```text
409
```

it might mean:

> This user already exists / there is some conflict.

If it receives:

```text
500
```

it knows:

> Something went wrong on the backend.

The status code lets different parts of the application communicate clearly.

---

# 8. Don't overuse `ResponseEntity`

You don't need to write:

```java
ResponseEntity
```

for absolutely everything.

This is perfectly fine:

```java
@GetMapping("/users")
public List<User> getUsers() {
    return service.getUsers();
}
```

Spring automatically gives you:

```text
200 OK
```

Use `ResponseEntity` when you actually need control over things like:

* status code
* headers
* response body

---

# 9. The important mental model

A Controller isn't just:

> "Give me some Java data."

It's actually responsible for translating between your application and HTTP.

For example:

```text
Incoming HTTP
     ↓
Controller
     ↓
Java objects
     ↓
Service
     ↓
Repository
     ↓
Java objects
     ↓
Controller
     ↓
HTTP response
```

And the Controller helps determine:

```text
Status code
+
Response body
+
Headers
```

This is why understanding HTTP is so important when learning Spring Boot.

---

# PP

Suppose we have:

```java
@GetMapping("/products/{id}")
public ResponseEntity<Product> getProduct(
        @PathVariable int id) {

    Product product = service.getProduct(id);

    if (product == null) {
        return ResponseEntity.notFound().build();
    }

    return ResponseEntity.ok(product);
}
```

### Q1.

If `/products/25` exists, what status code is returned?

### Q2.

If `/products/999` doesn't exist, what status code is returned?

### Q3.

Why don't we return `200 OK` when product 999 doesn't exist?

### Q4.

For a successful `POST /products` that creates a new product, which status code would you normally return?

### Q5.

What does `ResponseEntity` allow us to control?

### Q6 — think about this one

If the client sends:

```json
{
    "name": ""
}
```

and our backend says:

```text
400 Bad Request
```

who do you think is responsible for deciding that the empty name is invalid — **Controller, Service, or Repository?**

Don't worry if Q6 isn't obvious. It leads directly into **validation**, which is our next topic.


# Spring Lesson 10 — Validation

Now we tackle the situation from the last question:

```json
{
    "name": ""
}
```

What if our application says:

> "A user cannot have an empty name."

That's **validation**.

---

## 1. Why do we need validation?

Imagine someone sends:

```json
{
    "name": "",
    "age": -500
}
```

We don't want this garbage data reaching our database.

So we want to check the incoming data **before processing it**.

The flow becomes:

```text
Client
   ↓
JSON
   ↓
Controller
   ↓
Validation
   ↓
Service
   ↓
Repository
   ↓
Database
```

---

# 2. Put rules on our `User`

Our current class might look like:

```java
public class User {

    private int id;
    private String name;
    private int age;

    // constructor, getters, setters...
}
```

We can add validation rules:

```java
public class User {

    private int id;

    @NotBlank
    private String name;

    @Min(18)
    private int age;

    // constructor, getters, setters...
}
```

Now we've told Spring:

```text
name → cannot be blank
age  → must be at least 18
```

These annotations come from Jakarta Validation.

---

# 3. But how does Spring actually perform the validation?

Look at our Controller:

```java
@PostMapping("/users")
public ResponseEntity<User> createUser(
        @Valid @RequestBody User user) {

    return ResponseEntity.ok(
        service.createUser(user)
    );
}
```

The important part is:

```java
@Valid
```

You can mentally read:

> **"Before giving this `User` to my method, check whether it follows the validation rules."**

So if the client sends:

```json
{
    "name": "",
    "age": 22
}
```

Spring sees:

```java
@NotBlank
private String name;
```

and says:

> "Nope. Name is blank."

The request is rejected.

The Service doesn't even get the invalid User.

---

# 4. Another example

```java
public class Product {

    @NotBlank
    private String name;

    @Min(1)
    private double price;

    @Size(min = 3, max = 20)
    private String category;
}
```

This means:

```text
name     → cannot be blank
price    → minimum 1
category → 3–20 characters
```

So:

```json
{
    "name": "",
    "price": -50,
    "category": "A"
}
```

is invalid in **three different ways**.

---

# 5. Common validation annotations

You don't need to memorize all of these yet, but recognize the common ones:

```java
@NotNull
```

Value cannot be `null`.

```java
@NotBlank
```

String cannot be `null`, empty, or just whitespace.

```java
@NotEmpty
```

Collection/string cannot be empty.

```java
@Size(min = 3, max = 20)
```

Size must be between 3 and 20.

```java
@Min(18)
```

Number must be at least 18.

```java
@Max(100)
```

Number must not exceed 100.

```java
@Email
```

String should have a valid email format.

---

# 6. Where does validation happen?

This is an important distinction.

Suppose:

```text
Client
   ↓
Controller
   ↓
Service
   ↓
Repository
```

The **input validation** happens at the boundary where the request enters your application.

So:

```text
JSON
 ↓
Controller
 ↓
VALIDATE
 ↓
Service
```

The idea is:

> Don't send obviously invalid request data deeper into the application.

---

# 7. What happens when validation fails?

Suppose we have:

```java
@PostMapping("/users")
public User createUser(
        @Valid @RequestBody User user) {
    
    return service.createUser(user);
}
```

and:

```java
@NotBlank
private String name;
```

The client sends:

```json
{
    "name": ""
}
```

Spring detects the validation failure.

The request doesn't proceed normally to:

```java
service.createUser(user);
```

Instead, Spring generates an error response.

Typically you'll get:

```text
400 Bad Request
```

This connects directly to what we learned in the previous lesson.

---

# 8. Validation vs business logic

This distinction is **very important**.

Suppose:

```java
@NotBlank
private String name;
```

That's straightforward input validation.

But suppose the rule is:

> "A customer cannot place an order if their account has been suspended."

That's not simply a field-format problem.

That's **business logic**, so you'd generally handle it in the Service.

Think:

```text
@NotBlank
@Min
@Email
@Size
       ↓
Input validation


"Customer cannot order while suspended"
"User cannot withdraw more than balance"
"Discount only applies to premium users"
       ↓
Business logic → Service
```

This distinction will become very useful when reading your company's code.

---

# 9. Our architecture is getting more realistic

We started with:

```text
Controller
    ↓
Service
    ↓
Repository
```

Now:

```text
Request
   ↓
Controller
   ↓
Validation
   ↓
Service
   ↓
Repository
   ↓
Database
```

And if something goes wrong:

```text
Validation failure
       ↓
400 Bad Request
```

Later we'll learn how to make that error response clean and useful using **exception handling**.

---

# PP

Suppose we have:

```java
public class User {

    @NotBlank
    private String name;

    @Min(18)
    private int age;
}
```

and:

```java
@PostMapping("/users")
public User createUser(
        @Valid @RequestBody User user) {

    return service.createUser(user);
}
```

The client sends:

```json
{
    "name": "",
    "age": 15
}
```

### Q1.

What two validation rules are violated?

### Q2.

Does the request reach `service.createUser(user)`?

### Q3.

What HTTP status would you normally expect?

### Q4.

What does `@Valid` tell Spring to do?

### Q5.

Would `"name cannot be blank"` be a good example of input validation or business logic?

### Q6.

What about `"A user cannot place an order if their account is suspended"` — validation or business logic?

After this, we'll tackle **exception handling**, including why a real Spring application doesn't want to expose ugly error messages to API clients.


# Spring Lesson 11 — PUT: Updating Data

We already know:

```text
GET    /products/123  → get product 123
POST   /products      → create a product
```

Now:

```text
PUT    /products/123  → update product 123
```

This is where your earlier understanding was heading in the right direction.

---

## 1. Think about an e-commerce example

Suppose our database contains:

```json
{
    "id": 123,
    "name": "Black T-Shirt",
    "price": 999,
    "size": "M"
}
```

Now we want to change the price to `799`.

The client could send:

```text
PUT /products/123
```

with:

```json
{
    "name": "Black T-Shirt",
    "price": 799,
    "size": "M"
}
```

Notice:

* `/products/123` tells us **which product**
* The JSON tells us **what its new data should be**

---

# 2. The Controller

We use:

```java
@PutMapping("/products/{id}")
public Product updateProduct(
        @PathVariable int id,
        @RequestBody Product product) {

    return service.updateProduct(id, product);
}
```

There are **two pieces of information** coming into our method:

```text
URL
 ↓
id = 123

Request body
 ↓
Product object
```

So for:

```text
PUT /products/123
```

and:

```json
{
    "name": "Black T-Shirt",
    "price": 799
}
```

Spring gives us:

```java
id = 123;

product = Product(
    "Black T-Shirt",
    799
);
```

Conceptually, anyway.

---

# 3. Why do we need both?

This is important.

The URL:

```text
/products/123
```

answers:

> **Which product?**

The body:

```json
{
    "name": "Black T-Shirt",
    "price": 799
}
```

answers:

> **What should its data become?**

So:

```text
PUT /products/123
        │
        ├── PathVariable → which product?
        │
        └── RequestBody → new data
```

This is a very common pattern.

---

# 4. What happens in the Service?

The Controller shouldn't perform the actual update logic.

So:

```java
@Service
public class ProductService {

    private ProductRepository repository;

    public ProductService(ProductRepository repository) {
        this.repository = repository;
    }

    public Product updateProduct(int id, Product product) {

        // business logic

        return repository.updateProduct(id, product);
    }
}
```

And eventually the Repository would communicate with the database.

For now:

```java
@Repository
public class ProductRepository {

    public Product updateProduct(int id, Product product) {

        System.out.println(
            "Updating product " + id
        );

        return product;
    }
}
```

So:

```text
PUT /products/123
       ↓
Controller
       ↓
Service
       ↓
Repository
       ↓
Database
```

---

# 5. PUT vs POST

This distinction is important.

### POST

```text
POST /products
```

means:

> **Create a new product.**

The server typically determines the new resource's ID.

For example:

```text
POST /products
       ↓
creates
       ↓
Product #124
```

### PUT

```text
PUT /products/123
```

means:

> **Update/replace the resource identified by 123.**

The client is explicitly saying which resource it wants to modify.

---

# 6. PUT vs GET

Earlier you asked whether PUT is basically:

> GET + POST

**Not exactly.**

You can think of the workflow as:

```text
PUT /products/123
        ↓
Find product 123
        ↓
Apply the new data
        ↓
Save updated product
```

So internally, the application **might** need to retrieve the existing product before updating it.

But HTTP-wise, PUT is its own operation.

```text
GET → read
POST → create
PUT → update/replace
```

Don't think of PUT as literally being "GET + POST."

---

# 7. What about PATCH?

You'll also encounter:

```text
PATCH /products/123
```

The rough distinction is:

### PUT

> Here's the representation I want the resource to have.

### PATCH

> Change these particular fields.

For example, current product:

```json
{
    "id": 123,
    "name": "Black T-Shirt",
    "price": 999,
    "size": "M"
}
```

With PUT, you might send:

```json
{
    "name": "Black T-Shirt",
    "price": 799,
    "size": "M"
}
```

With PATCH, you might send only:

```json
{
    "price": 799
}
```

We'll only go deeper into PATCH if/when it's relevant to the APIs we're building.

---

# 8. What happens if the product doesn't exist?

Suppose:

```text
PUT /products/99999
```

but product `99999` doesn't exist.

Your Service might discover that and tell the Controller:

> "There is no such product."

The Controller could then return:

```text
404 Not Found
```

This connects back to our previous lesson about HTTP status codes.

So a realistic update endpoint eventually looks more like:

```java
@PutMapping("/products/{id}")
public ResponseEntity<Product> updateProduct(
        @PathVariable int id,
        @RequestBody Product product) {

    Product updated = service.updateProduct(id, product);

    if (updated == null) {
        return ResponseEntity.notFound().build();
    }

    return ResponseEntity.ok(updated);
}
```

---

# The mental model

For PUT, remember:

```text
PUT /products/123
        ↓
     Path
        ↓
   "Which one?"
        ↓
   Product #123

Request Body
        ↓
   "What data?"
        ↓
   New product data
```

Then:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Database
```

---

## PP

Suppose we have:

```java
@PutMapping("/users/{id}")
public User updateUser(
        @PathVariable int id,
        @RequestBody User user) {

    return service.updateUser(id, user);
}
```

The client sends:

```text
PUT /users/42
```

with:

```json
{
    "name": "Khushal",
    "age": 23
}
```

Answer:

**Q1.** What value does `id` contain?

**Q2.** What does `user` contain?

**Q3.** Why do we need the `id` in the URL if we're already sending a `User` in the body?

**Q4.** Which layer should ultimately deal with saving the updated user to the database?

**Q5.** If user 42 doesn't exist, what HTTP status would you normally return?

Then we'll do **DELETE**, which is considerably simpler.


# Spring Lesson 12 — DELETE

We've now covered 3 of the 4 main CRUD operations:

| HTTP method | Purpose    | Example                    |
| ----------- | ---------- | -------------------------- |
| GET         | Read       | `GET /products/123`        |
| POST        | Create     | `POST /products`           |
| PUT         | Update     | `PUT /products/123`        |
| **DELETE**  | **Delete** | **`DELETE /products/123`** |

## 1. What does DELETE do?

Suppose we have:

```text
Product 101 → Keyboard
Product 102 → Mouse
Product 103 → Monitor
```

The client wants to delete product `102`.

It sends:

```http
DELETE /products/102
```

The `102` tells us **which product** should be deleted.

In Spring:

```java
@DeleteMapping("/products/{id}")
public void deleteProduct(@PathVariable int id) {
    service.deleteProduct(id);
}
```

Very similar to PUT:

```java
@PutMapping("/products/{id}")
public Product updateProduct(@PathVariable int id,
                             @RequestBody Product product) {
    return service.updateProduct(id, product);
}
```

The major difference is that DELETE normally doesn't need a request body.

---

## 2. Why don't we need `@RequestBody`?

Think about the difference.

For PUT:

```http
PUT /products/102
```

We need to know:

> Which product?

`102`

And:

> What should its new data be?

```json
{
    "name": "Gaming Mouse",
    "price": 1500
}
```

So PUT needs both:

```text
URL       → which product
Request   → new data
```

But DELETE only needs:

> Which product should I delete?

```http
DELETE /products/102
```

Therefore:

```java
@DeleteMapping("/products/{id}")
public void deleteProduct(@PathVariable int id) {
    service.deleteProduct(id);
}
```

No `@RequestBody` is necessary.

---

# 3. The complete flow

Imagine:

```java
@DeleteMapping("/products/{id}")
public void deleteProduct(@PathVariable int id) {
    service.deleteProduct(id);
}
```

Request:

```http
DELETE /products/102
```

The flow is:

```text
HTTP Request
     ↓
Controller
     ↓
Service
     ↓
Repository
     ↓
Database
```

The controller receives:

```java
id = 102
```

Then:

```java
service.deleteProduct(102);
```

The service might do:

```java
public void deleteProduct(int id) {
    repository.deleteById(id);
}
```

And the repository handles the actual database operation.

---

# 4. What should DELETE return?

Usually, successful deletion doesn't need to return the deleted object.

For example:

```http
DELETE /products/102
```

could return:

```http
204 No Content
```

Meaning:

> The operation succeeded, and there is no response body.

In Spring:

```java
@DeleteMapping("/products/{id}")
public ResponseEntity<Void> deleteProduct(@PathVariable int id) {
    service.deleteProduct(id);
    return ResponseEntity.noContent().build();
}
```

We'll later learn when to use `ResponseEntity` and when Spring can handle the response for us.

---

# 5. What if the product doesn't exist?

Suppose:

```http
DELETE /products/999
```

but product `999` doesn't exist.

A typical API response would be:

```http
404 Not Found
```

The service/repository can detect that and the application can return the appropriate response.

We'll properly learn **how to handle these errors** when we reach exception handling.

---

# PP — DELETE

Consider:

```java
@DeleteMapping("/users/{id}")
public void deleteUser(@PathVariable int id) {
    service.deleteUser(id);
}
```

The client sends:

```http
DELETE /users/57
```

Answer these **without running the code**:

**Q1.** What value does `id` contain?

**Q2.** Does this request need `@RequestBody`? Why or why not?

**Q3.** Which layer should ultimately perform the database deletion?

**Q4.** What HTTP status would commonly be returned after successfully deleting the user if there is no response body?

**Q5.** What status would commonly be returned if user `57` doesn't exist?

**Q6.** In your own words, what's the difference between:

```http
PUT /users/57
```

and

```http
DELETE /users/57
```

Answer all six, then we'll do **PATCH**, which is the last CRUD-related HTTP method you need before we move on.


# Spring Lesson 13 — PATCH

PATCH is the last CRUD-related HTTP method we need before moving into more important Spring topics.

### PUT vs PATCH

You already know:

**PUT** → replace/update the resource with the supplied data.

```http
PUT /products/123
```

```json
{
  "name": "Keyboard",
  "price": 1500,
  "category": "Electronics"
}
```

Conceptually:

```text
Old:
name = Mouse
price = 1000
category = Electronics

        ↓ PUT

New:
name = Keyboard
price = 1500
category = Electronics
```

---

**PATCH** → change only specific fields.

```http
PATCH /products/123
```

```json
{
  "price": 1500
}
```

Conceptually:

```text
Old:
name = Mouse
price = 1000
category = Electronics

        ↓ PATCH price

New:
name = Mouse
price = 1500
category = Electronics
```

So the simplest mental model is:

```text
PUT   → "Here is the updated version."
PATCH → "Change these particular things."
```

---

## Why PATCH can be trickier in Java

Imagine your `Product` is:

```java
public class Product {
    private int id;
    private String name;
    private int price;
    private String category;
}
```

And you receive:

```json
{
  "price": 1500
}
```

What happens to `name` and `category`?

The incoming Java object might effectively look like:

```text
id       = 0
name     = null
price    = 1500
category = null
```

You **cannot simply replace** the existing product with this object, because you'd accidentally erase the other fields.

You therefore need logic like:

```java
if (product.getName() != null) {
    existing.setName(product.getName());
}

if (product.getPrice() != 0) {
    existing.setPrice(product.getPrice());
}
```

This is one reason PATCH implementations become more interesting than PUT.

And this connects directly to the question you raised earlier about using `Integer` instead of `int`.

If:

```java
private Integer price;
```

then:

```text
null → user did NOT provide price
1500 → user provided price
```

That's useful for partial updates.

With:

```java
private int price;
```

you can't distinguish:

```text
"price wasn't provided"
```

from a default value of:

```text
0
```

We'll revisit this properly when we learn **DTOs**, because that's where PATCH becomes much cleaner.

---

## Spring mapping

A basic PATCH endpoint looks like:

```java
@PatchMapping("/products/{id}")
public Product patchProduct(@PathVariable int id,
                            @RequestBody Product product) {
    return service.patchProduct(id, product);
}
```

Same fundamental structure:

```text
PATCH /products/123
        ↓
   Controller
        ↓
     Service
        ↓
   Repository
        ↓
    Database
```

The important difference is what the **Service does with the incoming object**.

---

### One important correction about PUT

Don't memorize:

> PUT always replaces every field.

In real Spring applications, you'll encounter PUT endpoints that perform updates without literally replacing every database column. The HTTP semantics describe the intended operation; the actual implementation can vary.

For now, use:

```text
PUT   → full/update representation
PATCH → partial update
```

as your working model.

---

# Harder PP

Consider this existing product:

```java
Product existing = new Product(
    10,
    "Keyboard",
    2000,
    "Electronics"
);
```

A client sends:

```http
PATCH /products/10
```

with:

```json
{
    "price": 2500
}
```

Assume Spring converts this JSON into:

```java
Product incoming
```

where unspecified fields become their normal Java defaults.

### Q1

What are the likely values of:

```java
incoming.getName()
incoming.getPrice()
incoming.getCategory()
```

### Q2

Why would blindly doing this be dangerous?

```java
existing = incoming;
```

### Q3

If you implement PATCH using the existing object, what should happen conceptually when `incoming.getName()` is `null`?

### Q4

Now consider this:

```json
{
    "price": 0
}
```

Why does using `int price` make it difficult to determine whether the client:

1. intentionally wants the price to become `0`, or
2. simply didn't send `price`?

### Q5 — harder

Why does changing `price` from:

```java
int
```

to:

```java
Integer
```

help solve that particular problem?

Don't worry about DTOs yet. I want you to reason through the object state first.


# Spring Lesson 14 — HTTP Request & Response

You've now covered the four main operations:

```text
GET     → retrieve
POST    → create
PUT     → update
PATCH   → partially update
DELETE  → delete
```

Before we jump into more Spring features, there's one thing worth understanding properly: **what actually travels between the client and your Spring application.**

---

## 1. An HTTP request has several parts

When a client calls:

```http
POST /products
```

it isn't really just sending "POST /products". An HTTP request can contain:

```text
Method
URL
Headers
Body
```

For example:

```http
POST /products
Content-Type: application/json
Authorization: Bearer abc123

{
    "name": "Keyboard",
    "price": 2000
}
```

Let's break that down.

### Method

```text
POST
```

Tells the server **what kind of operation is being requested**.

---

### URL

```text
/products
```

Tells the server **where/what resource the request concerns**.

With:

```http
GET /products/42
```

the `42` identifies a particular product.

---

### Headers

Headers are additional information about the request.

For example:

```http
Content-Type: application/json
```

means:

> "The data I'm sending in the body is JSON."

Another common header:

```http
Authorization: Bearer abc123
```

can contain authentication information.

You don't need to memorize headers yet. Just understand their purpose:

> **Headers provide additional information/instructions about the request.**

---

### Body

The body contains the actual data being sent.

For example:

```json
{
    "name": "Keyboard",
    "price": 2000
}
```

Spring can turn this JSON into a Java object through:

```java
@RequestBody Product product
```

---

# 2. The response has similar pieces

Your Spring application sends something back.

For example:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 42,
    "name": "Keyboard",
    "price": 2000
}
```

The response has:

```text
Status code
Headers
Body
```

The status code tells the client what happened.

```text
200 → successful
201 → successfully created
204 → successful, nothing to return
400 → bad request
404 → not found
500 → server error
```

---

# 3. Where does `ResponseEntity` fit?

You previously saw:

```java
return ResponseEntity.noContent().build();
```

`ResponseEntity` basically gives your controller explicit control over the HTTP response.

For example:

```java
@GetMapping("/products/{id}")
public ResponseEntity<Product> getProduct(@PathVariable int id) {

    Product product = service.getProduct(id);

    return ResponseEntity.ok(product);
}
```

This produces approximately:

```http
200 OK

{
    "id": 42,
    "name": "Keyboard",
    "price": 2000
}
```

Or:

```java
return ResponseEntity.notFound().build();
```

produces:

```http
404 Not Found
```

So you can think of it as:

```text
Normal return:
"Here's my Java object."

ResponseEntity:
"Here's my Java object + I explicitly want this HTTP status/headers."
```

---

# 4. Why this matters in real projects

Suppose you write:

```java
@GetMapping("/products/{id}")
public Product getProduct(@PathVariable int id) {
    return service.getProduct(id);
}
```

What if product `42` doesn't exist?

Returning:

```java
return null;
```

isn't a good API design.

You want something like:

```http
404 Not Found
```

rather than accidentally producing a successful response with no useful product.

Later, **exception handling** will give us a much cleaner way to handle this across the application instead of writing `ResponseEntity` checks everywhere.

---

# PP — now harder

Don't just identify definitions. Trace what happens.

Given:

```java
@PostMapping("/products")
public ResponseEntity<Product> createProduct(
        @RequestBody Product product) {

    Product saved = service.createProduct(product);

    return ResponseEntity.status(201).body(saved);
}
```

The client sends:

```http
POST /products
Content-Type: application/json

{
    "name": "Keyboard",
    "price": 2000
}
```

### Q1

Which part of the HTTP request tells Spring to execute this method rather than a `GET /products` method?

### Q2

Which part tells Spring what values should go into `Product product`?

### Q3

After this line:

```java
Product saved = service.createProduct(product);
```

why might `saved` contain an `id` even though the client never sent an `id`?

### Q4

What exactly does this return?

```java
ResponseEntity.status(201).body(saved);
```

Don't just say "201". Tell me **what two important things are being specified**.

### Q5 — harder

Suppose the client sends:

```http
POST /products
```

with **no request body at all**.

What problem would you expect when the controller tries to receive:

```java
@RequestBody Product product
```

Would this be a normal successful `201`, or would the request fail?

### Q6 — architecture

Why is this generally preferable:

```java
Product saved = service.createProduct(product);
```

to putting database-saving code directly inside the controller?

Answer these; I'm going to keep the PPs at this level or above from here.


# Spring Lesson 15 — Exception Handling

This is an important one for real-world Spring code.

So far, we've mostly assumed that everything works:

```text
Request
  ↓
Controller
  ↓
Service
  ↓
Repository
  ↓
Success
```

But real applications constantly encounter problems:

```text
Product doesn't exist
Invalid input
Duplicate email
Database failure
Unauthorized request
etc.
```

We need a clean way to turn those Java errors into useful HTTP responses.

---

## 1. The problem

Suppose your service does this:

```java
public Product getProduct(int id) {

    Product product = repository.findById(id);

    if (product == null) {
        throw new RuntimeException("Product not found");
    }

    return product;
}
```

Then the controller calls:

```java
@GetMapping("/products/{id}")
public Product getProduct(@PathVariable int id) {
    return service.getProduct(id);
}
```

Now imagine:

```http
GET /products/999
```

and product `999` doesn't exist.

The Service throws:

```java
throw new RuntimeException("Product not found");
```

The exception travels back up:

```text
Repository
    ↓
Service  ← exception happens
    ↓
Controller
    ↓
Spring
```

If we do nothing about it, Spring will generally turn an unhandled exception into a **500 Internal Server Error**.

But that's wrong conceptually.

The problem wasn't:

> "The server broke."

It was:

> "The requested product doesn't exist."

We want:

```http
404 Not Found
```

---

# 2. `@ExceptionHandler`

Spring gives us:

```java
@ExceptionHandler
```

which allows us to say:

> "If this particular exception occurs in this controller, use this method to handle it."

For example:

```java
@RestController
public class ProductController {

    @GetMapping("/products/{id}")
    public Product getProduct(@PathVariable int id) {
        return service.getProduct(id);
    }

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<String> handleException(RuntimeException e) {
        return ResponseEntity
                .status(404)
                .body(e.getMessage());
    }
}
```

Now if the Service throws:

```java
throw new RuntimeException("Product not found");
```

the `@ExceptionHandler` catches that exception.

The response can become:

```http
404 Not Found

Product not found
```

---

# 3. But there's a problem

Imagine you have **20 controllers**:

```text
ProductController
UserController
OrderController
PaymentController
ReviewController
...
```

If every controller has:

```java
@ExceptionHandler(...)
```

you'd be repeating the same error-handling code everywhere.

That's where:

```java
@ControllerAdvice
```

comes in.

---

# 4. `@ControllerAdvice`

You can create a separate class:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<String> handleException(RuntimeException e) {

        return ResponseEntity
                .status(404)
                .body(e.getMessage());
    }
}
```

Now this handler can handle exceptions thrown by **controllers across the application**.

The architecture becomes:

```text
                    ┌── ProductController
                    │
Request → Spring ───┼── UserController
                    │
                    └── OrderController
                           │
                           ↓
                    GlobalExceptionHandler
```

Instead of every controller having its own copy.

---

# 5. Why `RuntimeException.class`?

This:

```java
@ExceptionHandler(RuntimeException.class)
```

means:

> This method handles `RuntimeException` exceptions.

For example:

```java
throw new RuntimeException("Product not found");
```

matches it.

But eventually, we don't want to throw generic `RuntimeException` for everything.

We can create our own exception:

```java
public class ProductNotFoundException extends RuntimeException {

    public ProductNotFoundException(String message) {
        super(message);
    }
}
```

Then:

```java
if (product == null) {
    throw new ProductNotFoundException("Product not found");
}
```

And handle specifically:

```java
@ExceptionHandler(ProductNotFoundException.class)
public ResponseEntity<String> handleProductNotFound(
        ProductNotFoundException e) {

    return ResponseEntity
            .status(404)
            .body(e.getMessage());
}
```

Now the code communicates much more clearly:

```text
ProductNotFoundException
        ↓
GlobalExceptionHandler
        ↓
404 Not Found
```

We'll eventually build proper structured error responses instead of just returning a string.

---

# 6. The important architecture

This is the part I want you to understand, not memorize annotations:

```text
Controller
    ↓
Service
    ↓
Repository
```

If something goes wrong:

```text
Repository
    ↓
Service
    ↓
Exception
    ↓
Global Exception Handler
    ↓
HTTP error response
```

The controller doesn't need to write:

```java
if (product == null) {
    // ...
}
```

for every possible error.

The application has a **central place for handling exceptions**.

---

# Hard PP

Consider:

```java
@GetMapping("/products/{id}")
public Product getProduct(@PathVariable int id) {
    return service.getProduct(id);
}
```

Service:

```java
public Product getProduct(int id) {

    Product product = repository.findById(id);

    if (product == null) {
        throw new ProductNotFoundException("Product " + id + " not found");
    }

    return product;
}
```

Global handler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ProductNotFoundException.class)
    public ResponseEntity<String> handle(ProductNotFoundException e) {

        return ResponseEntity
                .status(404)
                .body(e.getMessage());
    }
}
```

Now the client sends:

```http
GET /products/42
```

and product `42` does **not** exist.

### Q1

Which layer discovers that product `42` doesn't exist?

### Q2

Which layer throws `ProductNotFoundException`?

### Q3

Does the controller itself catch the exception in this code?

### Q4

Which class handles the exception?

### Q5

What HTTP status eventually reaches the client?

### Q6 — harder

Why is this architecture better than doing something like this in every controller?

```java
if (product == null) {
    return ResponseEntity.status(404).build();
}
```

### Q7 — harder still

Suppose you have:

```text
ProductNotFoundException
UserNotFoundException
OrderNotFoundException
```

Why would it be better to have separate exception classes instead of throwing `RuntimeException` for all three?

This one is about **understanding the architecture**, not memorizing Spring annotations.


# Spring Lesson 16 — DTO Conversion & Mappers

You understand **why DTOs exist**. Now we need to understand what happens between the DTO and the Entity.

Our flow is:

```text id="s9qjwl"
JSON
 ↓
UserRequest DTO
 ↓
Service
 ↓
User Entity
 ↓
Repository
 ↓
User Entity
 ↓
Service
 ↓
UserResponse DTO
 ↓
JSON
```

The missing piece is:

> **Who converts `UserRequest` into `User`, and `User` into `UserResponse`?**

---

## 1. The conversion

Suppose:

```java id="v1h7fq"
public class UserRequest {

    private String name;
    private String email;
    private String password;
}
```

and:

```java id="3r9q3t"
public class User {

    private Integer id;
    private String name;
    private String email;
    private String password;
    private boolean admin;
}
```

The client sends:

```json id="02qfyg"
{
    "name": "Khushal",
    "email": "khushal@example.com",
    "password": "abc123"
}
```

Spring creates:

```java id="6u3pab"
UserRequest request
```

But the Repository expects a `User` entity.

So somewhere we need to do:

```java id="3c9kju"
User user = new User();

user.setName(request.getName());
user.setEmail(request.getEmail());
user.setPassword(request.getPassword());
```

Now:

```text id="xvcr0a"
UserRequest
     ↓
   convert
     ↓
User
```

---

# 2. Where could we put this conversion?

You could technically write it directly in the Service:

```java id="f8r9gv"
public User createUser(UserRequest request) {

    User user = new User();

    user.setName(request.getName());
    user.setEmail(request.getEmail());
    user.setPassword(request.getPassword());

    return repository.save(user);
}
```

For a small application, this is perfectly possible.

But imagine your project has:

```text id="b1qk3n"
UserRequest → User
UserUpdateRequest → User
User → UserResponse
OrderRequest → Order
Order → OrderResponse
ProductRequest → Product
Product → ProductResponse
...
```

Now your Services become full of conversion code.

That's where **Mapper classes** come in.

---

# 3. Mapper

A Mapper is simply a class whose job is:

> **Convert one type of object into another type of object.**

For example:

```java id="4y3dqo"
@Component
public class UserMapper {

    public User toEntity(UserRequest request) {

        User user = new User();

        user.setName(request.getName());
        user.setEmail(request.getEmail());
        user.setPassword(request.getPassword());

        return user;
    }
}
```

Now the Service can say:

```java id="z1tqaz"
User user = userMapper.toEntity(request);
```

Instead of writing all the setters itself.

---

# 4. Entity → Response DTO

We need the opposite direction too.

Suppose:

```java id="6cvzqy"
public class UserResponse {

    private Integer id;
    private String name;
    private String email;
}
```

Notice:

```text id="x93yjj"
User
├── id
├── name
├── email
├── password
└── admin

UserResponse
├── id
├── name
└── email
```

The password and admin status aren't exposed.

The mapper can handle that:

```java id="1cr2mz"
public UserResponse toResponse(User user) {

    UserResponse response = new UserResponse();

    response.setId(user.getId());
    response.setName(user.getName());
    response.setEmail(user.getEmail());

    return response;
}
```

Now:

```text id="y18h0f"
User Entity
     ↓
   Mapper
     ↓
UserResponse DTO
```

---

# 5. The complete Service

Now our Service becomes much cleaner:

```java id="txr6wq"
@Service
public class UserService {

    private final UserRepository repository;
    private final UserMapper mapper;

    public UserService(UserRepository repository,
                       UserMapper mapper) {
        this.repository = repository;
        this.mapper = mapper;
    }

    public UserResponse createUser(UserRequest request) {

        User user = mapper.toEntity(request);

        User savedUser = repository.save(user);

        return mapper.toResponse(savedUser);
    }
}
```

Look at what the Service is actually doing:

```text id="7ykd9t"
1. Receive request DTO
2. Convert it to Entity
3. Save Entity
4. Convert saved Entity to Response DTO
5. Return response
```

That is a **very realistic Spring pattern**.

---

# 6. Controller

Then the Controller becomes very simple:

```java id="m9i8ur"
@PostMapping("/users")
public UserResponse createUser(
        @RequestBody UserRequest request) {

    return service.createUser(request);
}
```

The Controller handles HTTP.

The Service handles the operation.

The Mapper handles conversion.

The Repository handles persistence.

```text id="by1fms"
                 Controller
                     │
              UserRequest
                     ↓
                  Service
                  ↙     ↘
             Mapper    Repository
                ↓          ↓
              User       Database
                ↓
             Mapper
                ↓
          UserResponse
                     ↓
                 Controller
                     ↓
                    JSON
```

This is the kind of structure you will repeatedly encounter in company Spring projects.

---

# 7. Important: Mapper is NOT a Spring-specific concept

Again, do not memorize it as another magical Spring feature.

This:

```java id="yrd7wq"
public class UserMapper {
    ...
}
```

is just a normal Java class.

We use:

```java id="1e0lzh"
@Component
```

so Spring creates and manages a `UserMapper` Bean, allowing us to inject it:

```java id="t1l5ro"
public UserService(UserRepository repository,
                   UserMapper mapper) {
    ...
}
```

And this connects directly back to the **Dependency Injection** you learned at the beginning.

---

# 8. One thing you will see in real projects

Sometimes you will see:

```text id="m8o6iz"
UserMapper
```

Sometimes:

```text id="6u0w5t"
UserMapperImpl
```

Sometimes libraries such as **MapStruct** are used to generate mapper implementations.

Do not worry about MapStruct yet.

The important thing is that when you see:

```java id="i0p3gk"
mapper.toEntity(request)
```

you should immediately understand:

> "This is converting a DTO into an Entity."

And:

```java id="h8z3kg"
mapper.toResponse(user)
```

means:

> "This is converting an Entity into a Response DTO."

That recognition will be extremely useful when reading unfamiliar code.

---

# Hard PP

You have:

```java
public class ProductRequest {

    private String name;
    private Integer price;
    private String category;
}
```

```java
public class Product {

    private Integer id;
    private String name;
    private Integer price;
    private String category;
    private String supplierSecret;
}
```

```java
public class ProductResponse {

    private Integer id;
    private String name;
    private Integer price;
}
```

And:

```java
public ProductResponse createProduct(ProductRequest request) {

    Product product = mapper.toEntity(request);

    Product saved = repository.save(product);

    return mapper.toResponse(saved);
}
```

### Q1

Why should `mapper.toEntity(request)` exist instead of simply passing `request` to the Repository?

### Q2

Why should `supplierSecret` not be copied into `ProductResponse`?

### Q3

The database generates the product ID during:

```java
Product saved = repository.save(product);
```

Why is it useful to create the response from `saved` rather than the original `product`?

### Q4 — harder

Suppose someone writes:

```java
public ProductResponse createProduct(ProductRequest request) {

    Product product = mapper.toEntity(request);

    repository.save(product);

    return mapper.toResponse(product);
}
```

Would this necessarily be wrong?

Or could it work?

Explain **what determines whether `product` contains the generated ID after `save()`**.

### Q5 — architecture

Which responsibility belongs to each?

```text
Controller → ?
Service → ?
Mapper → ?
Repository → ?
```

Do not just give one-word answers. Give the actual responsibility of each layer.


# Spring Lesson 17 — DTO Design: Request vs Response

You understand the basic DTO architecture. Now we need to make an important distinction that you will see constantly in real projects:

> **There is usually not just one DTO. Different operations often need different DTOs.**

---

## 1. Why `UserRequest` is not enough

Imagine registration:

```http id="8nqg2v"
POST /users
```

The client needs to send:

```json id="7krx1c"
{
    "name": "Khushal",
    "email": "khushal@example.com",
    "password": "abc123"
}
```

So:

```java id="e4t5y7"
public class UserCreateRequest {
    private String name;
    private String email;
    private String password;
}
```

But now consider updating a user:

```http id="0g7d5k"
PUT /users/42
```

Maybe you allow:

```json id="0v8a4w"
{
    "name": "Khushal Sharma",
    "email": "new@example.com"
}
```

There is no reason for the update request to contain:

```text
password
admin
id
```

So you might have:

```java id="d3d3qk"
public class UserUpdateRequest {
    private String name;
    private String email;
}
```

And for the response:

```java id="w4qz7k"
public class UserResponse {
    private Integer id;
    private String name;
    private String email;
}
```

Now we have:

```text id="n8i6w4"
UserCreateRequest
UserUpdateRequest
UserResponse
User
```

Four different objects with four different purposes.

---

# 2. Why not make one giant DTO?

You could create:

```java id="0f5x7a"
public class UserDTO {

    private Integer id;
    private String name;
    private String email;
    private String password;
    private boolean admin;
}
```

and use it everywhere.

But now you have the same problem we were trying to solve.

For example, during registration:

```json id="x7f5x3e"
{
    "id": 999,
    "name": "Khushal",
    "email": "...",
    "password": "...",
    "admin": true
}
```

Your API now has to carefully decide which fields it should ignore.

And for responses, you have to remember:

> "Do not accidentally serialize password."

Separate DTOs make the allowed data much more explicit.

---

# 3. Think of DTOs as contracts

This is the important concept.

Your API has a contract with the frontend/client.

For registration:

```text id="6cbg5e"
POST /users

Client is allowed to provide:
name
email
password
```

For updating:

```text id="e7iyb7"
PUT /users/{id}

Client is allowed to provide:
name
email
```

For response:

```text id="e9m4n8"
API is allowed to provide:
id
name
email
```

The DTO represents that contract.

This is one reason DTOs are so common in professional backend applications.

---

# 4. DTOs and validation

This also makes validation cleaner.

For example:

```java id="lx0p2h"
public class UserCreateRequest {

    @NotBlank
    private String name;

    @Email
    @NotBlank
    private String email;

    @Size(min = 8)
    private String password;
}
```

You can then have different rules for updating:

```java id="s4m1yo"
public class UserUpdateRequest {

    @NotBlank
    private String name;

    @Email
    @NotBlank
    private String email;
}
```

The request DTO therefore isn't merely controlling **which fields are accepted**.

It can also define **what valid input looks like for that particular operation**.

---

# 5. DTO ≠ Entity

This deserves repetition because it will save you confusion later.

You might see:

```java id="f5z5yc"
User
```

and:

```java id="g5w3hj"
UserResponse
```

and they may have several identical fields.

That does **not** mean they are duplicates.

They have different purposes.

```text id="8h7k3q"
User
→ application/database representation

UserCreateRequest
→ data accepted when creating a user

UserUpdateRequest
→ data accepted when updating a user

UserResponse
→ data exposed to the client
```

---

# 6. A realistic flow

Registration:

```text id="p9e1z2"
JSON
 ↓
UserCreateRequest
 ↓
Controller
 ↓
Service
 ↓
Mapper
 ↓
User
 ↓
Repository
 ↓
Database
```

Response:

```text id="y2q8x4"
Database
 ↓
User
 ↓
Mapper
 ↓
UserResponse
 ↓
Controller
 ↓
JSON
```

Update:

```text id="h8k2w1"
JSON
 ↓
UserUpdateRequest
 ↓
Controller
 ↓
Service
 ↓
Mapper / update logic
 ↓
User
 ↓
Repository
 ↓
Database
```

Notice something important:

**The DTO changes depending on what the API operation is trying to accomplish.**

---

# Hard PP

Consider this entity:

```java id="q8h3z9"
public class Employee {

    private Integer id;
    private String name;
    private String email;
    private String password;
    private String department;
    private boolean admin;
    private double salary;
}
```

The API has three operations.

### Create employee

```http id="q2y7j5"
POST /employees
```

Allowed input:

```json id="m4w1s9"
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "password": "secret123",
    "department": "Engineering"
}
```

### Update employee

```http id="z9v4k1"
PUT /employees/25
```

Allowed input:

```json id="r7n3w2"
{
    "name": "Rahul Sharma",
    "department": "Management"
}
```

### Get employee

```http id="e2m8q4"
GET /employees/25
```

Response should contain:

```json id="x5p9k3"
{
    "id": 25,
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "department": "Management"
}
```

Answer:

### Q1

Design the three DTO classes. What fields belong in:

```text
EmployeeCreateRequest
EmployeeUpdateRequest
EmployeeResponse
```

### Q2

Why is `salary` not present in the create request?

### Q3

Why is `admin` not present in either create or update request?

### Q4

Why is `password` absent from `EmployeeResponse`?

### Q5 — harder

Why is `id` present in `EmployeeResponse` but absent from `EmployeeCreateRequest`?

### Q6 — architecture

Suppose the frontend suddenly asks:

> "We also want the employee's department in the response."

Which class would you normally modify?

And why **would you not need to modify the `Employee` entity** if `department` already exists there?

### Q7 — real-world reasoning

A developer says:

> "DTOs are unnecessary because the Entity already has all the fields we need."

Give me **two separate problems** this approach can create in an API.

This is the level of reasoning we will continue using.


# Spring Lesson 18 — Mapper in Depth

You now understand why we have:

```text id="4g8k3z"
Request DTO
    ↓
Entity
    ↓
Response DTO
```

Now we will go one level deeper into **how the mapping actually works**, because you are going to see mapper code constantly in real Spring projects.

---

## 1. A Mapper is just a normal Java class

Suppose:

```java id="j3x8u2"
public class ProductMapper {

    public Product toEntity(ProductRequest request) {

        Product product = new Product();

        product.setName(request.getName());
        product.setPrice(request.getPrice());
        product.setCategory(request.getCategory());

        return product;
    }

    public ProductResponse toResponse(Product product) {

        ProductResponse response = new ProductResponse();

        response.setId(product.getId());
        response.setName(product.getName());
        response.setPrice(product.getPrice());

        return response;
    }
}
```

There is nothing special about:

```java id="3w7v1f"
toEntity()
```

or:

```java id="4f3n8j"
toResponse()
```

They are just methods.

The naming convention simply makes their purpose obvious.

---

# 2. Why `@Component`?

If we want Spring to manage the mapper:

```java id="j1c2fz"
@Component
public class ProductMapper {
    ...
}
```

Now Spring creates a Bean for it.

Then:

```java id="6h4z8b"
@Service
public class ProductService {

    private final ProductMapper mapper;

    public ProductService(ProductMapper mapper) {
        this.mapper = mapper;
    }
}
```

Spring sees:

```text id="7s2w8a"
ProductMapper → Bean
ProductService → Bean
```

and injects the mapper into the service.

This should feel familiar because it is the same **Dependency Injection** concept you learned earlier.

---

# 3. Mapper does NOT contain business logic

This distinction is important.

Suppose the business rule is:

> An employee with salary below ₹20,000 cannot become an admin.

This belongs in the **Service/business logic**, not the mapper.

Mapper:

```java id="j8r2k4"
employee.setName(request.getName());
employee.setSalary(request.getSalary());
```

Service:

```java id="v6y1p9"
if (employee.getSalary() < 20000) {
    throw new SomeException();
}
```

Think:

```text id="n5x7c2"
Mapper
→ "How do I convert this object?"

Service
→ "What should the application do?"
```

---

# 4. Mapper does NOT save anything

This is another important boundary.

Mapper:

```java id="g3d8w1"
Product toEntity(ProductRequest request)
```

does not:

```java id="q1z9m4"
repository.save(...)
```

And it does not talk to the database.

Its only job is conversion.

```text id="v2p6k8"
DTO → Entity
Entity → DTO
```

---

# 5. Why not put mapping inside Repository?

Because Repository's responsibility is data access.

Imagine:

```java id="m8s4q2"
repository.save(product);
```

The Repository should be concerned with:

```text id="a6f9w3"
"How do I persist Product?"
```

It should not care about:

```text id="j5c1r7"
"How do I convert ProductRequest to ProductResponse?"
```

That would mix unrelated responsibilities.

---

# 6. Why this separation becomes valuable

Imagine your project eventually has:

```text id="q7r4m2"
20 Controllers
30 Services
15 Repositories
40 DTOs
10 Entities
10 Mappers
```

If conversion is handled by dedicated mapper classes, you can quickly find:

```text id="k2v8p1"
UserMapper
OrderMapper
ProductMapper
EmployeeMapper
```

and know:

> "These classes are responsible for object conversion."

This makes navigating a large codebase easier.

---

# 7. One important real-world variation

You may see a mapper written like:

```java id="u8x3c5"
@Component
public class ProductMapper {

    public Product toEntity(ProductRequest request) {
        ...
    }
}
```

But you may also see:

```java id="e4m7q9"
@Mapper(componentModel = "spring")
public interface ProductMapper {
    Product toEntity(ProductRequest request);
    ProductResponse toResponse(Product product);
}
```

This is commonly associated with **MapStruct**.

Do not learn MapStruct yet.

For now, when you see this:

```java id="q6w2p8"
mapper.toEntity(request)
```

your brain should immediately translate it to:

> **"Convert the request DTO into the Entity."**

And:

```java id="b5r9t3"
mapper.toResponse(entity)
```

means:

> **"Convert the Entity into the Response DTO."**

That recognition is more important right now than knowing the library.

---

# 8. One subtle point: mapping is not always 1-to-1

Suppose:

```java id="n2j7v4"
Product {
    id
    name
    price
}
```

and:

```java id="c9k4x1"
ProductResponse {
    id
    name
    price
    discountedPrice
}
```

`discountedPrice` doesn't exist directly in the Entity.

The mapper might calculate it:

```java id="s8m1q5"
response.setDiscountedPrice(
    product.getPrice() * 0.9
);
```

But there is a boundary here.

Simple **data transformation** can belong in mapping.

A meaningful business rule such as:

> "Premium customers get 10% discount, regular customers get 5%."

belongs in the Service/business logic.

So do not interpret "Mapper contains absolutely zero calculations."

The better rule is:

> **Mapper converts data; Service decides business behavior.**

---

# Hard PP

Consider:

```java id="r7k2m9"
public class OrderRequest {
    private Integer productId;
    private Integer quantity;
}
```

```java id="z3p8q1"
public class Order {
    private Integer id;
    private Product product;
    private Integer quantity;
    private double totalPrice;
}
```

And:

```java id="w6c4n2"
public class OrderMapper {

    public Order toEntity(OrderRequest request) {
        Order order = new Order();

        order.setQuantity(request.getQuantity());

        return order;
    }
}
```

The Service:

```java id="f9d2k7"
public Order createOrder(OrderRequest request) {

    Product product =
        productRepository.findById(request.getProductId());

    Order order = mapper.toEntity(request);

    order.setProduct(product);

    order.setTotalPrice(
        product.getPrice() * request.getQuantity()
    );

    return orderRepository.save(order);
}
```

### Q1

Why doesn't `OrderMapper.toEntity()` set the `Product` itself?

### Q2

Why is the Service retrieving the Product?

### Q3

Why does calculating:

```java id="n8v3j1"
product.getPrice() * request.getQuantity()
```

belong in the Service rather than the Mapper?

### Q4 — harder

Suppose someone changes the mapper to:

```java id="x4m7p2"
public Order toEntity(OrderRequest request) {

    Order order = new Order();

    Product product =
        productRepository.findById(request.getProductId());

    order.setProduct(product);
    order.setQuantity(request.getQuantity());

    return order;
}
```

What architectural responsibility has now been incorrectly added to the Mapper?

### Q5 — harder still

Why is this distinction important when you eventually have to modify an unfamiliar company project?

I want you to explain **how knowing the responsibility of each layer helps you find where a change should be made.**


We will skip that PP since you said **NEXT**. The concept is straightforward enough to continue.

# Spring Lesson 19 — `@SpringBootApplication`, Component Scanning & Auto-Configuration

We have spent a lot of time on:

```text id="2j7k4m"
Controller
Service
Repository
DTO
Mapper
Dependency Injection
```

You know **what these components do**.

Now we need to understand something important:

> **How does Spring actually find these classes and start the whole application?**

You have probably seen this at the top of almost every Spring Boot application:

```java id="7h3k9p"
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Let's break this down.

---

# 1. `main()` is still Java

First, do not think Spring replaces Java's normal program execution.

This is still the normal Java entry point:

```java id="p4m8x2"
public static void main(String[] args)
```

The important difference is what happens here:

```java id="k6w1r9"
SpringApplication.run(Application.class, args);
```

This tells Spring Boot:

> Start the Spring application.

Spring then creates its environment, discovers components, creates Beans, connects dependencies, and starts the application.

Conceptually:

```text id="r8q3v5"
main()
  ↓
SpringApplication.run()
  ↓
Spring starts
  ↓
Find Components
  ↓
Create Beans
  ↓
Inject Dependencies
  ↓
Start application
```

---

# 2. What does `@SpringBootApplication` mean?

This:

```java id="x5n2k8"
@SpringBootApplication
```

is a very important annotation.

It combines several Spring annotations.

The three important ideas are:

```text id="c7m4p1"
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan
```

You do **not** need to memorize the internal implementation yet.

Understand what each concept means.

---

# 3. Component Scanning

You already know:

```java id="y9f3k6"
@Service
@Repository
@RestController
@Component
```

These tell Spring:

> This class should be managed by Spring.

But Spring needs to **find** these classes.

That's what component scanning does.

Suppose your project looks like:

```text id="h4q8m2"
com.example.shop
│
├── Application.java
│
├── controller
│   └── ProductController.java
│
├── service
│   └── ProductService.java
│
├── repository
│   └── ProductRepository.java
│
└── mapper
    └── ProductMapper.java
```

If your main application class is:

```java id="w2n7c4"
package com.example.shop;

@SpringBootApplication
public class Application {
}
```

Spring scans the relevant package and its subpackages.

It finds:

```text id="a8p5k1"
ProductController → @RestController
ProductService    → @Service
ProductRepository → @Repository
ProductMapper     → @Component
```

and creates the corresponding Beans.

---

# 4. Why package structure matters

This is something you will eventually encounter when debugging company projects.

Imagine:

```text id="q3m7v9"
com.example.shop
└── Application.java

com.other.controllers
└── ProductController.java
```

Your controller is outside the package structure Spring is scanning.

Spring may not discover it automatically.

Then you might wonder:

> "Why isn't Spring creating my Controller Bean?"

The problem could simply be **component scanning**.

This is why Spring Boot projects generally keep the main application class near the top-level package.

---

# 5. Auto-Configuration

This is one of the biggest conveniences Spring Boot provides.

Imagine you add a database dependency to your project.

You could manually configure a huge amount of infrastructure.

Spring Boot instead looks at:

```text id="s8k2v6"
What dependencies are present?
What configuration exists?
What environment am I running in?
```

and automatically configures many things that are likely needed.

That's **auto-configuration**.

For example, if Spring Boot detects the appropriate web dependencies, it can configure the infrastructure required for a web application.

If it detects database-related dependencies and configuration, it can configure database-related infrastructure.

The important word is:

> **Automatically.**

---

# 6. Spring vs Spring Boot

This distinction is useful.

### Spring

Provides the underlying framework and features:

```text id="e5m1q8"
IoC
Dependency Injection
Beans
MVC
Security
Data access
etc.
```

### Spring Boot

Makes building and running Spring applications easier by providing conventions, auto-configuration, starter dependencies, embedded server support, and other conveniences.

So:

```text id="d7r4x2"
Spring
   ↓
Framework

Spring Boot
   ↓
Easier way to build/run Spring applications
```

You are learning **Spring Boot**, but underneath it you are using the Spring Framework.

---

# 7. What happens when your application starts?

Imagine:

```java id="u9x5k2"
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Spring Boot roughly goes through this process:

```text id="n4c7m1"
Application starts
       ↓
Spring Boot starts
       ↓
Component scanning
       ↓
Find @Controller / @Service / @Repository / @Component
       ↓
Create Beans
       ↓
Resolve dependencies
       ↓
Inject dependencies
       ↓
Auto-configure required infrastructure
       ↓
Start application
```

This connects almost everything you've learned so far.

---

# 8. A useful example

Suppose:

```java id="p6k3r8"
@RestController
public class ProductController {

    private final ProductService service;

    public ProductController(ProductService service) {
        this.service = service;
    }
}
```

and:

```java id="w1m9q4"
@Service
public class ProductService {

    private final ProductRepository repository;

    public ProductService(ProductRepository repository) {
        this.repository = repository;
    }
}
```

When the application starts, Spring needs to solve:

```text id="x8q2m5"
ProductController
       ↓ needs
ProductService
       ↓ needs
ProductRepository
```

So Spring creates the dependency chain.

```text id="v3n7k1"
ProductRepository Bean
        ↓
ProductService Bean
        ↓
ProductController Bean
```

This is the same DI you already understand.

We are now simply learning **how Spring discovers the classes in the first place.**

---

# PP — Application Startup

Consider this project:

```text id="c9m4x7"
com.example.shop
│
├── Application.java
│
├── controller
│   └── ProductController.java
│
├── service
│   └── ProductService.java
│
└── repository
    └── ProductRepository.java
```

`Application.java` contains:

```java id="k2w8p3"
package com.example.shop;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Q1

Why does Spring need component scanning?

### Q2

What happens if `ProductService` has:

```java
@Service
```

but is placed somewhere Spring is **not scanning**?

### Q3

If Spring discovers:

```text id="m7q3x9"
ProductController
ProductService
ProductRepository
```

what dependency chain does it need to construct?

### Q4 — harder

Suppose `ProductController` requires:

```java id="f2n8v5"
ProductService
```

but Spring cannot create `ProductService`.

What happens to `ProductController`?

Why?

### Q5 — harder

What is the practical difference between:

```text id="r4k8m2"
Spring Framework
```

and:

```text id="j6p3x9"
Spring Boot
```

Do not give me textbook definitions. Explain it using the things you have already learned.

### Q6 — real-world debugging

You start a company project and see:

```text id="v8m2q5"
@RestController
ProductController
```

but requests to its endpoint return a 404 because Spring never maps the endpoint.

Give me **one possible reason related to what we just learned**, without assuming the Controller code itself is wrong.


# Spring Lesson 20 — Configuration: `application.properties`

We will skip the startup PP for now and keep moving.

You have seen:

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Now we need to understand another file you will almost certainly encounter in company projects:

```text id="k8p2v6"
src
└── main
    └── resources
        └── application.properties
```

This file is where we put **configuration** for the application.

---

# 1. What is configuration?

Your Java code contains the application's logic.

But many things should **not be hardcoded into Java code**.

For example:

```java
server.setPort(8080);
```

You might want the application to run on a different port in another environment.

Instead, you can put:

```properties
server.port=8081
```

in:

```text id="2m7x4q"
application.properties
```

Now the application uses port `8081`.

The idea is:

```text id="y5r8c2"
Java code
→ application logic

application.properties
→ configuration
```

---

# 2. Why separate configuration?

Imagine your company's application has:

```text
Development database
Testing database
Production database
```

You do **not** want to rewrite Java code every time you move between environments.

Instead, configuration can specify things such as:

```properties
spring.datasource.url=...
spring.datasource.username=...
spring.datasource.password=...
```

The Java code can remain the same.

Conceptually:

```text id="p3k9w1"
Same Java application
        ↓
Different configuration
        ↓
Different environment
```

---

# 3. Reading configuration from Java

You have already encountered:

```java
@Value
```

For example:

```properties
app.name=Shop API
```

Then:

```java
@Value("${app.name}")
private String appName;
```

Spring reads:

```text id="r6m2v8"
app.name
```

from configuration and injects:

```text id="h9x4q7"
"Shop API"
```

into the field.

So:

```text id="c5n8m3"
application.properties
       ↓
Spring reads configuration
       ↓
@Value
       ↓
Java field
```

---

# 4. Another example

```properties
app.max-products=100
```

Java:

```java
@Value("${app.max-products}")
private int maxProducts;
```

Now:

```java
maxProducts
```

contains:

```text id="s7v2k4"
100
```

Again, Spring is doing the injection.

Notice the pattern:

```text id="j8m3q5"
Configuration value
        ↓
Spring
        ↓
Java object/field
```

This is conceptually similar to Dependency Injection, although configuration values are not Beans in the same sense as your Services and Repositories.

---

# 5. What should NOT go into properties?

Do not put business logic there.

Bad idea:

```properties
if.user.is.admin=true
```

Configuration should describe **how the application should operate**, not implement business rules.

Good examples:

```properties
server.port=8081
```

```properties
app.name=Tracking API
```

```properties
spring.datasource.url=...
```

```properties
some.external-service.url=...
```

---

# 6. Configuration and secrets

You may encounter:

```properties
spring.datasource.username=admin
spring.datasource.password=supersecret
```

Technically this works.

But committing real passwords/secrets directly into source control is generally a bad practice.

In real projects, you will often see environment variables:

```properties
spring.datasource.password=${DB_PASSWORD}
```

Then the actual password is supplied externally.

Conceptually:

```text id="w2k6p9"
application.properties
        ↓
"${DB_PASSWORD}"
        ↓
Environment variable
        ↓
Actual secret
```

We will cover this properly when we reach production configuration.

---

# 7. `application.yml`

You may also encounter:

```text id="m4q8x1"
application.yml
```

instead of:

```text id="c7v3n5"
application.properties
```

For example:

```yaml
server:
  port: 8081

app:
  name: Shop API
```

These are simply **two common formats for configuration**.

You do not need to learn YAML syntax deeply right now.

When you see either file in a company project, you should recognize:

> **This is application configuration.**

---

# 8. Why this matters for reading company projects

You may open a project and see:

```java
@Value("${tracking.api.url}")
private String trackingApiUrl;
```

Instead of wondering:

> "Where the hell does this value come from?"

you should immediately look at:

```text id="x3p7m8"
application.properties
application.yml
environment variables
```

and search for:

```text id="h5k9q2"
tracking.api.url
```

That is exactly the kind of project-navigation skill we are building.

---

# Hard PP

Suppose your project has:

```properties
server.port=9090
app.name=Tracking API
app.max-retries=3
```

and:

```java
@RestController
public class TestController {

    @Value("${app.name}")
    private String appName;

    @Value("${app.max-retries}")
    private int maxRetries;
}
```

### Q1

What value will `appName` contain?

### Q2

What value will `maxRetries` contain?

### Q3

If you change:

```properties
app.max-retries=5
```

do you need to change the Java code?

Why?

### Q4 — harder

Why is:

```java
@Value("${app.name}")
private String appName;
```

preferable to:

```java
private String appName = "Tracking API";
```

if the value may differ between development and production?

### Q5 — real-world

You encounter this in a company project:

```java
@Value("${payment.service.url}")
private String paymentServiceUrl;
```

You search `application.properties` and cannot find:

```text
payment.service.url
```

Give me **two places/reasons you would investigate before assuming the code is broken.**

### Q6 — architecture

Why should database URLs, ports, external-service URLs, and similar environment-specific values generally be **configuration rather than hardcoded into Service classes**?




