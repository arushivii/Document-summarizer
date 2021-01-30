import spacy
import collections

from openie import StanfordOpenIE
nlp = spacy.load("en_core_web_sm")

with StanfordOpenIE() as client:
    text = '''Many parents are surprised to know that even young children can experience depression -- a lack of awareness that can lead to delays in diagnosis and treatment, and even untreated depression. The importance of early identification and treatment of depression in children cannot be overstated given its serious short- and long-term consequences.
Why Depression in Children May Not be Recognized
Other than a parent potentially being unaware that depression can occur in a child, it may go overlooked because of the following reasons:
Symptoms of depression in children may not be obvious . According to Maggie Chartier, MS, MPH and colleagues, who published a study in the Journal of School Health in March 2008, detecting depression in younger children can be especially challenging given the internalizing behaviors they often exhibit. These behaviors, such as shyness , withdrawal, or social avoidance are not disruptive and may not capture the attention of parents and teachers.
Depression in young children may look different than it does in older children and adults . While younger children experience sadness, they may not seem as obviously sad as a depressed adult may. Children may not completely understand what they are feeling, and may be less likely to report emotional pain. Instead, unexplained physical complaints , like headache or bellyache, are more common in depressed children than in depressed adults.
Some parents may refuse to have their children screened , as became evident in Chartier and team's 2008 study. While parental reasons for refusal were not studied, the researchers suggested that the fear of stigma, mistrust of the health care system, and lack of awareness of the impact of depression contributed to this. So, in an effort to perhaps do what a parent thinks is right and best for a child, an unintended negative consequence of non-evaluation can arise.
The Importance of the Treatment of Depression in Children
The range of potential consequences of childhood depression -- such as poor academic performance, relationship disturbances, substance abuse, early pregnancy, and suicide attempts -- are well established. Numerous research studies indicate that depression in children tends to recur through adulthood and predicts worse daily functioning, especially when left untreated.
Fortunately, early intervention and treatments have proven effective in relieving depression in children.
How to be Proactive
Be on the look out for signs of depression in your child, especially if she or anyone in the immediate family has had depression, or she has just experienced a stressful life event, such as the loss of a parent .
An older child or adolescent may show sudden academic decline; feelings of guilt or feeling misunderstood; withdrawal from friends and family; losing interest in thing of former enjoyment; appetite and weight changes; unexplained physical complaints; avoiding school and other social activities; and thoughts or actions of self-harm .
It is important to remember that having a depressed child does not make you a bad parent or indicate that you caused her pain. While it can be devastating to know that your child is suffering from emotional pain, it is important not to let your fears stand in the way of getting your child treatment. Finding your child appropriate treatment and providing her with support is the best thing for the whole family.
If you notice any signs or symptoms of depression in your child, consult with her pediatrician or a mental health professional.
Joan L. Luby. "Preschool Depression: The Importance of Identification of Depression Early in Development." Current Trends in Psychological Science August 2010; 19(4).
Maggie ChartiD., Elizabeth McCauley, PhD., Jerald R. Herting, PhD, Melissa Tracy, BA, and James Lymp, PhD. "Passive Versus Active Parental Consent: Implications for the Ability of School-based Depression Screening to Reach Youth at Risk." Journal of School Health. March 2008; 78(3): 157-168.'''
    print('Text: %s.' % text)
    for triple in client.annotate(text):
        print('|-', triple)
    for triple in client.annotate(text):
        counts = collections.Counter()
        obj=triple['object']
        sub=triple['subject']
        rel=triple['relation']
        totallen=len(obj.split())+len(sub.split())+len(rel.split())
        doc=nlp(obj)
        for token in doc:
            if ((totallen<=10) and (token.pos_) == 'NOUN'):
                print(triple)
