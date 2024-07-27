 



# Synthetic Data Field Types

Following bot provides synthetic data generation capability:

*   [@dm:synthetic-dataset](/Bots/cfxdm/#bot-dmsynthetic-dataset)
    

### Example usage


```
@dm:synthetic-dataset         row_count = 1000 &         email_addresss = "email" &         date_of_birth = "past_date"
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=synthetic_1)

In this example pipeline:

> *   `row_count`: Is number of rows that should be generated in the output
> *   `email_address`: Column to be included in the output with values of field\_type `email`
> *   `date_of_birth`: Column to be included in the output with values of field\_type `past_date`

### Supported Field Types

| field\_type | sample\_value |
| --- | --- |
| address | 494 Brenda Villages Brettburgh, IN 87564 |
| administrative\_unit | Idaho |
| am\_pm | PM  |
| android\_platform\_token | Android 2.3.2 |
| ascii\_company\_email | dpatton@wells-carroll.com |
| ascii\_email | christopher96@yahoo.com |
| ascii\_free\_email | stuartamanda@gmail.com |
| ascii\_safe\_email | justinsims@example.net |
| bban | ZFJV29267211105176 |
| binary | b'\\x01}c\\xc9\\x04\\x13\\x94y\\x94\\xa9\\xd5\\xec\\x15\\xbd\\x96\\x9e\*1\\xf6"<K\\x9d\\xdd\\xd9?C ... |
| boolean | True |
| bothify | 83 Hl |
| bs  | evolve end-to-end e-business |
| building\_number | 212 |
| catch\_phrase | Synergized hybrid superstructure |
| century | IV  |
| chrome | Mozilla/5.0 (iPad; CPU iPad OS 4\_2\_1 like Mac OS X) AppleWebKit/531.0 (KHTML, li ... |
| city | Lake Robert |
| city\_prefix | East |
| city\_suffix | view |
| color | #a591d8 |
| color\_name | Aquamarine |
| company | Boyer Group |
| company\_email | badams@jackson.com |
| company\_suffix | Group |
| coordinate | \-102.118406 |
| country | Venezuela |
| country\_calling\_code | +230 |
| country\_code | CG  |
| credit\_card\_expire | 04/25 |
| credit\_card\_full | Discover Gary Brown 6011575748310492 07/27 CVC: 553 |
| credit\_card\_number | 4069649843189914675 |
| credit\_card\_provider | JCB 16 digit |
| credit\_card\_security\_code | 268 |
| cryptocurrency | ('USDT', 'Tether') |
| cryptocurrency\_code | NMC |
| cryptocurrency\_name | Cardano |
| csv | "Matthew Jenkins","574 Bennett Turnpike Port Stacey, ND 32136" "Jeanette Wilson ... |
| currency | ('LAK', 'Lao kip') |
| currency\_code | BIF |
| currency\_name | Indonesian rupiah |
| currency\_symbol | $   |
| current\_country | United States |
| current\_country\_code | US  |
| date | 2014-08-05 |
| date\_object | 2012-05-26 |
| date\_of\_birth | 1963-06-14 |
| date\_this\_century | 2012-07-28 |
| date\_this\_decade | 2020-09-18 |
| date\_this\_month | 2022-05-01 |
| date\_this\_year | 2022-02-19 |
| date\_time | 2019-10-16 10:51:23 |
| date\_time\_ad | 0748-12-23 23:33:42 |
| date\_time\_this\_century | 2009-06-12 17:20:53 |
| date\_time\_this\_decade | 2022-04-11 02:35:59 |
| date\_time\_this\_month | 2022-05-03 09:22:29 |
| date\_time\_this\_year | 2022-03-02 11:34:17 |
| day\_of\_month | 12  |
| day\_of\_week | Tuesday |
| dga | uo.com |
| domain\_name | wilson.info |
| domain\_word | rivera |
| dsv | "Samantha Roman","60051 Serrano Track Suite 175 Bishopside, NJ 57655" "John Pow ... |
| ean | 2248201475151 |
| ean13 | 4011383164575 |
| ean8 | 27455357 |
| ein | 92-9197908 |
| email | brandon77@hotmail.com |
| file\_extension | avi |
| file\_name | life.js |
| file\_path | /different/discover.xlsx |
| firefox | Mozilla/5.0 (Android 3.2; Mobile; rv:27.0) Gecko/27.0 Firefox/27.0 |
| first\_name | Gregory |
| first\_name\_female | Debra |
| first\_name\_male | Jason |
| fixed\_width | Chase Brown 1 Michael King 14 Sarah Spencer MD 16 Maxwell ... |
| free\_email | jasonfernandez@gmail.com |
| free\_email\_domain | hotmail.com |
| future\_date | 2022-05-09 |
| future\_datetime | 2022-05-08 22:33:19 |
| hex\_color | #ddcac7 |
| hexify | 3dff |
| hostname | db-50.glover.net |
| http\_method | GET |
| iban | GB24ABAS81675798900946 |
| image\_url | https://placeimg.com/717/727/any |
| internet\_explorer | Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.0; Trident/4.0) |
| invalid\_ssn | 209-00-4355 |
| ios\_platform\_token | iPhone; CPU iPhone OS 14\_2 like Mac OS X |
| ipv4 | 153.184.59.242 |
| ipv4\_network\_class | b   |
| ipv4\_private | 172.17.154.73 |
| ipv4\_public | 140.188.47.134 |
| ipv6 | 8b3:e14d:7c69:2698:5c69:ce0c:eb66:e751 |
| isbn10 | 1-277-25738-8 |
| isbn13 | 978-1-03-694638-8 |
| iso8601 | 1987-08-11T01:25:44 |
| itin | 999-97-1978 |
| job | Designer, jewellery |
| json | \[{"name": "David Tucker", "residency": "17419 Valencia Turnpike Suite 986\\nSouth ... |\
| language\_code | gez |\
| language\_name | Albanian |\
| last\_name | Williams |\
| last\_name\_female | Scott |\
| last\_name\_male | Allison |\
| latitude | 58.897671 |\
| latlng | (Decimal('-46.5174805'), Decimal('45.022490')) |\
| lexify | cTps |\
| license\_plate | 541 ALT |\
| linux\_platform\_token | X11; Linux i686 |\
| linux\_processor | x86\_64 |\
| local\_latlng | ('38.17492', '-122.2608', 'American Canyon', 'US', 'America/Los\_Angeles') |\
| locale | ayc\_PE |\
| localized\_ean | 0385099767899 |\
| localized\_ean13 | 0348165764819 |\
| localized\_ean8 | 07109805 |\
| location\_on\_land | ('53.16167', '6.76111', 'Hoogezand', 'NL', 'Europe/Amsterdam') |\
| longitude | 104.375295 |\
| mac\_address | f3:e1:15:5c:56:67 |\
| mac\_platform\_token | Macintosh; PPC Mac OS X 10 12\_8 |\
| mac\_processor | Intel |\
| md5 | c22f211c2ff82a3f4e07ae58f0d53552 |\
| mime\_type | image/gif |\
| month | 10  |\
| month\_name | May |\
| msisdn | 0740423120625 |\
| name | Dana Parrish |\
| name\_female | Kelly Costa |\
| name\_male | Nathan Mccoy |\
| null\_boolean | False |\
| numerify | 894 |\
| opera | Opera/9.85.(Windows NT 6.0; nan-TW) Presto/2.9.171 Version/11.00 |\
| paragraph | Ground movement necessary. Give meeting manage season officer. Avoid pick type c ... |\
| paragraphs | \['Whom approach look role bring. Country customer science TV. Most amount miss p ... |\
| password | bsSgVVpl(3 |\
| past\_date | 2022-04-21 |\
| past\_datetime | 2022-05-02 04:02:32 |\
| phone\_number | 656-856-4162 |\
| port\_number | 61894 |\
| postalcode | 45583 |\
| postalcode\_plus4 | 93504-2666 |\
| postcode | 38401 |\
| prefix | Dr. |\
| pricetag | $6,402.98 |\
| profile | {'job': 'Public house manager', 'company': 'Drake, Bridges and Ellis', 'ssn': '1 ... |\
| psv | "Jean Stone"\|"74461 Moore Route New Adamland, WY 56875" "Taylor Page"\|"2734 Hug ... |\
| bool | True |\
| decimal | 93169931345566.6 |\
| dict | {'power': 'oEywpAQLhzqDhbhoYFmN', 'hard': 1642, 'coach': 1985, 'unit': 'xZscMoPG ... |\
| float | \-745343973880.74 |\
| int | 6291 |\
| list | \[4158, datetime.datetime(1984, 9, 19, 0, 9, 57), 5461, 'ylIBCQRTKOTgJMvnSaXB', ' ... |\
| set | {'EbJUjOzmSrgwtBQqduPH', 'carrie47@rosales-walters.com', 'qiOOKZWDdNTaMxCeQuOf', ... |\
| str | oJiXQGUFgrkApseeSTSA |\
| random\_choices | \['c', 'a', 'a'\] |\
| random\_digit | 0   |\
| random\_digit\_not\_null | 5   |\
| random\_digit\_not\_null\_or\_empty |     |\
| random\_digit\_or\_empty |     |\
| random\_element | a   |\
| random\_elements | \['c', 'a'\] |\
| random\_int | 2249 |\
| random\_letter | i   |\
| random\_letters | \['O', 'y', 'H', 'j', 't', 'T', 'G', 'R', 'H', 'o', 'f', 'm', 'W', 'c', 'I', 'q'\] |\
| random\_lowercase\_letter | a   |\
| random\_number | 2200 |\
| random\_sample | \['a', 'c', 'b'\] |\
| random\_uppercase\_letter | R   |\
| randomize\_nb\_elements | 11  |\
| rgb\_color | 79,94,5 |\
| rgb\_css\_color | rgb(158,115,182) |\
| safari | Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10 6\_5 rv:4.0; sk-SK) AppleWebKit/535. ... |\
| safe\_color\_name | fuchsia |\
| safe\_domain\_name | example.com |\
| safe\_email | james08@example.net |\
| safe\_hex\_color | #440011 |\
| secondary\_address | Suite 927 |\
| sentence | Billion process represent avoid training behavior. |\
| sentences | \['Scene difficult decide north establish.', 'Page while identify.', 'Form oil si ... |\
| sha1 | b5a60b804ab7ac714e09b4842a0bfbed51ce8536 |\
| sha256 | 8179cdbabcc896f86b09c4d410fbcef6d55d9ebd447fbb2a4c596823c5ad5c92 |\
| simple\_profile | {'username': 'nmyers', 'name': 'Heather White', 'sex': 'F', 'address': '4533 Mor ... |\
| slug | security-suffer |\
| ssn | 864-67-8162 |\
| state | Virginia |\
| state\_abbr | AR  |\
| street\_address | 7430 Murphy Junction |\
| street\_name | Williams Isle |\
| street\_suffix | Village |\
| suffix | MD  |\
| swift | VFUFGBCK |\
| swift11 | TXGCGBGEI7I |\
| swift8 | EOOEGBLX |\
| text | Not board scientist court smile need can manage. Product rock among increase fee ... |\
| texts | \['Find summer drug entire. Research avoid center how development. When ability p ... |\
| time | 07:34:22 |\
| time\_delta | 0:00:00 |\
| time\_object | 18:12:01 |\
| time\_series |     |\
| timezone | Africa/Nairobi |\
| tld | net |\
| tsv | "Anne Pope" "71926 Kevin Burgs Hayeston, AK 83779" "Carl Ramirez" "91261 Philli ... |\
| unix\_device | /dev/xvdz |\
| unix\_partition | /dev/sda1 |\
| unix\_time | 264888510 |\
| upc\_a | 832877102279 |\
| upc\_e | 04554653 |\
| uri | http://www.king.org/login.php |\
| uri\_extension | .php |\
| uri\_page | post |\
| uri\_path | app/wp-content/categories |\
| url | http://www.wilson-travis.org/ |\
| user\_agent | Opera/9.39.(Windows NT 6.1; lb-LU) Presto/2.9.165 Version/12.00 |\
| user\_name | jonwilliams |\
| uuid4 | 86fec95d-9ca8-4bb9-8299-5b61684265c9 |\
| windows\_platform\_token | Windows NT 5.2 |\
| word | college |\
| words | \['whether', 'ago', 'write'\] |\
| year | 1986 |\
| zipcode | 41241 |\
| zipcode\_plus4 | 12414-7642 |\
\
Was this page helpful?\
\
Thanks for your feedback!\
\
Thanks for your feedback!