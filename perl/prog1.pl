print "Please input teh circle's radius:";
$radius = <STDIN>;
$area = 3.14 * $radius * $radius;
print "The area is: $area \n";

@array = (1, 2, 3);
$length = @array;
print "@array,  $length\n";

@price_list = (4, 5, 6);
foreach $price (@price_list) {$price += 0.20;}
@price_list[$#price_list] = 5;
print "@price_list\n";
print "$#price_list\n";

$stuff = "233:::466::688";
@number = split(m":+", $stuff);
print "splited number is @number\n";

%salaries = ("Joe", 4000, "John", 3500, "Michel", 5200);
$salary = $salaries{"Joe"};
print "Joe's salary is $salary\n";

@ayy = qw(AAA BBB CCC);
print @ayy;
print "\n";

$line = 'It is THIS and not THAT';
($one, $two) = ($line =~ m/(TH..).*(TH..)/);
print "$1 $2 $& $one $two\n";

$string = "softly slowly surely subtly";
$string =~ m"((s...ly\s*)*)";
print "$1 $2\n";

@word = qw(a silly fox jumped over a silly horse);
print @word, "\n";
$howMany = grep /silly/, @word;
print $howMany, "\n";

@numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9);
@lessThanFive = grep ($_ < 5, @numbers);
print @lessThanFive, "\n";

@tokens = ("A String", 234, "String 2", 111);
@ints = grep (m"^\d+", @tokens);
print @ints, "\n";

@line = qw(jumped over a rail and hopped across a meadow);
@list = grep {s /ed/s/ if /^jump/} @line;
print @list, "\n";

@numbers = (1, 30, 200, 50, 200, 450, 2000);
@greaterThan50 = grep {$_ > 50} @numbers;
print @greaterThan50, "\n";
