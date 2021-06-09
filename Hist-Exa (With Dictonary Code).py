#Libraries
import speech_recognition as speech
import pyttsx3 as spch
import pygame

#Intilization
engine = spch.init()
voice = engine.getProperty("voices")

engine.setProperty("rate",150)
engine.setProperty("voice",voice[1].id)

pygame.init()

#Background Screen
width = 1200
height = 650
screen=pygame.display.set_mode( ( width, height) )

pygame.display.set_caption("Hist-Exa")

bg=pygame.image.load("Images/bg1.png")
image1=pygame.transform.scale(bg, (1200,650))
screen.blit(image1,(0,0))
pygame.display.update()

#Dictionary for Hist-Exa
history = {
    "mediaeval history":["SpchImg","For a period that has come to be so strongly associated with the Islamic influence and rule in India, Medieval Indian history went for almost three whole centuries under the so-called indigenous rulers, that included the Chalukyas, the Pallavas, the Pandyas, the Rashtrakutas, the Muslims rulers and finally the Mughal Empire.","medival.jpg"],
    "Pala":["SpchImg","Between 8th and 10th centuries A.D., a number of powerful empires dominated the eastern and northern parts of India. The Pala king Dharmpala, son of Gopala reigned from the 8th century A.D. to early 9th century A.D. Nalanda University and Vikramashila University were founded by Dharmpala."],
    "Pallava":["SpchImg","The Pallava dynasty was an Indian dynasty that existed from 275 CE to 897 CE, ruling a portion of southern India. "],
    "Cena":["SpchImg","After the decline of the Palas, the Sena dynasty established its rule in Bengal. The founder of the dynasty was Samantasena. The greatest ruler of the dynasty was Vijaysena. He conquered the whole of Bengal and was succeeded by his son Ballalasena."],
    "pratihara":["SpchImg","The Gurjara-Pratihara dynasty was an imperial power during the Late Classical period on the Indian subcontinent, that ruled much of Northern India from the mid-8th to the 11th century. They ruled first at Ujjain and later at Kannauj. The Gurjara-Pratiharas were instrumental in containing Arab armies moving east of the Indus River."],
    "rashtrakuta":["SpchImg","This dynasty, ruled Karnataka. They ruled the territory vaster than that of any other dynasty. They were great patrons of art and literature. The encouragement that several Rashtrakuta kings provided to education and literature is unique."],
    "Chola":["SpchImg","It emerged in the middle of the 9th century A.D., covered a large part of Indian peninsula, as well as parts of Sri Lanka and the Maldives Islands."],
    "Delhi sultanate":["SpchImg","During this period of over 300 years, five dynasties ruled in Delhi. These were: the Slave dynasty (1206-90), Khilji dynasty (1290-1320), Tughlaq dynasty (1320-1413), Sayyid dynasty (1414-51), and Lodhi dynasty (1451-1526)."],
    "slave":["SpchImg","Slave Dynasty was the first Muslim dynasty that ruled India. Qutub-ud-din Aibak, a slave of Muhammad Ghori, who became the ruler after the death of his master, founded the Slave Dynasty. He was a great builder who built the majestic 238 feet high stone tower known as Qutub Minar in Delhi."],
    "Khilji":["SpchImg","Following the death of Balban, the Sultanate became weak and there were number of revolts. This was the period when the nobles placed Jalal-ud-din Khilji on the throne. This marked the beginning of Khilji dynasty."],
    "Tughlaq":["SpchImg","Ghyasuddin Tughlaq, who was the Governor of Punjab during the reign of Ala-ud-din Khilji, ascended the throne in 1320 A.D. and founded the Tughlaq dynasty. He conquered Warrangal and put down a revolt in Bengal. Muhammad-Bin-Tughlaq succeeded his father and extended the kingdom beyond India, into Central Asia."],
    "Maratha":["SpchImg","The Maratha Empire or the  was a power that dominated a large portion of the Indian subcontinent in the 18th century. The empire formally existed from 1674 with the coronation of Shivaji Maharaj as the Chhatrapati and ended in 1818 with the defeat of Peshwa Bajirao 2 at the hands of the British East India Company. The Marathas are credited to a large extent for ending Mughal Rule over most of the Indian subcontinent."],
    "Mughal":["SpchImg","The Mughal Empire was founded by Babur, a Timurid prince and ruler from Central Asia. Babur was a descendant of the Timurid Emperor Tamerlane on his father's side, and the Mongol ruler Genghis Khan on his mother's side. He established himself in Kabul and then pushed steadily southward into India from Afghanistan through the Khyber Pass."],
    "British":["SpchImg","British raj, period of direct British rule over the Indian subcontinent from 1858 until the independence of India and Pakistan in 1947. The raj succeeded management of the subcontinent by the British East India Company."],
    "sunga":["SpchImg","The Shungas originated from Magadha, and controlled areas of the central and eastern Indian subcontinent from around 187 to 78 BCE. The dynasty was established by Pushyamitra Shunga, who overthrew the last Maurya emperor. Its capital was Pataliputra."],
    "Satavahana":["SpchImg","The Satavahanas were based from Amaravati in Andhra Pradesh as well as Junnar (Pune) and Prathisthan (Paithan) in Maharashtra. The territory of the empire covered large parts of India from the 1st century BCE onward. The Sātavāhanas started out as feudatories to the Mauryan dynasty, but declared independence with its decline."],
    "Kushan":["SpchImg","The Kushana Empire expanded out of what is now Afghanistan into the northwest of the Indian subcontinent under the leadership of their first emperor, Kujula Kadphises, about the middle of the 1st century CE."],
    "Gupta":["SpchImg","The Gupta period was noted for cultural creativity, especially in literature, architecture, sculpture, and painting. The military exploits of the first three rulers – Chandragupta 1, Samudragupta, and Chandragupta 2 – brought much of India under their leadership."],
    "vakataka":["SpchImg","The Vakaṭaka Empire originated from the Deccan in the mid-third century CE. Their state is believed to have extended from the southern edges of Malwa and Gujarat in the north to the Tungabhadra River in the south as well as from the Arabian Sea in the western to the edges of Chhattisgarh in the east."],
    "Sangam":["SpchImg","During the Sangam period Tamil literature flourished from the 3rd century BCE to the 4th century CE. During this period, three Tamil dynasties, collectively known as the Three Crowned Kings of Tamilakam: Chera dynasty, Chola dynasty, and the Pandyan dynasty ruled parts of southern India."],
    "Kadamba":["SpchImg","Kadambas originated from Karnataka, was founded by Mayurasharma in 345 CE."],
    "Vardhan":["SpchImg","Harshvardhan (Harsha) ruled northern India from 606 to 647 CE. He was the son of Prabhakarvardhana and the younger brother of Rajyavardhana, who were members of the Vardhana dynasty and ruled Thanesar, in present-day Haryana."],
    "Harsha":["SpchImg","Harshvardhan (Harsha) ruled northern India from 606 to 647 CE. He was the son of Prabhakarvardhana and the younger brother of Rajyavardhana, who were members of the Vardhana dynasty and ruled Thanesar, in present-day Haryana."],
    "gahadavala":["SpchImg","Gahadavala dynasty ruled parts of the present-day Indian states of Uttar Pradesh and Bihar, during 11th and 12th centuries."],
    "Mysore":["SpchImg","The Wadiyar dynasty was a noble family in the Indian subcontinent that ruled the Kingdom of Mysore from 1399 to 1950, with an interruption. They were a feudatory house under Vijayanagar Emperor, took advantage of weakening Vijaynagar Empire and became free."],
    "Vijayanagar":["SpchImg","The Vijayanagara Empire was established in 1336 by Harihara 1 and his brother Bukka Raya 1 of Sangama Dynasty."],
    "Maurya":["SpchImg","The Maurya Empire (322–185 BCE) unified most of the Indian subcontinent into one state, and was the largest empire ever to exist on the Indian subcontinent.At its greatest extent, the Mauryan Empire stretched to the north up to the natural boundaries of the Himalayas and to the east into what is now Assam. To the west, it reached beyond modern Pakistan, to the Hindu Kush mountains in what is now Afghanistan."],
    "Nanda":["SpchImg","The Nanda Empire, at its greatest extent, extended from Bengal in the east, to the Punjab region in the west and as far south as the Vindhya Range. The Nanda dynasty was famed for their great wealth."],
    "mahajanapada":["SpchImg","Some Janapadas gradually become stronger and expanded their geographical boundaries. Such janapads are called Mahajanapads."],
    "Magadha":["SpchImg","Magadha formed one of the sixteen Maha - Janapadas. Its first capital was Rajagriha (modern Rajgir) then Pataliputra (modern Patna)"],
    "Janapada":["SpchImg","Janapads were the many small states that spread from today’s Afganistan which is to northwest of Indian Subcontinent to Bengal and Odisha in the east and to Maharashtra in south."],
    "kosala":["SpchImg","Mahajanapda Kosala is located on foothills of Himalayas in Utter Pradesh and Nepal. Later empire merged in Magdha."],
    "Kalinga":["SpchImg","Kalinga is a historical region of India. It is generally defined as the eastern coastal region between the Mahanadi and the Godavari rivers, although its boundaries have fluctuated with the territory of its rulers. The core territory of Kalinga now encompasses a large part of Odisha and northerneastern part of Andhra Pradesh. At its widest extent, the Kalinga region also included parts of present-day southwestern West Bengal and Chhattisgarh."],
    "Avanti":["SpchImg","Mahajanpad Avanti is located in Malwa region Madhya Pradesh.Later empire too merged in Magdha."],
    "Vedic":["SpchImg","The Vedic civilization is the earliest civilization in the history of ancient India. It is named after the Vedas, the early literature of the Hindu people"],
    "Indus Valley":["SpchImg","It flourished around 2,500 BC, in the western part of South Asia, what today is Pakistan and Western India."],
    "Harapan":["SpchImg","It flourished around 2,500 BC, in the western part of South Asia, what today is Pakistan and Western India."],
    "Harappa":["SpchImg","It flourished around 2,500 BC, in the western part of South Asia, what today is Pakistan and Western India."],
    "Buddhist era":["SpchImg","The history of Buddhism spans from the 6th century BCE to the present. Buddhism arose in the eastern part of Ancient India, in and around the ancient Kingdom of Magadha (now in Bihar, India), and is based on the teachings of Siddhartha Gautama."],
    "Alexander":["SpchImg","The Indian campaign of Alexander the Great began in 327 BC. After conquering the Achaemenid Empire of Persia, the Macedonian king Alexander, launched a campaign into the Indian subcontinent in present-day Afghanistan and Pakistan, part of which formed the easternmost territories of the Achaemenid Empire following the Achaemenid conquest of the Indus Valley"],
    "exit":["Spch","Thanks for using Hist-Exa"]}

activate="none"
exitstatus="no"

while True:
    try:
        bgh=pygame.image.load("Images/bg1.png")
        image078=pygame.transform.scale(bgh, (1200,650))
        screen.blit(image078,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            
            #To Read whether 's' key is pressed
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_s:
                    activate = "s"
                    print("S pressed")
                    
                    
         # if "s" key is pressed
        if activate=="s":
            #Change the background image to Listening Image
            listenImg2=pygame.image.load("Images/bg1.png")
            image14=pygame.transform.scale(listenImg2, (1200,650))
            screen.blit(image14,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    listenImg=pygame.image.load("Images/bg2.png")
                    image761=pygame.transform.scale(listenImg, (1200,650))
                    screen.blit(image761,(0,0))
                    pygame.display.update()
                    engine.say("Starting to Take Voice Command")
                    engine.runAndWait()
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in history:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword
                    
                    #Image & Speech Response type
                    if history[keyword][0]=="SpchImg":
                        #Showing Image
                        
                        Img=pygame.image.load("Images/bg1.png")
                        image21=pygame.transform.scale(listenImg, (1200,650))
                        screen.blit(image21,(0,0))
                        
                        images=pygame.image.load("Images/"+ history[keyword][2])
                        image21=pygame.transform.scale(images, (1000,550))
                        screen.blit(image21,(45,145))
                        pygame.display.update()
                        
                        #Saying Text
                        engine.say(history[keyword][1])
                        engine.runAndWait()
                        
                    if history[keyword][0]=="exit":
                        engine.say(history[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("Images/bg1.png")
            image0=pygame.transform.scale(bg, (1200,650))
            screen.blit(image0,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print ("Could not understand audio")
        engine.say("Could not understand audio")
        engine.runAndWait
    except speech.RequestError as e:
        print ("Could not request results; {0}".format(e))
        engine.say("Could not request results; {0}".format(e))
        engine.runAndWait
    except KeyboardInterrupt:
        break