import pandas as pd

# Load dataset
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

print(df.head())
print("Dataset size:", len(df))

X = df["message"]
y = df["label"]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


messages = [
    "Congratulations! You won a free lottery ticket!",
    "Are we still meeting at 6 tonight?",
    "Urgent! Claim your free vacation now!"
]

messages_vec = vectorizer.transform(messages)
print(model.predict(messages_vec))
