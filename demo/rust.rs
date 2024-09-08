// Function
pub fn run() {
   greeting("Hello", "Jane");

   let get_sum = add(5, 5);
   println!("Sum: {}", get_sum);

   let n3: i32 = 10;
   let add_num = |n1: i32, n2: i32| n1 + n2 + n3;
   println!("C Sum: {}", add_num(3, 3));
 }

 fn greeting(greet: &str, name: &str) {
   println!("{} {}, nice to meet you!", greet, name);
 }

 fn add(n1: i32, n2: i32) -> i32 {
   n1 + n2
 }


// Conditionals
pub fn run() {
   let age: u8 = 22;
   let check_id: bool = true;
   let knows_person_of_age = true;

   // If Else
   if age >= 21 && check_id || knows_person_of_age {
     println!("Bartender: What would you like to drink?");
   } else if age < 21 && check_id {
     println!("Bartender: Sorry, you have to leave");
   } else {
     println!("Bartender: I'll need to see your ID");
   }

   // Shorthand If
   let is_of_age = if age >= 21 { true } else { false };
   println!("Is Of Age: {}", is_of_age)
 }