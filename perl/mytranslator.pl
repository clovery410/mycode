# Student Name: Qianhui Jiang;
# Student ID: W1189996;

sub plainPrint {
    print FILE @_;
}

sub getCount {
    while ($line = <INDATA>) {
	chomp($line);
	($school, $type, $number) = split(",", $line);
	$count{$type} .= $number . " ";
    }
    foreach $type (sort keys %count) {
	$total = 0;
	@count = split(" ", $count{$type});
	foreach $number (@count)
	{
	    $total += $number;
	}
	$height = $total / 2;
	$base = 500 - $height;
	$svg = qq{<svg width="180" height="500">
<rect x="40" y="$base" rx="20" ry="20" width="100" height=$height
style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
</svg>};
	plainPrint($svg);
    }
}

sub getName {
    foreach $type (sort keys %count) {
	print FILE qq{<svg width="180" height="50">
<text x="60" y="10" rx="20" ry="20" width="100" style="text-align:center">$type</text>
</svg>};
    }
}

# Main Function from here
open (FILE, '>', "cell-phones_yourstudentid.html") or die $!;
open (INDATA, "cell-phones.csv");
%count;
$html_first = qq{
<!DOCTYPE html>
<head>
<title>Cell-phone Usage</title>
<meta charset="uft-8" />
</head>
<body>
<h1>Cell-phone Usage Survey Results</h1>};
$html_second = qq{</body>
</html>};
$div_open = qq{<div>};
$div_close = qq{</div>};
plainPrint($html_first);
getCount();
plainPrint($div_open);
getName();
plainPrint($div_close);
plainPrint($html_second);
close FILE;
close INDATA;
