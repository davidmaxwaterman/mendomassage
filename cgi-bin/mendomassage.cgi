#!/usr/bin/perl
$mail_prog = '/usr/sbin/sendmail' ;
# This script was generated automatically by Visual Form Mail: http://www.oneseek.com

&GetFormInput;


@valid_ref = ('http://www.mendomassage.com','http://mendomassage.com') ;
foreach $ref (@valid_ref) {
if ($ENV{'HTTP_REFERER'} =~ m/$ref/i) {$is_valid = 1 ; last ;}
}
if (! $is_valid) {
print "Content-type: text/html\n\nERROR - Invalid Referrer\n" ;
exit 0 ;
}

$First_Name = $field{'First_Name'} ;	 
$Last_Name = $field{'Last_Name'} ;	 
$Area = $field{'Area'} ;	 
$Phone = $field{'Phone'} ;	 
$email_1 = $field{'email_1'} ;	 
$Date = $field{'Date'} ;	 
$Time = $field{'Time'} ;	 
$Treatment = $field{'Treatment'} ;	 
$Location = $field{'Location'} ;	 
$LocationOther = $field{'LocationOther'} ;	 
$test_1 = $field{'test_1'} ;	 
$No_People = $field{'No_People'} ;	 
$submit = $field{'submit'} ;	 
$reset = $field{'reset'} ;	 

$message = "" ;
$found_err = "" ;

$errmsg = "<p>Please enter your First Name</p>\n" ;

if ($First_Name eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please enter your Last Name</p>\n" ;

if ($Last_Name eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please enter your 3 digit phone Area Code</p>\n" ;

if ($Area eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }

elsif (length($Area) != 3) {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please enter your Phone Number</p>\n" ;

if ($Phone eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }

elsif (length($Phone) < 7) {
	$message = $message.$errmsg ;
	$found_err = 1 ; }

elsif (length($Phone) > 8) {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please enter a valid email address</p>\n" ;

if (($email_1 =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($email_1 !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please select a Date</p>\n" ;

if ($Date eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please select a Time</p>\n" ;

if ($Time eq "") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }


$errmsg = "<p>Please enter '9' (for the answer to what is 7+2)</p>\n" ;

if ($test_1 ne "9") {
	$message = $message.$errmsg ;
	$found_err = 1 ; }

if ($found_err) {
	&PrintError; }


$recip = "info\@mendomassage.com" ;
$frm_ = "info\@mendomassage.com" ;
$sbj_ = "Mendocino Coast Massage Reservation Request" ;
$hd_ = $recip.$frm_.$sbj ;
if (($hd =~ /(\n|\r)/m) || ($recip =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($recip !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
print "Fatal Error - Invalid email" ; 
exit 0; 
}

open (MAIL, "|$mail_prog -t");
print MAIL "To: $recip\n";
print MAIL "Reply-to: $frm_\n";
print MAIL "From: $frm_\n";
print MAIL "Subject: $sbj_\n";
print MAIL "Content-type: text/html\n\n";
print MAIL "\n\n";
print MAIL '<body style="background-color:#BBBA93;padding:0;margin:0">'."\n" ;
print MAIL '<div style="width:550px; background-color:#BBBA93; padding:10px">'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 9px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">Dear Felicity,</p>'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 6px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">The information below was sent to <span style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$First_Name.' '.$Last_Name.'</span></p>'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 6px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">---------/-----------------/------------------</p>'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 6px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">Thank you for contacting us through our website. Below is the information you entered.</p>'."\n" ;
print MAIL '<p style="margin-top: 6px;margin-bottom: 12px;font-family: \'Comic Sans MS\', cursive; font-size: 12pt;color: #2B3344;line-height:1.3em">Please note that this does not confirm your reservation. One of our therapists will contact you soon to make a final reservation.</p>'."\n" ;
print MAIL '<p style="margin-top: 6px;margin-bottom: 12px;font-family: \'Comic Sans MS\', cursive; font-size: 12pt;color: #2B3344;line-height:1.3em">If you need to contact us, please call Felicty on 707&bull;937&bull;2305, or reply to this email.</p>'."\n" ;
print MAIL '<table width="500" border="0" cellpadding="3" cellspacing="2">'."\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td width="162" align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Name:</div></td>'."\n" ;
print MAIL '    <td width="320"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$First_Name.' '.$Last_Name.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Phone:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold "> ('."\n" ;
print MAIL "    ".$Area.") ".$Phone."</div></td>\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">email:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$email_1.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Preferred Date &amp; Time:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Date.' at '.$Time.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Treatment:</font></div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Treatment.'</div> </td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Preferred Location:</div></td>'."\n" ;
print MAIL '    <td valign="top"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Location.'&nbsp;'.$LocationOther.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Number of Massages:</div></td>'."\n" ;
print MAIL '    <td valign="top"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$No_People.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "</table>\n" ;
print MAIL '<div style="clear:both; font-size:0px; line-height:0px">&nbsp;</div>'."\n" ;
print MAIL '<p style="margin-top: 12px;margin-bottom:6px;;font-family:\'Comic Sans MS\', cursive; font-size: 12pt;color:#2B3344;">Thanks from all of us at the Mendocino Coast Massage, and we look forward to meeting you soon.</p>'."\n" ;
print MAIL "</div>\n" ;
print MAIL "\n\n";
close (MAIL);


$recip = $email_1 ;
$frm_ = "info\@mendomassage.com" ;
$sbj_ = "Mendocino Coast Massage Reservation Request" ;
$hd_ = $recip.$frm_.$sbj ;
if (($hd =~ /(\n|\r)/m) || ($recip =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/) || ($recip !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z0-9]+)(\]?)$/)) {
print "Fatal Error - Invalid email" ; 
exit 0; 
}

open (MAIL, "|$mail_prog -t");
print MAIL "To: $recip\n";
print MAIL "Reply-to: $frm_\n";
print MAIL "From: $frm_\n";
print MAIL "Subject: $sbj_\n";
print MAIL "Content-type: text/html\n\n";
print MAIL "\n\n";
print MAIL '<body style="background-color:#BBBA93;padding:0;margin:0">'."\n" ;
print MAIL '<div style="width:550px; background-color:#BBBA93; padding:10px">'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 9px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">Dear '.$First_Name.',</p>'."\n" ;
print MAIL '<p style="margin-top: 6px; margin-bottom: 6px; font-family:\'Comic Sans MS\', cursive;font-size: 12pt;color: #2B3344;line-height:1.3em">Thank you for contacting us through our website. Below is the information you entered.</p>'."\n" ;
print MAIL '<p style="margin-top: 6px;margin-bottom: 12px;font-family: \'Comic Sans MS\', cursive; font-size: 12pt;color: #2B3344;line-height:1.3em">Please note that this does not confirm your reservation. One of our therapists will contact you soon, to make a final reservation.</p>'."\n" ;
print MAIL '<p style="margin-top: 6px;margin-bottom: 12px;font-family: \'Comic Sans MS\', cursive; font-size: 12pt;color: #2B3344;line-height:1.3em">In the meantime, if you need to contact us, please call Felicty on 707&bull;937&bull;2305, or reply to this email.</p>'."\n" ;
print MAIL '<table width="500" border="0" cellpadding="3" cellspacing="2">'."\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td width="162" align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Name:</div></td>'."\n" ;
print MAIL '    <td width="320"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$First_Name.' '.$Last_Name.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Phone:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold "> ('."\n" ;
print MAIL "    ".$Area.") ".$Phone."</div></td>\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">email:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$email_1.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Preferred Date &amp; Time:</div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Date.' at '.$Time.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Treatment:</font></div></td>'."\n" ;
print MAIL '    <td><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Treatment.'</div> </td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Preferred Location:</div></td>'."\n" ;
print MAIL '    <td valign="top"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$Location.'&nbsp;'.$LocationOther.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "  <tr>\n" ;
print MAIL '    <td align="right" valign="top"><div align="right" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt">Number of Massages:</div></td>'."\n" ;
print MAIL '    <td valign="top"><div align="left" style="font-family:Arial, Helvetica, sans-serif; font-size:11pt; font-weight:bold ">'.$No_People.'</div></td>'."\n" ;
print MAIL "  </tr>\n" ;
print MAIL "</table>\n" ;
print MAIL '<div style="clear:both; font-size:0px; line-height:0px">&nbsp;</div>'."\n" ;
print MAIL '<p style="margin-top: 12px;margin-bottom:6px;;font-family:\'Comic Sans MS\', cursive; font-size: 12pt;color:#2B3344;">Thanks from all of us at the Mendocino Coast Massage, and we look forward to meeting you soon.</p>'."\n" ;
print MAIL "</div>\n" ;
print MAIL "\n\n";
close (MAIL);
print "Content-type: text/html\n\n";
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'."\n" ;
print '<html xmlns="http://www.w3.org/1999/xhtml">'."\n" ;
print "<head>\n" ;
print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />'."\n" ;
print "<title>Mendocino Coast Massage - Contact Us</title>\n" ;
print '<link rel="stylesheet" href="../css/styles.css" type="text/css" />'."\n" ;
print "</head>\n" ;
print '<body style="background-color:#BBBA93">'."\n" ;
print '<div id="wrapper" style="width:600px; background-color:#BBBA93">'."\n" ;
print '<div id="content" style="padding-bottom:7px">'."\n" ;
print '     <img src="../images/contact_01_small.gif" width="125" height="112" alt="zen" style="float:right; margin:5px 0 5px 5px" />'."\n" ;
print "         <h1>Thanks for Contacting Us</h1>\n" ;
print "         <p>Below is the information you just entered.</p>\n" ;
print "         <p>We appreciate your interest, and someone will be in contact with you soon.</p>\n" ;
print '         <p style="font-family:Verdana, Geneva, sans-serif; font-size:13px"><strong>Name:</strong> '.$First_Name.' ['.$Last_Name.'<br />'."\n" ;
print "           <strong>Phone:</strong> (".$Area.") ".$Phone."<br />\n" ;
print "           <strong>Email:</strong> ".$email_1."<br />\n" ;
print "           <strong>Preferred Data &amp; Time:</strong> ".$Date." at ".$Time."<br />\n" ;
print "           <strong>Treatment:</strong> ".$Treatment."<br />\n" ;
print "           <strong>Preferred Location:</strong> ".$Location." ".$LocationOther."<br />\n" ;
print "          <strong>Number of People:</strong> ".$No_People."</p>\n" ;
print "         <p>A copy of the above will also be sent to ".$email_1.". Please note this is not a confirmed reservation. One of our therapists will call/email you for final confirmation.</p>\n" ;
print "         <p>Thanks again, and look forward to seeing you soon.</p>\n" ;
print "</div>\n" ;
print "</div>\n" ;
print "</body>\n" ;
print "</html>\n" ;

sub PrintError { 
print "Content-type: text/html\n\n";
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'."\n" ;
print '<html xmlns="http://www.w3.org/1999/xhtml">'."\n" ;
print "<head>\n" ;
print '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />'."\n" ;
print "<title>Mendocino Coast Massage - Contact Us</title>\n" ;
print '<link rel="stylesheet" href="../css/styles.css" type="text/css" />'."\n" ;
print "</head>\n" ;
print '<body style="background-color:#BBBA93">'."\n" ;
print '<div id="wrapper" style="width:600px; background-color:#BBBA93">'."\n" ;
print '<div id="content" style="padding-bottom:7px">'."\n" ;
print "     <h1>There was an error filling out the form </h1>\n" ;
print '         <p class="close">The following error(s) occurred.</p>'."\n" ;
print "         <ul>\n" ;
print "           <li><strong>".$message."</strong></li>\n" ;
print "         </ul>\n" ;
print "         <p>Please \n" ;
print '           <input style="margin-bottom:-3px" name="button" type="button" onclick="history.go(-1); return false;" value="Click here to return to form" />'."\n" ;
print "         </p>\n" ;
print "         <p>Then  make your corrections and click the &quot;Submit&quot; button again.</p>\n" ;
print "         <p>Thank you</p>\n" ;
print "</div>\n" ;
print "</div>\n" ;
print "</body>\n" ;
print "</html>\n" ;

exit 0 ;
return 1 ; 
}
sub GetFormInput {

	(*fval) = @_ if @_ ;

	local ($buf);
	if ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN,$buf,$ENV{'CONTENT_LENGTH'});
	}
	else {
		$buf=$ENV{'QUERY_STRING'};
	}
	if ($buf eq "") {
			return 0 ;
		}
	else {
 		@fval=split(/&/,$buf);
		foreach $i (0 .. $#fval){
			($name,$val)=split (/=/,$fval[$i],2);
			$val=~tr/+/ /;
			$val=~ s/%(..)/pack("c",hex($1))/ge;
			$name=~tr/+/ /;
			$name=~ s/%(..)/pack("c",hex($1))/ge;

			if (!defined($field{$name})) {
				$field{$name}=$val;
			}
			else {
				$field{$name} .= ",$val";
				
				#if you want multi-selects to goto into an array change to:
				#$field{$name} .= "\0$val";
			}


		   }
		}
return 1;
}

