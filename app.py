import streamlit as st
import google.generativeai as genai
import requests
from datetime import datetime, timedelta
from PIL import Image
import pandas as pd

# --- 1. GLOBAL INITIALIZATION & HARDCODED KEYS ---
st.set_page_config(
    page_title="ICE CHARTS HUNTER | Premium Financial AI", 
    layout="wide", 
    page_icon="❄️"
)

# Funguo za API zilizowekwa kiusalama
GEMINI_KEY = "AQ.Ab8RN6IHHURD5rbRJ7Wfdly2LG5N7FDlu8i4A4p_IZAAHF1bSA"
FINNHUB_KEY = "d94p8opr01qq8ms5ldtgd94p8opr01qq8ms5ldu0"

if "journal_history" not in st.session_state:
    st.session_state.journal_history = []

# Custom Premium Styling (Dark Ice Aesthetic)
st.markdown("""
    <style>
    .stApp { background-color: #0B0F19; color: #F1F5F9; font-family: 'Inter', sans-serif; }
    .brand-container {
        text-align: center; padding: 40px 20px;
        background: linear-gradient(145deg, #091523 0%, #112240 100%);
        border: 1px solid #00E5FF; border-radius: 16px;
        box-shadow: 0px 10px 30px rgba(0, 229, 255, 0.15); margin-bottom: 30px;
    }
    .brand-logo { font-size: 48px; font-weight: 900; color: #00E5FF; text-shadow: 0 0 20px rgba(0, 229, 255, 0.4); margin: 0; }
    .brand-tagline { font-size: 18px; color: #94A3B8; margin-top: 10px; }
    .feature-card { background: #111726; border: 1px solid #1E293B; border-radius: 12px; padding: 25px; text-align: center; }
    .pricing-card { background: #111726; border: 2px solid #1E293B; border-radius: 16px; padding: 35px; text-align: center; margin-bottom: 15px;}
    .pricing-card-vip { background: linear-gradient(180deg, #111726 0%, #0D2B45 100%); border: 2px solid #00E5FF; border-radius: 16px; padding: 35px; text-align: center; margin-bottom: 15px;}
    .price-text { font-size: 40px; font-weight: 800; color: #FFFFFF; margin: 15px 0; }
    .price-features { list-style: none; padding: 0; margin: 20px 0; color: #94A3B8; text-align: left; }
    .price-features li { margin-bottom: 10px; font-size: 15px; }
    .calc-box { background-color: #161b22; border: 1px solid #00E5FF; border-radius: 12px; padding: 20px; margin-top: 20px; }
    
    .stripe-button {
        display: block; width: 100%; background-color: #00E5FF; color: #0B0F19 !important; 
        text-align: center; padding: 12px; border-radius: 8px; font-weight: bold; 
        text-decoration: none; margin-top: 10px; box-shadow: 0 4px 15px rgba(0, 229, 255, 0.3);
    }
    .stripe-button:hover { background-color: #00B2CC; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER INTERFACE ---
st.markdown("""
    <div class="brand-container">
        <h1 class="brand-logo">❄️ ICE CHARTS HUNTER</h1>
        <p class="brand-tagline">Advanced Visual Intelligence Engine For Elite Traders</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. MULTI-PAGE NAVIGATION SYSTEM ---
tab_overview, tab_dash, tab_pricing = st.tabs(["🏠 Mfumo Overview", "⚡ AI Trading Dashboard", "💎 Vifurushi vya Huduma"])

# --- 4. TAB 1: PLATFORM OVERVIEW ---
with tab_overview:
    st.markdown("### 🎯 Kwanini Utumie Ice Charts Hunter?")
    st.write("Weka picha ya chati yako kutoka TradingView au MT5, kisha chagua mkakati unaoupenda (kama SMC au Liquidity), na kisha chagua mfumo wako wa biashara (Scalping, Intraday, au Swing). Mfumo wetu utasoma soko na kutoa majibu sahihi kulingana na chaguzi zako.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.markdown('<div class="feature-card"><h4 style="color:#00E5FF;">🔍 Mbinu za Taasisi (Institutional)</h4><p style="color:#94A3B8; font-size:14px;">Inachambua soko kwa kutumia mifumo ya SMC, Liquidity Sweeps, na Supply & Demand.</p></div>', unsafe_allow_html=True)
    with col_f2:
        st.markdown('<div class="feature-card"><h4 style="color:#00E5FF;">🎯 Uchambuzi wa Trading Style</h4><p style="color:#94A3B8; font-size:14px;">Inatoa viwango vya ENTRY, SL, na TP vinavyoendana kabisa na Scalping, Intraday, au Swing trading.</p></div>', unsafe_allow_html=True)
    with col_f3:
        st.markdown('<div class="feature-card"><h4 style="color:#00E5FF;">🌍 Live Fundamental Integration</h4><p style="color:#94A3B8; font-size:14px;">Inachambua habari za uchumi za dunia ili kuongeza usahihi wa signal yako kabla ya kuingia sokoni.</p></div>', unsafe_allow_html=True)

# --- 5. TAB 2: AI TRADING DASHBOARD & STRATEGY ENGINE ---
with tab_dash:
    st.sidebar.markdown("### ❄️ Hali ya Mfumo")
    st.sidebar.success("● AI Vision System: IMEWAKA")
    st.sidebar.success("● Trading Strategies: ZIPO ACTIVE")
    st.sidebar.success("● Style Customization: TAYARI")
    
    def fetch_live_market_news(api_key):
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
            url = f"https://finnhub.io{yesterday}&to={today}&token={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                return "\n".join([f"- **{item.get('headline')}**: {item.get('summary')[:120]}..." for item in response.json()[:4]])
            return "Imeshindwa kupata habari za masoko kwa sasa."
        except:
            return "Mfumo wa habari upo nje ya mtandao."

    col_dash_left, col_dash_right = st.columns(2)
    
    with col_dash_left:
        st.markdown("### 📥 Weka Picha ya Chati Hapa")
        uploaded_file = st.file_uploader("Pakia screenshot ya chati yako", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
        
        col_input1, col_input2 = st.columns(2)
        with col_input1:
            asset_name = st.text_input("Jina la Asset (Mfano: XAUUSD, EURUSD)", value="XAUUSD")
        with col_input2:
            selected_style = st.selectbox("Aina ya Trading Style:", ["Scalping", "Intraday", "Swing"])
        
        st.markdown("### 🧠 Chagua Mkakati wa Uchambuzi (Strategy)")
        selected_strategy = st.selectbox(
            "Chagua mbinu unayotaka AI itumie kuchambua chati yako:",
            [
                "Smart Money Concepts (SMC) - [BOS, CHoCH, Order Blocks, Fair Value Gaps]",
                "Supply and Demand - [Rally-Base-Drop, Drop-Base-Rally, Premium/Discount Zones]",
                "Order Flow Analysis - [Institutional Buying/Selling, Imbalance Verification]",
                "Liquidity Concepts - [Asia Session Sweeps, Equal Highs/Lows, Stop Hunts]"
            ]
        )
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Chati: {asset_name}", use_container_width=True)
            
    with col_dash_right:
        st.markdown("### 📊 Ripoti ya Uchambuzi wa AI")
        
        if st.button("⚡ AZIMIA UCHAMBUZI WA SOKO", use_container_width=True):
            if not uploaded_file:
                st.warning("Tafadhali pakia picha ya chati kutoka MT5 au TradingView kwanza.")
            else:
                with st.spinner("AI inachambua chati kwa kutumia mfumo ulioteuliwa..."):
                    live_fundamentals = fetch_live_market_news(FINNHUB_KEY)
                    try:
                        genai.configure(api_key=GEMINI_KEY)
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        
                        prompt = f"You are the expert institutional trading engine behind 'ICE CHARTS HUNTER'. Analyze this market image and cross-reference with these live economic data pieces:\n{live_fundamentals}\n\nCRITICAL INSTRUCTION 1: You MUST perform the analysis strictly based on the chosen trading strategy concept: {selected_strategy}\n\nCRITICAL INSTRUCTION 2: You MUST customize the trade setup according to this specific trading style: {selected_style}\n\nCRITICAL INSTRUCTION 3: You MUST write the entire response and breakdown in professional, fluent SWAHILI language.\n\nToa ripoti yako kwa kufuata muundo huu sahihi wa Markdown:\n- ### 📊 Uchambuzi wa Chati Kiteknolojia\n- ### 🎯 Ishara Rasmi ya Biashara (Trading Signal)\n  (Weka mistari iliyokolezwa ya Bold kwa ajili ya: **MWELEKEO (BUY/SELL/WAIT)**, **ENTRY**, **STOP LOSS (SL)**, na **TAKE PROFIT (TP)**)\n- ### 🌍 Muktadha wa Habari za Kiuchumi (Fundamental Impact)\n- ### ⚠️ Mpango wa Kusimamia Riski (Risk Management)"
                        
                        response = model.generate_content([prompt, image])
                        st.success("Uchambuzi Umekamilika!")
                        st.markdown(response.text)
                        
                        timestamp_now = datetime.now().strftime("%Y-%m-%d %H:%M")
                        st.session_state.journal_history.append({
                            "Muda": timestamp_now,
                            "Asset": asset_name.upper(),
                            "Muhtasari": "Uchambuzi wa kitaalamu umekamilika."
                        })
                        
                    except Exception as e:
                        st.error(f"Mfumo umeshindwa kusoma chati: {e}")

    # --- POSITION RISK CALCULATOR (HAPA PAMESAFISHWA KIKAMILIFU) ---
    st.markdown("---")
    st.markdown("### 🧮 Kikokotoo cha Riski na Ukubwa wa Lot Size")
    
    account_balance = st.number_input("Salio la Akaunti ($)", min_value=10.0, value=1000.0, step=100.0)
    risk_percent = st.number_input("Asilimia ya Riski (%)", min_value=0.1, max_value=10.0, value=1.0, step=0.5)
    asset_type = st.selectbox("Aina ya Soko", ["Forex / Currency Pairs", "Gold (XAUUSD)", "Indices / Crypto"])
    entry_price = st.number_input("Bei ya Kuingilia (Entry)", min_value=0.0, value=1.0750, format="%.5f")
    sl_price = st.number_input("Bei ya Kuzuia Hasara (SL)", min_value=0.0, value=1.0720, format="%.5f")
    
    risk_amount = account_balance * (risk_percent / 100.0)
    price_difference = abs(entry_price - sl_price)
    
    # Mahesabu yote yamewekwa kwenye mstari mmoja bila vitalu vya if/else ili kuondoa makosa ya Indentation
