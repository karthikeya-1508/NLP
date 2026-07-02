import streamlit as st
from model_train_and_predict import get_sentiment_label, predict_sentiment


def main():
    st.title("Amazon Review Sentiment Analysis")

    user_input = st.text_area("Enter your review:")

    if st.button("Predict"):
        if user_input and user_input.strip():
            try:
                prediction = predict_sentiment(user_input)
                if prediction is None:
                    st.warning("Please enter a review before predicting.")
                else:
                    label = get_sentiment_label(prediction)
                    if label == "Positive":
                        st.success(f"Positive Sentiment ({label})")
                    elif label == "Neutral":
                        st.info(f"Neutral Sentiment ({label})")
                    else:
                        st.error(f"Negative Sentiment ({label})")
            except Exception as exc:
                st.error(f"Prediction failed: {exc}")
        else:
            st.warning("Please enter a review.")


if __name__ == "__main__":
    main()
