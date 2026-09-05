import pandas as pd
import streamlit as st

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="TACTIQ - Football Analytics", page_icon="⚽", layout="wide"
)

st.title("⚽ TACTIQ: محرك تحليل كرة القدم وتوقعات المباريات")
st.markdown(
    "مرحباً بك في نظام التحليل التكتيكي المتقدم. أدخل بيانات الفريقين أدناه لمعالجة المؤشرات (Expected Goals و Win Probability)."
)

# شريط جانبي لإدخال البيانات
st.sidebar.header("إعدادات المباراة والفرق")

team_a = st.sidebar.text_input("الفريق الأول (المستضيف)", "برشلونة")
team_b = st.sidebar.text_input("الفريق الثاني (الضيف)", "ريال مدريد")

st.sidebar.subheader("مؤشرات الأداء المتوقعة (xG)")
xg_a = st.sidebar.slider(
    f"متوقع الأهداف (xG) لـ {team_a}", 0.0, 5.0, 1.8, 0.1
)
xg_b = st.sidebar.slider(
    f"متوقع الأهداف (xG) لـ {team_b}", 0.0, 5.0, 1.2, 0.1
)

st.sidebar.subheader("الاستحواذ والتسديدات")
possession_a = st.sidebar.slider(f"نسبة استحواذ {team_a} (%)", 20, 80, 55, 1)
possession_b = 100 - possession_a

shots_a = st.sidebar.number_input(f"تسديدات {team_a}", min_value=0, value=15)
shots_b = st.sidebar.number_input(f"تسديدات {team_b}", min_value=0, value=11)

# زر التحليل
if st.button("تشغيل التحليل التكتيكي"):
  st.markdown("---")
  st.subheader("📊 نتائج التحليل والمحاكاة الاحتمالية")

  col1, col2, col3 = st.columns(3)

  with col1:
    st.metric(label=f"مؤشر الخطورة لـ {team_a}", value=f"{xg_a} xG")
  with col2:
    st.metric(label=f"مؤشر الخطورة لـ {team_b}", value=f"{xg_b} xG")
  with col3:
    diff = round(xg_a - xg_b, 2)
    st.metric(
        label="فارق الأفضلية الهجومية", value=diff, delta=f"{diff:+} goals"
    )

  # جدول مقارنة الإحصائيات
  st.markdown("### مقارنة شاملة للإحصائيات")
  comparison_data = {
      "المؤشر": ["الاستحواذ", "التسديدات", "الأهداف المتوقعة (xG)"],
      team_a: [f"{possession_a}%", shots_a, xg_a],
      team_b: [f"{possession_b}%", shots_b, xg_b],
  }
  df_comp = pd.DataFrame(comparison_data)
  st.table(df_comp)

  # توقع النتيجة بناءً على الـ xG
  st.info(
      f"💡 **رأي النموذج التكتيكي:** بناءً على المعطيات والفرص المصنوعة، الكفة"
      f" ترجح لصالح **{team_a if xg_a >= xg_b else team_b}** بتحقيق نتيجة إيجابية"
      " في اللقاء."
  )

