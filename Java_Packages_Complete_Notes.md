# Java Packages - Complete Notes

## What is a Package?

A **package** is a namespace that groups related Java types (classes,
interfaces, enums, records, annotations).

It is **not just a folder**. The folder structure is how Java maps a
package to the filesystem.

Example:

``` text
com
└── company
    ├── Employee.java
    └── Manager.java
```

``` java
package com.company;
```

------------------------------------------------------------------------

## Why Packages Exist

1.  **Organization**
2.  **Avoid name collisions** (`java.util.Date` vs `java.sql.Date`)
3.  **Access control** (package-private access)

------------------------------------------------------------------------

## Package Declaration

The first non-comment line should be:

``` java
package com.company;
```

Only one package declaration is allowed per file.

------------------------------------------------------------------------

## Folder Structure

Every `.` becomes a folder.

``` java
package com.company.vehicle;
```

must live in

``` text
com/
└── company/
    └── vehicle/
```

------------------------------------------------------------------------

## Default Package

If no package declaration exists, the class belongs to the default
package.

Avoid using it in real projects.

------------------------------------------------------------------------

## Fully Qualified Name (FQN)

Every class has a complete name.

    java.util.Scanner
    com.company.Car

Imports simply let you omit the package prefix.

------------------------------------------------------------------------

## Imports

Normal import:

``` java
import com.vehicle.Car;
```

Wildcard:

``` java
import com.vehicle.*;
```

### Important Rule

Java imports **types**, not folders.

Wildcard imports all **public types directly inside that package**.

It does **NOT** import subpackages.

------------------------------------------------------------------------

## Example

Structure:

``` text
09dom/
└── com
    ├── mmm.java               -> package com;
    ├── mom
    │   ├── ram.java           -> package com.mom;
    │   └── hom
    │       ├── hom.java       -> package com.mom.hom;
    │       └── mmm.java       -> package com.mom.hom;
    └── rom
        ├── mmm.java           -> package com.rom;
        ├── orm.java
        ├── rmm.java
        └── vrm.java
```

### `import com.*;`

Imports only:

    com.mmm

### `import com.rom.*;`

Imports:

    com.rom.mmm
    com.rom.orm
    com.rom.rmm
    com.rom.vrm

### `import com.mom.*;`

Imports:

    com.mom.ram

### To use `com.mom.hom.hom`

Either:

``` java
import com.mom.hom.hom;
```

or

``` java
import com.mom.hom.*;
```

------------------------------------------------------------------------

## Packages are NOT Parent/Child

Although

``` text
com
└── mom
```

looks hierarchical, Java treats

    com
    com.mom
    com.mom.hom

as completely separate packages.

No inheritance. No special access.

------------------------------------------------------------------------

## Same Package

If two classes belong to the same package:

``` java
package com.school;
```

they can refer to each other without imports.

------------------------------------------------------------------------

## Different Packages

If one class is in

    com

and another is in

    com.school

an import is required.

------------------------------------------------------------------------

# javac and Packages

## Before Packages

Compile:

``` bash
javac Hello.java
```

Run:

``` bash
java Hello
```

------------------------------------------------------------------------

## With Packages

Project:

``` text
Project
└── com
    ├── Main.java
    └── vehicle
        └── Car.java
```

Compile:

``` bash
javac com/Main.java
```

The compiler may also compile dependent source files automatically if
needed.

------------------------------------------------------------------------

## Source Root

Always compile from the **source root/project root**, not from inside a
package directory.

------------------------------------------------------------------------

## Running

Wrong:

``` bash
java Main
```

Correct:

``` bash
java com.Main
```

The JVM expects the **fully qualified class name**, not the filename.

------------------------------------------------------------------------

## Output Directory (`-d`)

Instead of mixing `.class` and `.java` files:

``` bash
javac -d out com/Main.java
```

Produces:

``` text
out/
└── com
    ├── Main.class
    └── vehicle
        └── Car.class
```

Run:

``` bash
java -cp out com.Main
```

Where:

-   `-cp out` sets the classpath root.
-   `com.Main` is the FQN.

------------------------------------------------------------------------

## Classpath

The classpath is the list of locations Java searches for classes.

Java starts from the classpath root and follows the package path.

Example:

    Classpath root
        ↓
    com
        ↓
    vehicle
        ↓
    Car.class

------------------------------------------------------------------------

## Source Root vs Classpath

**Source Root** - Where `.java` files live. - Used by IDEs and the
compiler.

**Classpath** - Where `.class` files (or JARs) are searched at runtime
(and sometimes compile time).

------------------------------------------------------------------------

## Mental Model

Think of a class as having an address.

Name:

    Car

Address:

    com.vehicle.Car

The package declaration is part of the class's identity.

------------------------------------------------------------------------

# Practice

## Exercise 1

Create:

``` text
src
└── com
    ├── Main.java
    ├── Student.java
    └── school
        ├── Teacher.java
        └── Principal.java
```

Tasks:

1.  Write correct package declarations.
2.  Import `Student` into `Teacher`.
3.  Verify `Teacher` can use `Principal` without an import.
4.  Compile from the project root.
5.  Run `Main`.

------------------------------------------------------------------------

## Exercise 2

Add:

``` text
com
└── college
    └── Professor.java
```

Try:

``` java
import com.school.*;
import com.*;
```

Observe what is and is not accessible.

Then replace with explicit imports.

------------------------------------------------------------------------

# Key Takeaways

-   Packages are namespaces, not merely folders.
-   Every class belongs to exactly one package.
-   Folder structure must match the package declaration.
-   Imports bring names into scope; they do not move or copy classes.
-   Wildcard imports do not include subpackages.
-   The JVM runs classes using their fully qualified names.
-   Compile from the source root.
-   Prefer `javac -d out ...` and `java -cp out ...` when working from
    the command line.
