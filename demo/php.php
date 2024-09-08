<!-- 1. Example -->
<?php
  function getAdder($x) {
    return function($y) use ($x) {
      return $x + $y;
    };
  }

  $adder = getAdder(8);
  echo $adder(2);
?>

<?php
   class User {
   private $name;
   public $email;
   public $password;

   public function __construct($name, $email, $password) {
      $this->name = $name;
      $this->email = $email;
      $this->password = $password;
   }

   function getName() {
      return $this->name;
   }

   function __destruct() {
      echo "The user name is {$this->name}.";
   }
   }

   class employee extends User {
   public function __construct($name, $email, $password, $title) {
      parent::__construct($name, $email, $password);
      $this->title = $title;
   }

   public function getTitle() {
      return $this->title;
   }
   }

   $employee1 = new employee('John','johndoe@gmail.com','123456','Manager');
   echo $employee1->getTitle();
?>