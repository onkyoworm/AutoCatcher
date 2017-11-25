# AutoCatcher
Automate running scripts when pentesting
	
In beta 1, we only support the function of running SQLMap automatically</br>		
To get a best experience, we suggest you save all the url that you want to exploit into a textual file like `**.txt`</br>
By default, we provide some useful options for SQLMap's running. </br>
(Default argument:)
`python sqlmap.py -u "target url" --threads=10 --tamper=randomcomments --random-agent --level=5`	</br>
Also, you can provide your wanted options in belows format.	
	

	http://www.xxx.com/123.php?XXXXX --*options1||options2||……||optionsn*--
	
	Furthermore, the optionsn 's format is below:
	In SQLMap, maybe you use:
		python sqlmap.py -u "http://www.aaa.com" --post="xxxxxxx" --xxx="xxxxxx" --xxxx="xzxxx" --xxxx="xxxxxx"
	As you see, each options is split by a space, but remember we split it by "||" and no space.
	Below is this script's usage
	http://www.xxx.com/sdfasdf --*--xxx="xxxxxx"||--xxxx="xzxxx"||--xxxx="xxxxxx"*--
	