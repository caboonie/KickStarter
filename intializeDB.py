
from model import *
# import pandas as pd
# import numpy as np

class TeamObject:
	def __init__(self, name, members, video, description_he, description_ar, description_en, image):
		self.name=name
		self.members=members
		self.video=video
		self.description_he=description_he
		self.description_ar=description_ar
		self.description_en=description_en
		self.image=image
## Add Teams to the database
# num_teams = 10
teams = {
	1: TeamObject(name="Childn’t", members="Warrd, Nisreen, Gilead, Nicole, Lyne",
		video="https://www.youtube.com/embed/gopjiCJ0Y5k",
		description_he="מעל ל-37 ילדים מתים כל שנה בישראל בעקבות שכיחתם או השארתם ברכב חם. אנחנו יצרנו אפליקציה במטרה להזכיר לך לא לשכוח את ילדך ברכב. האפליקציה תתחבר ישירות למערכת הבלוטות' של הרכב וכאשר המנוע יתכבה, היא תזהה את התנתקות הבלוטות' ותשמיע קטע קול האומר \"אל תשכח את ילדך\". חזוננו הוא להפחית את הבעיה הכה שכיחה הזו ואף להכחידה כליל על מנת להבטיח חיים לילדנו.",
		description_ar="هناك أكثر من ٣٧ طفل كل عام يفقدون حياتهم في اسرائيل بسبب نسيانهم في السيارة. تصبح درجات الحرارة مرتفعة جداً في الصيف، وذلك يؤدي إلى مقتل الطفل. قمنا بعمل تطبيق يتصل بشكل تلقائي إلى بلوتوث السيارة، وعندما تطفئ السيارة سيلغى الاتصال بالبلوتوث ويتكلم التطبيق ويقول \"صباح الخير، لا تنسى طفلك\". هدفنا هو مساعدة الوالدين في تنظيم وقتهم لنقلل من هذه الظاهرة لتوفير حياة أفضل لأولادنا.",
		description_en="Over 37 children die every year in Israel due to being forgotten/left in a hot car. We created an app to remind you to not forget your child. The app will automatically connect to the car’s bluetooth. Once the car's engine turns off the app will recognize the bluetooth's disconnection and play an audio message saying \"don't forget your child\". Our vision is reducing, this  unfortunately increasing phenomenon and providing a future for our children.",
		image="/static/team_mockups18/childnt.png"
	),
	2:TeamObject(
		name="ArtFlict",
		members="Hala A.S, Ramzi, Naomi, Tomer, Siham",
		video="https://www.youtube.com/embed/XVCo2Z7i7b8",
		description_he="הבעיה:\n פלסטינים וישראלים סובלים מאירועים יומיומיים בהם הם מתמודדים בשל הסכסוך. \n\
			הפִּתָרוֹן:\n אפליקציה שבה אנשים באופן אנונימי חולקים את דאגותיהם, או דברים שהם נתקלו בהם במהלך היום בעקבות הסכסוך. האומנים הולכים להציג את האירועים באמצעות ציור. \n\
			המשימה:\n ArtFlict הוא יישום המוקדש לשרת את אלה הסובלים מן הסכסוך הישראלי פלסטיני, על ידי מתן פלטפורמה למשתמשים לחלוק סיפורים ולקשר אותם עם אומנים שיציירו ציורים בהקשר של הסיפורים שיובאו. אנו מתכוונים לייצר יותר חמלה בין אנשים. ולייצר אפליקציה שבה האנושיות והאמפתיה נמצאים בלבם של אנשים. \n\
			החָזוֹן=\n לספק פלטפורמה לפלסטינים ולישראלים לחלוק את הסבל שלהם ולקבל טיפול בצורה אמנותית.",
		description_ar="المشكلة:\n يعاني الفلسطينيون والإسرائيليون من أحداث يومية تحدث معهم بسبب الصراع الفلسطيني الإسرائيلي. \n\
			الحل:\n تطبيق يشارك فيه الأشخاص -بشكل مجهول- مخاوفهم، أو المواقف التي واجهوها خلال اليوم بسبب النزاع . بعد ذلك سيقوم فنانون  بعرض ووصف المعاناة من خلال لوحة فنية يرسمها الفنان. \n\
			المهمة:\n “Artflict”هو تطبيق مخصص لخدمة أولئك الذين يعانون من الصراع الفلسطيني الإسرائيلي عن طريق  توفير برنامج  للمستخدمين لتبادل القصص التي يعانون منها بسبب الصراع، وأيضا للفنانين لرسم لوحات فنية عن تلك القصص. نحن نعتزم خلق المزيد من التعاطف بين الناس، تطبيق حيث الإنسانية والتعاطف تغزو قلوب الناس. \n\
			الرؤية:\n توفير تطبيق للفلسطينيين والإسرائيليين لمشاركة معاناتهم اليومية والحصول على العلاج بطريقة فنية.",
		description_en="Problem:\n Palestinians and Israelis are suffering from daily based events they deal with due to the conflict. \n\
			Solution:\n An app in which people anonymously share their concerns, or things they have faced during the day due to the conflict. Artists are then going to demonstrate the suffer through a painting. \n\
			The Mission:\n ArtFlict is an app dedicated to serving those who suffer from the Palestinian Israeli conflict, by providing a platform for users to share stories and for artists to make paintings about those stories. We intend to create more compassion between people. An app where humanity and empathy are in people’s hearts. \n\
			Vision:\n Provide a platform for Palestinians and Israelis to share their sufferings and get treated in an artistic way.",
		image="/static/team_mockups18/artflict.jpg"
	),
	3:TeamObject(
		name="Group 2",
		members="Sama, Ade, Yuly, Mahmoud, Avigail",
		video="https://www.youtube.com/embed/8hsL16n_ku0",
		description_he="אחוז משמעותי של צעירים- פלסטינים ויהודים יוצרים קשר לעיתים נדירות עם אנשים מהלאום השני. \n\
			אז אנחנו רוצים להקים תוכנית לנוער וצעירים שתכלול מספר קבוצות, בכל קבוצה יהיו אנשים משני הלאומים באיזורים שונים. חברי הקבוצה יפגשו אחת לשבוע, ישבו יחד, עם פיצה וכיבוד וידונו על נושאים מסויימים (נתחיל בנושאים שונים כגון חברה, מוסר, מדע וכ׳ו.... ונעבור לאט לאט לפוליטיקה). \n\
			פעם או פעמיים בשנה, כל הקבוצות יפגשו בכנס גדול עם פעילויות שונות אחת מהפעילויות תהיה דיון פוליטי לפי כללים. \n\
			החזון שלנו הוא שפלסטינים וישראל יקבלו אחד את השני כאנשים, ואנחנו שואפים להבנה כללית שתהיה מהצד הפוליטי הנגדי כלומר הצד ההפוך לצד הלאומי בו אתה מצודד.",
		description_ar="نسبة كبيرة من الشباب والصبايا الفلسطينيين والإسرائيليين لا يتعاملون كثيرا مع اشخاص من القومية الاخرى. \n\
			لذلك، فإننا نريد ان نؤسس برنامج لهذه الفئة العمرية. البرنامج يتضمن عدة مجموعات، كل مجموعة للمشتركين من منطقة معينة، اعضاء كل فرقة يجتمعون بلقاءات اسبوعية ويجلسون بدائرة مع اطعمة ومشروبات بينهم ويتناقشون بموضوع مختلف كل لقاء (نبدأ بمواضيع اجتماعية/علمية/اخلاقية ومع الوقت ننتقل الى المواضيع السياسية). \n\
			مرة او مرتين بالسنة تلتقي كل المجموعات في مؤتمر واحد، فيه يشتركون بفعاليات مختلفة احداها المناظرات بادوار متعاكسة. \n\
			رؤيتنا هي الفلسطينيين والاسرائيليين متقبلين بعضهم بعضا كأشخاص، نحن نطمح لوعي الجميع بأن معارضة سياسة معينة لا تعني معارضة شعب كامل.",
		description_en="A significant percentage of Palestinians and Israelis rarely interact with people from the other nationality. \n\
			So we want to estestablish a program for teenagers and young adults that contains a number of groups each for people from a certain area, the group members meet up once a week and sit in a circle with pizza and drinks in the middle to discuss a certain topic (we'll start off with social/scientific/moral topics and slowly move to politics). \n\
			Once or twice a year all the groups meet up in one big conference in which they take part in different activities one of them is having a political debate in reversed roles. \n\
			Our vision is Palestinians and Israelis accepting each other as people, we aspire to the general realization that being against a certain policy does not mean opposing an entire nationality.",
		image="/static/team_mockups18/group2.jpg"
	),
	4:TeamObject(
		name="Scope",
		members="Malak Jabarin, Nasif Francis, Luna Abu Jaber, Noa Hadad, Zohar Liberman, Guy Sila",
		video="https://www.youtube.com/embed/b5YzDd_ZJ80",
		description_he="העולם אותו אנחנו מדמיינים מורכב מאנשים שיודעים איך לנהל את הזמן, האנרגיה והכסף שלהם בצורה יעילה, והם בעלי יכולות תקשורתיות ויכולת לפתור בעיות הצצות בחייהם. אנחנו מדמיינים אנשים בוגרים ומפותחים, שלומדים מהניסיון שלהם, אנשים שיש להם את הכלים והמשאבים להתנהל במצבים חדשים ולא מוכרים, אנשים שיש להם ידע רחב בכישורים הכרחיים לחיים.",
		description_ar="نصوّر في مخيّلتنا عالمًا حيث الناس قادرين على ادارة وقتهم ومالهم وطاقاتهم بشكل سليم، ولديهم قدرة على التواصل وحل المشاكل. نحن نتخيّل البالغين الصغار واعون و متطورون، قد تعلموا من تجاربهم، عندما يواجهون ظروف وبيئة جديدة، لديهم القدرة والأدوات الكافية للتعامل معها بشكل ناجع، أشخاص لديهم نطاق واسع من المعلومات الضرورية .",
		description_en="We envision a world where people know how to manage their time, money and energy well, and have strong networking and problem solving skills. We imagine mature, evolved young adults, who have learned from their experiences, People that when faced with a new surrounding, they have tools and resources to cope with it effectively, people who have a wide scope of essential knowledge.",
		image="/static/team_mockups18/scope.jpeg"
	),
	5:TeamObject(
		name="MegaBite",
		members="Adi, Yonatan, Alicia H, Alicia K, and Rajai ",
		video="https://www.youtube.com/embed/2MOnk0by5uI",
		description_he="בעיה:\n מרכולים ומסעדות בישראל ובגדה המערבית קונים יותר מדי סחורה ונמצאים בעודף סחורה בסופו של הדבר, מה שגורם להם לזרוק את הסחורה הנותרת שעומדת לפוג תוקפה. \n\
			פתרון:\n אפליקציה/אתר/פלטפורמה כלשהי שתחבר בין מרכולים ומסעדות לעמותות שמטרתן לתרום את האוכל לנזקקים. הפלטפורמה תאפשר לחנויות בעודף סחורה למכור במחיר זול יותר לעמותות. \n\
			חזון:\n אנחנו מקווים להרחיב את שירותינו, לתרום חבילות עם מגוון דברים ולא רק כמות גדולה של סוג אחד, לאפשר תרומות של יחידים לעמותות המשתפות עימנו פעולה ולהתרחב למדינות אחרות. \n\
			משימה:\n הפרויקט שלנו ינסה להפחית את כמות פסולת המזון המיוצאת כל שנה ולתרום אוכל לנזקקים בדרך של לחבר בין עמותות וארגונים לחנויות כמו מרכולים ומסעדות שיכולות לתרום מזון בדרך קלה ונוחה.",
		description_ar="المشكله:\n تقوم متاجر مواد التموين في الضفه الغربيه واسرائيل بتخزين مواد اكثر من المطلوب مما يؤدي الى هدر عام للمأكولات. \n\
			الحل:\n ايجاد سبيل او برنامج لربط متاجر التموين بالمؤسسات الغير حكوميه والتي هدفها مساعدة الناس المحتاجه. وهذا البرنامج يسمح للمتاجر التي عندها فائض بالمواد التموينيه ببيعها للمؤسسات الغير حكوميه بسعر أقل من السوق. \n\
			الرؤيه:\n نأمل بتوسيع خدماتنا حتى تصل المطاعم أيضاً بجانب متاجر التموين، تقديم حزم الرعايه للمؤسسات بدل الكميه فقط، إعطاء الفرصه للأشخاص بالتبرع لتلك المؤسسات وثم توسيع خدماتنا للدول المجاوره. \n\
			رؤيتنا هي رسالتنا:\n العمل على ترتيب النموذج الغير منظم الى خدمه توصيل المواد الغذائيه للمحتاجين بطريقه نظيفه واكثر فعاليه وبنفس الوقت العمل على إنزال نسبة التبذير والانتاج في اسرائيل والضفه الغربيه. ثم توفير المواد الغذائيه للمحتاجين والمؤسسات بسعر معقول وبمتناول اليد. ايجاد برنامج مركزي للمؤسسات والمتاجر التموينيه يمكنهم من تبادل البضائع لأنه بالوقت الحاضر الطريقه غير منهجيه. ",
		description_en="Problem:\n Grocery stores in the West Bank and Israel overstock in produce resulting in general waste of food. \n\
			Solution:\n A platform that connects grocery stores and non-profit organizations whos goal is to help people in need. The platform allows grocery stores to offer overstocked produce for large price cuts to these organizations. \n\
			Vision:\n We hope to expand our services to restaurants in addition to grocery stores, deliver care packages to organizations instead of a quantity of produce, allow single individuals to donate to these organizations, and expand our services to neighboring countries. \n\
			Mission:\n Our vision and mission is: Our mission is to make the archaic model of getting food to the poor much cleaner and efficient while decreasing waste and production in Isreal and the West Bank, to provide food to people in need and organizations at an affordable price. Our mission is to have a centralized platform organizations and grocery stores can exchanged goods since as it is now the method is archaic. ",
		image="/static/team_mockups18/megabite.jpeg"
	),
	6:TeamObject(
		name="limitless",
		members="Amir, Ben, Carlos, Leen, Sham, Hala",
		video="https://www.youtube.com/embed/ABKgKTdCIPY",
		description_he="התקווה שלנו לעתיד הקרוב הוא שאנשים לא יהיו תלויים בחברים ובבני משפחתם כדי לגלות דברים ותחומי עניין חדשים, אנו מקווים כי אנשים יגלו את תחומי עניין ואת התשוקות שלהם בחיים ללא הלחץ של האנשים סביבם, באופן עצמאי. אנו מקווים שאנשים יצאו מאזור הנוחות שלהם ומהמעגל הפנימי שלהם, וכך ייצרו לעצמם מציאות לפי דעתם וללא התערבות חיצונית.",
		description_ar="كلنا أمل بأن يعبر الناس عما يجول في خاطرهم فيبدعون ويخلقون أشياءهم ويمارسون هواياتهم من غير ان ينصاعوا لإملاءات المحيط القريب منهم او البعيد ، كلنا أمل بأن ينهض الناس بأنفسهم متجاوزين جميع المعيقات النفسية والاجتماعية التي من شأنها احباط مسيرتهم لاكتشاف قدراتهم وأهدافهم والتحليق في فضاء  وسيع ولا نهائي من الإبداع",
		description_en="We hope that in the near future people dont depend on their friends and family to create their intrests, we hope that people create their own intrests and their own passions in life without the pressure of the people around them. We hope that people step out of their comfort zone and their inner circle and create a reality where everything is possible and the sky is their limit.",
		image="/static/team_mockups18/limitless.jpg"
	),
	7:TeamObject(
		name="Group 5",
		members="Malak L, Luna AN, May R, Robert K, Chris E & George R",
		video="https://www.youtube.com/embed/wLvs5ruS9Zo",
		description_he="המטרה שלנו היא להעלות את ההערכה העצמית של התלמידים, ולעזור להם להיות יותר מוכנים לחייהם הבוגרים ע\"י זה שיכירו את עצמם יותר טוב ואת מי הם שואפים להיות.",
		description_ar="هدفنا هو مساعدة الطلاب في تقوية ثقتهم بأنفسهم, وتجهيزهم لمواجهة الحياة الخارجية وبناء مستقبل ناجح كبالغون عن طريق معرفتهم لأنفسهم بعمق ومن يريدون ان يصبحوا بالمستقبل.",
		description_en="Our goal is to help the students improve their self esteem, and help them be more ready to face the outer life and build a successful future as adults by knowing themselves better and who they want to become.",
		image="/static/team_mockups18/group5.png"
	),
	8:TeamObject(
		name="ReGu",
		members="Zain Al Qalawi, Dana Ghoul, Fouad Jaber, and Yotam Asael",
		video="https://www.youtube.com/embed/KMLYbUbLecY",
		description_he="הבעיה בה התמקדנו היא שאנשים רבים מתקשים בניהול חשבונות הבנק שלהם ובהצבת גבולות תקציבים להוצאות, במיוחד כאשר מדובר בצעירים שהצטרפו זה עתה ל\"עולם המבוגרים\", או כאשר מדובר בסטודנטים רחוקים מביתם וממשפחותם שמקבלים את שכרם דרך האשראי. על כן, אנו מכינים אפליקציה אשר תעזור לאנשים הללו לנהל את החשבונות שלהם, ותכלול עזרים לחישוב תקצוב הוצאותם כדי לחסוך בכסף ולהעמיד אותם על רגליהם. דבר נוסף שיכלל באפליקציה הוא עמוד טיפים וטריקים שיעזרו ללקוח עם הנתונים הכספיים שלו.",
		description_ar="مشكلتنا هي أن الناس لا يجيدون إدارة حساباتهم المصرفية ولا يستطيعون تشكيل حدود الإنفاق المناسبة لهم، لا سيما عندما يكونون صغارًا شبابًا انضموا حديثًا إلى مرحلة البلوغ ، أو إذا كانوا طلابًا بعيدين عن عائلاتهم ويحصلون على دخلهم عبر بطاقات الائتمان. ولذلك ، فإننا نقوم بإنشاء تطبيق من شأنه أن يساعد هؤلاء الأشخاص على إدارة حساباتهم المصرفية وسيكون لديهم ميزات تساعدهم على حساب حدود الإنفاق الخاصة بهم من أجل توفير المال وأن يكونوا على المسار الصحيح. هناك شيء آخر سيظهر على تطبيقنا و هو النصائح والحيل لمساعدة الزبون في بياناته المالية.",
		description_en="Our problem is that people tend to struggle with managing their bank accounts and proper spending limits, especially when they are young adults who have recently joined adulthood, or if they are students that are far away from their families and receive their income via credit cards. Therefore, we are creating an application that will help these people manage their bank accounts and will have features that will help them calculate their spending limits in order to save money and to be on the right track. Another thing our app will feature is tips and tricks to help the customer with their financials.",
		image="/static/team_mockups18/regu.jpeg"
	),
	9:TeamObject(
		name="EasyLicense",
		members="Naim Mousa, George Abo Dauod, Sivan Ben Moha, Shira Zuker, Layan Makhool",
		video="https://www.youtube.com/embed/LmfowVWerrg",
		description_he="עם כל כך הרבה מדריכי נהיגה אך משאבים מעטים, כדי למצוא את האדם הנכון, בני נוער נאלצים פעמים רבות להתפשר על מדריך שאינו בהכרח המתאים ביותר עבורם. הפלטפורמה שלנו, מאפשרת לבני נוער למצוא את מדריך הנהיגה המושלם עבורם על בסיס ביקורות שהמורה מקבל מבני נוער אחרים שהמורה לימד. בדרך זו, בני נוער יכולים למצוא את המדריך המושלם עבורם, ולקבל רישיון נהיגה ללא כאב הראש שמגיע עם העניין. החזון שלנו, הוא ליצור סביבה שבה יש רשת חופשית הולכת וגדלה בין מדריכים ותלמידים רשת זו תאפשר הקלה על התלמידים למצוא מדריך, ועל המדריך לקבל תלמידים ללמד.\n https://pr.to/EDS27P/ - MVP",
		description_ar="العديد من معلمي القيادة والقليل من الوسائل لإيجاد المناسب، الشباب في العديد من الأحيان يضطرون للإكتفاء بالموجود ما قد لا يكون الأفضل لهم. مشروعنا يتيح لهؤلاء المراهقين إيجاد مرشد القيادة الأفضل لهم بحسب التقييمات التي يحصل عليها كل مدرس من طلاب آخرين. بهذه الطريقة، باستطاعة المراهقين إيجاد مدرس القيادة الذي يلائمهم شخصيا، والحصول على رخصة القيادة بدون المتاعب التي قد ترافق مدرس قيادة غير مناسب. هدفنا هو توفير إطار وحيز حيث تطور شبكة تربط بين مدرسي القيادة والشباب المعنيين بالحصول على الرخصة ما سوف يسهل على الطلاب إيجاد مدرسين، وعلى المدرسين إيجاد طلاب.\n https://pr.to/EDS27P/ - MVP",
		description_en="With so many driving instructors out there and so few resources to find the right one, teenagers are many times forced to settle for an instructor that may not necessarily be the best fit for them. Our platform, allows teenagers to find the perfect driving instructor for the based on reviews the instructor gets from other teenagers they have taught. That way, teenagers can find the perfect instructor for themselves, and get a driver’s license without the headache that comes with it. Our vision, is to create an environment where there is a free and ever growing network between instructors and students they will make it both easier for the students to find an instructor, and easier for the instructor to find students to teach.\n https://pr.to/EDS27P/ - MVP",
		image="/static/team_mockups18/easylicense.jpg"
	),
	10:TeamObject(
		name="FamilyTime",
		members="Michella Kopti, Nadia Tahhan, Mariel Basous, Shira Struminski",
		video="https://www.youtube.com/embed/FyAQxcUwYNo",
		description_he="החזון שלנו הוא לבנות מחדש את הקשרים בין חברי משפחות מרוחקות שמושפעות מהטכנולוגיה רבות ליצירת ריחוק, דרך שימוש בטכנולוגיה ככלי לחבר אותם מחדש אחד לשני מאשר להרחיק אותם.",
		description_ar="رؤيتنا هي إعادة ربط وتحسين العلاقات بين أفراد العائلة ، عن طريق تحويل الاداة المسببة لهذه المشكلة الا اداة تحد منها",
		description_en="Our vision is to re-establish the connection among divided families whom are deeply embedded in technology, through using it as a tool to re-connect them rather than to disconnect them.",
		image="/static/team_mockups18/familytime.jpg"
	)
}


# for i in range(12):
# 	newTeam = Team(name = "Team " + str(i+1))
# 	session.add(newTeam)
# 	session.commit()

# ## Add all students to the database:


# students = pd.read_csv('../students.csv')

# first_names = students['Student first name']
# last_names = students['Student last name']
# student_ids = students['ID number']
# team_number = students['Team Number']

# for i in range(len(first_names)):
# 	student = User(group = 'student', first_name = first_names[i],  last_name = last_names[i], email = first_names[i]+last_names[i][0])
# 	if int(team_number[i]) != 0:
# 		student.team_id = int(team_number[i])
# 	student.hash_password(str(student_ids[i])[0:9])
# 	session.add(student)
# 	session.commit()


## Add products to the database
# photos = ["https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4057.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4058.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4065.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4051.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4054.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4074.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4078.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4072.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4075.JPG","https://raw.githubusercontent.com/meet-projects/KickStarter/master/static/pictures/IMG_4081.JPG","https://github.com/meet-projects/KickStarter/blob/master/static/pictures/IMG_4084.JPG"]
# videos = ["https://www.youtube.com/embed/RZydfIkI1f4","https://www.youtube.com/embed/Rw35xX-tAu8","https://www.youtube.com/embed/jgSUpPOf0ww","https://www.youtube.com/embed/tuh6bEbXLaM","https://www.youtube.com/embed/UJ7CnUSZvvQ","https://www.youtube.com/embed/gwMvt7RU09Q","https://www.youtube.com/embed/XmD_iChKh-g","https://www.youtube.com/embed/JtLkUoKmPZc","https://www.youtube.com/embed/D_drrBUkT88","https://www.youtube.com/embed/0Hw5i7LoPeE","https://www.youtube.com/embed/g1YGnbKKjTw"]


# ipsum_he = "פנאי ניווט משחקים ארץ אל. דת ריקוד שדרות קודמות כדי, של כדי שתפו מושגי, צ'ט אל זקוק הבאים. אחרים אתנולוגיה מה עוד, אחד מה לציין בדפים. לתרום ייִדיש לאחרונה על עוד, על ויקי סרבול מתמטיקה עזה. מלא מדעי בישול איטליה ב. שמו אם לערך בויקיפדיה, זכר אל העזרה טכניים."  
# ipsum_ar= "واستمر العصبة ضرب قد. وباءت الأمريكي الأوربيين هو به،, هو العالم، الثقيلة بال. مع وايرلندا الأوروبيّون كان, قد بحق أسابيع"  
# ipsum_en = "Normcore banjo umami sriracha intelligentsia bushwick. Leggings kale chips iPhone prism copper mug ethical, yr fanny pack lomo live-edge tumblr selvage master cleanse pitchfork health goth. Vegan chambray listicle 90's gochujang. Seitan narwhal iceland, marfa poutine poke craft beer fixie twee PBR&B fashion axe chambray."
# website_url = "http://meet.mit.edu"

# for i in range(11):
# 	newProduct = Product(team_id = i+1, video = videos[i], photo=photos[i], description_he = ipsum_he, description_ar = ipsum_ar, description_en = ipsum_en, website_url = website_url)
# 	session.add(newProduct)
# 	session.commit()

for i in range(1, 11):
	current_team = teams[i]

	newTeam = Team(id=i, name=current_team.name)
	session.add(newTeam)
	
	newProduct = Product(
		team_id=i,
		# product_name=current_team.name,
		team_members=current_team.members,
		description_en=current_team.description_en,
		description_he=current_team.description_he,
		description_ar=current_team.description_ar,
		photo=current_team.image,
		video=current_team.video
	)

	session.add(newProduct)
	session.commit()

## Add fake Users to the database

#larry = User(first_name = "Larry", last_name = "Page", username = "larry", group = 'investor bronze', email = "larry@larry.com")
#larry.hash_password("larry")
#session.add(larry)
#session.commit()

## Make a Wallet for Larry
#larrysWallet = Wallet(initial_value = '10000.00', current_value = '10000.00', user=larry)
#session.add_all([larry,larrysWallet])
#session.commit()


#jill = User(first_name = "Jill", last_name = "Scott", username = "jill", group = 'investor silver', email = "jill@jill.com")
#jill.hash_password('jill')
#session.add(jill)
#session.commit()

## Make a Wallet for  Jill
#jillsWallet = Wallet(initial_value = '50000.00', current_value = '50000.00', user = jill)
#session.add_all([jill,jillsWallet])
#session.commit()

#brad = User(first_name = "Brad", last_name = "Brown", username = "brad", group = 'investor gold', email = "brad@brad.com")
#brad.hash_password('brad')
#session.add(brad)
#session.commit()

## Make a Wallet for  Brad
#bradsWallet = Wallet(initial_value = '100000.00', current_value = '100000.00', user = brad)
#session.add_all([brad,bradsWallet])
#session.commit()



#def makeAnInvestment(user_id, product_id, amount):
#	wallet = session.query(Wallet).filter_by(user_id =user_id).one()
#	product = session.query(Product).filter_by(id = product_id).one()
#	if wallet.current_value > amount:
#		inv = Investment(wallet_id = wallet.id, product_id = product.id, amount = amount)
#		wallet.current_value = wallet.current_value - amount
#		session.add_all([wallet,inv])
#		session.commit()
#	else:
#		print("%s does not have enough money to make this investment" % wallet.user.first_name)
#Larry Invests 600 dollars in Team 4
#makeAnInvestment(71, 4, 6000.00)
#Jill Invests 4000 dollars in Team 5
#makeAnInvestment(72, 5, 4000.00)
#Brad Invests 200 dollars in Team 1
#makeAnInvestment(73, 1, 200.00)
#Brad invests 3000 dollars in Team 4
#makeAnInvestment(73,4, 3000.00)
#Print total amounts of investments for each team

#products = session.query(Product).all()
#for product in products:
#	print(product.team.name)
#	total_investments = 0.0
#	investors = []
#	for inv in product.investments:
#		total_investments += inv.amount
#		investors.append(inv.wallet.user.first_name)
#	print("Total Investments: " + str(total_investments))
#	print("Investors:")
#	print(investors)

