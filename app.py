import streamlit as st
from evaluator import evaluate_answer

st.set_page_config(page_title="Answer Sheet Evaluator", page_icon="📝")
st.title("📝 Answer Sheet Evaluator")
st.caption("Compares a student's answer with a model answer and suggests marks with feedback.")

with st.form("eval_form"):
    question = st.text_area("Question", height=80)
    model_answer = st.text_area("Model answer", height=150)
    student_answer = st.text_area("Student answer", height=150)
    max_marks = st.number_input("Maximum marks", min_value=1, max_value=100, value=10)
    submitted = st.form_submit_button("Evaluate")

if submitted:
    if not question.strip() or not model_answer.strip():
        st.warning("Please enter the question and the model answer.")
    else:
        with st.spinner("Evaluating the answer..."):
            try:
                result = evaluate_answer(question, model_answer, student_answer, int(max_marks))
            except Exception as e:
                st.error(f"Evaluation failed: {e}")
                st.stop()

        st.subheader(f"Suggested score: {result['score']} / {result['max_marks']}")
        st.progress(result["score"] / result["max_marks"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**✅ Points covered**")
            for point in result["key_points_covered"] or ["None"]:
                st.markdown(f"- {point}")
        with col2:
            st.markdown("**❌ Missing points**")
            for point in result["missing_points"] or ["None"]:
                st.markdown(f"- {point}")

        st.markdown("**💬 Feedback**")
        st.write(result["feedback"])