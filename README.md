<div style="
    position: relative; 
    width: 100%; 
    height: 330px; 
    border-radius: 16px; 
    overflow: hidden; 
    background-color: #0b1a2e;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
">
    <!-- Фоновое изображение (городской пейзаж / недвижимость) -->
    <div style="
        position: absolute; 
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://images.unsplash.com/photo-1568605117036-5fe5e7b4b5e5?q=80&w=2070&auto=format&fit=crop'); 
        background-size: cover; 
        background-position: center;
        filter: brightness(0.35) contrast(1.1);
    "></div>
    <!-- Дополнительная тёмная вуаль -->
    <div style="
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(5, 15, 25, 0.4);
    "></div>
    <!-- Карточка с заголовком -->
    <div style="
        position: absolute; 
        top: 50%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        background: rgba(20, 30, 45, 0.5); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px); 
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 40px 60px; 
        border-radius: 28px; 
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), 
                    inset 0 1px 1px rgba(255, 255, 255, 0.1);
        width: 75%;
        max-width: 750px;
    ">
        <h1 style="
            margin: 0; 
            font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; 
            font-weight: 800; 
            font-size: 3.4em; 
            letter-spacing: -1.5px;
            line-height: 1.1;
            color: #ffffff;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        ">
            🏡 <span style="color: #ffb347; text-shadow: 0 0 12px rgba(255, 180, 70, 0.6);">House Price</span> Prediction
        </h1>
        <div style="
            width: 70px; 
            height: 4px; 
            background: linear-gradient(90deg, #ffb347, #ff7f50); 
            margin: 18px auto;
            border-radius: 4px;
            box-shadow: 0 0 12px rgba(255, 140, 0, 0.6);
        "></div>
        <p style="
            margin: 0; 
            font-family: 'Courier New', monospace; 
            font-size: 1.05em; 
            font-weight: 600; 
            letter-spacing: 3.5px; 
            color: rgba(255, 255, 255, 0.95);
            text-transform: uppercase;
        ">
            EDA <span style="color: #ffb347;">✦</span> Cleaning <span style="color: #ffb347;">✦</span> Feature Engineering 
            <br style="display: none;"> <!-- для адаптивности на маленьких экранах -->
            <span style="color: #ffb347;">✦</span> CatBoost <span style="color: #ffb347;">✦</span> XGBoost <span style="color: #ffb347;">✦</span> LightGBM
        </p>
    </div>
</div>
